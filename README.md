# 🚀 Haqdarshak Scheme Data Parser (S2 Solution)

## 📌 What This Does
Automatically converts messy government welfare text (e.g., *"₹6,000 a year in three instalments"*) into clean, structured JSON format for automated eligibility checks.

---

## 🛠️ How It Works (Simple Logic)
1. **Deterministic Regex Rules:** Fast & reliable extraction for currency, amounts (lakhs), and frequencies.
2. **Strict Fallback:** If the text is ambiguous or unmapped, the system **never guesses**—it flags the record with `status: "needs_review"` for human verification.

---

## 🧑‍💻 How to Run
```bash
python smart_schema_parser.py
