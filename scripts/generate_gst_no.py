# #!/usr/bin/env python3
# import random
# import json
# import string
# from stdnum.in_ import gstin

# # ----------------------------
# # 1. GSTIN generators & validators
# # ----------------------------
# def gen_base_gstin_partial():
#     """First 14 chars: state code + PAN + entity + 'Z'."""
#     state   = f"{random.randint(1,35):02d}"
#     pan     = ''.join(random.choice(string.ascii_uppercase) for _ in range(5)) + \
#               ''.join(random.choice(string.digits) for _ in range(4)) + \
#               random.choice(string.ascii_uppercase)
#     entity  = str(random.randint(1, 9))
#     return state + pan + entity + 'Z'

# def complete_gstin(partial14):
#     """
#     Brute-force the 15th character to find a valid GSTIN.
#     Returns full 15-char GSTIN or None if none found (very unlikely).
#     """
#     for ch in string.digits + string.ascii_uppercase:
#         candidate = partial14 + ch
#         if gstin.is_valid(candidate):
#             return candidate
#     return None

# def is_valid_gstin(value):
#     cleaned = value.replace(" ", "").replace("-", "").upper()
#     return gstin.is_valid(cleaned)

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(v):        return v
# def embedded(v):     return v
# def lowercase(v):    return v.lower()
# def with_space(v):   return f"{v[:2]} {v[2:12]} {v[12]} {v[13:]}"
# def alt_label(v):    return v

# VARIATIONS = {
#     "plain":      plain,
#     "embedded":   embedded,
#     "lowercase":  lowercase,
#     "with_space": with_space,
#     "alt_label":  alt_label,
# }

# # ----------------------------
# # 3. Contextual sentence templates
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Our GSTIN is {v}.",
#         "Please share your GST number {v} for registration.",
#         "Enter the company GSTIN: {v}.",
#     ],
#     "embedded": [
#         "GSTIN: {v}.",
#         "Goods and services tax ID is {v}.",
#         "Use GSTIN {v} when filing returns.",
#     ],
#     "lowercase": [
#         "Recorded as gstin {v}.",
#         "Some systems list the gst number as {v}.",
#     ],
#     "with_space": [
#         "Please enter GSTIN with spaces: {v}.",
#         "Enterprise tax ID appears as {v}.",
#     ],
#     "alt_label": [
#         "gst no {v} on file.",
#         "GST account number: {v}.",
#         "Indirect tax ID {v} recorded.",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_gstin_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())
#     while len(records) < count:
#         partial = gen_base_gstin_partial()
#         full = complete_gstin(partial)
#         # If we somehow fail to find a checksum, skip this iteration
#         if not full:
#             continue

#         key     = random.choice(keys)
#         variant = VARIATIONS[key](full)
#         tmpl    = random.choice(TEMPLATES[key])
#         text    = tmpl.format(v=variant)

#         records.append({
#             "text":      text,
#             "gstin":     variant,
#             "variation": key,
#             "is_valid":  is_valid_gstin(variant)
#         })

#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_gstin_variations(count=50)
#     with open("gstin_numbers.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ gstin_numbers.json generated with realistic context and valid GSTINs.")




#!/usr/bin/env python3
import random
import json
import string
from stdnum.in_ import gstin

# ----------------------------
# 1. GSTIN generators & validators
# ----------------------------
def gen_base_gstin_partial():
    """First 14 chars: state code + PAN + entity + 'Z'."""
    state   = f"{random.randint(1,35):02d}"
    pan     = ''.join(random.choice(string.ascii_uppercase) for _ in range(5)) + \
              ''.join(random.choice(string.digits) for _ in range(4)) + \
              random.choice(string.ascii_uppercase)
    entity  = str(random.randint(1, 9))
    return state + pan + entity + 'Z'

def complete_gstin(partial14):
    """
    Brute‐force 15th character to find a valid GSTIN.
    """
    for ch in string.digits + string.ascii_uppercase:
        candidate = partial14 + ch
        if gstin.is_valid(candidate):
            return candidate
    return None

def is_valid_gstin(value):
    cleaned = value.replace(" ", "").replace("-", "").upper()
    return gstin.is_valid(cleaned)

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(v):        return v
def embedded(v):     return v
def lowercase(v):    return v.lower()
def with_space(v):   return f"{v[:2]} {v[2:12]} {v[12]} {v[13:]}"
def alt_label(v):    return v

VARIATIONS = {
    "plain":      plain,
    "embedded":   embedded,
    "lowercase":  lowercase,
    "with_space": with_space,
    "alt_label":  alt_label,
}

# ----------------------------
# 3. Contextual sentence templates
#    Must use all context terms across them:
#    gst, gstin, gst number, gst no, tax id,
#    indirect tax, business id, goods and services tax,
#    company gstin, enterprise tax id, commercial tax id,
#    gst account number
# ----------------------------
TEMPLATES = {
    "plain": [
        "Our gstin is {v} for filing goods and services tax returns",
        "Enter the gst number {v} when you register your business id",
        "Please share company gstin {v} to generate your gst account number",
    ],
    "embedded": [
        "GSTIN: {v} must appear on every invoice as per tax id rules",
        "This company gstin {v} is used for commercial tax id verification",
        "Use {v} as your gst no in enterprise tax id submissions",
    ],
    "lowercase": [
        "Recorded as gstin {v} in lowercase in the system",
        "Some systems list your gst number as {v}",
        "The indirect tax id field shows {v}",
    ],
    "with_space": [
        "Format with spaces as gst in {v} for readability",
        "Enter your enterprise tax id like {v} when prompted",
        "Please enter indirect tax id as {v}",
    ],
    "alt_label": [
        "gst no {v} is on file with the tax department",
        "commercial tax id {v} appears in your profile",
        "gst account number {v} must be updated if changed",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_gstin_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        partial = gen_base_gstin_partial()
        full = complete_gstin(partial)
        if not full:
            continue
        key     = random.choice(keys)
        variant = VARIATIONS[key](full)
        template= random.choice(TEMPLATES[key])
        text    = template.format(v=variant)
        records.append({
            "text":      text,
            "gstin":     variant,
            "variation": key,
            "is_valid":  is_valid_gstin(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_gstin_variations(count=50)
    with open("gstin_numbers.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ gstin_numbers.json generated with all context terms in sentences.")
