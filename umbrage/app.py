import sqlite3
import json
from flask import Flask, render_template, request, redirect
 
#from image_processing import *

app = Flask(__name__,template_folder='templates')
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def homepage():

    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    locations = conn.execute('SELECT * FROM location l LEFT JOIN  history h ON h.id = ( SELECT id from history where loc_id = l.id ORDER BY date DESC LIMIT 1) ').fetchall()
    conn.close()
    
    data = [dict(lc) for lc in locations]
    return render_template('homepage.html', locations=data)
    
@app.route('/map/<locid>')
def mappage( locid):
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    onelocation = conn.execute('SELECT * FROM location l INNER JOIN  history h ON h.id = ( SELECT id from history where loc_id = l.id ORDER BY date DESC LIMIT 1) WHERE l.id = ?',[locid]).fetchone()
    history = conn.execute('SELECT * FROM history h where h.loc_id = ? ORDER BY date DESC',[locid]).fetchall()
    conn.close()

    hdata = [dict(hs) for hs in history]
    return render_template('mappage.html', location=onelocation, history=hdata)

@app.route('/newmap')
def newmappage():
    
    return render_template('newmappage.html')


app.run();
