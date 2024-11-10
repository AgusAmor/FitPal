from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necesario para usar mensajes flash

# Función para inicializar la base de datos
def init_db():
    with sqlite3.connect('UsuariosFT.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS UsuariosFT (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                dni TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                is_admin INTEGER DEFAULT 0 
            )
        ''')
        conn.commit()

# Rutas
@app.route('/')
def index():
    return render_template('inicio.html')  # Mostrar formulario de inicio de sesión y registro

@app.route('/registro')
def registro():
    return render_template('form.html')  # Mostrar formulario de registro

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    dni = request.form['dni']
    email = request.form['email']
    password = request.form['password']
    is_admin = int(request.form.get('is_admin', 0))
    
    # Generar hash MD5 de la contraseña
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    
    # Guardar el usuario, dni, email y contraseña en la base de datos
    with sqlite3.connect('UsuariosFT.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO UsuariosFT (username, dni, email, password, is_admin)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, dni, email, hashed_password, is_admin))
        conn.commit()
    
    # Redirigir a la página de inicio
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Generar hash MD5 de la contraseña ingresada
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    
    with sqlite3.connect('UsuariosFT.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT is_admin FROM UsuariosFT WHERE username = ? AND password = ?', (username, hashed_password))
        user = cursor.fetchone()
    
    if user:
        is_admin = user[0]
        if is_admin == 1:
            return redirect(url_for('usuarios'))  # Redirigir a la lista de usuarios si es admin
        else:
            return redirect(url_for('home'))  # Redirigir a la página de usuario normal
    else:
        flash('Nombre de usuario o contraseña incorrectos.')  # Mensaje de error
        return redirect(url_for('index'))  # Regresar al formulario de inicio

@app.route('/home')
def home():
    return render_template('home.html')  # Página para usuarios normales

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')  # Asegúrate de tener un archivo catalogo.html en la carpeta templates


@app.route('/usuarios')
def usuarios():
    with sqlite3.connect('UsuariosFT.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, dni, email, is_admin FROM UsuariosFT')
        usuarios = cursor.fetchall()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/eliminar', methods=['POST'])
def eliminar_usuario():
    user_id = request.form['user_id']
    
    # Conectar a la base de datos y eliminar el usuario por su id
    with sqlite3.connect('UsuariosFT.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM UsuariosFT WHERE id = ?', (user_id,))
        conn.commit()
    
    # Después de eliminar, redirigir nuevamente a la lista de usuarios
    return redirect(url_for('usuarios'))

if __name__ == '__main__':
    init_db()  # Inicializa la base de datos al iniciar la app
    app.run(debug=True)
