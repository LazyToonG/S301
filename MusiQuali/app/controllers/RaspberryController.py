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
    ip = request.form.get("ipRasp")
    

    rasps = rs.montreToutRasp()
    if any(r.ipRasp == ip for r in rasps):
        flash("Raspberry déjà existant")
    
    try:
        ipaddress.IPv4Address(ip)
        rs.ajoutR(request.form["nom"], request.form["ipRasp"])
    except ipaddress.AddressValueError:
        flash("IP invalid")

    
    return redirect(url_for("admin_dashboard"))




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
