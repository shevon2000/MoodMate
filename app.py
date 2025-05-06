import os
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user
from database import init_db
from models import User, DiaryEntry, Task
from blueprints.auth import auth
from blueprints.diary import diary
from blueprints.tasks import tasks
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a9f3b726e21c4a6d8db2f963efcbb9a5f1c2a7c7d5c842a3b9d59cf4c0b78a9e'

# Initialize database
init_db(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(diary, url_prefix='/diary')
app.register_blueprint(tasks, url_prefix='/tasks')

# Create necessary directories
os.makedirs('diary_entries', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    recent_entries = DiaryEntry.query.filter_by(user_id=current_user.id).order_by(DiaryEntry.date.desc()).limit(50).all()
    pending_tasks = Task.query.filter_by(user_id=current_user.id, completed=False).order_by(Task.due_date).limit(50).all()
    overdue_tasks = Task.query.filter_by(user_id=current_user.id, completed=False).filter(Task.due_date < datetime.now().date()).count()
    current_date = datetime.now().date()
    return render_template('dashboard.html', recent_entries=recent_entries, pending_tasks=pending_tasks, overdue_tasks=overdue_tasks, current_date=current_date)

@app.route('/helpdesk')
def helpdesk():
    return render_template('helpdesk.html')

if __name__ == '__main__':
    app.run(debug=True)