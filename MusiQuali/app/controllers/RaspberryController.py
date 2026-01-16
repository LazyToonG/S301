from flask import render_template, request, redirect, url_for, Flask
from app import app
from app.controllers.LoginController import reqrole
from app.services.RaspberryService import RaspberryService
import subprocess, datetime

rs = RaspberryService()

@app.route('/testRasp', methods = ['POST'])
def ajoutDansRasp():
    rs.ajoutR(request.form["nom"], request.form["ipRasp"])
    return redirect(url_for('ToutRaspberry'))

@app.route('/admin', methods = ['GET'])
def ToutRaspberry():
    toutRasp = rs.montreToutRasp()
    tab = []
    for chaque in toutRasp:
            tab.append(chaque)
            subprocess.run(["ping", "-c", "1", chaque.ipRasp])
    return render_template("admin.html", listRasp = tab)

    today = datetime.datetime.today()

    if today.weekday() == 0:
        subprocess.run(["scp", "-v", "/home/shishkovskiy/Documents/perso_S301_perso/Musiquali.png", identifiant.identifiant_requested+"@"+identifiant.ip_requested+":/home/darragh/Images"])


