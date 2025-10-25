# LangChain ATS — AI Resume Matcher & Job Tracker (In Progress)

This is my LangChain + Streamlit + Gemini experiment turned real-world project —
the goal? Build a personal AI job agent that hunts down the best matching job postings for me while I sleep.

It compares my resume with newly posted jobs (from my target locations and within the last 24 hours), gives a match percentage, and sends me a notification if it’s worth applying (>70% match).

I’m basically trying to automate the whole “job scrolling and comparing” pain using LLMs — hands-on learning while building something actually useful.

---

### Tech Stack

* LangChain — powering LLM pipelines and vector embeddings
* Google Gemini API — for semantic ranking and text understanding
* Streamlit — lightweight UI for experiments and dashboards
* FAISS / ChromaDB — fast vector similarity search
* Python — glue that holds everything together 

---

### Current Progress

* ✅ Resume parsing & embedding done
* ✅ Streamlit structure and sidebar navigation live
* ⚙️ Job scraping + match scoring engine in progress
* 🚧 Notification system cooking
* 📊 Next up: automated daily scan with email/push alerts

---

### The Vision

Think of it as “Jarvis for job hunting” — a system that knows your resume better than you do, tracks the market in real time, and pings you only when it finds something actually worth your time.

---

### Dev Note
Still a work in progress — I’m learning LangChain and Gemini as I go (might throw in LangGraph soon for some deeper experiments). If the repo looks messy, that’s just because it’s alive and evolving.
