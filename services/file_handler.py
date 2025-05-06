import os

def save_entry_to_file(entry):
    file_path = f'diary_entries/entry_{entry.id}.txt'
    with open(file_path, 'w') as f:
        f.write(f"Date: {entry.date}\n")
        f.write(f"Mood: {entry.mood}\n")
        f.write(f"Sentiment: {entry.sentiment}\n\n")
        f.write(entry.content)