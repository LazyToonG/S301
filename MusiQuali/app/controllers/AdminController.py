from flask import render_template, request, session, redirect, url_for, flash
from app import app
from app.services.UserService import UserService

user_service = UserService()




@app.route("/admin", methods=["GET"])
def users_page():

    return render_template("admin.html")


# Création utilisateur


@app.route("/admin/create", methods=["POST"])
def create_user():
    username = request.form.get("username")
    password = request.form.get("password")
    role = request.form.get("role")

    if not username or not password or not role:
        flash("Tous les champs sont obligatoires", "error")
        return redirect(url_for("users_page"))

    user_service.signin(username, password, role)

    flash("Utilisateur créé avec succès", "success")
    return redirect(url_for("users_page"))




@app.route("/admin/search", methods=["POST"])
def admin_search_user():
    username = request.form.get("username")

    if not username:
        return redirect(url_for("admin_page"))

    searched_users = user_service.getUserByUsername(username)

    return render_template(
        "admin.html",
        searched_users=searched_users
    )

