from flask import render_template, request, redirect, url_for, Flask
from app import app
from app.controllers.LoginController import reqrole
from app.services.RaspberryService import RaspberryService
import subprocess, datetime

rs = RaspberryService()

@app.route('/jsp', methods = ['GET'])
def ajoutDansRasp():
    rs.ajoutR(request.form["identifiant"], request.form["ip"])

#supposer envoyer un fichier à raspberry mais y'a un problème car quel raspberry?

    today = datetime.datetime.today()

    if today.weekday() == 0:
        subprocess.run(["scp", "-v", "/home/shishkovskiy/Documents/perso_S301_perso/Musiquali.png", identifiant.identifiant_requested+"@"+identifiant.ip_requested+":/home/darragh/Images"])


