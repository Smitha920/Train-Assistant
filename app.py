from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import uuid

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Simulated in-memory databases
seat_swap_db = []
coach_alert_db = []
track_guard_db = []
lost_found_db = []

# Home
@app.route('/')
def home():
    return render_template('index.html')

# SeatSwap Module
@app.route('/seatswap', methods=['GET', 'POST'])
def seatswap():
    if request.method == 'POST':
        entry = {
            'id': str(uuid.uuid4()),
            'pnr': request.form['pnr'],
            'current': request.form['current_seat'],
            'preferred': request.form['preferred_seat']
        }
        seat_swap_db.append(entry)
        flash('Seat preference submitted.')
        return redirect(url_for('seatswap'))
    return render_template('seatswap.html', entries=seat_swap_db)

# CoachAlert Module
@app.route('/coachalert', methods=['GET', 'POST'])
def coachalert():
    if request.method == 'POST':
        alert = {
            'station': request.form['station'],
            'minutes_before': int(request.form['minutes_before'])
        }
        coach_alert_db.append(alert)
        flash('Wake-up alert set!')
        return redirect(url_for('coachalert'))
    return render_template('coachalert.html', alerts=coach_alert_db)

# TrackGuard Module
@app.route('/trackguard', methods=['GET', 'POST'])
def trackguard():
    if request.method == 'POST':
        report = {
            'type': request.form['issue_type'],
            'details': request.form['details'],
            'coach': request.form['coach'],
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        track_guard_db.append(report)
        flash('Safety issue reported.')
        return redirect(url_for('trackguard'))
    return render_template('trackguard.html', reports=track_guard_db)

# Lost and Found Module
@app.route('/lostfound', methods=['GET', 'POST'])
def lostfound():
    if request.method == 'POST':
        entry = {
            'id': str(uuid.uuid4()),
            'type': request.form['entry_type'],
            'description': request.form['description'],
            'coach': request.form['coach'],
            'contact': request.form['contact'],
            'date': datetime.now().strftime("%Y-%m-%d")
        }
        lost_found_db.append(entry)
        flash('Lost/Found item submitted.')
        return redirect(url_for('lostfound'))
    return render_template('lostfound.html', entries=lost_found_db)

if __name__ == '__main__':
    app.run(debug=True)
