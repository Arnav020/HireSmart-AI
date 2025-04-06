# 💼 HireSmart AI

**Automating Job Screening with Multi-Agent Intelligence**

HireSmart AI is a smart recruitment assistant that automates the candidate screening process using a collaborative multi-agent architecture. It reads job descriptions, extracts key data from CVs, matches and shortlists top candidates, and even schedules interviews — all with minimal human intervention.

---

## 🚀 Features

- 📄 **JD Summarizer Agent**: Cleans and summarizes job descriptions.
- 🧠 **CV Extractor Agent**: Extracts relevant data from resumes.
- ⚖️ **Matcher Agent**: Calculates match scores between JDs and CVs.
- 🎯 **Shortlister Agent**: Selects top candidates based on scores.
- 🗓️ **Scheduler Agent**: Sends interview invites and generates Google Meet links.

---

## 🗂️ Folder Structure

```bash
HireSmartAI/
│
├── Agents/
│   ├── jd_summarizer.py
│   ├── cv_extractor.py
│   ├── matcher.py
│   ├── shortlister.py
│   └── scheduler.py
│
├── Data/
│   ├── CVs/                  # Candidate resumes
│   └── job_descriptions/     # Raw JDs and summaries
│
├── Database/
│   ├── hire_smart.db         # SQLite database
│   └── db_handler.py         # Handles data persistence
│
├── Emails/
│   └── email_sender.py       # Sends interview invites
│
├── Utils/
│   └── text_utils.py         # Common text processing utilities
│
├── main.py                   # Pipeline execution file
├── requirements.txt          # Python dependencies
└── README.md
