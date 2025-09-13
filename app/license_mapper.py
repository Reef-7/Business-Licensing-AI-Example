import json
# mapping between business details to regulatory requirements

MAPPINGS = [
    {
        "condition": lambda b: b.get("uses_gas", False),
        "requirements": [
            {
                "title": "בדיקת צנרת גז",
                "priority": "high",
                "details": "שימוש בגז מחייב אישור מהרשויות המקומיות והבטיחות."
            }
        ]
    },
    {
        "condition": lambda b: b.get("serves_meat", False),
        "requirements": [
            {
                "title": "אחסון והגשה של בשר",
                "priority": "medium",
                "details": "שמירה על שרשרת קור ותקני היגיינה."
            }
        ]
    },
    {
        "condition": lambda b: b.get("seating", 0) > 50,
        "requirements": [
            {
                "title": "פיקוח על תוספות מקומות ישיבה",
                "priority": "medium",
                "details": "נדרש אישור מרשות המקומית בהתאם לתקנות תברואה."
            }
        ]
    },
]

def map_requirements(business: dict):
    """
    gets dict with the business details and returns customized requirements list

    """
    reqs = []
    for mapping in MAPPINGS:
        try:
            if mapping["condition"](business):
                reqs.extend(mapping["requirements"])
        except Exception as e:
            print(f"Warning: couldn't apply mapping {mapping}, error: {e}")
    return reqs


# For Testing
if __name__ == "__main__":
    # דוגמה לנתוני עסק (אפשר לשנות את הערכים כדי לבדוק תרחישים שונים)
    sample_business = {
        "uses_gas": True,   # האם העסק משתמש בגז
        "seating": 60,      # מספר מקומות ישיבה
        "delivers": False   # אפשר להוסיף שדות נוספים לפי הצורך
    }

    # מפעיל את פונקציית המיפוי
    mapped = map_requirements(sample_business)

    # שומר את התוצאה לקובץ JSON
    with open("data\mapped_requirements.json", "w", encoding="utf-8") as f:
        json.dump(mapped, f, ensure_ascii=False, indent=2)

    print("Mapped requirements saved to app/data/mapped_requirements.json")
    print(mapped)