"""Core data structures used to model glitchlings and their interactions."""

import inspect
import random
from enum import IntEnum, auto
from hashlib import blake2s
from typing import TYPE_CHECKING, Any, Protocol

_datasets_error: ModuleNotFoundError | None = None
try:  # pragma: no cover - optional dependency
    from datasets import Dataset as _DatasetsDataset
except ModuleNotFoundError as error:  # pragma: no cover - optional dependency
    _DatasetsDataset = None  # type: ignore[assignment]
    _datasets_error = error
else:
    _datasets_error = None

if TYPE_CHECKING:  # pragma: no cover - typing only
    from datasets import Dataset  # type: ignore
elif _DatasetsDataset is not None:
    Dataset = _DatasetsDataset
else:

    class Dataset(Protocol):  # type: ignore[no-redef]
        """Typed stub mirroring the Hugging Face dataset interface used here."""

        def with_transform(self, function: Any) -> "Dataset": ...


def _is_transcript(value: Any) -> bool:
    """Return True when the value resembles a chat transcript."""

    if not isinstance(value, list):
        return False

    if not value:
        return True

    if not all(isinstance(turn, dict) for turn in value):
        return False

    return "content" in value[-1]


class CorruptionCallable(Protocol):
    """Protocol describing a callable capable of corrupting text."""

    def __call__(self, text: str, *args: Any, **kwargs: Any) -> str: ...


# Text levels for glitchlings, to enforce a sort order
# Work from highest level down, because e.g.
# duplicating a word then adding a typo is potentially different than
# adding a typo then duplicating a word
class AttackWave(IntEnum):
    """Granularity of text that a glitchling corrupts."""

    DOCUMENT = auto()
    PARAGRAPH = auto()
    SENTENCE = auto()
    WORD = auto()
    CHARACTER = auto()


# Modifier for within the same attack wave
class AttackOrder(IntEnum):
    """Relative execution order for glitchlings within the same wave."""

    FIRST = auto()
    EARLY = auto()
    NORMAL = auto()
    LATE = auto()
    LAST = auto()


class Glitchling:
    """A single text corruption agent with deterministic behaviour."""

    def __init__(
        self,
        name: str,
        corruption_function: CorruptionCallable,
        scope: AttackWave,
        order: AttackOrder = AttackOrder.NORMAL,
        seed: int | None = None,
        **kwargs: Any,
    ) -> None:
        """Initialize a glitchling.

        Args:
            name: Human readable glitchling name.
            corruption_function: Callable used to transform text.
            scope: Text granularity on which the glitchling operates.
            order: Relative ordering within the same scope.
            seed: Optional seed for deterministic random behaviour.
            **kwargs: Additional parameters forwarded to the corruption callable.
        """

        # Each Glitchling maintains its own RNG for deterministic yet isolated behavior.
        # If no seed is supplied, we fall back to Python's default entropy.
        self.seed = seed
        self.rng: random.Random = random.Random(seed)
        self.name: str = name
        self.corruption_function: CorruptionCallable = corruption_function
        self.level: AttackWave = scope
        self.order: AttackOrder = order
        self.kwargs: dict[str, Any] = {}
        for kw, val in kwargs.items():
            self.set_param(kw, val)

    def set_param(self, key: str, value: Any) -> None:
        """Persist a parameter for use by the corruption callable."""

        setattr(self, key, value)
        self.kwargs[key] = value
        if key == "seed":
            self.reset_rng(value)

    def __corrupt(self, text: str, *args: Any, **kwargs: Any) -> str:
        """Execute the corruption callable, injecting the RNG when required."""

        # Pass rng to underlying corruption function if it expects it.
        try:
            signature = inspect.signature(self.corruption_function)
        except (TypeError, ValueError):
            signature = None

        expects_rng = False
        if signature is not None:
            expects_rng = "rng" in signature.parameters

        if expects_rng:
            corrupted = self.corruption_function(text, *args, rng=self.rng, **kwargs)
        else:
            corrupted = self.corruption_function(text, *args, **kwargs)
        return corrupted

    def corrupt(self, text: str | list[dict[str, Any]]) -> str | list[dict[str, Any]]:
        """Apply the corruption function to text or conversational transcripts."""

        if _is_transcript(text):
            transcript = [dict(turn) for turn in text]
            if transcript:
                transcript[-1]["content"] = self.__corrupt(
                    transcript[-1]["content"], **self.kwargs
                )
            return transcript

        return self.__corrupt(text, **self.kwargs)

    def corrupt_dataset(self, dataset: Dataset, columns: list[str]) -> Dataset:
        """Apply corruption lazily across dataset columns."""

        if _DatasetsDataset is None:
            message = "datasets is not installed"
            raise ModuleNotFoundError(message) from _datasets_error

        def _is_transcript(value: Any) -> bool:
            """Return ``True`` when the value resembles a chat transcript."""

            if not isinstance(value, list) or not value:
                return False

            return all(
                isinstance(turn, dict) and "content" in turn for turn in value
            )

        def __corrupt_row(row: dict[str, Any]) -> dict[str, Any]:
            row = dict(row)
            for column in columns:
                value = row[column]
                if _is_transcript(value):
                    row[column] = self.corrupt(value)
                elif isinstance(value, list):
                    row[column] = [self.corrupt(item) for item in value]
                else:
                    row[column] = self.corrupt(value)
            return row

        return dataset.with_transform(__corrupt_row)

    def __call__(self, text: str, *args: Any, **kwds: Any) -> str | list[dict[str, Any]]:
        """Allow a glitchling to be invoked directly like a callable."""

        return self.corrupt(text, *args, **kwds)

    def reset_rng(self, seed: int | None = None) -> None:
        """Reset the glitchling's RNG to its initial seed."""

        if seed is not None:
            self.seed = seed
        if self.seed is not None:
            self.rng = random.Random(self.seed)

    def clone(self, seed: int | None = None) -> "Glitchling":
        """Create a copy of this glitchling, optionally with a new seed."""

        cls = self.__class__
        filtered_kwargs = {k: v for k, v in self.kwargs.items() if k != "seed"}
        clone_seed = seed if seed is not None else self.seed
        if clone_seed is not None:
            filtered_kwargs["seed"] = clone_seed

        if cls is Glitchling:
            return Glitchling(
                self.name,
                self.corruption_function,
                self.level,
                self.order,
                **filtered_kwargs,
            )

        return cls(**filtered_kwargs)


class Gaggle(Glitchling):
    """A collection of glitchlings executed in a deterministic order."""

    def __init__(self, glitchlings: list[Glitchling], seed: int = 151):
        """Initialize the gaggle and derive per-glitchling RNG seeds.

        Args:
            glitchlings: Glitchlings to orchestrate.
            seed: Master seed used to derive per-glitchling seeds.
        """

        super().__init__("Gaggle", self.corrupt, AttackWave.DOCUMENT, seed=seed)
        self.glitchlings: dict[AttackWave, list[Glitchling]] = {
            level: [] for level in AttackWave
        }
        self.apply_order: list[Glitchling] = []
        # Derive deterministic per-glitchling seeds from master seed if provided
        for idx, g in enumerate(glitchlings):
            _g = g.clone()
            derived_seed = Gaggle.derive_seed(seed, _g.name, idx)
            _g.reset_rng(derived_seed)
            self.glitchlings[g.level].append(_g)
        self.sort_glitchlings()

    @staticmethod
    def derive_seed(master_seed: int, glitchling_name: str, index: int) -> int:
        """Derive a deterministic seed for a glitchling based on the master seed."""
        def _int_to_bytes(value: int) -> bytes:
            if value == 0:
                return b"\x00"

            abs_value = abs(value)
            length = max(1, (abs_value.bit_length() + 7) // 8)

            if value < 0:
                while True:
                    try:
                        return value.to_bytes(length, "big", signed=True)
                    except OverflowError:
                        length += 1

            return abs_value.to_bytes(length, "big", signed=False)

        hasher = blake2s(digest_size=8)
        hasher.update(_int_to_bytes(master_seed))
        hasher.update(b"\x00")
        hasher.update(glitchling_name.encode("utf-8"))
        hasher.update(b"\x00")
        hasher.update(_int_to_bytes(index))
        return int.from_bytes(hasher.digest(), "big")

    def sort_glitchlings(self) -> None:
        """Sort glitchlings by wave then order to produce application order."""

        self.apply_order = [
            g
            for _, glitchlings in sorted(self.glitchlings.items())
            for g in sorted(glitchlings, key=lambda x: (x.order, x.name))
        ]

    def corrupt(self, text: str) -> str:
        """Apply each glitchling to the provided text sequentially."""

        corrupted = text
        for glitchling in self.apply_order:
            corrupted = glitchling(corrupted)
        return corrupted
