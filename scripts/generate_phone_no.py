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
