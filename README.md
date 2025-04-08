# AI-Business-Consultant
# 💼 AI Business Consultant - SWOT Analysis

Welcome to the **AI Business Consultant**, an intelligent Streamlit-based application that provides detailed **SWOT analysis** (Strengths, Weaknesses, Opportunities, Threats) for any company based on simulated market context and AI insights.

This tool leverages **Google's Gemini API** to generate comprehensive business insights, including optional financial data, competitive analysis, and strategic recommendations.

---

## 🚀 Features

- 📋 **User Inputs**:
  - Company Name
  - Industry
  - Country (Optional)
  - Date of Analysis

- 🔍 **Toggleable Insights**:
  - Financial Context
  - Competitive Landscape
  - Strategic Recommendations

- 🧠 **AI-Generated SWOT**:
  - Contextualized with simulated financial, industry, and competitive data
  - Generated using Gemini (Google Generative AI)

- 🧾 **Session-based Chat**:
  - Remembers analysis history in a conversational format
  - Option to clear analysis and start fresh

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Python](https://www.python.org/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/harshit6ioy/AI-Business-Consultant
   cd AI-Business-Consultant


2.Install Dependencies
pip install -r requirements.txt


3.Set up your .env file Create a .env file in the root directory with the following content:
GOOGLE_API_KEY=your_google_generative_ai_api_key_here


4.Run the app

streamlit run chatbot.py
