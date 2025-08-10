from werkzeug.utils import secure_filename
from flask import Blueprint , render_template ,flash ,request
import os
from models import PROJECT_POSTS ,db


edit_proc =Blueprint('edit_proc',__name__,template_folder="templates",static_folder="static")



@edit_proc.route("/maaz-project-edits/")
def maaz_project_edit():
    post = PROJECT_POSTS.query.all()
    return render_template("delete.html", post=post)



delete_proc =Blueprint('delete_proc',__name__,template_folder="templates",static_folder="static")


@delete_proc.route("/delete-maaz-project/<id>")
def delete_maaz_project(id):
    post = PROJECT_POSTS.query.filter_by(id=int(id)).first()
    db.session.delete(post)
    db.session.commit()
    
    post = PROJECT_POSTS.query.all()
    return render_template("delete.html", post=post)
