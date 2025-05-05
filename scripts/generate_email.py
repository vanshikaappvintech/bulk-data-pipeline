# #!/usr/bin/env python3
# import random
# import json
# import re

# # ----------------------------
# # 1. Email generators & validators
# # ----------------------------
# LOCAL_NAMES = [
#     "hema", "hemlata", "john.doe", "jane_smith", "alex", "kumar", "patel", "singh"
# ]
# DOMAINS = [
#     "email.com", "domain.in", "gmail.com", "yahoo.com",
#     "outlook.com", "hotmail.com", "sub.domain.co.in", "xyz.in"
# ]
# EMAIL_REGEX = re.compile(
#     r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
# )

# def gen_base_email():
#     """Generate a random plain email: local@domain."""
#     local = random.choice(LOCAL_NAMES)
#     domain = random.choice(DOMAINS)
#     return f"{local}@{domain}"

# def is_valid_email(addr):
#     return bool(EMAIL_REGEX.fullmatch(addr))

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(email):  
#     return email

# def with_dots(email):
#     """Ensure extra dot in local part, e.g. hema.lata@domain.com."""
#     local, domain = email.split('@')
#     if '.' not in local:
#         # insert a dot in the middle
#         idx = len(local)//2
#         local = local[:idx] + '.' + local[idx:]
#     return f"{local}@{domain}"

# def subdomain(email):
#     """Force a subdomain, e.g. user@sub.domain.co.in."""
#     local, _ = email.split('@')
#     return f"{local}@sub.{random.choice(DOMAINS)}"

# def embedded(email):
#     return email  # will be wrapped in sentence

# def alt_label(email):
#     return email  # label applied in template

# VARIATIONS = {
#     "plain": plain,
#     "with_dots": with_dots,
#     "subdomain": subdomain,
#     "embedded": embedded,
#     "alt_label": alt_label,
# }

# # ----------------------------
# # 3. Real-world sentence templates with context keywords
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Her email address is {v}.",
#         "You can reach me at {v}.",
#         "Please send an email to {v}.",
#     ],
#     "with_dots": [
#         "My mail ID is {v}.",
#         "Use this email id: {v}.",
#         "I check my e-mail at {v}.",
#     ],
#     "subdomain": [
#         "Contact me at {v}.",
#         "This is my business email: {v}.",
#         "You can write to me at {v}.",
#     ],
#     "embedded": [
#         "Contact: {v}.",
#         "Mailing contact — {v}.",
#         "Drop an email at {v}.",
#     ],
#     "alt_label": [
#         "official email: {v}",
#         "work email: {v}",
#         "personal email: {v}",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_email_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())
#     while len(records) < count:
#         base = gen_base_email()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)
#         tmpl = random.choice(TEMPLATES[key])
#         text = tmpl.format(v=variant)
#         records.append({
#             "text": text,
#             "email": variant,
#             "variation": key,
#             "is_valid": is_valid_email(variant)
#         })
#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_email_variations(count=50)
#     with open("email_addresses.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ email_addresses.json generated with realistic sentences.")



#!/usr/bin/env python3
import random
import json
import re
import string

# ----------------------------
# 1. Email generators & validators
# ----------------------------
LOCAL_NAMES = [
    "hema", "hemlata", "john.doe", "jane_smith", "alex", "kumar", "patel", "singh"
]
DOMAINS = [
    "email.com", "domain.in", "gmail.com", "yahoo.com",
    "outlook.com", "hotmail.com", "sub.domain.co.in", "xyz.in"
]
EMAIL_REGEX = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

def gen_base_email():
    local  = random.choice(LOCAL_NAMES)
    domain = random.choice(DOMAINS)
    return f"{local}@{domain}"

def is_valid_email(addr):
    return bool(EMAIL_REGEX.fullmatch(addr))

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(email):        return email
def with_dots(email):
    local, dom = email.split("@")
    if "." not in local:
        i = len(local)//2
        local = local[:i] + "." + local[i:]
    return f"{local}@{dom}"
def subdomain(email):
    local, _ = email.split("@")
    return f"{local}@sub.{random.choice(DOMAINS)}"
def embedded(email):     return email
def alt_label(email):    return email

VARIATIONS = {
    "plain":     plain,
    "with_dots": with_dots,
    "subdomain": subdomain,
    "embedded":  embedded,
    "alt_label": alt_label,
}

# ----------------------------
# 3. Sentence templates covering ALL context keywords:
# email, mail, email address, contact me at, email id, e-mail,
# official email, personal email, business email, work email,
# mail id, mail address, send an email, reach me at, drop an email,
# mailing contact, message via email, write to me at, email contact,
# gmail, google mail, yahoo mail, yahoo, outlook, hotmail
# ----------------------------
TEMPLATES = {
    "plain": [
        "Her email address is {v} so you can reach me at that contact",
        "Please send an email to {v} as this is my official email",
        "You can reach me at {v} and it serves as my mail address",
    ],
    "with_dots": [
        "My email id is {v} and it works for e-mail alerts",
        "Use mail id {v} for business email correspondence",
        "I check my personal email at {v}",
    ],
    "subdomain": [
        "Contact me at {v} when you need to message via email",
        "This is my work email: {v} for customer inquiries",
        "Write to me at {v} for any email contact",
    ],
    "embedded": [
        "Drop an email at {v} and I will reply promptly",
        "Mailing contact is {v} if you need to get in touch",
        "Reach me at {v} for any google mail or gmail questions",
    ],
    "alt_label": [
        "official email: {v}",
        "business email: {v}",
        "hotmail users can write to me at {v}",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_email_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        base    = gen_base_email()
        key     = random.choice(keys)
        variant = VARIATIONS[key](base)
        text    = random.choice(TEMPLATES[key]).format(v=variant)
        records.append({
            "text":      text,
            "email":     variant,
            "variation": key,
            "is_valid":  is_valid_email(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_email_variations(count=50)
    with open("email_addresses.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ email_addresses.json generated with all context keywords in sentences.")
