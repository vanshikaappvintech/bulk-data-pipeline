# #!/usr/bin/env python3
# import random
# import json
# from stdnum.luhn import calc_check_digit, is_valid as luhn_is_valid

# # ----------------------------
# # 1. Generators & validators
# # ----------------------------
# def gen_base_debit():
#     """
#     Generate a 16-digit debit card number using common BIN prefixes:
#     Visa (4), MasterCard (5), Discover (6).
#     """
#     prefix = str(random.choice([4, 5, 6]))
#     body = "".join(str(random.randint(0, 9)) for _ in range(14))
#     check = calc_check_digit(prefix + body)
#     return prefix + body + check

# def gen_invalid_debit():
#     """Flip the last digit to produce an invalid card."""
#     card = gen_base_debit()
#     bad = (int(card[-1]) + random.randint(1, 9)) % 10
#     return card[:-1] + str(bad)

# def is_valid_debit(card):
#     """Strip non-digits and validate via Luhn."""
#     digits = "".join(ch for ch in card if ch.isdigit())
#     return luhn_is_valid(digits)

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(card):
#     return card

# def with_spaces(card):
#     nums = card.replace('-', '').replace('_', '')
#     return ' '.join(nums[i:i+4] for i in range(0, 16, 4))

# def with_dashes(card):
#     nums = card.replace(' ', '').replace('_', '')
#     return '-'.join(nums[i:i+4] for i in range(0, 16, 4))

# def ocr_spacing(card):
#     nums = card.replace('-', '').replace(' ', '')
#     return nums[:8] + ' ' + nums[8:]

# def short_card(card):
#     return card[:15]  # drop final digit

# def masked(card):
#     return 'XXXX-XXXX-XXXX-' + card[-4:]

# def embedded(card):
#     return card  # last4 used in sentence

# def alt_label(card):
#     return card  # label added in template

# def mixed(card):
#     nums = card.replace(' ', '').replace('-', '')
#     return f"{nums[:4]}-{nums[4:8]} {nums[8:12]}-{nums[12:16]}"

# def with_underscores(card):
#     nums = card.replace('-', '').replace(' ', '')
#     return '_'.join(nums[i:i+4] for i in range(0, 16, 4))

# def punctuation_sep(card):
#     nums = card.replace(' ', '').replace('-', '')
#     punct = random.choice(['.', '/', '_'])
#     idx = random.choice([4, 8, 12])
#     return nums[:idx] + punct + nums[idx:]

# VARIATIONS = {
#     "plain": plain,
#     "with_spaces": with_spaces,
#     "with_dashes": with_dashes,
#     "ocr": ocr_spacing,
#     "short": short_card,
#     "masked": masked,
#     "embedded": embedded,
#     "alt_label": alt_label,
#     "mixed": mixed,
#     "with_underscores": with_underscores,
#     "punctuation": punctuation_sep,
# }

# # ----------------------------
# # 3. Sentence templates
# #   {v} = variant, {last4} = final four digits
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Her debit card number is {v}, issued by her bank.",
#         "Use this 16-digit number for withdrawals: {v}.",
#     ],
#     "with_spaces": [
#         "Spaced format for readability: {v}.",
#         "When called out loud she says: {v}.",
#     ],
#     "with_dashes": [
#         "Dashed format on receipt: {v}.",
#         "You’ll see: {v} on the POS terminal.",
#     ],
#     "ocr": [
#         "OCR readout: {v}.",
#         "Scanned as: {v}.",
#     ],
#     "short": [
#         "Truncated (15-digit) form: {v}.",
#         "Missing last digit: {v}.",
#     ],
#     "masked": [
#         "Masked view: {v}.",
#         "Only last four digits visible: {v}.",
#     ],
#     "embedded": [
#         "My debit card ends with {last4}.",
#         "Last four digits are {last4}.",
#     ],
#     "alt_label": [
#         "card no: {v}",
#         "debit #: {v}",
#         "credit card: {v}",
#     ],
#     "mixed": [
#         "Mixed separators: {v}.",
#         "Hybrid format: {v}.",
#     ],
#     "with_underscores": [
#         "Underscore style: {v}.",
#         "Logged as: {v}.",
#     ],
#     "punctuation": [
#         "Punctuation inserted: {v}.",
#         "It appears as {v}.",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_debit_variations(count=20):
#     records = []
#     keys = list(VARIATIONS.keys())

#     while len(records) < count:
#         base = gen_base_debit() if random.random() < 0.7 else gen_invalid_debit()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)
#         last4 = base[-4:]

#         tmpl = random.choice(TEMPLATES[key])
#         text = tmpl.format(v=variant, last4=last4)

#         records.append({
#             "text": text,
#             "debit_card": variant,
#             "variation": key,
#             "is_valid": is_valid_debit(variant)
#         })

#     return records

# # ----------------------------
# # 5. Write to JSON
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_debit_variations(count=20)
#     with open("debit_cards.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ debit_cards.json generated with all requested debit-card variations.")




#!/usr/bin/env python3
import random
import json
from stdnum.luhn import calc_check_digit, is_valid as luhn_is_valid

# ----------------------------
# 1. Generators & validators
# ----------------------------
def gen_base_card():
    prefix = str(random.choice([4, 5, 6]))
    body   = "".join(str(random.randint(0, 9)) for _ in range(14))
    check  = calc_check_digit(prefix + body)
    return prefix + body + check

def gen_invalid_card():
    card = gen_base_card()
    bad   = (int(card[-1]) + random.randint(1, 9)) % 10
    return card[:-1] + str(bad)

def is_valid_card(card):
    nums = "".join(ch for ch in card if ch.isdigit())
    return luhn_is_valid(nums)

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
    nums   = card.replace(' ', '').replace('-', '')
    punct  = random.choice(['.', '/', '_'])
    idx    = random.choice([4, 8, 12])
    return nums[:idx] + punct + nums[idx:]
def masked(card):       return 'XXXX-XXXX-XXXX-' + card[-4:]
def short_card(card):   return ' '.join(card[i:i+4] for i in range(0, 12, 4))
def embedded(card):     return card
def alt_label(card):    return card

VARIATIONS = {
    "plain":        plain,
    "with_spaces":  with_spaces,
    "with_dashes":  with_dashes,
    "with_underscores": with_underscores,
    "mixed":        mixed,
    "ocr":          ocr_spacing,
    "punctuation":  punctuation_sep,
    "masked":       masked,
    "short":        short_card,
    "embedded":     embedded,
    "alt_label":    alt_label,
}

# ----------------------------
# 3. Sentence templates with all context keywords
# ----------------------------
TEMPLATES = {
    "plain": [
        "Use this debit card number {v} in your atm card reader",
        "Your debit card details for online banking are {v}"
    ],
    "with_spaces": [
        "Enter the card number with spaces as {v} when you swipe card",
        "The payment card info appears as {v} at the teller machine"
    ],
    "with_dashes": [
        "You can view the card info with dashes {v} in your card information",
        "The debit card number printed on receipts reads {v}"
    ],
    "with_underscores": [
        "We log card credentials under {v} in secure storage",
        "Enter your card credentials with underscores as {v}"
    ],
    "mixed": [
        "Hybrid ATM card format example shown as {v}",
        "Test entry for card info uses mixed separators {v}"
    ],
    "ocr": [
        "OCR log may read the debit card number as {v}",
        "Scanned debit card info might look like {v}"
    ],
    "punctuation": [
        "Punctuation test in card info example is {v}",
        "The swipe card simulation uses punctuation separated number {v}"
    ],
    "masked": [
        "Masked card credentials appear as {v} for your card information",
        "Only last four digits are visible in card info {v}"
    ],
    "short": [
        "Truncated swipe card number example is {v}",
        "Partial debit card number entry used in card credentials is {v}"
    ],
    "embedded": [
        "For verification my card ends with {v}",
        "The system uses only last four digits {v} for card info checks"
    ],
    "alt_label": [
        "debit card number {v} saved in card details",
        "payment card info {v} is stored under card information"
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_debit_card_variations(count=50):
    records = []
    keys    = list(VARIATIONS.keys())
    while len(records) < count:
        base    = gen_base_card() if random.random() < 0.7 else gen_invalid_card()
        key     = random.choice(keys)
        variant = VARIATIONS[key](base)
        tmpl    = random.choice(TEMPLATES[key])
        text    = tmpl.format(v=variant)
        records.append({
            "text":       text,
            "card":       variant,
            "variation":  key,
            "is_valid":   is_valid_card(variant),
            "fake_data":  True
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_debit_card_variations(count=50)
    with open("debit_cards.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ debit_cards.json generated with full context coverage")
