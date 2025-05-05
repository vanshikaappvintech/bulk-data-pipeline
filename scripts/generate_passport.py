# #!/usr/bin/env python3
# import random
# import json
# import re
# import string

# # ----------------------------
# # 1. Passport generators & validators
# # ----------------------------
# PASSPORT_REGEX = re.compile(r'^[A-Z][0-9]{7}$')

# def gen_base_passport():
#     """Generate a valid Indian passport: 1 uppercase letter + 7 digits."""
#     letter = random.choice(string.ascii_uppercase)
#     digits = ''.join(str(random.randint(0,9)) for _ in range(7))
#     return letter + digits

# def is_valid_passport(value):
#     """Valid if it matches the 1-letter + 7-digit pattern."""
#     return bool(PASSPORT_REGEX.fullmatch(value))

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(p):
#     return p

# def with_space(p):
#     return p[0:2] + " " + p[2:]

# def with_dashes(p):
#     return p[0:2] + "-" + p[2:]

# def lowercase(p):
#     return p.lower()

# def embedded(p):
#     return p  # wrapped by template

# def alt_label(p):
#     return p  # label applied in template

# VARIATIONS = {
#     "plain": plain,
#     "with_space": with_space,
#     "with_dashes": with_dashes,
#     "lowercase": lowercase,
#     "embedded": embedded,
#     "alt_label": alt_label,
# }

# # ----------------------------
# # 3. Real-world sentence templates
# #    Context keywords: passport, travel document, etc.
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Her passport number is {v}.",
#         "Please record Passport ID {v}.",
#         "Travel document {v} verified at border control.",
#     ],
#     "with_space": [
#         "Enter your travel document as {v}.",
#         "International travel entry: {v}.",
#     ],
#     "with_dashes": [
#         "Border control reads {v}.",
#         "Use passport no. {v} for visa application.",
#     ],
#     "lowercase": [
#         "Stored as passport {v}.",
#         "Some systems display it lowercased: {v}.",
#     ],
#     "embedded": [
#         "My passport {v} expires next year.",
#         "Present your passport {v} at immigration.",
#     ],
#     "alt_label": [
#         "passport no: {v}",
#         "global travel document {v}",
#         "national travel document ID {v}",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_passport_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())
#     while len(records) < count:
#         base = gen_base_passport()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)
#         template = random.choice(TEMPLATES[key])
#         text = template.format(v=variant)
#         records.append({
#             "text":        text,
#             "passport":    variant,
#             "variation":   key,
#             "is_valid":    is_valid_passport(variant)
#         })
#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_passport_variations(count=50)
#     with open("passports.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ passports.json generated with passport variations and real-world sentences.")



#!/usr/bin/env python3
import random
import json
import re
import string

# ----------------------------
# 1. Passport generators & validators
# ----------------------------
PASSPORT_REGEX = re.compile(r'^[A-Z][0-9]{7}$')

def gen_base_passport():
    """Generate a valid Indian passport: 1 uppercase letter + 7 digits."""
    letter = random.choice(string.ascii_uppercase)
    digits = ''.join(str(random.randint(0,9)) for _ in range(7))
    return letter + digits

def is_valid_passport(value):
    """Valid if it matches the 1-letter + 7-digit pattern."""
    return bool(PASSPORT_REGEX.fullmatch(value))

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(p):
    return p

def with_space(p):
    # e.g. "K4 981234"
    return p[0:2] + " " + p[2:]

def with_dashes(p):
    # e.g. "K4-981234"
    return p[0:2] + "-" + p[2:]

def lowercase(p):
    return p.lower()

def embedded(p):
    return p

def alt_label(p):
    return p

VARIATIONS = {
    "plain":       plain,
    "with_space":  with_space,
    "with_dashes": with_dashes,
    "lowercase":   lowercase,
    "embedded":    embedded,
    "alt_label":   alt_label,
}

# ----------------------------
# 3. Real-world sentence templates covering all contexts
# Context terms:
# passport, passport number, travel document, international travel,
# passport id, overseas travel document, travel identification,
# national travel document, border control document, global travel document
# ----------------------------
TEMPLATES = {
    "plain": [
        "Her passport is {v} and the passport number is verified",
        "Please record passport id {v} in your travel document file",
        "This national travel document {v} is valid for international travel",
    ],
    "with_space": [
        "Enter your travel document code as {v} for border control document checks",
        "Your overseas travel document entry is {v} in the system",
    ],
    "with_dashes": [
        "Use global travel document number {v} at immigration",
        "Border control document shows {v} for your passport number",
    ],
    "lowercase": [
        "The passport number appears lowercase as {v} in the database",
        "Some systems list the travel identification as {v}",
    ],
    "embedded": [
        "My passport {v} is due to expire next year during international travel",
        "Present your travel identification {v} at the airport",
    ],
    "alt_label": [
        "passport number {v} will be scanned as a border control document",
        "The national travel document ID {v} is linked to your profile",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_passport_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        base      = gen_base_passport()
        key       = random.choice(keys)
        variant   = VARIATIONS[key](base)
        template  = random.choice(TEMPLATES[key])
        text      = template.format(v=variant)
        records.append({
            "text":      text,
            "passport":  variant,
            "variation": key,
            "is_valid":  is_valid_passport(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_passport_variations(count=50)
    with open("passports.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ passports.json generated with all context terms in real-world sentences.")
