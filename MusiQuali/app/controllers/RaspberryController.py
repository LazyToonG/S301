from flask import render_template, request, redirect, url_for, Flask
from app import app
from app.controllers.LoginController import reqrole
from app.services.RaspberryService import RaspberryService
import subprocess, datetime

rs = RaspberryService()

@app.route('/test', methods = ['POST'])
def ajoutDansRasp():
    rs.ajoutR(request.form["identifiant"], request.form["ip"])

@app.route('/admin', methods = ['POST'])
def ToutRaspberry():
    toutRasp = rs.montreToutRasp()
    list = ()
    for chaque in toutRasp:
        if toutRasp.entreprise: #vérifier quel entreprise vient la raspberry
            list.append(chaque)
            subprocess.run(["ping", chaque.ipRasp])
    return render_template("admin", listRasp = list)

    today = datetime.datetime.today()

    if today.weekday() == 0:
        subprocess.run(["scp", "-v", "/home/shishkovskiy/Documents/perso_S301_perso/Musiquali.png", identifiant.identifiant_requested+"@"+identifiant.ip_requested+":/home/darragh/Images"])


