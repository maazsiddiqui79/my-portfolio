from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PROJECT_POSTS(db.Model):
    __tablename__ = 'PROJECTS'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    s_description = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"<PROJECT_POSTS(id={self.id}, title='{self.title}'),DESC={self.s_description}>"
    