# #!/usr/bin/env python3
# import importlib, json, os, random, sys
# import pandas as pd
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from docx import Document

# # -----------------------------------------------------------------------------
# # 1. Configuration
# # -----------------------------------------------------------------------------
# DEFAULT_COUNT   = 50    # records per module
# PARA_COUNT      = 5
# SENTS_PER_PARA  = 5
# OUT_DIR         = "mixed_output"
# os.makedirs(OUT_DIR, exist_ok=True)

# # -----------------------------------------------------------------------------
# # 2. Discover & import your generate_*.py modules
# # -----------------------------------------------------------------------------
# MODULES = []
# for fn in os.listdir("."):
#     if fn.startswith("generate_") and fn.endswith(".py"):
#         MODULES.append(importlib.import_module(fn[:-3]))

# # -----------------------------------------------------------------------------
# # 3. Find each module’s *_variations() function
# # -----------------------------------------------------------------------------
# def get_generator(mod):
#     funcs = [getattr(mod, n) for n in dir(mod)
#              if n.endswith("_variations") and callable(getattr(mod, n))]
#     if not funcs:
#         raise AttributeError(f"No `*_variations` in {mod.__name__}")
#     if len(funcs)==1:
#         return funcs[0]
#     base = mod.__name__.split("generate_")[-1]
#     for fn in funcs:
#         if base in fn.__name__:
#             return fn
#     return funcs[0]

# # -----------------------------------------------------------------------------
# # 4. Collect & shuffle
# # -----------------------------------------------------------------------------
# def collect_records(count_per_module):
#     pool = []
#     for mod in MODULES:
#         gen = get_generator(mod)
#         pool.extend(gen(count_per_module))
#     random.shuffle(pool)
#     return pool

# # -----------------------------------------------------------------------------
# # 5. Structured output
# # -----------------------------------------------------------------------------
# def emit_structured(df):
#     # CSV
#     df.to_csv(os.path.join(OUT_DIR, "output.csv"), index=False)
#     # filtered JSON (no nulls)
#     records = df.to_dict(orient="records")
#     cleaned = []
#     for r in records:
#         clean = {k: v for k, v in r.items() if pd.notna(v)}
#         cleaned.append(clean)
#     with open(os.path.join(OUT_DIR, "output.json"), "w", encoding="utf-8") as f:
#         json.dump(cleaned, f, ensure_ascii=False, indent=2)
#     # Excel .xlsx
#     df.to_excel(os.path.join(OUT_DIR, "output.xlsx"), index=False)
#     # Parquet
#     try:
#         df.to_parquet(os.path.join(OUT_DIR, "output.parquet"), index=False)
#     except ImportError:
#         pass

# # -----------------------------------------------------------------------------
# # 6. PST as SQL dump
# # -----------------------------------------------------------------------------
# def emit_pst(records):
#     with open(os.path.join(OUT_DIR, "output.pst"), "w", encoding="utf-8") as f:
#         for r in records:
#             txt = r["text"].replace("'", "''")
#             var = r["variation"]
#             val = '1' if r.get("is_valid") else '0'
#             f.write(
#                 f"INSERT INTO sentences(text,variation,is_valid)"
#                 f" VALUES('{txt}','{var}',{val});\n"
#             )

# # -----------------------------------------------------------------------------
# # 7. Unstructured exports
# # -----------------------------------------------------------------------------
# def emit_txt(records):
#     with open(os.path.join(OUT_DIR, "output.txt"), "w", encoding="utf-8") as f:
#         for r in records:
#             f.write(r["text"] + "\n\n")

# def emit_log(records):
#     with open(os.path.join(OUT_DIR, "output.log"), "w", encoding="utf-8") as f:
#         for r in records:
#             f.write(r["text"] + "\n")

# def emit_html(records):
#     with open(os.path.join(OUT_DIR, "output.html"), "w", encoding="utf-8") as f:
#         f.write("<!doctype html>\n<html><body>\n")
#         for r in records:
#             # wrap each sentence in a <p>
#             f.write(f"  <p>{r['text']}</p>\n")
#         f.write("</body></html>")

# def emit_pdf(records):
#     c = canvas.Canvas(os.path.join(OUT_DIR, "output.pdf"), pagesize=letter)
#     w, h = letter; y = h - 40
#     for r in records:
#         c.drawString(40, y, r["text"])
#         y -= 14
#         if y < 40:
#             c.showPage(); y = h - 40
#     c.save()

# def emit_docx(records):
#     doc = Document()
#     for r in records:
#         doc.add_paragraph(r["text"])
#     doc.save(os.path.join(OUT_DIR, "output.docx"))

# def emit_sql(records):
#     with open(os.path.join(OUT_DIR, "output.sql"), "w", encoding="utf-8") as f:
#         for r in records:
#             txt = r["text"].replace("'", "''")
#             var = r["variation"]
#             val = '1' if r.get("is_valid") else '0'
#             f.write(
#                 f"INSERT INTO sentences(text,variation,is_valid)"
#                 f" VALUES('{txt}','{var}',{val});\n"
#             )

# def emit_diff(records):
#     with open(os.path.join(OUT_DIR, "output.diff"), "w", encoding="utf-8") as f:
#         f.write("--- original\n+++ mixed\n")
#         for r in records:
#             f.write(f"+ {r['text']}\n")

# def emit_paragraphs(records):
#     needed = PARA_COUNT * SENTS_PER_PARA
#     block  = records[:needed]
#     with open(os.path.join(OUT_DIR, "output_paras.txt"), "w", encoding="utf-8") as f:
#         for i in range(PARA_COUNT):
#             chunk = block[i*SENTS_PER_PARA:(i+1)*SENTS_PER_PARA]
#             para = " ".join(r["text"] for r in chunk)
#             f.write(para + "\n\n")

# # -----------------------------------------------------------------------------
# # 8. Main
# # -----------------------------------------------------------------------------
# if __name__ == "__main__":
#     count   = int(sys.argv[1]) if len(sys.argv)>1 else DEFAULT_COUNT
#     records = collect_records(count)
#     df      = pd.DataFrame(records)

#     emit_structured(df)
#     emit_pst(records)          # now SQL, not JSON
#     emit_txt(records)
#     emit_log(records)
#     emit_html(records)         # real HTML
#     emit_pdf(records)
#     emit_docx(records)
#     emit_sql(records)          # INSERT statements
#     emit_diff(records)
#     emit_paragraphs(records)

#     print(f"✅ Generated {count} records per module from {len(MODULES)} generators")
#     print(f"   → all outputs in folder: {OUT_DIR}")


#!/usr/bin/env python3
import importlib
import json
import os
import random
import sys

import pandas as pd
import xlwt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document

# -----------------------------------------------------------------------------
# 1. Configuration
# -----------------------------------------------------------------------------
DEFAULT_COUNT   = 50    # records per module
PARA_COUNT      = 5
SENTS_PER_PARA  = 5
OUT_DIR         = "mixed_output"
os.makedirs(OUT_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# 2. Discover & import your generate_*.py modules
# -----------------------------------------------------------------------------
MODULES = []
for fn in os.listdir("."):
    if fn.startswith("generate_") and fn.endswith(".py"):
        MODULES.append(importlib.import_module(fn[:-3]))

# -----------------------------------------------------------------------------
# 3. Find each module’s *_variations() function
# -----------------------------------------------------------------------------
def get_generator(mod):
    funcs = [getattr(mod, n) for n in dir(mod)
             if n.endswith("_variations") and callable(getattr(mod, n))]
    if not funcs:
        raise AttributeError(f"No `*_variations` in {mod.__name__}")
    if len(funcs) == 1:
        return funcs[0]
    base = mod.__name__.split("generate_")[-1]
    for fn in funcs:
        if base in fn.__name__:
            return fn
    return funcs[0]

# -----------------------------------------------------------------------------
# 4. Collect & shuffle
# -----------------------------------------------------------------------------
def collect_records(count_per_module):
    pool = []
    for mod in MODULES:
        gen = get_generator(mod)
        pool.extend(gen(count_per_module))
    random.shuffle(pool)
    return pool

# -----------------------------------------------------------------------------
# 5. Structured outputs
# -----------------------------------------------------------------------------
def emit_csv(df):
    df.to_csv(os.path.join(OUT_DIR, "output.csv"), index=False)

def emit_json(df):
    records = df.to_dict(orient="records")
    cleaned = [{k: v for k, v in r.items() if pd.notna(v)} for r in records]
    with open(os.path.join(OUT_DIR, "output.json"), "w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)

def emit_xlsx(df):
    df.to_excel(os.path.join(OUT_DIR, "output.xlsx"), index=False)

def emit_xls(df):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Sheet1")
    cols = list(df.columns)
    # header
    for j, col in enumerate(cols):
        ws.write(0, j, col)
    # data rows
    for i, row in enumerate(df.itertuples(index=False), start=1):
        for j, val in enumerate(row):
            ws.write(i, j, val)
    wb.save(os.path.join(OUT_DIR, "output.xls"))

def emit_parquet(df):
    try:
        df.to_parquet(os.path.join(OUT_DIR, "output.parquet"), index=False)
    except ImportError:
        print("⚠️  Skipping Parquet (no engine).")

# -----------------------------------------------------------------------------
# 6. Unstructured exports
# -----------------------------------------------------------------------------
def emit_txt(records):
    with open(os.path.join(OUT_DIR, "output.txt"), "w", encoding="utf-8") as f:
        for r in records:
            f.write(r["text"] + "\n\n")

def emit_log(records):
    with open(os.path.join(OUT_DIR, "output.log"), "w", encoding="utf-8") as f:
        for r in records:
            f.write(r["text"] + "\n")

def emit_html(records):
    with open(os.path.join(OUT_DIR, "output.html"), "w", encoding="utf-8") as f:
        f.write("<!doctype html>\n<html><body>\n")
        for r in records:
            f.write(f"  <p>{r['text']}</p>\n")
        f.write("</body></html>")

def emit_pdf(records):
    c = canvas.Canvas(os.path.join(OUT_DIR, "output.pdf"), pagesize=letter)
    w, h = letter; y = h - 40
    for r in records:
        c.drawString(40, y, r["text"])
        y -= 14
        if y < 40:
            c.showPage(); y = h - 40
    c.save()

def emit_docx_and_doc(records):
    path_x = os.path.join(OUT_DIR, "output.docx")
    path_d = os.path.join(OUT_DIR, "output.doc")
    doc = Document()
    for r in records:
        doc.add_paragraph(r["text"])
    doc.save(path_x)
    doc.save(path_d)

def emit_sql(records):
    with open(os.path.join(OUT_DIR, "output.sql"), "w", encoding="utf-8") as f:
        for r in records:
            txt = r["text"].replace("'", "''")
            var = r["variation"]
            val = '1' if r.get("is_valid") else '0'
            f.write(f"INSERT INTO sentences(text,variation,is_valid)"
                    f" VALUES('{txt}','{var}',{val});\n")

def emit_diff(records):
    with open(os.path.join(OUT_DIR, "output.diff"), "w", encoding="utf-8") as f:
        f.write("--- original\n+++ mixed\n")
        for r in records:
            f.write(f"+ {r['text']}\n")

def emit_paragraphs(records):
    needed = PARA_COUNT * SENTS_PER_PARA
    block  = records[:needed]
    with open(os.path.join(OUT_DIR, "output_paras.txt"), "w", encoding="utf-8") as f:
        for i in range(PARA_COUNT):
            chunk = block[i*SENTS_PER_PARA:(i+1)*SENTS_PER_PARA]
            para = " ".join(r["text"] for r in chunk)
            f.write(para + "\n\n")

# -----------------------------------------------------------------------------
# 7. Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    count   = int(sys.argv[1]) if len(sys.argv)>1 else DEFAULT_COUNT
    records = collect_records(count)
    df      = pd.DataFrame(records)

    # structured
    emit_csv(df)
    emit_json(df)
    emit_xlsx(df)
    emit_xls(df)
    emit_parquet(df)

    # unstructured
    emit_txt(records)
    emit_log(records)
    emit_html(records)
    emit_pdf(records)
    emit_docx_and_doc(records)
    emit_sql(records)
    emit_diff(records)
    emit_paragraphs(records)

    print(f"✅ Generated {count} records per module from {len(MODULES)} generators")
    print(f"   → all 14 outputs in: {OUT_DIR}")
