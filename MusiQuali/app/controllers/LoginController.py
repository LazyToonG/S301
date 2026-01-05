from flask import render_template, redirect, url_for, request
from flask import session, flash, abort
from app import app
from functools import wraps
from app.services.UserService import UserService

us = UserService()

def reqlogged(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged' in session:
            return f(*args, **kwargs)
        else:
            flash('Denied. You need to login.')
            return redirect(url_for('login'))
    return wrap


def reqrole(role):
    """
    Décorateur vérifiant si l'utilisateur est connecté et s'il a le rôle requis.
    """
    def wrap(f):
        @wraps(f)
        def verifyRole(*args, **kwargs):
            if not session.get('logged'):
                return redirect(url_for('login'))

            current_role = session.get('role')
            if current_role != role:
                abort(403)

            return f(*args, **kwargs)
        return verifyRole
    return wrap


class LoginController:

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        msg_error = None
        if request.method == 'POST':
            user = us.login(request.form["username"], request.form["password"])
            if user:
                session["logged"] = True
                session["username"] = user.username
                session["role"] = user.role
                if user.role == "admin":
                    return redirect(url_for("admin_dashboard"))
                elif user.role == "marketing":
                    return redirect(url_for("marketing_dashboard"))
                elif user.role == "commercial":
                    return redirect(url_for("commercial_dashboard"))
                else:
                    return redirect(url_for("index"))
            else:
                msg_error = 'Invalid Credentials'
        return render_template('login.html', msg_error=msg_error)

    @app.route("/signin", methods=['GET', 'POST'])
    def signin():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            role = request.form.get("role", "commercial")

            result = us.signin(username, password, role)
            if result:
                session["logged"] = True
                session["username"] = username
                session["role"] = role

                if role == "admin":
                    return redirect(url_for("admin_dashboard"))
                elif role == "marketing":
                    return redirect(url_for("marketing_dashboard"))
                elif role == "commercial":
                    return redirect(url_for("commercial_dashboard"))
                else:
                    return redirect(url_for("index"))
            else:
                return render_template("signin.html", msg_error="creation error")
        else:
            return render_template('signin.html', msg_error=None)

    @app.route('/logout')
    @reqlogged
    def logout():
        session.clear()
        flash('Successfully logged out')
        return redirect(url_for('login'))
