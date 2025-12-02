"""
Minimal test dataset for evaluation imports.

This module exposes a single variable `TEST_DATASET` which is a plain list
of dictionaries. There are no functions or classes here — only the data
structure so other modules can import `TEST_DATASET` directly.
"""

TEST_DATASET = [
    {"ticket": "I was charged twice this month.", "expected": "billing"},
    {"ticket": "The app crashes when uploading files.", "expected": "bug"},
    {"ticket": "Can you add dark mode?", "expected": "feature"},
    {"ticket": "I forgot my password.", "expected": "account"},
]


