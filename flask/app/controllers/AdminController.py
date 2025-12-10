from flask import render_template
from app import app
from app.controllers.LoginController import reqrole

# class AdminController:

#     @app.route('/admin', methods=['GET'])
#     @reqrole("admin")
#     def admin_dashboard():
#         metadata = {"title": "Panel Admin", "pagename": "admin"}

#         data = {
#             "messages_diffuses": [],
#             "etat_lecteurs": [],
#             "playlist_ok": True,
#         }

#         return render_template('admin/index.html', metadata=metadata, data=data)

#     @app.route('/admin/playlist/resync', methods=['POST'])
#     @reqrole("admin")
#     #def resync_playlist():

#     @app.route('/admin/playlist/update', methods=['POST'])
#     @reqrole("admin")
#     #def update_playlist():

#     @app.route('/admin/alert', methods=['POST'])
#     @reqrole("admin")
#     #def trigger_alert():