from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file
from flask_login import login_required, current_user
from models import DiaryEntry
from database import db
from services.sentiment import analyze_sentiment
from services.file_handler import save_entry_to_file
from datetime import datetime
import os
import whisper
from io import BytesIO
import tempfile

diary = Blueprint('diary', __name__)

@diary.route('/add', methods=['GET', 'POST'])
@login_required
def add_entry():
    if request.method == 'POST':
        content = request.form['content']
        mood = request.form['mood']
        date_str = request.form['date']
        date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M')
        sentiment = analyze_sentiment(content)
        entry = DiaryEntry(content=content, mood=mood, sentiment=sentiment, date=date, user_id=current_user.id)
        db.session.add(entry)
        db.session.commit()
        save_entry_to_file(entry)
        flash('Diary entry added successfully!')
        return redirect(url_for('diary.all_entries'))
    return render_template('diary/add_entry.html')

@diary.route('/entries')
@login_required
def all_entries():
    date_filter = request.args.get('date')
    entries = DiaryEntry.query.filter_by(user_id=current_user.id)
    if date_filter:
        entries = entries.filter(DiaryEntry.date.startswith(date_filter))
    entries = entries.order_by(DiaryEntry.date.desc()).all()
    return render_template('diary/all_entries.html', entries=entries)

@diary.route('/entry/<int:id>')
@login_required
def view_entry(id):
    entry = DiaryEntry.query.get_or_404(id)
    if entry.user_id != current_user.id:
        flash('Unauthorized access')
        return redirect(url_for('diary.all_entries'))
    return render_template('diary/view_entry.html', entry=entry)

@diary.route('/download/<int:id>')
@login_required
def download_entry(id):
    entry = DiaryEntry.query.get_or_404(id)
    if entry.user_id != current_user.id:
        flash('Unauthorized access')
        return redirect(url_for('diary.all_entries'))
    file_path = f'diary_entries/entry_{entry.id}.txt'
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    flash('File not found')
    return redirect(url_for('diary.all_entries'))

@diary.route('/visualize')
@login_required
def visualize():
    entries = DiaryEntry.query.filter_by(user_id=current_user.id).order_by(DiaryEntry.date).all()
    # Convert DiaryEntry objects to a JSON-serializable format
    entries_data = [
        {
            'date': entry.date.isoformat(),
            'mood': entry.mood,
            'sentiment': entry.sentiment
        } for entry in entries
    ]
    return render_template('visualize.html', entries=entries_data)

@diary.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return {'error': 'No audio file provided'}, 400
    audio_file = request.files['audio']
    try:
        # Save audio to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as temp_file:
            audio_file.save(temp_file.name)
            temp_file_path = temp_file.name
        
        # Load Whisper model and transcribe
        model = whisper.load_model("base")
        result = model.transcribe(temp_file_path, fp16=False)
        text = result["text"]
        
        # Clean up temporary file
        os.unlink(temp_file_path)
        
        return {'text': text}, 200
    except Exception as e:
        # Clean up temporary file in case of error
        if 'temp_file_path' in locals():
            os.unlink(temp_file_path)
        return {'error': f'Transcription failed: {str(e)}'}, 500