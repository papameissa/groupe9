from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import json
import os
import logging

app = Flask(__name__)

# Configuration du logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Fichier pour stocker les données
DATA_FILE = 'mood_data.json'

# Initialiser le fichier de données s'il n'existe pas
def init_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

# Charger les données
def load_moods():
    init_data_file()
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Sauvegarder les données
def save_moods(moods):
    with open(DATA_FILE, 'w') as f:
        json.dump(moods, f, indent=2)

@app.route('/')
def index():
    logging.info("Page d'accueil consultée")
    moods = load_moods()
    moods.sort(key=lambda x: x['date'], reverse=True)
    return render_template('index.html', moods=moods)

@app.route('/add_mood', methods=['POST'])
def add_mood():
    mood_emoji = request.form.get('mood')
    note = request.form.get('note', '')

    moods = load_moods()

    new_mood = {
        'id': len(moods) + 1,
        'emoji': mood_emoji,
        'note': note,
        'date': datetime.now().strftime('%Y-%m-%d'),
        'time': datetime.now().strftime('%H:%M')
    }

    moods.append(new_mood)
    save_moods(moods)

    logging.info(f"Nouvelle humeur ajoutée : {mood_emoji} - Note : {note}")
    return redirect(url_for('index'))

@app.route('/delete_mood/<int:mood_id>', methods=['POST'])
def delete_mood(mood_id):
    moods = load_moods()
    moods = [m for m in moods if m['id'] != mood_id]
    save_moods(moods)
    logging.info(f"Humeur supprimée : id={mood_id}")
    return redirect(url_for('index'))

@app.route('/stats')
def stats():
    logging.info("Page des statistiques consultée")
    moods = load_moods()
    return render_template('stats.html', moods=moods)

@app.route('/api/mood_stats')
def mood_stats():
    moods = load_moods()

    mood_count = {}
    for mood in moods:
        emoji = mood['emoji']
        mood_count[emoji] = mood_count.get(emoji, 0) + 1

    daily_moods = {}
    for mood in moods:
        date = mood['date']
        if date not in daily_moods:
            daily_moods[date] = []
        daily_moods[date].append(mood['emoji'])

    return jsonify({
        'mood_count': mood_count,
        'daily_moods': daily_moods,
        'total': len(moods)
    })

@app.route('/logs')
def view_logs():
    """Route pour visualiser les logs dans le navigateur."""
    try:
        with open('app.log', 'r') as f:
            content = f.read()
        logging.info("Page des logs consultée")
        return (
            '<html><head><title>App Logs</title></head>'
            '<body style="background:#111;margin:0;padding:20px;">'
            f'<pre style="color:#0f0;font-size:13px;font-family:monospace;">{content}</pre>'
            '</body></html>'
        )
    except FileNotFoundError:
        return "Aucun log disponible.", 404

if __name__ == '__main__':
    init_data_file()
    logging.info("Démarrage de l'application Flask")
    app.run(debug=True, host='0.0.0.0', port=5009)
