# #!/usr/bin/env python3
# import random
# import json
# import re
# import sys

# # ----------------------------
# # 1. IP generators & validators
# # ----------------------------
# OCTET = lambda: str(random.randint(0, 255))
# IP_REGEX = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')

# def gen_base_ip():
#     """Generate a random IPv4 address."""
#     return ".".join(OCTET() for _ in range(4))

# def is_valid_ip(value):
#     """Validate dotted IPv4 (each octet 0–255)."""
#     if not IP_REGEX.fullmatch(value):
#         return False
#     return all(0 <= int(octet) <= 255 for octet in value.split("."))

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(ip):
#     return ip

# def with_space(ip):
#     return " ".join(ip.split("."))

# def with_dashes(ip):
#     return "-".join(ip.split("."))

# def lowercase(ip):
#     # digits unaffected; prefix/lowercase handled in template
#     return ip

# def embedded(ip):
#     return ip

# def alt_label(ip):
#     return ip

# VARIATIONS = {
#     "plain":      plain,
#     "with_space": with_space,
#     "with_dashes":with_dashes,
#     "lowercase":  lowercase,
#     "embedded":   embedded,
#     "alt_label":  alt_label,
# }

# # ----------------------------
# # 3. Real‑world sentence templates
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "My IP address is {v}",
#         "Current network IP is {v}"
#     ],
#     "with_space": [
#         "My IP address is {v}",
#         "Current network IP is {v}"
#     ],
#     "with_dashes": [
#         "My IP address is {v}",
#         "Current network IP is {v}"
#     ],
#     "lowercase": [
#         "my ip address is {v}",
#         "network host ip is {v}"
#     ],
#     "embedded": [
#         "The server is hosted at IP address {v}",
#         "Connect to the service at {v}"
#     ],
#     "alt_label": [
#         "IP Address: {v}",
#         "Device IP Address: {v}"
#     ],
# }

# # ----------------------------
# # 4. Bulk generator with count
# # ----------------------------
# def generate_ip_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())
#     while len(records) < count:
#         ip = gen_base_ip()
#         # ensure base is valid
#         if not is_valid_ip(ip):
#             continue
#         key = random.choice(keys)
#         variant = VARIATIONS[key](ip)
#         text = random.choice(TEMPLATES[key]).format(v=variant)
#         records.append({
#             "text":       text,
#             "ip":         variant,
#             "variation":  key,
#             "is_valid":   is_valid_ip(variant.replace(" ", ".").replace("-", "."))
#         })
#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     # optional command‑line argument for count
#     count = int(sys.argv[1]) if len(sys.argv) > 1 else 50
#     out = generate_ip_variations(count)
#     with open("ip_variations.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print(f"✅ ip_variations.json generated with {count} entries")





#!/usr/bin/env python3
import random
import json
import re

# ----------------------------
# 1. IP generators & validators
# ----------------------------
OCTET = r"(25[0-5]|2[0-4]\d|1?\d?\d)"
IP_REGEX = re.compile(rf"^{OCTET}\.{OCTET}\.{OCTET}\.{OCTET}$")

def gen_plain_ip():
    """Generate a random IPv4 address in dotted form."""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def is_valid_ip(addr):
    """Valid only if it matches a full dotted‑quad IPv4."""
    return bool(IP_REGEX.fullmatch(addr))

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(ip):
    return ip

def with_space(ip):
    return ip.replace(".", " ")

def with_dashes(ip):
    return ip.replace(".", "-")

def lowercase(ip):
    # IP is numeric but we lowercase the surrounding text only
    return ip

def embedded(ip):
    return ip

def alt_label(ip):
    return ip

VARIATIONS = {
    "plain":       plain,
    "with_space":  with_space,
    "with_dashes": with_dashes,
    "lowercase":   lowercase,
    "embedded":    embedded,
    "alt_label":   alt_label,
}

# ----------------------------
# 3. Real‑world sentence templates
# ----------------------------
TEMPLATES = {
    "plain": [
        "My current IP address assigned by DHCP is {v}",
        "This workstation reports its IPv4 address as {v} to the network"
    ],
    "with_space": [
        "The network interface shows the address with spaces as {v}",
        "For logging purposes the host IP appears as {v}"
    ],
    "with_dashes": [
        "Our firewall logs represent the client address with dashes as {v}",
        "Some legacy systems display the IP in dashed format {v}"
    ],
    "lowercase": [
        "in lowercase notation the ip address reads {v}",
        "the system audit reports the host ip in lowercase as {v}"
    ],
    "embedded": [
        "Please connect to the server at ip address {v} for the update",
        "When troubleshooting please ping the service at {v} to verify reachability"
    ],
    "alt_label": [
        "IP Address of the router is recorded as {v}",
        "Device IP Address on record for this interface is {v}"
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_ip_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        base = gen_plain_ip()
        key = random.choice(keys)
        variant = VARIATIONS[key](base)
        template = random.choice(TEMPLATES[key])
        text = template.format(v=variant)
        records.append({
            "text":      text,
            "ip":        variant,
            "variation": key,
            "is_valid":  is_valid_ip(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_ip_variations(count=50)
    with open("ip_variations.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ ip_variations.json generated with IP permutations")
