# MoodMate

MoodMate is a Flask-based web application designed to help users track their moods, record diary entries, and manage tasks. With AI-powered sentiment analysis, voice-to-text transcription using Whisper, and a user-friendly dashboard, MoodMate provides a personal space to reflect on emotions and stay organized. Whether you're managing stress or planning your day, MoodMate supports your mental well-being and productivity.

![MoodMate Dashboard](https://github.com/shevon2000/MoodMate/raw/main/static/dashboard-preview.png)

## ✨ Features

- **Diary Entries**: Write or record (via voice input) diary entries with mood selection (Happy, Neutral, Sad)
- **Sentiment Analysis**: Analyzes entry text using TextBlob and VADER, scoring sentiment on a 1–10 scale
- **Task Management**: Create, track, and mark tasks as complete, with overdue task alerts
- **Dashboard**: View recent diary entries, pending tasks, and overdue tasks at a glance
- **User Authentication**: Secure login and registration using Flask-Login
- **Voice Input**: Record diary entries with voice-to-text transcription using OpenAI's Whisper
- **Data Export**: Download diary entries as text files saved locally
- **Responsive UI**: Built with Bootstrap and Chart.js for a clean, interactive experience

## 🛠️ Tech Stack

- **Backend**: Python 3.8+, Flask, Flask-Login, Flask-SQLAlchemy
- **Frontend**: HTML, Bootstrap 5, Chart.js
- **Sentiment Analysis**: TextBlob, VADER
- **Voice-to-Text**: OpenAI Whisper
- **Database**: SQLite (local)

## 📁 Directory Structure

```
MoodMate/
│
├── app.py                    # Main Flask application
├── blueprints/               # Flask blueprints for modular routes
│   ├── auth.py               # Authentication routes (login, signup)
│   ├── diary.py              # Diary routes (add, view, download, transcribe entries)
│   └── tasks.py              # Task routes (add, complete tasks)
│
├── templates/                # HTML templates
│   ├── add_entry.html        # Diary entry form with voice input
│   ├── dashboard.html        # User dashboard
│   ├── base.html             # Base template with common layout
│   ├── index.html            # Landing page
│   ├── helpdesk.html         # Helpdesk page
│   ├── login.html            # Login page
│   ├── signup.html           # Signup page
│   ├── entries.html          # List all diary entries
│   └── view_entry.html       # View single diary entry
│
├── static/                   # Static files (CSS, JS)
│   ├── css/                  # Bootstrap and custom CSS
│   └── js/                   # Chart.js and custom scripts
│
├── services/                 # Utility services
│   ├── file_handler.py       # File operations for saving diary entries
│   └── sentiment.py          # Sentiment analysis with TextBlob/VADER
│
├── instance/                 # SQLite database (excluded in .gitignore)
├── diary_entries/            # Downloaded diary entry files (excluded)
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore file
└── README.md                 # This file
```

## 📋 Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shevon2000/MoodMate.git
   cd MoodMate

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
  Note: Whisper may require additional setup (e.g., FFmpeg). See Whisper documentation for details.

4. **Run the Application**:
   ```bash
   python app.py
  Access at http://localhost:5000.

## 💡 Usage

### Register/Login:
* Go to `/auth/signup` to create an account
* Log in at `/auth/login`

### Add Diary Entries:
* Navigate to `/diary/add`
* Enter text or use voice input (click "Start Recording") for Whisper transcription
* Select a mood (Happy, Neutral, Sad) and submit
* Sentiment is automatically analyzed (1–10 scale)

### View Dashboard:
* Go to `/dashboard` to see recent entries, pending tasks, and overdue tasks
* Click "View" to see entry details or download as text

### Manage Tasks:
* Add tasks at `/tasks/add`
* Mark tasks as complete at `/tasks/complete/<id>`

## 📄 License

This project is licensed under the MIT License.

## 📞 Contact

For questions, contact [shevon2000](https://github.com/shevon2000) or open an issue on GitHub.

---

<p align="center">Made with ❤️ for better mental health</p>
