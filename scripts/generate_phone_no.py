# #!/usr/bin/env python3
# import random
# import json

# # ----------------------------
# # 1. Phone number generators & validators
# # ----------------------------
# def gen_plain_phone():
#     """Generate a valid 10-digit Indian phone (starts with 6–9)."""
#     first = str(random.randint(6, 9))
#     rest = "".join(str(random.randint(0, 9)) for _ in range(9))
#     return first + rest

# def is_valid_phone(raw):
#     """Consider valid if 10 digits starting 6–9, or +91 formats."""
#     digits = "".join(ch for ch in raw if ch.isdigit())
#     if len(digits) == 10 and digits[0] in "6789":
#         return True
#     if len(digits) == 12 and digits.startswith("91") and digits[2] in "6789":
#         return True
#     return False

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(phone):
#     return phone

# def country_scientific(phone):
#     """Represent +91<phone> in scientific E notation."""
#     num = int("91" + phone)
#     # e.g. '9.1234567890E+11'
#     return f"{num:.10E}"

# def no_plus_scientific(phone):
#     """Same scientific form but without '+' (invalid)."""
#     s = country_scientific(phone)
#     return s.lstrip('+')

# def leading_zero(phone):
#     """Prepend a zero (invalid)."""
#     return "0" + phone

# def spaced(phone):
#     """+91 98765 43210"""
#     return f"+91 {phone[:5]} {phone[5:]}"

# def dashed(phone):
#     """987-654-3210 (invalid format)"""
#     return f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"

# def plus_dashed(phone):
#     """+91-9876543210"""
#     return f"+91-{phone}"

# def embedded(phone):
#     return phone  # sentence will wrap it

# VARIATIONS = {
#     "plain": plain,
#     "country_scientific": country_scientific,
#     "no_plus_scientific": no_plus_scientific,
#     "leading_zero": leading_zero,
#     "spaced": spaced,
#     "dashed": dashed,
#     "plus_dashed": plus_dashed,
#     "embedded": embedded,
# }

# # ----------------------------
# # 3. Sentence templates
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Her phone number is {v}.",
#         "You can reach her at {v}.",
#     ],
#     "country_scientific": [
#         "In Excel it appears as {v}.",
#         "System reads her contact as {v}.",
#     ],
#     "no_plus_scientific": [
#         "Without plus it shows {v}.",
#         "Mis-notated like {v}.",
#     ],
#     "leading_zero": [
#         "With leading zero: {v}.",
#         "Invalid form {v}.",
#     ],
#     "spaced": [
#         "Formatted with spaces: {v}.",
#         "International style: {v}.",
#     ],
#     "dashed": [
#         "Dashed format: {v}.",
#         "ID-like reading: {v}.",
#     ],
#     "plus_dashed": [
#         "Prefixed with plus and dash: {v}.",
#         "Call format: {v}.",
#     ],
#     "embedded": [
#         "Please dial {v} to connect.",
#         "Call me at {v}.",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_phone_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())

#     while len(records) < count:
#         base = gen_plain_phone()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)

#         tmpl = random.choice(TEMPLATES[key])
#         text = tmpl.format(v=variant)

#         records.append({
#             "text": text,
#             "phone": variant,
#             "variation": key,
#             "is_valid": is_valid_phone(variant)
#         })

#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_phone_variations(count=50)
#     with open("phone_numbers.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ phone_numbers.json generated with 20 permutations of Indian phone variations.")




#----------with real world context based sentences ---------------
# #!/usr/bin/env python3
# import random
# import json

# # ----------------------------
# # 1. Phone number generators & validators
# # ----------------------------
# def gen_plain_phone():
#     """Generate a valid 10-digit Indian phone (starts with 6–9)."""
#     first = str(random.randint(6, 9))
#     rest = "".join(str(random.randint(0, 9)) for _ in range(9))
#     return first + rest

# def is_valid_phone(raw):
#     """Valid if 10 digits starting 6–9, or +91 formats."""
#     digits = "".join(ch for ch in raw if ch.isdigit())
#     if len(digits) == 10 and digits[0] in "6789":
#         return True
#     if len(digits) == 12 and digits.startswith("91") and digits[2] in "6789":
#         return True
#     return False

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(phone):             return phone
# def country_scientific(phone): return f"{int('91'+phone):.10E}"
# def no_plus_scientific(phone): return country_scientific(phone).lstrip('+')
# def leading_zero(phone):      return "0" + phone
# def spaced(phone):            return f"+91 {phone[:5]} {phone[5:]}"
# def dashed(phone):            return f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
# def plus_dashed(phone):       return f"+91-{phone}"
# def embedded(phone):          return phone

# VARIATIONS = {
#     "plain": plain,
#     "country_scientific": country_scientific,
#     "no_plus_scientific": no_plus_scientific,
#     "leading_zero": leading_zero,
#     "spaced": spaced,
#     "dashed": dashed,
#     "plus_dashed": plus_dashed,
#     "embedded": embedded,
# }

# # ----------------------------
# # 3. Real-world sentence templates with context keywords
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Her phone number is {v}.",
#         "You can reach her mobile at {v}.",
#         "For any query, text me on {v}.",
#     ],
#     "country_scientific": [
#         "The contact appears in Excel as {v}.",
#         "System logs mobile number as {v}.",
#     ],
#     "no_plus_scientific": [
#         "Invalid SMS number format: {v}.",
#         "Mis-notated telephone number: {v}.",
#     ],
#     "leading_zero": [
#         "You accidentally added a zero: {v}.",
#         "Emergency contact entered as {v}.",
#     ],
#     "spaced": [
#         "Customer service number: {v}.",
#         "Our helpline is available at {v}.",
#     ],
#     "dashed": [
#         "Use this cell phone for voice calls: {v}.",
#         "Please dial {v} for assistance.",
#     ],
#     "plus_dashed": [
#         "Your WhatsApp number is set to {v}.",
#         "We have registered your communication number as {v}.",
#     ],
#     "embedded": [
#         "Call me at {v}.",
#         "Message me on {v}.",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_phone_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())

#     while len(records) < count:
#         base = gen_plain_phone()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)
#         tmpl = random.choice(TEMPLATES[key])
#         text = tmpl.format(v=variant)
#         records.append({
#             "text": text,
#             "phone": variant,
#             "variation": key,
#             "is_valid": is_valid_phone(variant)
#         })

#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_phone_variations(count=50)
#     with open("phone_numbers.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ phone_numbers.json generated with rich, real-world sentences.")






# #!/usr/bin/env python3
# import random
# import json

# # ----------------------------
# # 1. Phone number generators & validators
# # ----------------------------
# def gen_plain_phone():
#     """Generate a valid 10-digit Indian phone number (starts with 6–9)."""
#     first = str(random.randint(6, 9))
#     rest  = "".join(str(random.randint(0, 9)) for _ in range(9))
#     return first + rest

# def is_valid_phone(raw):
#     """Valid if 10 digits starting 6–9, or +91 formats with correct prefix."""
#     digits = "".join(ch for ch in raw if ch.isdigit())
#     if len(digits) == 10 and digits[0] in "6789":
#         return True
#     if len(digits) == 12 and digits.startswith("91") and digits[2] in "6789":
#         return True
#     return False

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(phone):             
#     return phone

# def country_scientific(phone):
#     """Excel/scientific: +91<phone> in E notation."""
#     num = int("91" + phone)
#     return f"{num:.10E}"

# def no_plus_scientific(phone):
#     """Scientific without leading '+': invalid."""
#     return country_scientific(phone).lstrip('+')

# def leading_zero(phone):
#     """Invalid: extra leading zero."""
#     return "0" + phone

# def spaced(phone):
#     """International style with spaces."""
#     return f"+91 {phone[:5]} {phone[5:]}"

# def dashed(phone):
#     """Grouped with dashes."""
#     return f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"

# def plus_dashed(phone):
#     """+91-prefixed with dash."""
#     return f"+91-{phone}"

# def embedded(phone):
#     """Raw phone; sentence will embed it."""
#     return phone

# VARIATIONS = {
#     "plain": plain,
#     "country_scientific": country_scientific,
#     "no_plus_scientific": no_plus_scientific,
#     "leading_zero": leading_zero,
#     "spaced": spaced,
#     "dashed": dashed,
#     "plus_dashed": plus_dashed,
#     "embedded": embedded,
# }

# # ----------------------------
# # 3. Real-world sentence templates using context keywords
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Her mobile number is {v}.",
#         "You can reach her on this phone number: {v}.",
#         "For quick updates, text me at {v}.",
#     ],
#     "country_scientific": [
#         "In our database the contact is stored as {v}.",
#         "The system logs your communication number as {v}.",
#         "Imported into Excel as {v}.",
#     ],
#     "no_plus_scientific": [
#         "The SMS gateway misreads it as {v}.",
#         "Invalid telephone number format detected: {v}.",
#         "Cannot send SMS to {v}.",
#     ],
#     "leading_zero": [
#         "Emergency contact must be 10 digits; yours is recorded as {v}.",
#         "Customer service number entered incorrectly as {v}.",
#         "Please remove the extra zero from {v}.",
#     ],
#     "spaced": [
#         "Our helpline number is {v}.",
#         "Call our customer service at {v}.",
#         "We’re available on WhatsApp at {v}.",
#     ],
#     "dashed": [
#         "For voice calls use cell number {v}.",
#         "Dial {v} to reach the call me service.",
#         "Your telephone number is {v} for support.",
#     ],
#     "plus_dashed": [
#         "Your WhatsApp number is set to {v}.",
#         "We have registered your mobile number as {v}.",
#         "Use {v} for emergency contact.",
#     ],
#     "embedded": [
#         "Call me at {v}.",
#         "Message me on {v}.",
#         "Send an SMS to {v}.",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_phone_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())
#     while len(records) < count:
#         base = gen_plain_phone()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)
#         template = random.choice(TEMPLATES[key])
#         text = template.format(v=variant)
#         records.append({
#             "text": text,
#             "phone": variant,
#             "variation": key,
#             "is_valid": is_valid_phone(variant)
#         })
#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_phone_variations(count=50)
#     with open("phone_numbers.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ phone_numbers.json generated with realistic sentences.")




#!/usr/bin/env python3
import random
import json

# ----------------------------
# 1. Phone number generators & validators
# ----------------------------
def gen_plain_phone():
    """Generate a valid 10-digit Indian phone number (starts with 6–9)."""
    first = str(random.randint(6, 9))
    rest  = "".join(str(random.randint(0, 9)) for _ in range(9))
    return first + rest

def is_valid_phone(raw):
    """Valid if 10 digits starting 6–9, or +91 formats with correct prefix."""
    digits = "".join(ch for ch in raw if ch.isdigit())
    if len(digits) == 10 and digits[0] in "6789":
        return True
    if len(digits) == 12 and digits.startswith("91") and digits[2] in "6789":
        return True
    return False

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(phone):             
    return phone

def country_scientific(phone):
    num = int("91" + phone)
    return f"{num:.10E}"

def no_plus_scientific(phone):
    return country_scientific(phone).lstrip('+')

def leading_zero(phone):
    return "0" + phone

def spaced(phone):
    return f"+91 {phone[:5]} {phone[5:]}"

def dashed(phone):
    return f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"

def plus_dashed(phone):
    return f"+91-{phone}"

def embedded(phone):
    return phone

VARIATIONS = {
    "plain":               plain,
    "country_scientific":  country_scientific,
    "no_plus_scientific":  no_plus_scientific,
    "leading_zero":        leading_zero,
    "spaced":              spaced,
    "dashed":              dashed,
    "plus_dashed":         plus_dashed,
    "embedded":            embedded,
}

# ----------------------------
# 3. Real-world sentence templates with **all** context keywords**
#     context = [
#       "phone number", "mobile", "contact", "call me", "mobile number",
#       "text me", "message me", "cell number", "cell phone",
#       "whatsapp number", "sms number", "voice call number",
#       "communication number", "customer service number",
#       "helpline number", "emergency contact", "emergency number",
#       "telephone number"
#     ]
# ----------------------------
TEMPLATES = {
    "plain": [
        "Her mobile number is {v} and you can call me on this telephone number",
        "Please save this phone number {v} as your emergency contact",
        "This mobile number {v} is also our customer service number",
    ],
    "country_scientific": [
        "In the system the communication number appears as {v}",
        "Our database stores your telephone number as {v}",
        "Imported into Excel as {v} for sms number logs",
    ],
    "no_plus_scientific": [
        "SMS dispatch failed to {v} because the format lacks a plus sign",
        "Invalid phone number format {v} cannot be used for sms number",
        "Cannot send message me to {v} due to missing country code",
    ],
    "leading_zero": [
        "I tried to call me at {v} but it shows an extra zero error",
        "Your voice call number entry {v} is invalid with a leading zero",
        "The cell number {v} must not start with zero for voice call number",
    ],
    "spaced": [
        "Our helpline number is {v} on WhatsApp number directory",
        "For quick support text me on {v} as an sms number",
        "We answer on our whatsapp number {v} 24x7",
    ],
    "dashed": [
        "Dial our cell phone at {v} for immediate assistance",
        "For voice call number support use {v} today",
        "The helpline number to contact is {v}",
    ],
    "plus_dashed": [
        "Use whatsapp number {v} to message me",
        "We have registered this mobile number as {v}",
        "Emergency number {v} is active for urgent contact",
    ],
    "embedded": [
        "Call me at {v} if you need any assistance",
        "Send SMS to {v} as an sms number for updates",
        "Text me on {v} to get your verification code",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_phone_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        base    = gen_plain_phone()
        key     = random.choice(keys)
        variant = VARIATIONS[key](base)
        text    = random.choice(TEMPLATES[key]).format(v=variant)
        records.append({
            "text":       text,
            "phone":      variant,
            "variation":  key,
            "is_valid":   is_valid_phone(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_phone_variations(count=50)
    with open("phone_numbers.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ phone_numbers.json generated with all context keywords in real-world sentences.")
