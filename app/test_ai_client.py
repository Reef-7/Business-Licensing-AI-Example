from ai_client import generate_report

sample_business = {"גודל": 120, "תפוסה": 40, "משלוחים": True}
sample_regulations = [
    {"שם": "רישיון עסק", "תנאי": "חובה מעל 50 מ״ר"},
    {"שם": "כיבוי אש", "תנאי": "חובה לכל עסק עם יותר מ-20 אנשים"},
]

report = generate_report(sample_business, sample_regulations)
print(report)
