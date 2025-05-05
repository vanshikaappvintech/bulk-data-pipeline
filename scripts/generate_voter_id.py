# #!/usr/bin/env python3
# import random
# import json
# import string
# import re

# # ----------------------------
# # 1. Voter ID (EPIC) generators & validators
# # ----------------------------
# # Valid EPIC: 3 letters (A–Z) + 7 digits
# EPIC_REGEX = re.compile(r'^[A-Z]{3}[0-9]{7}$', re.IGNORECASE)

# def gen_base_epic():
#     """Generate a valid EPIC: 3 uppercase letters + 7 digits."""
#     letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
#     digits  = ''.join(str(random.randint(0, 9)) for _ in range(7))
#     return letters + digits

# def is_valid_epic(value):
#     """Valid if it matches the EPIC pattern (case‐insensitive)."""
#     return bool(EPIC_REGEX.fullmatch(value.replace(" ", "").replace("-", "")))

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(epic):
#     return epic

# def with_space(epic):
#     return epic[:3] + " " + epic[3:]

# def with_dashes(epic):
#     return epic[:3] + "-" + epic[3:]

# def lowercase(epic):
#     return epic.lower()

# def embedded(epic):
#     return epic  # will be wrapped in full sentence

# def alt_label(epic):
#     return epic  # label applied in template

# VARIATIONS = {
#     "plain":       plain,
#     "with_space":  with_space,
#     "with_dashes": with_dashes,
#     "lowercase":   lowercase,
#     "embedded":    embedded,
#     "alt_label":   alt_label,
# }

# # ----------------------------
# # 3. Contextual sentence templates
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Her voter ID is {v}.",
#         "Please record EPIC number {v}.",
#         "Electoral ID {v} verified.",
#     ],
#     "with_space": [
#         "Enter your voter id like {v}.",
#         "Your EPIC recorded as {v}.",
#     ],
#     "with_dashes": [
#         "Election commission ID: {v}.",
#         "Use voter card number {v}.",
#     ],
#     "lowercase": [
#         "Recorded as voter id {v}.",
#         "Some systems list epic as {v}.",
#     ],
#     "embedded": [
#         "EPIC ID is {v}.",
#         "Your election identity {v} is confirmed.",
#     ],
#     "alt_label": [
#         "voter card {v} on file.",
#         "citizen voter id {v} recorded.",
#         "election identity number {v}.",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_epic_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())
#     while len(records) < count:
#         base = gen_base_epic()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)
#         tmpl = random.choice(TEMPLATES[key])
#         text = tmpl.format(v=variant)
#         records.append({
#             "text":       text,
#             "voter_id":   variant,
#             "variation":  key,
#             "is_valid":   is_valid_epic(variant)
#         })
#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_epic_variations(count=50)
#     with open("voter_ids.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ voter_ids.json generated with EPIC variations and context-rich sentences.")



# #!/usr/bin/env python3
# import random
# import json
# import string
# import re

# # ----------------------------
# # 1. Voter ID (EPIC) generators & validators
# # ----------------------------
# # Valid EPIC: 3 letters (A–Z) + 7 digits
# EPIC_REGEX = re.compile(r'^[A-Z]{3}[0-9]{7}$', re.IGNORECASE)

# def gen_base_epic():
#     letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
#     digits  = ''.join(str(random.randint(0, 9)) for _ in range(7))
#     return letters + digits

# def is_valid_epic(value):
#     cleaned = value.replace(" ", "").replace("-", "")
#     return bool(EPIC_REGEX.fullmatch(cleaned))

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(epic):        return epic
# def with_space(epic):   return epic[:3] + " " + epic[3:]
# def with_dashes(epic):  return epic[:3] + "-" + epic[3:]
# def lowercase(epic):    return epic.lower()
# def embedded(epic):     return epic
# def alt_label(epic):    return epic

# VARIATIONS = {
#     "plain":       plain,
#     "with_space":  with_space,
#     "with_dashes": with_dashes,
#     "lowercase":   lowercase,
#     "embedded":    embedded,
#     "alt_label":   alt_label,
# }

# # ----------------------------
# # 3. Real-world sentence templates including every context term
# # Context terms:
# # "voter id", "epic", "electoral", "voting", "election", 
# # "voter card", "election commission id", "citizen voter id", 
# # "election identity", "voter registration number"
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Please enter your voter id {v} to complete voting registration",
#         "Your electoral EPIC {v} is on record for the upcoming election",
#         "The citizen voter id {v} matches your voter registration number",
#     ],
#     "with_space": [
#         "Enter EPIC with space as {v} when filling the voter card form",
#         "The election commission id recorded is {v} for your profile",
#     ],
#     "with_dashes": [
#         "Use the voter card number {v} at the polling booth",
#         "Your election identity code is {v} in the system",
#     ],
#     "lowercase": [
#         "System stored epic in lowercase as {v} in your electoral record",
#         "Check your voter id in lowercase: {v} for mobile voting",
#     ],
#     "embedded": [
#         "Your voting profile shows EPIC ID is {v} for device authentication",
#         "Please verify that your election identity {v} is correct",
#     ],
#     "alt_label": [
#         "Voter registration number {v} will be used at the election commission",
#         "Citizen voter id {v} appears on your voter card",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_epic_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())
#     while len(records) < count:
#         base = gen_base_epic()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)
#         text = random.choice(TEMPLATES[key]).replace("{v}", variant)
#         records.append({
#             "text":       text,
#             "voter_id":   variant,
#             "variation":  key,
#             "is_valid":   is_valid_epic(variant)
#         })
#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_epic_variations(count=50)
#     with open("voter_ids.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ voter_ids.json generated with all contexts included in real-world sentences.")




#!/usr/bin/env python3
import random
import json
import string
from stdnum.in_.epic import is_valid as epic_is_valid

# ----------------------------
# 1. Voter ID (EPIC) generators & validators
# ----------------------------
# Valid EPIC: use stdnum.in_.epic.is_valid
def gen_base_epic():
    letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    digits  = ''.join(str(random.randint(0, 9)) for _ in range(7))
    return letters + digits

def is_valid_epic(value):
    # strip any separators
    cleaned = value.replace(" ", "").replace("-", "")
    return epic_is_valid(cleaned)

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(epic):        return epic
def with_space(epic):   return epic[:3] + " " + epic[3:]
def with_dashes(epic):  return epic[:3] + "-" + epic[3:]
def lowercase(epic):    return epic.lower()
def embedded(epic):     return epic
def alt_label(epic):    return epic

VARIATIONS = {
    "plain":       plain,
    "with_space":  with_space,
    "with_dashes": with_dashes,
    "lowercase":   lowercase,
    "embedded":    embedded,
    "alt_label":   alt_label,
}

# ----------------------------
# 3. Real-world sentence templates
# ----------------------------
TEMPLATES = {
    "plain": [
        "Please enter your voter id {v} to complete voting registration",
        "Your electoral EPIC {v} is on record for the upcoming election",
        "The citizen voter id {v} matches your voter registration number",
    ],
    "with_space": [
        "Enter EPIC with space as {v} when filling the voter card form",
        "The election commission id recorded is {v} for your profile",
    ],
    "with_dashes": [
        "Use the voter card number {v} at the polling booth",
        "Your election identity code is {v} in the system",
    ],
    "lowercase": [
        "System stored epic in lowercase as {v} in your electoral record",
        "Check your voter id in lowercase: {v} for mobile voting",
    ],
    "embedded": [
        "Your voting profile shows EPIC ID is {v} for device authentication",
        "Please verify that your election identity {v} is correct",
    ],
    "alt_label": [
        "Voter registration number {v} will be used at the election commission",
        "Citizen voter id {v} appears on your voter card",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_epic_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        base    = gen_base_epic()
        key     = random.choice(keys)
        variant = VARIATIONS[key](base)
        text    = random.choice(TEMPLATES[key]).format(v=variant)
        records.append({
            "text":      text,
            "voter_id":  variant,
            "variation": key,
            "is_valid":  is_valid_epic(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_epic_variations(count=50)
    with open("voter_ids.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ voter_ids.json generated with stdnum.in_.epic validation")
