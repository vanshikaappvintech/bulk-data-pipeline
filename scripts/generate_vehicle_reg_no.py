#!/usr/bin/env python3
import random
import json
import re
import string

# ----------------------------
# 1. Vehicle registration generators & validators
# ----------------------------
# Valid format: 2 letters (state) + 2 digits (district) + 2 letters (RTO) + 4 digits (unique)
REGEX = re.compile(r'^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$')
STATES = ["MH","DL","KA","TN","UP","GJ","RJ","PB","WB","AP"]

def gen_base_reg():
    state    = random.choice(STATES)
    district = f"{random.randint(1,99):02d}"
    rto      = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
    unique   = f"{random.randint(0,9999):04d}"
    return state + district + rto + unique

def is_valid_reg(val):
    clean = val.replace(" ", "").replace("-", "").upper()
    return bool(REGEX.fullmatch(clean))

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(reg):       return reg
def with_space(reg):  return f"{reg[:2]} {reg[2:4]} {reg[4:6]} {reg[6:]}"
def with_dashes(reg): return f"{reg[:2]}-{reg[2:4]}-{reg[4:6]}-{reg[6:]}"
def lowercase(reg):   return reg.lower()
def embedded(reg):    return reg
def alt_label(reg):   return reg

VARIATIONS = {
    "plain":       plain,
    "with_space":  with_space,
    "with_dashes": with_dashes,
    "lowercase":   lowercase,
    "embedded":    embedded,
    "alt_label":   alt_label,
}

# ----------------------------
# 3. Real-world sentence templates (covering every context)
# ----------------------------
TEMPLATES = {
    "plain": [
        "Your vehicle registration reads {v}.",
        "I’ve updated your registration number to {v} in the automobile records.",
        "The motor vehicle number assigned is {v}.",
    ],
    "with_space": [
        "Please enter the car number as {v}.",
        "Your transport registration appears as {v}.",
        "On your registration plate it shows {v}.",
    ],
    "with_dashes": [
        "Police logs list your bike number as {v}.",
        "The registration plate number for your vehicle is {v}.",
        "We have your motorcycle number recorded as {v}.",
    ],
    "lowercase": [
        "Our system stored the rc number as {v}.",
        "Sometimes the vehicle number appears lowercase like {v}.",
        "For some imports, the license plate number is {v}.",
    ],
    "embedded": [
        "Vehicle No: {v} must match your motor vehicle insurance.",
        "Registration: {v} appears on your transport permit.",
        "Please verify your registration number {v} before border control.",
    ],
    "alt_label": [
        "Registration number {v} will appear on your RC card.",
        "License plate number {v} is needed for toll payments.",
        "Automobile number {v} is linked to your account.",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_reg_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        base    = gen_base_reg()
        key     = random.choice(keys)
        variant = VARIATIONS[key](base)
        tpl     = random.choice(TEMPLATES[key])
        text    = tpl.format(v=variant)
        records.append({
            "text":         text,
            "registration": variant,
            "variation":    key,
            "is_valid":     is_valid_reg(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_reg_variations(count=50)
    with open("vehicle_regs.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ vehicle_regs.json generated with full-context, real-world sentences.")
