from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Task(db.Model):
    """Representa una tarea en la base de datos.
    SQLAlchemy mapea esta clase a una tabla llamada 'task'.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)
    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'