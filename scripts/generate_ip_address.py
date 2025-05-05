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
