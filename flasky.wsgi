activate_this = " /home/admin/Flask-Social-Blogging-Web-App/flask-venv/bin/activate"
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from flasky import create_app

app = create_app()
