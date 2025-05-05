# #!/usr/bin/env python3
# import random
# import json
# from datetime import datetime, timedelta, timezone

# # ----------------------------
# # 1. Generate a random base datetime
# # ----------------------------
# def gen_base_dt():
#     """Pick a random datetime within the last two years."""
#     now = datetime.now(timezone.utc)
#     past = now - timedelta(days=365*2)
#     rand_seconds = random.randint(0, int((now - past).total_seconds()))
#     return past + timedelta(seconds=rand_seconds)

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain_iso(dt):
#     return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

# def iso_with_offset(dt):
#     offset = timezone(timedelta(hours=5, minutes=30))
#     local = dt.astimezone(offset)
#     s = local.strftime("%Y-%m-%dT%H:%M:%S%z")
#     # insert colon in offset
#     return s[:-2] + ":" + s[-2:]

# def date_space_time(dt):
#     return dt.strftime("%-m/%-d/%Y %H:%M")

# def date_slash_time(dt):
#     return dt.strftime("%d/%m/%Y %H:%M")

# def us_style_12h(dt):
#     return dt.strftime("%-m/%-d/%Y %I:%M %p")

# def readable_long(dt):
#     return dt.strftime("%B %-d, %Y %H:%M:%S")

# def unix_timestamp(dt):
#     return str(int(dt.timestamp()))

# def date_with_millis(dt):
#     return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

# def time_only(dt):
#     return dt.strftime("%H:%M:%S")

# def partial_iso(dt):
#     return dt.strftime("%Y-%m-%dT%H")

# def datetime_range(dt):
#     end = dt + timedelta(hours=1, minutes=random.randint(0, 59))
#     return f"{dt.strftime('%Y-%m-%d %H:%M')} to {end.strftime('%H:%M')}"

# def alt_label(dt):
#     return dt.strftime("%Y-%m-%d %H:%M:%S")

# VARIATIONS = {
#     "plain_iso":        plain_iso,
#     "iso_with_offset":  iso_with_offset,
#     "date_space_time":  date_space_time,
#     "date_slash_time":  date_slash_time,
#     "us_style_12h":     us_style_12h,
#     "readable_long":    readable_long,
#     "unix_timestamp":   unix_timestamp,
#     "date_with_millis": date_with_millis,
#     "time_only":        time_only,
#     "partial_iso":      partial_iso,
#     "datetime_range":   datetime_range,
#     "alt_label":        alt_label,
# }

# # ----------------------------
# # 3. Sentence templates
# # ----------------------------
# TEMPLATES = {
#     "plain_iso": [
#         "The backup started at {v}",
#         "Full UTC timestamp is {v}",
#     ],
#     "iso_with_offset": [
#         "Local time with offset reads {v}",
#         "Task scheduled for {v}",
#     ],
#     "date_space_time": [
#         "Database entry created on {v}",
#         "Logged at {v}",
#     ],
#     "date_slash_time": [
#         "Report time stamp is {v}",
#         "Document saved on {v}",
#     ],
#     "us_style_12h": [
#         "Reminder set for {v}",
#         "Meeting begins at {v}",
#     ],
#     "readable_long": [
#         "Report generated on {v}",
#         "Event recorded on {v}",
#     ],
#     "unix_timestamp": [
#         "Epoch record is {v}",
#         "Logged epoch time {v}",
#     ],
#     "date_with_millis": [
#         "Trace event at {v}",
#         "Precision log at {v}",
#     ],
#     "time_only": [
#         "System time now is {v}",
#         "Current time stamp {v}",
#     ],
#     "partial_iso": [
#         "Hourly snapshot at {v}",
#         "Data as of {v}",
#     ],
#     "datetime_range": [
#         "Maintenance window {v}",
#         "Available from {v}",
#     ],
#     "alt_label": [
#         "Timestamp: {v}",
#         "Recorded at: {v}",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_datetime_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())
#     while len(records) < count:
#         dt   = gen_base_dt()
#         key  = random.choice(keys)
#         val  = VARIATIONS[key](dt)
#         txt  = random.choice(TEMPLATES[key]).format(v=val)
#         records.append({
#             "text":      txt,
#             "datetime":  val,
#             "variation": key,
#             "is_valid":  True
#         })
#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_datetime_variations(count=50)
#     with open("datetime_variations.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ datetime_variations.json generated with all date/time permutations.")




#!/usr/bin/env python3
import random
import json
from datetime import datetime, timedelta, timezone

# ----------------------------
# 1. Generate a random base datetime
# ----------------------------
def gen_base_dt():
    """Pick a random datetime within the last two years."""
    now = datetime.now(timezone.utc)
    past = now - timedelta(days=365*2)
    rand_seconds = random.randint(0, int((now - past).total_seconds()))
    return past + timedelta(seconds=rand_seconds)

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain_iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

def iso_with_offset(dt):
    offset = timezone(timedelta(hours=5, minutes=30))
    local = dt.astimezone(offset)
    s = local.strftime("%Y-%m-%dT%H:%M:%S%z")
    return s[:-2] + ":" + s[-2:]

def date_space_time(dt):
    return dt.strftime("%-m/%-d/%Y %H:%M")

def date_slash_time(dt):
    return dt.strftime("%d/%m/%Y %H:%M")

def us_style_12h(dt):
    return dt.strftime("%-m/%-d/%Y %I:%M %p")

def readable_long(dt):
    return dt.strftime("%B %-d, %Y %H:%M:%S")

def unix_timestamp(dt):
    return str(int(dt.timestamp()))

def date_with_millis(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

def time_only(dt):
    return dt.strftime("%H:%M:%S")

def partial_iso(dt):
    return dt.strftime("%Y-%m-%dT%H")

def datetime_range(dt):
    end = dt + timedelta(hours=1, minutes=random.randint(0, 59))
    return f"{dt.strftime('%Y-%m-%d %H:%M')} to {end.strftime('%H:%M')}"

def alt_label(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

VARIATIONS = {
    "plain_iso":        plain_iso,
    "iso_with_offset":  iso_with_offset,
    "date_space_time":  date_space_time,
    "date_slash_time":  date_slash_time,
    "us_style_12h":     us_style_12h,
    "readable_long":    readable_long,
    "unix_timestamp":   unix_timestamp,
    "date_with_millis": date_with_millis,
    "time_only":        time_only,
    "partial_iso":      partial_iso,
    "datetime_range":   datetime_range,
    "alt_label":        alt_label,
}

# ----------------------------
# 3. Sentence templates
# ----------------------------
TEMPLATES = {
    "plain_iso": [
        "The backup started at {v}",
        "Full UTC timestamp is {v}",
        "Log entry recorded at {v}",
        "Server synced at {v}"
    ],
    "iso_with_offset": [
        "Local time with offset reads {v}",
        "Task scheduled for {v}",
        "Job triggered at {v}",
        "Local audit started at {v}"
    ],
    "date_space_time": [
        "Database entry created on {v}",
        "Logged at {v}",
        "Snapshot taken on {v}",
        "Record updated on {v}"
    ],
    "date_slash_time": [
        "Report time stamp is {v}",
        "Document saved on {v}",
        "Invoice dated {v}",
        "Form submitted on {v}"
    ],
    "us_style_12h": [
        "Reminder set for {v}",
        "Meeting begins at {v}",
        "Alarm scheduled at {v}",
        "Call arranged at {v}"
    ],
    "readable_long": [
        "Report generated on {v}",
        "Event recorded on {v}",
        "Change logged on {v}",
        "Session started on {v}"
    ],
    "unix_timestamp": [
        "Epoch record is {v}",
        "Logged epoch time {v}",
        "System tick at {v}",
        "Metric captured at {v}"
    ],
    "date_with_millis": [
        "Trace event at {v}",
        "Precision log at {v}",
        "Debug marker at {v}",
        "High‑res timestamp {v}"
    ],
    "time_only": [
        "System time now is {v}",
        "Current time stamp {v}",
        "Clock reading {v}",
        "Time check at {v}"
    ],
    "partial_iso": [
        "Hourly snapshot at {v}",
        "Data as of {v}",
        "Checkpoint at {v}",
        "Rollup at {v}"
    ],
    "datetime_range": [
        "Maintenance window {v}",
        "Available from {v}",
        "Service outage window {v}",
        "Support hours {v}"
    ],
    "alt_label": [
        "Timestamp {v}",
        "Recorded at {v}",
        "Logged at {v}",
        "Time record {v}"
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_datetime_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        dt   = gen_base_dt()
        key  = random.choice(keys)
        val  = VARIATIONS[key](dt)
        txt  = random.choice(TEMPLATES[key]).format(v=val)
        records.append({
            "text":      txt,
            "datetime":  val,
            "variation": key,
            "is_valid":  True
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_datetime_variations(count=50)
    with open("datetime_variations.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ datetime_variations.json generated with rich real‑world sentences")
