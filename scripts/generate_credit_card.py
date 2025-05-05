# #!/usr/bin/env python3
# import random
# import json
# from stdnum.luhn import calc_check_digit, is_valid as luhn_is_valid

# # ----------------------------
# # 1. Luhn-based generators + validators
# # ----------------------------
# def gen_base_card():
#     """Generate a 16-digit number with correct Luhn checksum starting with valid prefixes (4,5,6)."""
#     prefix = str(random.choice([4, 5, 6]))
#     body = "".join(str(random.randint(0, 9)) for _ in range(14))
#     partial = prefix + body
#     # Use calc_check_digit, NOT calc_checksum
#     check_digit = calc_check_digit(partial)
#     return partial + check_digit

# def gen_invalid_card():
#     """Create an almost-valid card by flipping the check digit."""
#     card = gen_base_card()
#     bad = (int(card[-1]) + random.randint(1, 9)) % 10
#     return card[:-1] + str(bad)

# def is_valid_card(card):
#     """Strip separators and test Luhn validity."""
#     nums = "".join(ch for ch in card if ch.isdigit())
#     return luhn_is_valid(nums)

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(card):
#     return card

# def with_spaces(card):
#     nums = card.replace("-", "")
#     return " ".join(nums[i:i+4] for i in range(0, 16, 4))

# def with_dashes(card):
#     nums = card.replace(" ", "")
#     return "-".join(nums[i:i+4] for i in range(0, 16, 4))

# def embedded_text(card):
#     return f"My card ends with {card[-4:]}."

# def short_card(card):
#     return card[:15]  # drop last digit

# def ocr_spacing(card):
#     part1, part2 = card[:8], card[8:]
#     return f"{part1} {part2}"

# def masked(card):
#     return "XXXX-XXXX-XXXX-" + card[-4:]

# def alt_label(card):
#     return f"card no: {card}"

# # ----------------------------
# # 3. Bulk generator
# # ----------------------------
# def generate_credit_card_variations(count=10):
#     variants = []
#     funcs = [
#         plain, with_spaces, with_dashes, embedded_text,
#         short_card, ocr_spacing, masked, alt_label
#     ]

#     while len(variants) < count:
#         # 70% valid, 30% invalid
#         base = gen_base_card() if random.random() < 0.7 else gen_invalid_card()
#         fn = random.choice(funcs)
#         transformed = fn(base)

#         variants.append({
#             "text": transformed,
#             "card": transformed,
#             "is_valid": is_valid_card(transformed)
#         })

#     return variants

# # ----------------------------
# # 4. Entry point
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_credit_card_variations(count=10)
#     for rec in out:
#         print(json.dumps(rec, ensure_ascii=False))


#--------------correct format but not worded sentences-----------------------------------
#!/usr/bin/env python3
# import random
# import json
# from stdnum.luhn import calc_check_digit, is_valid as luhn_is_valid

# # ----------------------------
# # 1. Generators & validators
# # ----------------------------
# def gen_base_card():
#     prefix = str(random.choice([4, 5, 6]))
#     body = "".join(str(random.randint(0, 9)) for _ in range(14))
#     check_digit = calc_check_digit(prefix + body)
#     return prefix + body + check_digit

# def gen_invalid_card():
#     card = gen_base_card()
#     bad = (int(card[-1]) + random.randint(1, 9)) % 10
#     return card[:-1] + str(bad)

# def is_valid_card(card):
#     digits = "".join(ch for ch in card if ch.isdigit())
#     return luhn_is_valid(digits)

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(card):      return card
# def with_spaces(card): return " ".join(card.replace("-", "")[i:i+4] for i in range(0,16,4))
# def with_dashes(card): return "-".join(card.replace(" ", "")[i:i+4] for i in range(0,16,4))
# def embedded(card):    return card  # we'll slice later
# def short_card(card):  return card[:15]
# def ocr_spacing(card): return card[:8] + " " + card[8:]
# def masked(card):      return "XXXX-XXXX-XXXX-" + card[-4:]
# def alt_label(card):   return card

# VARIATIONS = {
#     "plain": plain,
#     "with_spaces": with_spaces,
#     "with_dashes": with_dashes,
#     "embedded": embedded,
#     "short": short_card,
#     "ocr": ocr_spacing,
#     "masked": masked,
#     "alt_label": alt_label,
# }

# # ----------------------------
# # 3. Sentence templates
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Her credit card number is {v}.",
#         "The card number assigned to her is {v}.",
#         "This is a valid credit card: {v}.",
#     ],
#     "with_spaces": [
#         "Please check the spaced card: {v}.",
#         "Card displayed with spaces: {v}.",
#         "Her card in groups: {v}.",
#     ],
#     "with_dashes": [
#         "Dashed card format: {v}.",
#         "My credit card looks like {v}.",
#         "Here’s the number with dashes: {v}.",
#     ],
#     # Embedded now expects that v = last 4 digits
#     "embedded": [
#         "My card ends with {v}.",
#         "You can spot the last four digits: {v}.",
#         "I routinely use …{v} on payments.",
#     ],
#     "short": [
#         "Truncated card: {v}.",
#         "Short form: {v}.",
#         "Only first 15 digits: {v}.",
#     ],
#     "ocr": [
#         "OCR output: {v}.",
#         "Scanned as: {v}.",
#         "Detected reading: {v}.",
#     ],
#     "masked": [
#         "For privacy, it shows {v}.",
#         "Masked number: {v}.",
#         "Hidden except last four: {v}.",
#     ],
#     "alt_label": [
#         "card no: {v}",
#         "credit card: {v}",
#         "debit #: {v}",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_credit_card_variations(count=10):
#     records = []
#     keys = list(VARIATIONS.keys())

#     while len(records) < count:
#         base = gen_base_card() if random.random() < 0.7 else gen_invalid_card()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)

#         # For embedded, we only want the last 4 digits:
#         if key == "embedded":
#             v = base[-4:]
#         else:
#             v = variant

#         tmpl = random.choice(TEMPLATES[key])
#         text = tmpl.format(v=v)

#         records.append({
#             "text": text,
#             "card": variant,
#             "variation": key,
#             "is_valid": is_valid_card(variant)
#         })

#     return records

# # ----------------------------
# # 5. Write to file
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_credit_card_variations(count=10)
#     with open("credit_cards.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ credit_cards.json generated with 10 records.")
# #----------------------------------------------------------------------------------------





#---------------missing  . / _  variations-------------------------------------------------------------
#!/usr/bin/env python3
# import random
# import json
# from stdnum.luhn import calc_check_digit, is_valid as luhn_is_valid

# # ----------------------------
# # 1. Generators & validators
# # ----------------------------
# def gen_base_card():
#     prefix = str(random.choice([4, 5, 6]))
#     body = "".join(str(random.randint(0, 9)) for _ in range(14))
#     check = calc_check_digit(prefix + body)
#     return prefix + body + check

# def gen_invalid_card():
#     card = gen_base_card()
#     bad = (int(card[-1]) + random.randint(1, 9)) % 10
#     return card[:-1] + str(bad)

# def is_valid_card(card):
#     nums = "".join(ch for ch in card if ch.isdigit())
#     return luhn_is_valid(nums)

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(card):      return card
# def with_spaces(card): return ' '.join(card.replace('-', '')[i:i+4] for i in range(0,16,4))
# def with_dashes(card): return '-'.join(card.replace(' ', '')[i:i+4] for i in range(0,16,4))
# def mixed(card):
#     nums = card.replace(' ', '').replace('-', '')
#     return f"{nums[:4]}-{nums[4:8]} {nums[8:12]}-{nums[12:16]}"
# def ocr_spacing(card):
#     nums = card.replace('-', '')
#     return nums[:8] + ' ' + nums[8:]
# def masked(card):      return 'XXXX-XXXX-XXXX-' + card[-4:]
# def short_card(card):  return card[:15]
# def embedded(card):    return card     # we'll use last4 separately
# def alt_label(card):   return card     # label in template

# VARIATIONS = {
#     "plain": plain,
#     "with_spaces": with_spaces,
#     "with_dashes": with_dashes,
#     "mixed": mixed,
#     "ocr": ocr_spacing,
#     "masked": masked,
#     "short": short_card,
#     "embedded": embedded,
#     "alt_label": alt_label,
# }

# # ----------------------------
# # 3. Rich sentence templates
# #   Note: use {v} for the formatted variant,
# #         and {last4} for the final four digits.
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Her credit card number is {v}, which serves as a unique payment instrument issued by HDFC Bank.",
#         "This 16-digit number, {v}, is linked to her premium rewards program.",
#         "The full card {v} appears on her HDFC Platinum statement.",
#     ],
#     "with_spaces": [
#         "For clarity she reads it spaced: {v}, especially over the phone.",
#         "The bank printed her card as {v} on the welcome package.",
#         "When entering manually, she types groups: {v}.",
#     ],
#     "with_dashes": [
#         "Dashed format shown on receipts: {v}.",
#         "At checkout you’ll see: {v}.",
#         "Her statement shows number as {v}.",
#     ],
#     "mixed": [
#         "Mixed separators appear as: {v}.",
#         "Sometimes it’s formatted like {v} for system compatibility.",
#         "Hybrid style shown: {v}.",
#     ],
#     "ocr": [
#         "OCR scan recognized: {v}.",
#         "Scanned output: {v}.",
#         "Detected reading: {v}.",
#     ],
#     "masked": [
#         "For security it appears as {v}.",
#         "Only last four digits visible: {v}.",
#         "Masked in logs as {v}.",
#     ],
#     "short": [
#         "Truncated for display: {v}.",
#         "Short code: {v}.",
#         "First 15 digits only: {v}.",
#     ],
#     "embedded": [
#         "My card ends with {last4}.",
#         "You can spot the last four digits: {last4}.",
#         "I routinely use …{last4} for quick payments.",
#     ],
#     "alt_label": [
#         "card no: {v}",
#         "credit card: {v}",
#         "debit #: {v}",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_credit_card_variations(count=20):
#     records = []
#     keys = list(VARIATIONS.keys())

#     while len(records) < count:
#         base = gen_base_card() if random.random() < 0.7 else gen_invalid_card()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)

#         # prepare template values
#         last4 = base[-4:]
#         v = variant

#         tmpl = random.choice(TEMPLATES[key])
#         text = tmpl.format(v=v, last4=last4)

#         records.append({
#             "text": text,
#             "card": v,
#             "variation": key,
#             "is_valid": is_valid_card(v)
#         })

#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_credit_card_variations(count=20)
#     with open("credit_cards.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ credit_cards.json generated with 20 richly worded variants.")
# #----------------------------------------------------------------------------------


# #!/usr/bin/env python3
# import random
# import json
# from stdnum.luhn import calc_check_digit, is_valid as luhn_is_valid

# # ----------------------------
# # 1. Generators & validators
# # ----------------------------
# def gen_base_card():
#     prefix = str(random.choice([4, 5, 6]))
#     body = "".join(str(random.randint(0, 9)) for _ in range(14))
#     check = calc_check_digit(prefix + body)
#     return prefix + body + check

# def gen_invalid_card():
#     card = gen_base_card()
#     bad = (int(card[-1]) + random.randint(1, 9)) % 10
#     return card[:-1] + str(bad)

# def is_valid_card(card):
#     nums = "".join(ch for ch in card if ch.isdigit())
#     return luhn_is_valid(nums)

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(card):
#     return card

# def with_spaces(card):
#     nums = card.replace('-', '')
#     return ' '.join(nums[i:i+4] for i in range(0, 16, 4))

# def with_dashes(card):
#     nums = card.replace(' ', '')
#     return '-'.join(nums[i:i+4] for i in range(0, 16, 4))

# def with_underscores(card):
#     nums = card.replace('-', '').replace(' ', '')
#     return '_'.join(nums[i:i+4] for i in range(0, 16, 4))

# def mixed(card):
#     nums = card.replace(' ', '').replace('-', '')
#     return f"{nums[:4]}-{nums[4:8]} {nums[8:12]}-{nums[12:16]}"

# def ocr_spacing(card):
#     nums = card.replace('-', '')
#     return nums[:8] + ' ' + nums[8:]

# def punctuation_sep(card):
#     """Insert one random punctuation (., /, _) between groups."""
#     nums = card.replace(' ', '').replace('-', '')
#     punct = random.choice(['.', '/', '_'])
#     # split into two halves at random group boundary
#     idx = random.choice([4, 8, 12])
#     return nums[:idx] + punct + nums[idx:]

# def masked(card):
#     return 'XXXX-XXXX-XXXX-' + card[-4:]

# def short_card(card):
#     return card[:15]

# def embedded(card):
#     return card  # last4 used separately

# def alt_label(card):
#     return card  # label applied in template

# VARIATIONS = {
#     "plain": plain,
#     "with_spaces": with_spaces,
#     "with_dashes": with_dashes,
#     "with_underscores": with_underscores,
#     "mixed": mixed,
#     "ocr": ocr_spacing,
#     "punctuation": punctuation_sep,
#     "masked": masked,
#     "short": short_card,
#     "embedded": embedded,
#     "alt_label": alt_label,
# }

# # ----------------------------
# # 3. Rich sentence templates
# #   {v} = full variant, {last4} = final four digits
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "Her credit card number is {v}, which serves as a unique payment instrument issued by HDFC Bank.",
#         "This 16-digit number, {v}, is linked to her premium rewards program.",
#     ],
#     "with_spaces": [
#         "For clarity she reads it spaced: {v}, especially over the phone.",
#         "The bank printed her card as {v} on the welcome package.",
#     ],
#     "with_dashes": [
#         "Dashed format shown on receipts: {v}.",
#         "At checkout you’ll see: {v}.",
#     ],
#     "with_underscores": [
#         "Underscore format appears as: {v}.",
#         "Sometimes it’s written like {v} in logs.",
#     ],
#     "mixed": [
#         "Mixed separators appear as: {v}.",
#         "Hybrid style shown: {v}.",
#     ],
#     "ocr": [
#         "OCR scan recognized: {v}.",
#         "Scanned output: {v}.",
#     ],
#     "punctuation": [
#         "Punctuation inserted: {v}.",
#         "It parsed with punctuation: {v}.",
#     ],
#     "masked": [
#         "For security it appears as {v}.",
#         "Only last four digits visible: {v}.",
#     ],
#     "short": [
#         "Truncated for display: {v}.",
#         "Short code: {v}.",
#     ],
#     "embedded": [
#         "My card ends with {last4}.",
#         "Last four digits: {last4}.",
#     ],
#     "alt_label": [
#         "card no: {v}",
#         "credit card: {v}",
#         "debit #: {v}",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_credit_card_variations(count=20):
#     records = []
#     keys = list(VARIATIONS.keys())

#     while len(records) < count:
#         base = gen_base_card() if random.random() < 0.7 else gen_invalid_card()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)

#         last4 = base[-4:]
#         v = variant

#         tmpl = random.choice(TEMPLATES[key])
#         text = tmpl.format(v=v, last4=last4)

#         records.append({
#             "text": text,
#             "card": v,
#             "variation": key,
#             "is_valid": is_valid_card(v)
#         })

#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_credit_card_variations(count=20)
#     with open("credit_cards.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ credit_cards.json generated with all permutations (spaces, dashes, underscores, punctuation, etc.).")



# #!/usr/bin/env python3
# import random
# import json
# from stdnum.luhn import calc_check_digit, is_valid as luhn_is_valid

# # ----------------------------
# # 1. Generators & validators
# # ----------------------------
# def gen_base_card():
#     prefix = str(random.choice([4, 5, 6]))
#     body = "".join(str(random.randint(0, 9)) for _ in range(14))
#     check = calc_check_digit(prefix + body)
#     return prefix + body + check

# def gen_invalid_card():
#     card = gen_base_card()
#     bad = (int(card[-1]) + random.randint(1, 9)) % 10
#     return card[:-1] + str(bad)

# def is_valid_card(card):
#     nums = "".join(ch for ch in card if ch.isdigit())
#     return luhn_is_valid(nums)

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(card):      return card
# def with_spaces(card): return ' '.join(card.replace('-', '')[i:i+4] for i in range(0,16,4))
# def with_dashes(card): return '-'.join(card.replace(' ', '')[i:i+4] for i in range(0,16,4))
# def with_underscores(card): return '_'.join(card.replace('-', '').replace(' ', '')[i:i+4] for i in range(0,16,4))
# def mixed(card):
#     nums = card.replace(' ', '').replace('-', '')
#     return f"{nums[:4]}-{nums[4:8]} {nums[8:12]}-{nums[12:16]}"
# def ocr_spacing(card):
#     nums = card.replace('-', '')
#     return nums[:8] + ' ' + nums[8:]
# def punctuation_sep(card):
#     nums = card.replace(' ', '').replace('-', '')
#     punct = random.choice(['.', '/', '_'])
#     idx = random.choice([4, 8, 12])
#     return nums[:idx] + punct + nums[idx:]
# def masked(card):      return 'XXXX-XXXX-XXXX-' + card[-4:]
# def short_card(card):  return card[:15]
# def embedded(card):    return card  # last4 used separately
# def alt_label(card):   return card  # label applied in template

# VARIATIONS = {
#     "plain": plain,
#     "with_spaces": with_spaces,
#     "with_dashes": with_dashes,
#     "with_underscores": with_underscores,
#     "mixed": mixed,
#     "ocr": ocr_spacing,
#     "punctuation": punctuation_sep,
#     "masked": masked,
#     "short": short_card,
#     "embedded": embedded,
#     "alt_label": alt_label,
# }

# # ----------------------------
# # 3. Rich sentence templates
# #    {v} = full variant, {last4} = final four digits
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "FAKE DATA – Her credit card number is {v}.",
#         "FAKE DATA – This 16-digit number, {v}, is for testing only.",
#     ],
#     "with_spaces": [
#         "FAKE – Spaced format: {v}.",
#         "TEST ONLY – She reads it as {v}.",
#     ],
#     "with_dashes": [
#         "FAKE – Dashed receipt style: {v}.",
#         "TEST – You’ll see {v} on mock terminals.",
#     ],
#     "with_underscores": [
#         "FAKE – Underscore style: {v}.",
#         "TEST – Logged as {v}.",
#     ],
#     "mixed": [
#         "FAKE – Mixed separators: {v}.",
#         "TEST – Hybrid style: {v}.",
#     ],
#     "ocr": [
#         "FAKE – OCR readout: {v}.",
#         "TEST – Scanned as: {v}.",
#     ],
#     "punctuation": [
#         "FAKE – Punctuation inserted: {v}.",
#         "TEST – Parsed with punctuation: {v}.",
#     ],
#     "masked": [
#         "FAKE – Masked view: {v}.",
#         "TEST – Only last four visible: {v}.",
#     ],
#     "short": [
#         "FAKE – Truncated form: {v}.",
#         "TEST – First 15 digits only: {v}.",
#     ],
#     "embedded": [
#         "FAKE – My card ends with {last4}.",
#         "TEST – Last four digits: {last4}.",
#     ],
#     "alt_label": [
#         "FAKE – card no: {v}",
#         "TEST – credit card: {v}",
#         "FAKE – debit #: {v}",
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_credit_card_variations(count=50):
#     records = []
#     keys = list(VARIATIONS.keys())

#     while len(records) < count:
#         base = gen_base_card() if random.random() < 0.7 else gen_invalid_card()
#         key = random.choice(keys)
#         variant = VARIATIONS[key](base)
#         last4 = base[-4:]

#         tmpl = random.choice(TEMPLATES[key])
#         text = tmpl.format(v=variant, last4=last4)

#         records.append({
#             "text": text,
#             "card": variant,
#             "variation": key,
#             "is_valid": is_valid_card(variant),
#             "fake_data": True
#         })

#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_credit_card_variations(count=50)
#     with open("credit_cards.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ credit_cards.json generated with fake test data flagged.")




# #!/usr/bin/env python3
# import random
# import json
# from stdnum.luhn import calc_check_digit, is_valid as luhn_is_valid

# # ----------------------------
# # 1. Generators & validators
# # ----------------------------
# def gen_base_card():
#     prefix = str(random.choice([4, 5, 6]))  # Visa, MasterCard, Discover ranges
#     body   = "".join(str(random.randint(0, 9)) for _ in range(14))
#     check  = calc_check_digit(prefix + body)
#     return prefix + body + check

# def gen_invalid_card():
#     card = gen_base_card()
#     bad   = (int(card[-1]) + random.randint(1, 9)) % 10
#     return card[:-1] + str(bad)

# def is_valid_card(card):
#     nums = "".join(ch for ch in card if ch.isdigit())
#     return luhn_is_valid(nums)

# # ----------------------------
# # 2. Variation functions
# # ----------------------------
# def plain(card):        return card
# def with_spaces(card):  return ' '.join(card[i:i+4] for i in range(0, 16, 4))
# def with_dashes(card):  return '-'.join(card[i:i+4] for i in range(0, 16, 4))
# def with_underscores(card):
#     nums = card.replace(' ', '').replace('-', '')
#     return '_'.join(nums[i:i+4] for i in range(0, 16, 4))
# def mixed(card):
#     nums = card.replace(' ', '').replace('-', '')
#     return f"{nums[:4]}-{nums[4:8]} {nums[8:12]}-{nums[12:]}"
# def ocr_spacing(card):
#     nums = card.replace('-', '')
#     return nums[:8] + ' ' + nums[8:]
# def punctuation_sep(card):
#     nums = card.replace(' ', '').replace('-', '')
#     punct = random.choice(['.', '/', '_'])
#     idx   = random.choice([4, 8, 12])
#     return nums[:idx] + punct + nums[idx:]
# def masked(card):       return 'XXXX-XXXX-XXXX-' + card[-4:]
# def short_card(card):   return ' '.join(card[i:i+4] for i in range(0, 12, 4))
# def embedded(card):     return card
# def alt_label(card):    return card

# VARIATIONS = {
#     "plain":        plain,
#     "with_spaces":  with_spaces,
#     "with_dashes":  with_dashes,
#     "with_underscores": with_underscores,
#     "mixed":        mixed,
#     "ocr":          ocr_spacing,
#     "punctuation":  punctuation_sep,
#     "masked":       masked,
#     "short":        short_card,
#     "embedded":     embedded,
#     "alt_label":    alt_label,
# }

# # ----------------------------
# # 3. Sentence templates with all context keywords
# # ----------------------------
# TEMPLATES = {
#     "plain": [
#         "For secure payment use this credit card number {v} in your payment card form",
#         "Your card details for your swipe card test are recorded as {v}"
#     ],
#     "with_spaces": [
#         "Enter the card number with spaces as {v} into your card credentials field",
#         "The payment card info is shown as {v} on test terminals"
#     ],
#     "with_dashes": [
#         "You can view the card info with dashes {v} in the card information display",
#         "The credit card number printed on mock receipts reads {v}"
#     ],
#     "with_underscores": [
#         "Our test harness logs card details under {v} in account info",
#         "Fake data for card credentials uses underscore format {v}"
#     ],
#     "mixed": [
#         "Hybrid card format example in card details is {v}",
#         "Test entry for card credentials shows mixed separators {v}"
#     ],
#     "ocr": [
#         "OCR simulation may read the credit card number as {v} in card information",
#         "Machine scan example for card number scanned as {v}"
#     ],
#     "punctuation": [
#         "Punctuation test in card info example is {v} for payment card validation",
#         "The swipe card mock uses punctuation separated number {v}"
#     ],
#     "masked": [
#         "Masked card credentials appear as {v} for your credit card test",
#         "Only last four digits are visible in card info {v}"
#     ],
#     "short": [
#         "Truncated swipe card number example is {v} for testing error handling",
#         "Partial card number entry used in card details is {v}"
#     ],
#     "embedded": [
#         "For fraud simulation my card ends with {v} in the card information log",
#         "Verification only requires last four digits {v} in card credentials"
#     ],
#     "alt_label": [
#         "credit card number {v} is stored in payment card records",
#         "debit card like card no {v} may also be tested under card info"
#     ],
# }

# # ----------------------------
# # 4. Bulk generator
# # ----------------------------
# def generate_credit_card_variations(count=50):
#     records = []
#     keys    = list(VARIATIONS.keys())
#     while len(records) < count:
#         base    = gen_base_card() if random.random() < 0.7 else gen_invalid_card()
#         key     = random.choice(keys)
#         variant = VARIATIONS[key](base)
#         last4   = base[-4:]
#         tmpl    = random.choice(TEMPLATES[key])
#         text    = tmpl.format(v=variant, last4=last4)
#         records.append({
#             "text":       text,
#             "card":       variant,
#             "variation":  key,
#             "is_valid":   is_valid_card(variant),
#             "fake_data":  True
#         })
#     return records

# # ----------------------------
# # 5. Write JSON output
# # ----------------------------
# if __name__ == "__main__":
#     out = generate_credit_card_variations(count=50)
#     with open("credit_cards.json", "w", encoding="utf-8") as f:
#         json.dump(out, f, ensure_ascii=False, indent=2)
#     print("✅ credit_cards.json generated with full context coverage")





#!/usr/bin/env python3
import random
import json
from stdnum.luhn import calc_check_digit, is_valid as luhn_is_valid

# ----------------------------
# 1. Generators & validators
# ----------------------------
def gen_base_card():
    prefix = str(random.choice([4, 5, 6]))  # Visa, MasterCard, Discover
    body   = "".join(str(random.randint(0, 9)) for _ in range(14))
    check  = calc_check_digit(prefix + body)
    return prefix + body + check

def gen_invalid_card():
    card = gen_base_card()
    bad  = (int(card[-1]) + random.randint(1, 9)) % 10
    return card[:-1] + str(bad)

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(card):        return card
def with_spaces(card):  return ' '.join(card[i:i+4] for i in range(0, 16, 4))
def with_dashes(card):  return '-'.join(card[i:i+4] for i in range(0, 16, 4))
def with_underscores(card):
    nums = card.replace(' ', '').replace('-', '')
    return '_'.join(nums[i:i+4] for i in range(0, 16, 4))
def mixed(card):
    nums = card.replace(' ', '').replace('-', '')
    return f"{nums[:4]}-{nums[4:8]} {nums[8:12]}-{nums[12:]}"
def ocr_spacing(card):
    nums = card.replace('-', '')
    return nums[:8] + ' ' + nums[8:]
def punctuation_sep(card):
    nums  = card.replace(' ', '').replace('-', '')
    punct = random.choice(['.', '/', '_'])
    idx   = random.choice([4, 8, 12])
    return nums[:idx] + punct + nums[idx:]
def masked(card):       return 'XXXX-XXXX-XXXX-' + card[-4:]
def short_card(card):   return ' '.join(card[i:i+4] for i in range(0, 12, 4))
def embedded(card):     return card
def alt_label(card):    return card

VARIATIONS = {
    "plain":            plain,
    "with_spaces":      with_spaces,
    "with_dashes":      with_dashes,
    "with_underscores": with_underscores,
    "mixed":            mixed,
    "ocr":              ocr_spacing,
    "punctuation":      punctuation_sep,
    "masked":           masked,
    "short":            short_card,
    "embedded":         embedded,
    "alt_label":        alt_label,
}

# ----------------------------
# 3. Sentence templates
# ----------------------------
TEMPLATES = {
    "plain": [
        "For secure payment use this credit card number {v} in your payment card form",
        "Your card details for your swipe card test are recorded as {v}"
    ],
    "with_spaces": [
        "Enter the card number with spaces as {v} into your card credentials field",
        "The payment card info is shown as {v} on test terminals"
    ],
    "with_dashes": [
        "You can view the card info with dashes {v} in the card information display",
        "The credit card number printed on mock receipts reads {v}"
    ],
    "with_underscores": [
        "Our test harness logs card details under {v} in account info",
        "Fake data for card credentials uses underscore format {v}"
    ],
    "mixed": [
        "Hybrid card format example in card details is {v}",
        "Test entry for card credentials shows mixed separators {v}"
    ],
    "ocr": [
        "OCR simulation may read the credit card number as {v} in card information",
        "Machine scan example for card number scanned as {v}"
    ],
    "punctuation": [
        "Punctuation test in card info example is {v} for payment card validation",
        "The swipe card mock uses punctuation separated number {v}"
    ],
    "masked": [
        "Masked card credentials appear as {v} for your credit card test",
        "Only last four digits are visible in card info {v}"
    ],
    "short": [
        "Truncated swipe card number example is {v} for testing error handling",
        "Partial card number entry used in card details is {v}"
    ],
    "embedded": [
        "For fraud simulation my card ends with {v} in the card information log",
        "Verification only requires last four digits {v} in card credentials"
    ],
    "alt_label": [
        "credit card number {v} is stored in payment card records",
        "debit card like card no {v} may also be tested under card info"
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_credit_card_variations(count=50):
    records = []
    keys    = list(VARIATIONS.keys())
    while len(records) < count:
        # 70% valid, 30% invalid
        base   = gen_base_card() if random.random() < 0.7 else gen_invalid_card()
        valid  = luhn_is_valid("".join(ch for ch in base if ch.isdigit()))
        key    = random.choice(keys)
        variant = VARIATIONS[key](base)

        # for masked/short we preserve the base's validity
        if key in ("masked", "short"):
            is_valid = valid
        else:
            digits = "".join(ch for ch in variant if ch.isdigit())
            is_valid = luhn_is_valid(digits)

        text = random.choice(TEMPLATES[key]).format(v=variant)
        records.append({
            "text":      text,
            "card":      variant,
            "variation": key,
            "is_valid":  is_valid,
            "fake_data": True
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_credit_card_variations(count=50)
    with open("credit_cards.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ credit_cards.json generated with correct validity flags")
