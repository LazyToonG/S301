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
    langue_choisie=ts.getLangue()
    textes = traductions[langue_choisie]

    user=session['username']
    role=session['role']

    rasp = rs.montreToutRasp()

    return render_template("admin.html", raspberry=rasp, t=textes, current_lang=langue_choisie, user=user, role=role)


# Création utilisateur


@app.route("/admin/create", methods=["POST", "GET"])
@reqrole('admin')
def create_user():
    langue_choisie=ts.getLangue()
    
    username = request.form.get("username")
    password = request.form.get("password")
    role = request.form.get("role")

    if not username or not password or not role:
        flash("Tous les champs sont obligatoires", "error")
        return redirect(url_for("admin_dashboard"))
    searched_users = user_service.getUserByUsername(username)

    for users in searched_users:
        if users!=None:
            if users.username==username:
                if langue_choisie=='fr':
                    message = "Nom d'utilisateur déjà existant"
                elif langue_choisie=="en":
                    message="Username already exists"
                flash(message, "error")
                return redirect(url_for("admin_dashboard"))
                
    user_service.signin(username, password, role)

    if langue_choisie=='fr':
        message = "Utilisateur créé avec succès"
    elif langue_choisie=="en":
        message="User successfully created"
    flash(message, "success")
    return redirect(url_for("admin_dashboard"))

#suppression utilisateur
@app.route("/admin/delete", methods=["POST"])
@reqrole('admin')
def delete_user():
    langue_choisie=ts.getLangue()
    user=session['username']

    username = request.form.get("username")

    if username==user:
        if langue_choisie=='fr':
            message = "Utilisateur ne peut pas être supprimé (actuellement connecté)"
        elif langue_choisie=="en":
            message="User cannot be deleted (currently logged)"
        flash(message, "error")
        return redirect(url_for("admin_dashboard"))
    
    user_service.deleteUser(username)

    if langue_choisie=='fr':
        message = "Utilisateur supprimé avec succès"
    elif langue_choisie=="en":
        message="User successfully deleted"
    flash(message, "success")
    return redirect(url_for("admin_dashboard"))

@app.route("/admin/search", methods=["POST", "GET"])
@reqrole('admin')
def admin_search_user():
    traductions=ts.tradAdmin()

    langue_choisie=ts.getLangue()
    textes = traductions[langue_choisie]

    user=session['username']
    role=session['role']
    username = request.form.get("username")

    if not username:
        return redirect(url_for("admin_dashboard"))

    searched_users = user_service.getUserByUsername(username)
    for users in searched_users:
        if users==None:
            if langue_choisie=='fr':
                message = "Utilisateur non trouvé"
            elif langue_choisie=="en":
                message="User not found"
            flash(message, "error")
            return redirect(url_for("admin_dashboard"))
    if langue_choisie=='fr':
        message = "Utilisateur trouvé avec succès"
    elif langue_choisie=="en":
        message="User successfully found"
    flash(message, "success")
    return render_template("admin.html",searched_users=searched_users, t=textes, current_lang=langue_choisie, user=user, role=role)

