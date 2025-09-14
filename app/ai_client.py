# ai_client.py
import os
import google.generativeai as genai


from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Make sure you set it in your .env file.")

genai.configure(api_key=GEMINI_API_KEY)

# model creation
model = genai.GenerativeModel("gemini-1.5-flash")  

def generate_report(business_data, regulations):
    """
    קבלת נתוני עסק ורשימת דרישות רגולציה,
    שליחתן למודל Gemini לקבלת דוח מותאם בעברית.
    """
    prompt = f"""
    אתה יועץ רגולציה לעסקים קטנים בישראל.
    הנה נתוני העסק:
    {business_data}

    הנה הדרישות הרלוונטיות בפורמט JSON:
    {regulations}

    צור דוח בעברית פשוטה וברורה שמסביר לבעל העסק:
    1. אילו דרישות חלות עליו
    2. סדר עדיפויות לביצוע
    3. המלצות פעולה
    4. הסברים קצרים בשפה לא משפטית
    """

    response = model.generate_content(prompt)
    return response.text
