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

# @app.route("/admin/delete_rasp", methods=["POST"])
# @reqrole('admin')
# def delete_user():
 

#     raspb_id = request.form.get("raspberry-select")


#     rs.supprimeR(raspb_id)

#     flash("delete", "success")
#     return redirect(url_for("admin_dashboard"))

@app.route("/admin/delete_rasp", methods=["POST"])
@reqrole('admin')
def delete_rasp():
    rasp_id = request.form.get("raspberry-select")

    if not rasp_id:
        flash("Aucun Raspberry sélectionné", "error")
        return redirect(url_for("admin_dashboard"))

    rs.supprimeR(rasp_id)

    flash("Raspberry supprimé avec succès", "success")
    
    return redirect(url_for("admin_dashboard"))

@app.route("/admin/envoie_ping", methods=["POST"])
@reqrole('admin')
def envoie_ping():
    rasp_ip = request.form.get("raspberry-select")
    r=rs.selectR(rasp_ip)
    print(rasp_ip)
    print(r)
    result = subprocess.run(["ping", "-c", "4", r], capture_output=True, text=True)
    if result.returncode == 0:
        flash("Ping et initialisation OK", "success" + rasp_ip)
    else:
        flash("Erreur lors de l'initialisation", "error")

    return redirect(url_for("admin_dashboard"))

@app.route("/admin/envoie_ping", methods=["POST"])#chemin doit être changer pour correspondre au bouton sauvegarder planning
@reqrole('commercial')
def envoieChaqueChangementPlanning():
    time.sleep(20)  # Attendre 20 secondes avant d'exécuter la fonction pour s'assurer que le fichier est complètement sauvegardé
    raspberrys = rs.findAll()
    for r in raspberrys:
        subprocess.run(["rsync", "-avze", app.static_fold + "/data/schedule/",  r.nom + "@" + r.ipRasp + ":/home/" + r.nom + "musiquali/"])


# ping_status = {"state": "idle", "message": ""}

# @app.route("/admin/envoie_ping", methods=["POST"])
# @reqrole('admin')
# def envoie_ping():
#     def background():
#         if rs.verifieShellRasp():
#             ping_status["state"] = "success"
#             ping_status["message"] = "Ping et initialisation OK"
#         else:
#             ping_status["state"] = "error"
#             ping_status["message"] = "Erreur lors de l'initialisation"


#     Thread(target=background).start()
#     flash("Ping lancé en arrière-plan", "success")
#     return redirect(url_for("admin_dashboard"))


def pingTout():
    toutRasp = rs.montreToutRasp()
    for chaque in toutRasp:
            subprocess.run(["ping", "-c", "1", "192.168.56.104"])
             


    # today = datetime.datetime.today()

    # if today.weekday() == 0:
    #     subprocess.run(["scp", "-v", "/home/shishkovskiy/Documents/perso_S301_perso/Musiquali.png", identifiant.identifiant_requested+"@"+identifiant.ip_requested+":/home/darragh/Images"])
