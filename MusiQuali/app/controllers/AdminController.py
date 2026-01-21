from flask import render_template, request, session, redirect, url_for, flash
from app import app
from app.controllers.LoginController import reqrole

from app.services.UserService import UserService
from app.services.RaspberryService import RaspberryService
from app.services.TraductionService import Traductionservice

rs = RaspberryService()
ts = Traductionservice()
user_service = UserService()


@app.route("/admin", methods=["GET"])
@reqrole('admin')
def admin_dashboard():

    traductions=ts.tradAdmin()

    langue_url = request.args.get('lang')
    if langue_url:
        session['langue'] = langue_url
        langue_choisie = langue_url
    else:
        langue_choisie = session.get('langue')

    if langue_choisie not in ['fr', 'en']:
        langue_choisie = 'fr'
    textes = traductions[langue_choisie]

    user=session['username']
    role=session['role']

    rasp = rs.montreToutRasp()

    return render_template("admin.html", raspberry=rasp, t=textes, current_lang=langue_choisie, user=user, role=role)


# Création utilisateur


@app.route("/admin/create", methods=["POST"])
@reqrole('admin')
def create_user():
    username = request.form.get("username")
    password = request.form.get("password")
    role = request.form.get("role")

    if not username or not password or not role:
        flash("Tous les champs sont obligatoires", "error")
        return redirect(url_for("admin_dashboard"))

    user_service.signin(username, password, role)

    flash("Utilisateur créé avec succès", "success")
    return redirect(url_for("admin_dashboard"))




@app.route("/admin/search", methods=["POST"])
@reqrole('admin')
def admin_search_user():
    traductions=ts.tradAdmin()

    langue_url = request.args.get('lang')
    if langue_url:
        session['langue'] = langue_url
        langue_choisie = langue_url
    else:
        langue_choisie = session.get('langue')

    if langue_choisie not in ['fr', 'en']:
        langue_choisie = 'fr'
    textes = traductions[langue_choisie]

    user=session['username']
    role=session['role']
    username = request.form.get("username")

    if not username:
        return redirect(url_for("admin_dashboard"))

    searched_users = user_service.getUserByUsername(username)

    return render_template("admin.html",searched_users=searched_users, t=textes, current_lang=langue_choisie, user=user, role=role)

