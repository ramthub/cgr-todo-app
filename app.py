from flask import Flask, render_template, request, redirect
from models import db, Task
import os

app = Flask(__name__)

# La URI de conexión se lee de una variable de entorno, nunca hardcodeada
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    """Ruta principal: lista todas las tareas."""
    tasks = Task.query.order_by(Task.done.asc(), Task.id.desc()).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
    def add_task():
    """Recibe el formulario y crea una nueva tarea en la BD."""
    title = request.form.get('title', '').strip()
    if title:
        task = Task(title=title)
        db.session.add(task)
        db.session.commit()
    return redirect('/')
@app.route('/done/<int:task_id>')
def mark_done(task_id):
    """Marca una tarea como completada."""
    task = Task.query.get_or_404(task_id)
    task.done = True
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Crea las tablas si no existen
    app.run(host='0.0.0.0', port=5000, debug=False)