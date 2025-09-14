## 🛠️ Prompts לפיתוח
במהלך הפיתוח נעשה שימוש בכלי AI (ChatGPT ) לכתיבת קוד ראשוני עבור:
- FastAPI endpoints (`main.py`)
- סקריפטים לעיבוד PDF ל-JSON (`pdf_processor.py`)
- לוגיקת מיפוי דרישות לפי פרטי העסק (`license_mapper.py`)
- Frontend בסיסי עם HTML/JS (`index.html` ו-`app.js`)

**דוגמה לפרומפטים שהופעלו במהלך הפיתוח:**

1. **FastAPI Endpoint**
> "צור קוד ל-FastAPI שמקבל POST עם פרטי עסק ומחזיר JSON עם דרישות רישוי מותאמות, כולל שם העסק, שטח במ"ר, מספר מקומות ישיבה, ושימוש במאפיינים נוספים."

2. **עיבוד PDF**
> "כתוב סקריפט פייתון שקורא קובץ PDF בעברית ומחלץ טקסט רלוונטי על פי מילות מפתח, ושומר את התוצאה ב-JSON."

3. **Frontend בסיסי**
> "צור שאלון HTML/JS שבו המשתמש מזין שם עסק, שטח, מקומות ישיבה, ושדות מאפיינים (גז, בשר, משלוחים), ושולח את הנתונים ל-API."

---

## 📊 Prompts בזמן ריצה (Run-time Prompts)
בשלב הריצה, ה-AI (Google Gemini API) מקבל את הפרטים שהוזנו בטופס ומחזיר דוח מותאם אישית.  
הפרומפט שנשלח ל-Gemini:

```json
{
  "role": "system",
  "content": "You are an assistant that writes clear and simple licensing requirement reports in Hebrew."
},
{
  "role": "user",
  "content": "פרטי עסק:\nשם עסק: {business_name}\nשטח: {area} מ\"ר\nמקומות ישיבה: {seats}\nמאפיינים: {features}\n\nדרישות רישוי רלוונטיות:\n{mapped_requirements}\n\nצור דוח תמציתי וברור בעברית, כולל המלצות פעולה ממוקדות."
}