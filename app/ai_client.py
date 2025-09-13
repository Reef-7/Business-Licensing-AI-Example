# ai_client.py
import os
import json
import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("Missing OPENAI_API_KEY. Set it in your .env file")

client = OpenAI(api_key=API_KEY)

def generate_report_llm(business_info: dict, mapped_requirements: list):
    """
    gets information about the business and regulatory mapping and returns customized report
    
    """
    prompt = f"""
    צור דוח ידידותי לבעל עסק בהתבסס על הנתונים הבאים:

    פרטי העסק:
    {json.dumps(business_info, ensure_ascii=False, indent=2)}

    דרישות רגולטוריות:
    {json.dumps(mapped_requirements, ensure_ascii=False, indent=2)}

    נא להציג:
    1. כותרת קצרה בעברית
    2. סקירה כללית של מצב העסק
    3. רשימה מסודרת של הדרישות עם עדיפות גבוהה/בינונית/נמוכה
    4. המלצות פרקטיות לביצוע
    """

    response = client.chat.completions.create(
        model="gpt-4o",  # או gpt-4 אם יש לך גישה
        messages=[
            {"role": "system", "content": "אתה יועץ מומחה לרגולציה לעסקים קטנים בישראל."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    # דוגמה לנתוני עסק (בפועל תוכל לטעון מקובץ JSON אם תרצה)
    test_business = {
        "name": "חומוס אבו-יוסף",
        "location": "תל אביב",
        "business_type": "מסעדה"
    }

    with open("data\mapped_requirements.json", "r", encoding="utf-8") as f:
        mapped = json.load(f)

    report = generate_report_llm(test_business, mapped)
    print("\n==== AI Report ====\n")
    print(report)