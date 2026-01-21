from flask import render_template, request, redirect, url_for, flash
from app import app
from app.controllers.LoginController import reqrole
from app.services.RaspberryService import RaspberryService
import subprocess, ipaddress
from app.services.TraductionService import Traductionservice

rs = RaspberryService()

ts = Traductionservice()
#import datetime

@app.route("/admin/add_rasp", methods=["POST"])
@reqrole('admin')
def addRaspberry():
    nom = request.form.get("nom")
    ip = request.form.get("ipRasp")
    

    rasps = rs.montreToutRasp()
    if any(r.ipRasp == ip for r in rasps) or any(r.nom == nom for r in rasps):
        flash("Raspberry déjà existant", "error")
        return redirect(url_for("admin_dashboard"))
    
    try:
        ipaddress.IPv4Address(ip)
        rs.ajoutR(request.form["nom"], request.form["ipRasp"])
    except ipaddress.AddressValueError:
        flash("IP invalid", "error")

    
    return redirect(url_for("admin_dashboard"))

<<<<<<< HEAD
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

# @app.route("/admin/envoie_ping", methods=["POST"])
# @reqrole('admin')
# def delete_rasp():
#     rs.verifieShellRasp()
    
#     return redirect(url_for("admin_dashboard"))


=======
@app.route("/admin/delete_rasp", methods=["POST"])
@reqrole('admin')
def deleteRaspberry():
    ip = request.form.get("ipRasp")
    rs.supprimeR(ip)
    return redirect(url_for("admin_dashboard"))
>>>>>>> 77c5713236df339ae3d3b235e6a63f54d1a342e0



    # traductions=ts.tradAdmin()
    # langue_choisie=ts.getLangue()
    # textes = traductions[langue_choisie]

# @app.route('/admin/raspberries', methods = ['GET'])
# @app.route('/testRasp', methods = ['GET'])
# def ToutRaspberry():

#     traductions=ts.tradAdmin()
#     langue_url = request.args.get('lang')
#     if langue_url:
#         session['langue'] = langue_url
#         langue_choisie = langue_url
#     else:
#         langue_choisie = session.get('langue')

#     if langue_choisie not in ['fr', 'en']:
#         langue_choisie = 'fr'
#     textes = traductions[langue_choisie]

#     user=session['username']
#     role=session['role']

#     toutRasp = rs.montreToutRasp()
#     tab = []
#     for chaque in toutRasp:
#             tab.append(chaque)
#     return render_template("testRasp.html", listRasp = tab, t=textes, current_lang=langue_choisie, user=user, role=role)

def pingTout():
    toutRasp = rs.montreToutRasp()
    for chaque in toutRasp:
            subprocess.run(["ping", "-c", "1", chaque.ipRasp])


    # today = datetime.datetime.today()

    # if today.weekday() == 0:
    #     subprocess.run(["scp", "-v", "/home/shishkovskiy/Documents/perso_S301_perso/Musiquali.png", identifiant.identifiant_requested+"@"+identifiant.ip_requested+":/home/darragh/Images"])
