# #!/usr/bin/env python3
# import random
# import json
# import string

# # ----------------------------
# # 1. Base domain and helpers
# # ----------------------------
# BASE_DOMAIN = "example.com"
# SUBDOMAINS = ["", "blog.", "shop."]
# USERS = ["user", "alice", "bob"]
# PASSWORDS = ["pass", "secret", "1234"]
# PATHS = ["login/user", "search/results", "docs/tutorial"]
# QUERIES = ["q=hello", "page=2", "ref=homepage"]

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(_):
#     return f"https://{BASE_DOMAIN}"

# def with_http(_):
#     return f"http://{BASE_DOMAIN}"

# def without_protocol(_):
#     return BASE_DOMAIN

# def with_www(_):
#     return f"www.{BASE_DOMAIN}"

# def lowercase(_):
#     return f"https://{BASE_DOMAIN}/page".lower()

# def uppercase(_):
#     return f"https://{BASE_DOMAIN}/PAGE".upper()

# def with_path(_):
#     path = random.choice(PATHS)
#     return f"https://{BASE_DOMAIN}/{path}"

# def with_query(_):
#     query = random.choice(QUERIES)
#     return f"https://{BASE_DOMAIN}/search?{query}"

# def with_port(_):
#     port = random.choice([8080, 3000, 8000])
#     return f"https://{BASE_DOMAIN}:{port}"

# def embedded(_):
#     return plain(None)

# def surrounded(_):
#     return plain(None)

# def trailing_slash(_):
#     return f"https://{BASE_DOMAIN}/"

# def subdomain(_):
#     sd = random.choice(SUBDOMAINS[1:])
#     return f"https://{sd}{BASE_DOMAIN}"

# def obfuscated(_):
#     return f"hxxps://{BASE_DOMAIN.replace('.', '[.]')}"

# def ip_address(_):
#     return "http://192.168.1.1"

# def partial_domain(_):
#     return "example.com"

# def with_username(_):
#     user = random.choice(USERS)
#     return f"https://{user}@{BASE_DOMAIN}"

# def with_user_pass(_):
#     user = random.choice(USERS)
#     pwd  = random.choice(PASSWORDS)
#     return f"https://{user}:{pwd}@{BASE_DOMAIN}"

# def no_proto_path(_):
#     path = random.choice(PATHS)
#     return f"{BASE_DOMAIN}/{path}"

# def edge_no_dot(_):
#     return "examplecom"

# VARIATIONS = {
#     "plain":           (plain,       True),
#     "with_http":       (with_http,   True),
#     "without_protocol":(without_protocol, True),
#     "with_www":        (with_www,    True),
#     "lowercase":       (lowercase,   True),
#     "uppercase":       (uppercase,   True),
#     "with_path":       (with_path,   True),
#     "with_query":      (with_query,  True),
#     "with_port":       (with_port,   True),
#     "embedded":        (embedded,    True),
#     "surrounded":      (surrounded,  True),
#     "trailing_slash":  (trailing_slash, True),
#     "subdomain":       (subdomain,   True),
#     "obfuscated":      (obfuscated,  False),
#     "ip_address":      (ip_address,  False),
#     "partial_domain":  (partial_domain, True),
#     "with_username":   (with_username, True),
#     "with_user_pass":  (with_user_pass, True),
#     "no_proto_path":   (no_proto_path, True),
#     "edge_no_dot":     (edge_no_dot, True),
# }

# # ----------------------------
# # 3. Natural‑language templates
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Open the homepage at {v}",
#         "Navigate to {v} to start"
#     ],
#     "with_http": [
#         "Use the secure link {v} for data",
#         "Server is reachable at {v}"
#     ],
#     "without_protocol": [
#         "Type in example domain {v}",
#         "Visit {v} to learn more"
#     ],
#     "with_www": [
#         "The site mirror is at {v}",
#         "Try {v} if the main site is down"
#     ],
#     "lowercase": [
#         "Check this page at {v}",
#         "Lowercase URL example {v}"
#     ],
#     "uppercase": [
#         "Uppercase link example {v}",
#         "Test with uppercase URL {v}"
#     ],
#     "with_path": [
#         "Login portal available at {v}",
#         "User area located at {v}"
#     ],
#     "with_query": [
#         "Search API endpoint: {v}",
#         "Lookup service at {v}"
#     ],
#     "with_port": [
#         "Development server runs at {v}",
#         "Alternate port available at {v}"
#     ],
#     "embedded": [
#         "Check out this link: {v}",
#         "Documentation lives here {v}"
#     ],
#     "surrounded": [
#         "Refer to the site ({v}) for details",
#         "Find resources at ({v})"
#     ],
#     "trailing_slash": [
#         "Directory index at {v}",
#         "Root path ends with slash {v}"
#     ],
#     "subdomain": [
#         "Blog is hosted at {v}",
#         "Shopfront available at {v}"
#     ],
#     "obfuscated": [
#         "Malware test link {v}",
#         "Phishing example {v}"
#     ],
#     "ip_address": [
#         "Local router UI at {v}",
#         "Network gateway is at {v}"
#     ],
#     "partial_domain": [
#         "Visit example site now {v}",
#         "Quick access at {v}"
#     ],
#     "with_username": [
#         "User profile at {v}",
#         "Login as user at {v}"
#     ],
#     "with_user_pass": [
#         "Automated login may use {v}",
#         "Test credentials at {v}"
#     ],
#     "no_proto_path": [
#         "Direct resource path {v}",
#         "Access folder at {v}"
#     ],
#     "edge_no_dot": [
#         "Typo domain test {v}",
#         "Robustness check for {v}"
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_url_variations():
#     records = []
#     for key, (fn, valid) in VARIATIONS.items():
#         url = fn(None)
#         template = random.choice(TEMPLATES[key])
#         text = template.format(v=url)
#         records.append({
#             "text":       text,
#             "url":        url,
#             "variation":  key,
#             "is_valid":   valid
#         })
#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_url_variations()
#     with open("url_variations.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ url_variations.json generated with URL permutations")




#!/usr/bin/env python3
import random
import json
import string
import sys

# ----------------------------
# 1. Base domain and helpers
# ----------------------------
BASE_DOMAIN = "example.com"
SUBDOMAINS = ["", "blog.", "shop."]
USERS = ["user", "alice", "bob"]
PASSWORDS = ["pass", "secret", "1234"]
PATHS = ["login/user", "search/results", "docs/tutorial"]
QUERIES = ["q=hello", "page=2", "ref=homepage"]

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(_):
    return f"https://{BASE_DOMAIN}"

def with_http(_):
    return f"http://{BASE_DOMAIN}"

def without_protocol(_):
    return BASE_DOMAIN

def with_www(_):
    return f"www.{BASE_DOMAIN}"

def lowercase(_):
    return f"https://{BASE_DOMAIN}/page".lower()

def uppercase(_):
    return f"https://{BASE_DOMAIN}/PAGE".upper()

def with_path(_):
    path = random.choice(PATHS)
    return f"https://{BASE_DOMAIN}/{path}"

def with_query(_):
    query = random.choice(QUERIES)
    return f"https://{BASE_DOMAIN}/search?{query}"

def with_port(_):
    port = random.choice([8080, 3000, 8000])
    return f"https://{BASE_DOMAIN}:{port}"

def embedded(_):
    return plain(None)

def surrounded(_):
    return plain(None)

def trailing_slash(_):
    return f"https://{BASE_DOMAIN}/"

def subdomain(_):
    sd = random.choice(SUBDOMAINS[1:])
    return f"https://{sd}{BASE_DOMAIN}"

def obfuscated(_):
    return f"hxxps://{BASE_DOMAIN.replace('.', '[.]')}"

def ip_address(_):
    return "http://192.168.1.1"

def partial_domain(_):
    return "example.com"

def with_username(_):
    user = random.choice(USERS)
    return f"https://{user}@{BASE_DOMAIN}"

def with_user_pass(_):
    user = random.choice(USERS)
    pwd  = random.choice(PASSWORDS)
    return f"https://{user}:{pwd}@{BASE_DOMAIN}"

def no_proto_path(_):
    path = random.choice(PATHS)
    return f"{BASE_DOMAIN}/{path}"

def edge_no_dot(_):
    return "examplecom"

# each tuple is (function, is_valid)
VARIATIONS = {
    "plain":            (plain,            True),
    "with_http":        (with_http,        True),
    "without_protocol": (without_protocol, True),
    "with_www":         (with_www,         True),
    "lowercase":        (lowercase,        True),
    "uppercase":        (uppercase,        True),
    "with_path":        (with_path,        True),
    "with_query":       (with_query,       True),
    "with_port":        (with_port,        True),
    "embedded":         (embedded,         True),
    "surrounded":       (surrounded,       True),
    "trailing_slash":   (trailing_slash,   True),
    "subdomain":        (subdomain,        True),
    "obfuscated":       (obfuscated,       False),
    "ip_address":       (ip_address,       False),
    "partial_domain":   (partial_domain,   True),
    "with_username":    (with_username,    True),
    "with_user_pass":   (with_user_pass,   True),
    "no_proto_path":    (no_proto_path,    True),
    "edge_no_dot":      (edge_no_dot,      True),
}

# ----------------------------
# 3. Natural‑language templates
# ----------------------------
TEMPLATES = {
    "plain": [
        "Open the homepage at {v}",
        "Navigate to {v} to start"
    ],
    "with_http": [
        "Use the secure link {v} for data",
        "Server is reachable at {v}"
    ],
    "without_protocol": [
        "Type in example domain {v}",
        "Visit {v} to learn more"
    ],
    "with_www": [
        "The site mirror is at {v}",
        "Try {v} if the main site is down"
    ],
    "lowercase": [
        "Check this page at {v}",
        "Lowercase URL example {v}"
    ],
    "uppercase": [
        "Uppercase link example {v}",
        "Test with uppercase URL {v}"
    ],
    "with_path": [
        "Login portal available at {v}",
        "User area located at {v}"
    ],
    "with_query": [
        "Search API endpoint: {v}",
        "Lookup service at {v}"
    ],
    "with_port": [
        "Development server runs at {v}",
        "Alternate port available at {v}"
    ],
    "embedded": [
        "Check out this link: {v}",
        "Documentation lives here {v}"
    ],
    "surrounded": [
        "Refer to the site ({v}) for details",
        "Find resources at ({v})"
    ],
    "trailing_slash": [
        "Directory index at {v}",
        "Root path ends with slash {v}"
    ],
    "subdomain": [
        "Blog is hosted at {v}",
        "Shopfront available at {v}"
    ],
    "obfuscated": [
        "Malware test link {v}",
        "Phishing example {v}"
    ],
    "ip_address": [
        "Local router UI at {v}",
        "Network gateway is at {v}"
    ],
    "partial_domain": [
        "Visit example site now {v}",
        "Quick access at {v}"
    ],
    "with_username": [
        "User profile at {v}",
        "Login as user at {v}"
    ],
    "with_user_pass": [
        "Automated login may use {v}",
        "Test credentials at {v}"
    ],
    "no_proto_path": [
        "Direct resource path {v}",
        "Access folder at {v}"
    ],
    "edge_no_dot": [
        "Typo domain test {v}",
        "Robustness check for {v}"
    ],
}

# ----------------------------
# 4. Bulk generator with count
# ----------------------------
def generate_url_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    for _ in range(count):
        key = random.choice(keys)
        fn, validity = VARIATIONS[key]
        url = fn(None)
        text = random.choice(TEMPLATES[key]).format(v=url)
        records.append({
            "text":      text,
            "url":       url,
            "variation": key,
            "is_valid":  validity
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    # allow an optional count via command‑line, default to 50
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    out = generate_url_variations(count)
    with open("url_variations.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"✅ url_variations.json generated with {count} entries")
