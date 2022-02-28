import sqlite3
import json
import os
from flask import Flask, render_template, request, redirect
from image_processing import processImageForGreenCover
 
app = Flask(__name__,template_folder='templates')
 

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def addDirectory(locid):
    dirname = 'static/' + str(locid)
    os.makedirs(dirname,exist_ok=True)


@app.route('/addlocation', methods = ['POST'])
def addnewlocation():
    print( request.form)
    name = request.form['name']
    desc = request.form['description']
    lattitude= request.form['lat']
    longitude= request.form['lng']
    zoom = request.form['zoom']
   

    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("INSERT INTO location (name, description, lat, lng, zoom) VALUES (?,?,?,?,?)",
            [name,desc, lattitude , longitude, zoom]
            )
    locid = cursor.lastrowid

    historyid = 1
    
    conn.commit()
    conn.close()

    addDirectory(locid)
    coverData = processImageForGreenCover(locid, historyid, lattitude, longitude, zoom)

    garea = round(coverData['greenarea'], 3)
    tarea = round(coverData['totalarea'], 3)
    gcover = round(coverData['percentage'], 3)

    conn = get_db_connection()

    conn.execute("INSERT INTO history (loc_id, mapimage, greyimage, greencover, greenarea, totalarea) VALUES (?,?,?,?,?,?)",
            [locid, coverData['in_image'], coverData['out_image'],gcover, garea, tarea]
            )
 
    conn.commit()
    conn.close()

    return redirect('/map/'+str(locid)) 


@app.route('/findcover', methods = ['POST'])
def findCurrentGreenCover():
    print( request.form)
    locid = request.form['locid']
    name = request.form['name']
    lattitude= request.form['lat']
    longitude= request.form['lng']
    zoom = request.form['zoom']
   
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row

    history = conn.execute('SELECT * FROM history h where h.loc_id = ? ORDER BY date DESC LIMIT 1',[locid]).fetchone()

    
    if history is None:
        historyid = 1
    else:
        historyid = history[0] +1
    
    conn.commit()
    conn.close()

    addDirectory(locid)
    coverData = processImageForGreenCover(locid, historyid, lattitude, longitude, zoom)

    garea = round(coverData['greenarea'], 3)
    tarea = round(coverData['totalarea'], 3)
    gcover = round(coverData['percentage'], 3)

    conn = get_db_connection()

    conn.execute("INSERT INTO history (loc_id, mapimage, greyimage, greencover, greenarea, totalarea) VALUES (?,?,?,?,?,?)",
                [locid, coverData['in_image'], coverData['out_image'],gcover, garea, tarea]
                )
 
    conn.commit()
    conn.close()

    return redirect('/map/'+str(locid)) 

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




if __name__ == '__main__':
    app.run(debug=True)

