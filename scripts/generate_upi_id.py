# #!/usr/bin/env python3
# import random
# import json
# import re

# # ----------------------------
# # 1. UPI ID generators & validators
# # ----------------------------
# # Basic regex for VPA (username@bank); allows letters, digits, dots, underscores in username
# UPI_REGEX = re.compile(r'^[a-zA-Z0-9._]{3,256}@[a-zA-Z]{3,64}$')

# BANK_DOMAINS = [
#     "oksbi", "okaxis", "okhdfcbank", "okicici", "okpaytm",
#     "oksbi", "okyes", "okkotak", "okpnb", "okunion"
# ]

# def gen_base_upi():
#     """Generate a plain UPI ID: username@bank."""
#     user = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(6))
#     domain = random.choice(BANK_DOMAINS)
#     return f"{user}@{domain}"

# def is_valid_upi(vpa: str) -> bool:
#     """Validate VPA against a basic regex; no checksum exists."""
#     return bool(UPI_REGEX.fullmatch(vpa))

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(vpa):
#     return vpa

# def with_dots(vpa):
#     user, domain = vpa.split('@')
#     # insert random dots in username
#     parts = [user[i:i+2] for i in range(0, len(user), 2)]
#     return '.'.join(parts) + '@' + domain

# def with_digits(vpa):
#     user, domain = vpa.split('@')
#     # append 2–4 random digits
#     digits = ''.join(str(random.randint(0,9)) for _ in range(random.randint(2,4)))
#     return user + digits + '@' + domain

# def embedded(vpa):
#     return vpa  # will wrap in sentence

# def alt_label(vpa):
#     return vpa  # label applied by template

# VARIATIONS = {
#     "plain": plain,
#     "with_dots": with_dots,
#     "with_digits": with_digits,
#     "embedded": embedded,
#     "alt_label": alt_label,
# }

# # ----------------------------
# # 3. Real-world sentence templates
# #    Context keywords: upi id, payment id, unified payment interface, etc.
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Her UPI ID is {v}.",
#         "You can use payment ID {v} for transfers.",
#         "Send via unified payment interface to {v}.",
#     ],
#     "with_dots": [
#         "Please send to VPA {v}.",
#         "Use virtual payment address {v}.",
#         "Pay via UPI handle {v}.",
#     ],
#     "with_digits": [
#         "My UPI address is {v}.",
#         "For quick payment, use {v}.",
#     ],
#     "embedded": [
#         "Send to UPI {v}.",
#         "Payment through UPI ID {v}.",
#     ],
#     "alt_label": [
#         "upi id: {v}",
#         "upi account id {v}",
#         "upi address {v}",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_upi_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())
#     while len(records) < count:
#         base = gen_base_upi()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)
#         tmpl = random.choice(TEMPLATES[key])
#         text = tmpl.format(v=variant)
#         records.append({
#             "text": text,
#             "upi_id": variant,
#             "variation": key,
#             "is_valid": is_valid_upi(variant)
#         })
#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_upi_variations(count=50)
#     with open("upi_ids.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ upi_ids.json generated with realistic sentences and validity flags.")



#!/usr/bin/env python3
import random
import json
import re
import string

# ----------------------------
# 1. UPI ID generators & validators
# ----------------------------
# Basic VPA regex: 3–256 chars username (letters/digits/._), then @, then 3–64 letters
UPI_REGEX = re.compile(r'^[a-zA-Z0-9._]{3,256}@[a-zA-Z]{3,64}$')

BANK_DOMAINS = [
    "oksbi", "okaxis", "okhdfcbank", "okicici", "okpaytm",
    "okyes", "okkotak", "okpnb", "okunion"
]

def gen_base_upi():
    user = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    domain = random.choice(BANK_DOMAINS)
    return f"{user}@{domain}"

def is_valid_upi(vpa: str) -> bool:
    return bool(UPI_REGEX.fullmatch(vpa))

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(vpa):       return vpa
def with_dots(vpa):
    user, dom = vpa.split('@')
    # insert one dot after 2nd character
    return user[:2] + '.' + user[2:] + '@' + dom
def with_digits(vpa):
    user, dom = vpa.split('@')
    extra = ''.join(str(random.randint(0,9)) for _ in range(3))
    return user + extra + '@' + dom
def embedded(vpa):    return vpa
def alt_label(vpa):   return vpa

VARIATIONS = {
    "plain":       plain,
    "with_dots":   with_dots,
    "with_digits": with_digits,
    "embedded":    embedded,
    "alt_label":   alt_label,
}

# ----------------------------
# 3. Sentence templates
#    We include every one of:
#      "upi id", "payment id", "upi", "unified payment interface",
#      "vpa", "virtual payment address", "upi account id",
#      "upi transaction id", "upi handle", "upi address"
# ----------------------------
TEMPLATES = {
    "plain": [
        "Her upi id is {v} so you can make payment id transfers",
        "This vpa {v} works over the unified payment interface",
        "Save this upi address {v} in your mobile",
    ],
    "with_dots": [
        "Use the virtual payment address {v} when you send money",
        "For quick pay, enter upi handle {v}",
        "My upi account id is {v} for any peer to peer transfer",
    ],
    "with_digits": [
        "Please use upi {v} to complete the transaction",
        "When you request payment, use upi transaction id via {v}",
        "Enter this payment id {v} in your banking app",
    ],
    "embedded": [
        "Send funds through upi id {v} right now",
        "I receive alerts on vpa {v}",
        "Payment through upi handle {v} succeeded",
    ],
    "alt_label": [
        "upi id: {v} saved in my profile",
        "virtual payment address {v} is linked to my account",
        "use this upi address {v} for any transfer",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_upi_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        base    = gen_base_upi()
        key     = random.choice(keys)
        variant = VARIATIONS[key](base)
        text    = random.choice(TEMPLATES[key]).format(v=variant)
        records.append({
            "text":       text,
            "upi_id":     variant,
            "variation":  key,
            "is_valid":   is_valid_upi(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_upi_variations(count=50)
    with open("upi_ids.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ upi_ids.json generated with all context keywords in real-world sentences.")
