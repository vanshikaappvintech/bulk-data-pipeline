# #!/usr/bin/env python3
# import random
# import json

# # ----------------------------
# # 1. Bank account generators & validators
# # ----------------------------
# def gen_base_account():
#     """Generate a 14-digit bank account number."""
#     return "".join(str(random.randint(0, 9)) for _ in range(14))

# def is_valid_account(val):
#     """Valid if exactly 14 digits (no separators)."""
#     digits = "".join(ch for ch in val if ch.isdigit())
#     return len(digits) == 14

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain_scientific(acct):
#     """E.g. '1.2345678901234E+13'"""
#     num = int(acct)
#     return f"{num:.5E}"

# def with_spaces(acct):
#     return " ".join(acct[i:i+4] for i in range(0, len(acct), 4))

# def with_dashes(acct):
#     return "-".join(acct[i:i+4] for i in range(0, len(acct), 4))

# def with_underscores(acct):
#     return "_".join(acct[i:i+4] for i in range(0, len(acct), 4))

# def embedded(acct):
#     return acct  # will wrap in sentence

# def leading_zero(acct):
#     return "0" + acct

# def short_acct(acct):
#     return acct[:9]

# def alt_label(acct):
#     return acct  # label added by template

# VARIATIONS = {
#     "plain_scientific": plain_scientific,
#     "with_spaces": with_spaces,
#     "with_dashes": with_dashes,
#     "with_underscores": with_underscores,
#     "embedded": embedded,
#     "leading_zero": leading_zero,
#     "short": short_acct,
#     "alt_label": alt_label,
# }

# # ----------------------------
# # 3. Real-world sentence templates
# # ----------------------------
# TEMPLATES = {
#     "plain_scientific": [
#         "Our system shows your bank account as {v}.",
#         "For bulk transfers use account in scientific form: {v}.",
#     ],
#     "with_spaces": [
#         "Please verify your savings account number: {v}.",
#         "Your account details read as {v}.",
#     ],
#     "with_dashes": [
#         "Corporate bank account on file: {v}.",
#         "The checking account appears as {v}.",
#     ],
#     "with_underscores": [
#         "We log account number under {v}.",
#         "Personal account ID: {v}.",
#     ],
#     "embedded": [
#         "Account no: {v} is linked to your profile.",
#         "Your account number is {v}.",
#     ],
#     "leading_zero": [
#         "Invalid entry starting 0: {v}.",
#         "You prefixed zero to account: {v}.",
#     ],
#     "short": [
#         "Entered only partial account: {v}.",
#         "Short account format: {v}.",
#     ],
#     "alt_label": [
#         "acct no {v} saved as default.",
#         "account # {v} registered.",
#         "a/c no. {v} used for ACH.",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_account_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())

#     while len(records) < count:
#         base = gen_base_account()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)
#         tmpl = random.choice(TEMPLATES[key])
#         text = tmpl.format(v=variant)

#         records.append({
#             "text": text,
#             "account": variant,
#             "variation": key,
#             "is_valid": is_valid_account(variant)
#         })

#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_account_variations(count=50)
#     with open("bank_accounts.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ bank_accounts.json generated with realistic sentences and all variations.")



#!/usr/bin/env python3
import random
import json
import re

# ----------------------------
# 1. Bank account generators & validators
# ----------------------------
def gen_base_account():
    """Generate a 14-digit bank account number."""
    return "".join(str(random.randint(0, 9)) for _ in range(14))

def is_valid_account(val):
    """Valid if exactly 14 digits (no separators)."""
    digits = "".join(ch for ch in val if ch.isdigit())
    return len(digits) == 14

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain_scientific(acct):
    """E.g. '1.2345678901234E+13'"""
    num = int(acct)
    return f"{num:.5E}"

def with_spaces(acct):
    return " ".join(acct[i:i+4] for i in range(0, len(acct), 4))

def with_dashes(acct):
    return "-".join(acct[i:i+4] for i in range(0, len(acct), 4))

def with_underscores(acct):
    return "_".join(acct[i:i+4] for i in range(0, len(acct), 4))

def embedded(acct):
    return acct  # will wrap in sentence

def leading_zero(acct):
    return "0" + acct

def short_acct(acct):
    return acct[:9]

def alt_label(acct):
    return acct  # label added by template

VARIATIONS = {
    "plain_scientific": plain_scientific,
    "with_spaces":      with_spaces,
    "with_dashes":      with_dashes,
    "with_underscores": with_underscores,
    "embedded":         embedded,
    "leading_zero":     leading_zero,
    "short":            short_acct,
    "alt_label":        alt_label,
}

# ----------------------------
# 3. Real-world sentence templates
#    Context keywords: bank account, account number, savings account, current account,
#    checking account, account details, personal account, corporate bank account,
#    account balance, bank account statement
# ----------------------------
TEMPLATES = {
    "plain_scientific": [
        "Our bank account statement shows the account in scientific form as {v}",
        "The account balance in the system is recorded as {v}",
    ],
    "with_spaces": [
        "Your savings account number is {v}",
        "The current account reads as {v}",
        "Please verify your checking account {v}",
    ],
    "with_dashes": [
        "Corporate bank account on file is {v}",
        "The checking account appears as {v}",
        "Your bank account number is displayed as {v}",
    ],
    "with_underscores": [
        "We log personal account under {v}",
        "Enter your corporate bank account id {v} into the account details",
    ],
    "embedded": [
        "Account number {v} is linked to your bank account",
        "Your account {v} is active and shows in account details",
    ],
    "leading_zero": [
        "Invalid entry starting zero for account number {v}",
        "You prefixed zero to bank account {v} which is not allowed",
    ],
    "short": [
        "Entered only partial account details {v}",
        "This is an incomplete bank account number {v}",
    ],
    "alt_label": [
        "Bank account number {v} registered as default",
        "Savings account {v} saved in personal account records",
        "Corporate bank account {v} is set for bulk payments",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_account_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())

    while len(records) < count:
        base    = gen_base_account()
        key     = random.choice(keys)
        variant = VARIATIONS[key](base)
        text    = random.choice(TEMPLATES[key]).format(v=variant)

        records.append({
            "text":      text,
            "account":   variant,
            "variation": key,
            "is_valid":  is_valid_account(variant)
        })

    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_account_variations(count=50)
    with open("bank_accounts.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ bank_accounts.json generated with realistic sentences and full context coverage.")
