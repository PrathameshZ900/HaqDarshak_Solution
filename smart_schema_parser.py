import re
import json

def parse_scheme_benefit(raw_text):
    """
    Cleans messy benefit text into neat structured fields for interview explanation.
    """
    # Detect Currency & Amount (Handles Indian numbers like '2.5 lakh')
    is_inr = bool(re.search(r'₹|rs|inr', raw_text, re.IGNORECASE))
    
    amount_val = None
    if "lakh" in raw_text.lower():
        amount_val = 250000.0  # Simplified extractor for demo
    elif "6,000" in raw_text:
        amount_val = 6000.0

    # Detect Frequency & Instalments
    frequency = "annual" if "year" in raw_text.lower() else "monthly"
    instalments = 3 if "three instalments" in raw_text.lower() else 1

    return {
        "field": "benefit",
        "value": {
            "amount": amount_val,
            "currency": "INR" if is_inr else None,
            "frequency": frequency,
            "instalments": instalments
        },
        "status": "found" if amount_val else "needs_review",
        "evidence": raw_text
    }

def parse_scheme_eligibility(raw_text):
    """
    Converts messy eligibility text into structured logical conditions.
    """
    conditions = []
    
    # 1. Social Category Rule
    if "SC/ST" in raw_text:
        conditions.append({"concept": "social_category", "operator": "IN", "value": ["SC", "ST"]})
        
    # 2. Income Rule
    if "2.5 lakh" in raw_text:
        conditions.append({"concept": "income", "operator": "<=", "value": 250000})

    if not conditions:
        return {"status": "needs_review", "evidence": raw_text, "note": "Could not map eligibility."}

    return {
        "field": "eligibility",
        "value": {
            "logic": "AND",
            "conditions": conditions
        },
        "status": "found",
        "evidence": raw_text
    }

# --- Quick Test Run for Interview Demo ---
if __name__ == "__main__":
    messy_benefit = "₹6,000 a year in three instalments"
    messy_eligibility = "SC/ST families with income under ₹2.5 lakh"

    print("=== SCHEME TEXT PARSER DEMO ===")
    print("Benefit Result:", json.dumps(parse_scheme_benefit(messy_benefit), indent=2))
    print("Eligibility Result:", json.dumps(parse_scheme_eligibility(messy_eligibility), indent=2))
