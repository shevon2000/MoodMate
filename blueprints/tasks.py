from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import Task
from database import db
from datetime import datetime

tasks = Blueprint('tasks', __name__)

@tasks.route('/add', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
        task = Task(title=title, description=description, due_date=due_date, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully!')
        return redirect(url_for('tasks.all_tasks'))
    return render_template('tasks/add_task.html')

@tasks.route('/tasks')
@login_required
def all_tasks():
    date_filter = request.args.get('date')
    tasks = Task.query.filter_by(user_id=current_user.id)
    if date_filter:
        tasks = tasks.filter(Task.due_date.startswith(date_filter))
    tasks = tasks.order_by(Task.due_date).all()
    current_date = datetime.now().date()
    return render_template('tasks/tasks.html', tasks=tasks, current_date=current_date)

@tasks.route('/complete/<int:id>')
@login_required
def complete_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash('Unauthorized access')
        return redirect(url_for('tasks.all_tasks'))
    task.completed = True
    db.session.commit()
    flash('Task marked as completed!')
    return redirect(url_for('tasks.all_tasks'))