# #!/usr/bin/env python3
# import random
# import json
# import re

# # ----------------------------
# # 1. MAC address generator & validator
# # ----------------------------
# MAC_REGEX = re.compile(r'^([0-9A-F]{2}:){5}[0-9A-F]{2}$', re.IGNORECASE)

# def gen_base_mac():
#     """Generate a random MAC address (6 octets)."""
#     return ":".join(f"{random.randint(0,255):02X}" for _ in range(6))

# def is_valid_mac(value):
#     """Valid if it matches six hex pairs separated by colons."""
#     return bool(MAC_REGEX.fullmatch(value.strip()))

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(mac):
#     return mac.upper()

# def with_space(mac):
#     # replace second colon and onward with spaces
#     parts = mac.split(":")
#     return ":".join(parts[:2]) + " " + " ".join(parts[2:])

# def with_dashes(mac):
#     return "-".join(mac.split(":"))

# def lowercase(mac):
#     return mac.lower()

# def embedded(mac):
#     return mac.upper()

# def alt_label(mac):
#     return mac.upper()

# VARIATIONS = {
#     "plain": plain,
#     "with_space": with_space,
#     "with_dashes": with_dashes,
#     "lowercase": lowercase,
#     "embedded": embedded,
#     "alt_label": alt_label,
# }

# # ----------------------------
# # 3. Contextual sentence templates
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "The device’s MAC address is {v}.",
#         "Check the network address of this interface: {v}.",
#         "Your hardware address reads {v}.",
#     ],
#     "with_space": [
#         "Inspect the ethernet address: {v}.",
#         "Use this LAN address for diagnostics: {v}.",
#         "Device address shown as {v} in logs.",
#     ],
#     "with_dashes": [
#         "On Bluetooth setup, it shows {v}.",
#         "Wi-Fi hardware address: {v}.",
#         "Media Access Control entry: {v}.",
#     ],
#     "lowercase": [
#         "The mac address recorded is {v}.",
#         "Your device address appears lowercase: {v}.",
#         "Check the network address field: {v}.",
#     ],
#     "embedded": [
#         "Please verify the device using MAC address {v}.",
#         "Confirm the ethernet address {v} before provisioning.",
#         "Assign VLAN to hardware address {v}.",
#     ],
#     "alt_label": [
#         "Device MAC ID: {v}.",
#         "Media access control ID is {v}.",
#         "Bluetooth address recorded as {v}.",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_mac_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())
#     while len(records) < count:
#         base = gen_base_mac()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)
#         tmpl = random.choice(TEMPLATES[key])
#         text = tmpl.format(v=variant)
#         records.append({
#             "text":       text,
#             "mac":        variant,
#             "variation":  key,
#             "is_valid":   is_valid_mac(variant)
#         })
#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_mac_variations(count=50)
#     with open("mac_addresses.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ mac_addresses.json generated with MAC variations and context-rich sentences.")



#!/usr/bin/env python3
import random
import json
import re

# ----------------------------
# 1. MAC address generator & validator
# ----------------------------
MAC_REGEX = re.compile(r'^([0-9A-F]{2}:){5}[0-9A-F]{2}$')

def gen_base_mac():
    """Generate a valid MAC: 6 uppercase hex byte pairs separated by colons."""
    return ":".join(f"{random.randint(0, 255):02X}" for _ in range(6))

def is_valid_mac(val):
    """Normalize to uppercase colon format and test."""
    cleaned = val.replace("-", ":").replace(" ", ":").upper()
    # collapse multiple colons/spaces into single colon separators
    parts = [p for p in re.split(r'[:\s\-]+', cleaned) if p]
    if len(parts) != 6:
        return False
    candidate = ":".join(parts)
    return bool(MAC_REGEX.fullmatch(candidate))

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(mac):
    return mac  # e.g. "00:1A:2B:3C:4D:5E"

def with_space(mac):
    parts = mac.split(":")
    # first separator stays colon, rest become spaces
    return parts[0] + ":" + " ".join(parts[1:])

def with_dashes(mac):
    return "-".join(mac.split(":"))

def lowercase(mac):
    return mac.lower()

def embedded(mac):
    return mac  # will be wrapped in sentence

def alt_label(mac):
    return mac  # template will prepend "Device MAC ID"

VARIATIONS = {
    "plain": plain,
    "with_space": with_space,
    "with_dashes": with_dashes,
    "lowercase": lowercase,
    "embedded": embedded,
    "alt_label": alt_label,
}

# ----------------------------
# 3. Real-world sentence templates
#    Context: mac address, ethernet address, network address, etc.
# ----------------------------
TEMPLATES = {
    "plain": [
        "The device’s MAC address is {v}.",
        "Please note the ethernet address {v}.",
        "Your network address is set to {v}.",
    ],
    "with_space": [
        "Enter the hardware address as {v}.",
        "The wifi address configured is {v}.",
        "The LAN address shows up as {v}.",
    ],
    "with_dashes": [
        "Our system logs the MAC as {v}.",
        "Bluetooth address recorded is {v}.",
        "Media Access Control ID: {v}.",
    ],
    "lowercase": [
        "The device address appears lowercase like {v}.",
        "Sometimes the MAC address is shown as {v}.",
        "Check the hardware address field for {v}.",
    ],
    "embedded": [
        "Please verify the media access control address {v}.",
        "Use device address {v} for network setup.",
        "Ensure the MAC address {v} matches your records.",
    ],
    "alt_label": [
        "Device MAC ID: {v}.",
        "MAC address of the device: {v}.",
        "Your MAC address is logged as {v}.",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_mac_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        base = gen_base_mac()
        key = random.choice(keys)
        variant = VARIATIONS[key](base)
        template = random.choice(TEMPLATES[key])
        text = template.format(v=variant)
        records.append({
            "text":      text,
            "mac":       variant,
            "variation": key,
            "is_valid":  is_valid_mac(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_mac_variations(count=50)
    with open("mac_addresses.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ mac_addresses.json generated with context-rich sentences and validity flags.")
