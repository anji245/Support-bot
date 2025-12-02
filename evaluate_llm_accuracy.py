"""
Simple accuracy evaluator for your local LLM classifier logic.
This DOES NOT download any model. It uses your classify_ticket_via_api()
function exactly the way Streamlit does.

Runs each model independently and prints only accuracy %
(no precision, no recall, no logs, no traceback).
"""

import sys
from pathlib import Path

# Add src/ path
ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from inference_api import classify_ticket_via_api, MODEL_OPTIONS   # your logic
from evaluate_model import TEST_DATASET                            # synthetic dataset


def evaluate_model(model_name: str):
    """
    Forces classification using ONLY the selected LLM model.
    Returns accuracy %.
    """
    correct = 0
    total = len(TEST_DATASET)

    # temporarily override MODEL_OPTIONS
    original = list(MODEL_OPTIONS)
    MODEL_OPTIONS.clear()
    MODEL_OPTIONS.append(model_name)

    for sample in TEST_DATASET:
        ticket = sample["ticket"]
        expected = sample["expected"]

        try:
            pred = classify_ticket_via_api(ticket)
            if isinstance(pred, str) and pred.lower().strip() == expected:
                correct += 1
        except:
            pass

    # restore models
    MODEL_OPTIONS.clear()
    MODEL_OPTIONS.extend(original)

    accuracy = correct / total if total else 0
    return round(accuracy * 100, 2)


def main():
    MODELS = [
        "mistralai/Mistral-7B-Instruct-v0.2",
        "tiiuae/falcon-7b-instruct",
        "microsoft/Phi-3-mini-4k-instruct",
    ]

    print("\n=== LLM Accuracy Results ===\n")
    for m in MODELS:
        acc = evaluate_model(m)
        print(f"{m} → {acc}% accuracy")
    print("\n============================\n")


if __name__ == "__main__":
    main()
