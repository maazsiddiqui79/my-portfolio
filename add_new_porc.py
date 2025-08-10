from flask import Blueprint, render_template, flash, request, current_app
from werkzeug.utils import secure_filename
import os
from models import PROJECT_POSTS, db

add_new_proc = Blueprint('add_new_proc', __name__, template_folder="templates", static_folder="static")

# Ensure upload folder exists once app context is available
@add_new_proc.before_app_request
def create_upload_folder():
    upload_folder = current_app.config.get('UPLOAD_FOLDER', 'static/uploads')
    os.makedirs(upload_folder, exist_ok=True)

@add_new_proc.route('/add-new-project', methods=['GET', 'POST'])
def add_new_project():
    if request.method == 'POST':
        title = request.form.get('title')
        short_desc = request.form.get('short_desc')
        body = request.form.get('body')
        img_filename = ""

        img = request.files.get('image')

        upload_folder = current_app.config.get('UPLOAD_FOLDER')
        if not upload_folder:
            raise RuntimeError("UPLOAD_FOLDER not configured in app.config")

        if img and img.filename != '':
            filename = secure_filename(img.filename)
            img.save(os.path.join(upload_folder, filename))
            img_filename = filename

        try:
            new_post = PROJECT_POSTS(
                title=title,
                s_description=short_desc,
                img=img_filename,
                body=body
            )
            db.session.add(new_post)
            db.session.commit()
            flash('Project added successfully.', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding project: {e}', 'danger')

        return render_template('new_pro.html')

    return render_template('new_pro.html')
