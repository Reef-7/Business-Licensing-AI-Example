# 🏪 Business Licensing AI  
A system for business owners in Israel for understanding of relevant licensing requirements.

## 📌 Project Goals
This system allows business owners to:
- Fill out a short questionnaire about their business.
- Receive a customized report using AI with the licensing requirements that apply to it.
- Understand the priorities and recommendations for action an in accessible and clear way.
- Download the report as a text file for future use.


## 🏗 General Architecture
**Frontend** : HTML + CSS + Vanilla JS
**Backend**  : Python + FastAPI 
**AI**       : Google Gemini 
**Data**     : PDF File Processing → JSON → Requirements mapping

📊 **Flowchart:**

[User] → [Questionnaire Form in Frontend] → [API in FastAPI] → [Matching Engine and Requirements Mapping]
→ [Large Language Model (Gemini)] → [Customized Report] → [Frontend Displays and Download Option]

## ⚙️ Installation and Run Instructions

### 1. Installing a Development Environment
bash
git clone git@github.com:Reef-7/Business-Licensing-AI-Example.git
cd business-licensing-ai-example
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt

### 2. .env file

Create a .env file in the app/ folder with:

GEMINI_API_KEY=your_google_gemini_key_here

### 3. Start the server
cd app
uvicorn main:app --reload --host 127.0.0.1 --port 8000

The server will be up at:
http://127.0.0.1:8000

You can test the API via Swagger UI at:
http://127.0.0.1:8000/docs

### 4. Open the interface

Open frontend/index.html in a browser or use the Live Server from VSCode.
Fill out the questionnaire and click "Create Report".


## 🧠 AI 
- Selected model : Google Gemini(gemini-1.5-flash)
- Reason: Good support in Hebrew, high speed, relatively free to use
- Usage: The model receives the business data and the processed requirements and returns clear text in Hebrew, divided into categories with priorities.
- Prompts: documented in the file doc/prompts.md

  
## 📂 Project Structure 

business-licensing-ai-example/
│
├── app/
│   ├── main.py               # FastAPI endpoints
│   ├── ai_client.py          # Calls for Gemini API
│   ├── license_mapper.py     # Mapping requirements according to business properties 
│   ├── pdf_processor.py      # PDF → JSON processing script
│   ├── data/
│   │   ├── raw/              # original files 
│   │   ├── processed.json    # processed text 
│   │   └── mapped_requirements.json
│   └── ...
│
├── frontend/
│   ├── index.html
│   └── app.js
│
├── doc/
│   ├── development_log.md
│   ├── prompts.md
│   └── screenshots/
│
├── requirements.txt
└── README.md

## 🧪 API Examples

Generate Report

curl -X POST http://127.0.0.1:8000/api/generate-report \
-H "Content-Type: application/json" \
-d '{
  "name": "מסעדת דוגמה",
  "area_sqm": 120,
  "seating": 50,
  "uses_gas": true,
  "serves_meat": true,
  "delivers": false
}

Sample Response:


{
  "mapped_requirements": [
    {"title":"אישור כיבוי אש","priority":"high"},
    {"title":"אישור תברואתי","priority":"medium"}
  ],
  "report": "לפי הנתונים שמסרת, לעסק שלך חלות הדרישות הבאות..."
}

## 🛠 Development Tools
- ChatGPT : Help with coding, clarifications, and optimizations.
- Google Gemini API : Real-time reporting 
