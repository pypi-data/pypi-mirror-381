from __future__ import annotations

import pytest

import nltk
from nltk.corpus import wordnet as wn

from glitchlings.zoo.jargoyle import substitute_random_synonyms


def _ensure_wordnet_loaded() -> bool:
    """Attempt to load WordNet, downloading it on demand if necessary."""

    try:  # pragma: no cover - exercised by missing corpus branches
        wn.ensure_loaded()
    except LookupError:
        # Fetch the corpus quietly; pytest output already reports skips.
        nltk.download("wordnet", quiet=True)
        try:
            wn.ensure_loaded()
        except LookupError:
            return False
    return True


WORDNET_AVAILABLE = _ensure_wordnet_loaded()


pytestmark = pytest.mark.skipif(
    not WORDNET_AVAILABLE,
    reason="NLTK WordNet corpus unavailable; skipping jargoyle POS tests.",
)


def _clean_tokens(text: str) -> list[str]:
    return [token.strip(".,") for token in text.split()]


def test_jargoyle_multiple_pos_targets_change_words():
    text = "They sing happy songs."
    result = substitute_random_synonyms(
        text,
        replacement_rate=1.0,
        part_of_speech=("v", "a"),
        seed=123,
    )

    original_tokens = _clean_tokens(text)
    result_tokens = _clean_tokens(result)

    # Expect both verb and adjective replacements to differ from input
    changed = {
        orig for orig, new in zip(original_tokens, result_tokens) if orig != new
    }
    assert {"sing", "happy"} <= changed


def test_jargoyle_any_includes_all_supported_pos():
    text = "They sing happy songs quickly."
    result = substitute_random_synonyms(
        text,
        replacement_rate=1.0,
        part_of_speech="any",
        seed=99,
    )

    original_tokens = _clean_tokens(text)
    result_tokens = _clean_tokens(result)

    changed = {
        orig for orig, new in zip(original_tokens, result_tokens) if orig != new
    }
    assert {"sing", "happy", "songs", "quickly"} <= changed
