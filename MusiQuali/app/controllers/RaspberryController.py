from flask import render_template, request, redirect, url_for, flash
from app import app
from app.controllers.LoginController import reqrole
from app.services.RaspberryService import RaspberryService
import subprocess, ipaddress, time
from app.services.TraductionService import Traductionservice
import os
from werkzeug.utils import secure_filename

rs = RaspberryService()

ts = Traductionservice()
#import datetime


@app.route("/admin/add_rasp", methods=["POST"])
@reqrole('admin')
def addRaspberry():
    ip = request.form.get("ipRasp")
    

    rasps = rs.montreToutRasp()
    if any(r.ipRasp == ip for r in rasps):
        flash("Raspberry déjà existant","error")
        return redirect(url_for("admin_dashboard"))
    
    try:
        ipaddress.IPv4Address(ip)
        rs.ajoutR(request.form["nom"], request.form["ipRasp"])
    except ipaddress.AddressValueError:
        flash("IP invalid", "error")

    
    return redirect(url_for("admin_dashboard"))

@app.route("/admin/action_rasp", methods=["POST"])
@reqrole('admin')
def action_rasp():
    button=request.form.get("action")
    rasp_id = request.form.get("raspberry-select")
    nom = rs.selectRNom(rasp_id)
    ip = rs.selectRIp(rasp_id)

    if rasp_id==None:
        flash("Pas de Raspberry trouvé", "error")
        return redirect(url_for("admin_dashboard"))
    else : 
        rasp_id = int(rasp_id)
    print("rasp_id :",rasp_id)

    if not rasp_id:
        flash("Aucun Raspberry sélectionné", "error")
        return redirect(url_for("admin_dashboard"))
    
    if button=="delete-rasp":
        rs.supprimeR(rasp_id)
        flash("Raspberry supprimé avec succès", "success")

    elif button=="envoie-ping":
        print(ip)
        result = subprocess.run(["ping", "-c", "4", ip], capture_output=True, text=True)
        if result.returncode == 0:
            flash("Ping et initialisation OK", "success")
        else:
            flash("Erreur lors de l'initialisation", "error")
    #tmp
    elif button=="test":
        # subprocess.run(["scp", "-r", "./app/static/", "test@" + rs.selectRIp(rasp_id) + ":/home/test/musiquali/"])
        subprocess.run(["rsync", "-avz", "--delete", "-e", "ssh","./app/static/rasdata/",  f"{nom}@{ip}:/home/{nom}/musiquali/"])
        flash("envoyer", "success")
        time.sleep(5)
        print(subprocess.run(["ssh", f"{nom}@{ip}", "python3", f"/home/{nom}/musiquali/RAS.py"]))
    
    return redirect(url_for("admin_dashboard"))

@app.route("/admin/envoie_ping", methods=["POST"])#chemin doit être changer pour correspondre au bouton sauvegarder planning
@reqrole('commercial')
def envoieChaqueChangementPlanning():
    time.sleep(20)  # Attendre 20 secondes avant d'exécuter la fonction pour s'assurer que le fichier est complètement sauvegardé
    raspberrys = rs.findAll()
    for r in raspberrys:
        subprocess.run(["rsync", "-avze", app.static_folder + "/data/schedule/",  r.nom + "@" + r.ipRasp + ":/home/" + r.nom + "musiquali/"])


def pingTout():
    toutRasp = rs.montreToutRasp()
    for chaque in toutRasp:
            subprocess.run(["ping", "-c", "1", chaque["ipRasp"]])
             


    # today = datetime.datetime.today()

    # if today.weekday() == 0:
    #     subprocess.run(["scp", "-v", "/home/shishkovskiy/Documents/perso_S301_perso/Musiquali.png", identifiant.identifiant_requested+"@"+identifiant.ip_requested+":/home/darragh/Images"])
