#!/usr/bin/env python3
import random
import json
import re

# ----------------------------
# 1. Sample data pools
# ----------------------------
STREETS     = ["MG Road", "Brigade Road", "Park Street", "Linking Road", "Bandra West"]
AREAS       = ["Bandra", "Civil Lines", "Patel Nagar", "Banjara Hills", "Koramangala"]
CITIES      = ["Mumbai", "Bangalore", "Jaipur", "Delhi", "Hyderabad"]
LANDMARKS   = ["HDFC Bank", "Central Mall", "City Park", "Metro Station", "Post Office"]
FLAT_TYPES  = ["Flat", "Apartment", "Block", "Sector"]
PIN_REGEX   = re.compile(r"\b\d{6}\b")

# ----------------------------
# 2. Generators & validity
# ----------------------------
def gen_flat_street():
    flat   = f"{random.choice(FLAT_TYPES)} {random.randint(1, 500)}"
    street = random.choice(STREETS)
    area   = random.choice(AREAS)
    city   = random.choice(CITIES)
    return f"{flat}, {street}, {area}, {city}"

def gen_with_pin():
    num    = random.randint(1,200)
    street = random.choice(STREETS)
    city   = random.choice(CITIES)
    pin    = f"{random.randint(100000, 999999)}"
    return f"{num} {street}, {city} - {pin}"

def gen_with_landmark():
    lm    = random.choice(LANDMARKS)
    area  = random.choice(AREAS)
    city  = random.choice(CITIES)
    return f"Near {lm}, {area}, {city}"

def gen_embedded():
    num  = random.randint(1,200)
    area = random.choice(AREAS)
    city = random.choice(CITIES)
    return f"{num}, {area}, {city}"

def gen_alt_terms():
    num  = random.randint(1,200)
    area = random.choice(AREAS)
    city = random.choice(CITIES)
    return f"{num}/{area}, {city}"

def is_valid_address(addr):
    if PIN_REGEX.search(addr):
        return True
    if re.match(r"^(Flat|Apartment|Block|Sector)\b", addr) and any(c in addr for c in CITIES):
        return True
    return False

VARIATIONS = {
    "flat_street":   gen_flat_street,
    "with_pin":      gen_with_pin,
    "with_landmark": gen_with_landmark,
    "embedded":      gen_embedded,
    "alt_terms":     gen_alt_terms,
}

# ----------------------------
# 3. Templates with ALL context terms
# ----------------------------
TEMPLATES = {
    "flat_street": [
        "Her home address is {v} with house number and street in the city record",
        "Save this permanent address {v} as your residential address proof",
        "The office address line reads {v} in the mailing address book",
    ],
    "with_pin": [
        "Please update your billing address to {v} including the correct pincode",
        "Your current address is recorded as {v} in the address details",
        "This address line {v} includes street, town, state and postal code",
    ],
    "with_landmark": [
        "Our delivery address is {v} in the neighborhood area",
        "The colony entrance is located at {v} for shipment",
        "Locate your flat near landmark {v} when you live at this address",
    ],
    "embedded": [
        "The customer resides at {v} per the address proof",
        "Records show she lives at {v} in the district and mandal directory",
        "Contact mailng address details state {v} under residential address",
    ],
    "alt_terms": [
        "You have registered your apartment as {v} in the personal address",
        "Your residence is {v} in the village and town logs",
        "The address line stored as {v} covers the area and locality info",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_address_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        key  = random.choice(keys)
        addr = VARIATIONS[key]()
        text = random.choice(TEMPLATES[key]).format(v=addr)
        records.append({
            "text":      text,
            "address":   addr,
            "variation": key,
            "is_valid":  is_valid_address(addr)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_address_variations(count=50)
    with open("addresses.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ addresses.json generated with all context terms embedded.")
