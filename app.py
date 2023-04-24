from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
import sqlite3
import random

app = Flask(__name__)
app.secret_key = "seu-segredo-aqui" # troque pelo seu próprio segredo

DATABASE = 'presenca.db'

# Função para conectar ao banco de dados
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


app = Flask(__name__, template_folder='templates')

# Rota para página de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password)).fetchone()
        db.close()
        if user is None:
            flash('E-mail ou senha inválidos!')
            return redirect(url_for('login'))
        else:
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_role'] = user['role']
            return redirect(url_for('dashboard'))
    else:
        return render_template('login.html')

# Rota para página de registro de aluno
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        db.execute('INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)', (name, email, password, 'aluno'))
        db.commit()
        db.close()
        flash('Registro realizado com sucesso! Faça login para acessar.')
        return redirect(url_for('login'))
    else:
        return render_template('register.html')

# Rota para página de dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    elif session['user_role'] == 'professor':
        db = get_db()
        classes = db.execute('SELECT * FROM classes WHERE professor_id = ?', (session['user_id'],)).fetchall()
        db.close()
        return render_template('dashboard_professor.html', classes=classes)
    else:
        db = get_db()
        attendances = db.execute('SELECT * FROM attendances JOIN classes ON attendances.class_id = classes.id WHERE student_id = ?', (session['user_id'],)).fetchall()
        db.close()
        return render_template('dashboard_aluno.html', attendances=attendances)

# Rota para página de criação de nova aula
@app.route('/aulas')
def aulas():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    db = get_db()
    if session['user_role'] == 'professor':
        classes_data = db.execute('SELECT * FROM classes WHERE professor_id = ? ORDER BY date DESC', (session['user_id'],)).fetchall()
    else:
        classes_data = db.execute('SELECT classes.*, presences.id as presence_id FROM classes LEFT JOIN presences ON classes.id = presences.class_id AND presences.student_id = ? ORDER BY date DESC', (session['user_id'],)).fetchall()
    db.close()
    return render_template('aulas.html', classes_data=classes_data)

@app.route('/nova-aula', methods=['GET', 'POST'])
def nova_aula():
    if 'user_id' not in session or session['user_role'] != 'professor':
        return redirect(url_for('login'))
    elif request.method == 'POST':
        code = random.randint(1000, 9999) # gera um código numérico aleatório de 4 dígitos
        date = request.form['date']
        db = get_db()
        db.execute('INSERT INTO classes (professor_id, code, date) VALUES (?, ?, ?)', (session['user_id'], code, date))
        db.commit()
        db.close()
        flash('Aula criada com sucesso! Código de presença: {}'.format(code), 'success')
        return redirect(url_for('aulas'))
    else:
        return render_template('nova-aula.html')

@app.route('/presenca-aluno/<int:class_id>')
def presenca_aluno(class_id):
    if 'user_id' not in session or session['user_role'] != 'aluno':
        return redirect(url_for('login'))
    db = get_db()
    class_data = db.execute('SELECT * FROM classes WHERE id = ?', (class_id,)).fetchone()
    if not class_data:
        flash('Aula não encontrada.', 'error')
        return redirect(url_for('aulas'))
    presence_data = db.execute('SELECT * FROM presences WHERE class_id = ? AND student_id = ?', (class_id, session['user_id'])).fetchone()
    db.close()
    return render_template('presenca-aluno.html', class_data=class_data, presence_data=presence_data)

if __name__ == '__main__':
    app.run(debug=True)