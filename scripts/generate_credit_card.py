#!/usr/bin/env python3
import random
import json
from stdnum.luhn import calc_check_digit, is_valid as luhn_is_valid

# ----------------------------
# 1. Generators & validators
# ----------------------------
def gen_base_card():
    prefix = str(random.choice([4, 5, 6]))  # Visa, MasterCard, Discover
    body   = "".join(str(random.randint(0, 9)) for _ in range(14))
    check  = calc_check_digit(prefix + body)
    return prefix + body + check

def gen_invalid_card():
    card = gen_base_card()
    bad  = (int(card[-1]) + random.randint(1, 9)) % 10
    return card[:-1] + str(bad)

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(card):        return card
def with_spaces(card):  return ' '.join(card[i:i+4] for i in range(0, 16, 4))
def with_dashes(card):  return '-'.join(card[i:i+4] for i in range(0, 16, 4))
def with_underscores(card):
    nums = card.replace(' ', '').replace('-', '')
    return '_'.join(nums[i:i+4] for i in range(0, 16, 4))
def mixed(card):
    nums = card.replace(' ', '').replace('-', '')
    return f"{nums[:4]}-{nums[4:8]} {nums[8:12]}-{nums[12:]}"
def ocr_spacing(card):
    nums = card.replace('-', '')
    return nums[:8] + ' ' + nums[8:]
def punctuation_sep(card):
    nums  = card.replace(' ', '').replace('-', '')
    punct = random.choice(['.', '/', '_'])
    idx   = random.choice([4, 8, 12])
    return nums[:idx] + punct + nums[idx:]
def masked(card):       return 'XXXX-XXXX-XXXX-' + card[-4:]
def short_card(card):   return ' '.join(card[i:i+4] for i in range(0, 12, 4))
def embedded(card):     return card
def alt_label(card):    return card

VARIATIONS = {
    "plain":            plain,
    "with_spaces":      with_spaces,
    "with_dashes":      with_dashes,
    "with_underscores": with_underscores,
    "mixed":            mixed,
    "ocr":              ocr_spacing,
    "punctuation":      punctuation_sep,
    "masked":           masked,
    "short":            short_card,
    "embedded":         embedded,
    "alt_label":        alt_label,
}

# ----------------------------
# 3. Sentence templates
# ----------------------------
TEMPLATES = {
    "plain": [
        "For secure payment use this credit card number {v} in your payment card form",
        "Your card details for your swipe card test are recorded as {v}"
    ],
    "with_spaces": [
        "Enter the card number with spaces as {v} into your card credentials field",
        "The payment card info is shown as {v} on test terminals"
    ],
    "with_dashes": [
        "You can view the card info with dashes {v} in the card information display",
        "The credit card number printed on mock receipts reads {v}"
    ],
    "with_underscores": [
        "Our test harness logs card details under {v} in account info",
        "Fake data for card credentials uses underscore format {v}"
    ],
    "mixed": [
        "Hybrid card format example in card details is {v}",
        "Test entry for card credentials shows mixed separators {v}"
    ],
    "ocr": [
        "OCR simulation may read the credit card number as {v} in card information",
        "Machine scan example for card number scanned as {v}"
    ],
    "punctuation": [
        "Punctuation test in card info example is {v} for payment card validation",
        "The swipe card mock uses punctuation separated number {v}"
    ],
    "masked": [
        "Masked card credentials appear as {v} for your credit card test",
        "Only last four digits are visible in card info {v}"
    ],
    "short": [
        "Truncated swipe card number example is {v} for testing error handling",
        "Partial card number entry used in card details is {v}"
    ],
    "embedded": [
        "For fraud simulation my card ends with {v} in the card information log",
        "Verification only requires last four digits {v} in card credentials"
    ],
    "alt_label": [
        "credit card number {v} is stored in payment card records",
        "debit card like card no {v} may also be tested under card info"
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_credit_card_variations(count=50):
    records = []
    keys    = list(VARIATIONS.keys())
    while len(records) < count:
        # 70% valid, 30% invalid
        base   = gen_base_card() if random.random() < 0.7 else gen_invalid_card()
        valid  = luhn_is_valid("".join(ch for ch in base if ch.isdigit()))
        key    = random.choice(keys)
        variant = VARIATIONS[key](base)

        # for masked/short we preserve the base's validity
        if key in ("masked", "short"):
            is_valid = valid
        else:
            digits = "".join(ch for ch in variant if ch.isdigit())
            is_valid = luhn_is_valid(digits)

        text = random.choice(TEMPLATES[key]).format(v=variant)
        records.append({
            "text":      text,
            "card":      variant,
            "variation": key,
            "is_valid":  is_valid,
            "fake_data": True
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_credit_card_variations(count=50)
    with open("credit_cards.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ credit_cards.json generated with correct validity flags")
