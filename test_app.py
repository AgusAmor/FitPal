import unittest
import sqlite3
from app import app, init_db

class FitPalTestCase(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DATABASE'] = 'test_UsuariosFT.db'  # Usar una base de datos de prueba
        self.client = app.test_client()
        
        # Crea la base de datos de prueba y su tabla
        with sqlite3.connect(app.config['DATABASE']) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS test_UsuariosFT (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    dni TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL,
                    is_admin INTEGER DEFAULT 0
                )
            ''')
            conn.commit()

    def tearDown(self):
        # Elimina la base de datos de prueba después de cada prueba
        with sqlite3.connect(app.config['DATABASE']) as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS test_UsuariosFT")
            conn.commit()

    # Prueba de registro de usuario
    def test_registro_usuario(self):
        response = self.client.post('/submit', data={
            'username': 'testuser',
            'dni': '12345678',
            'email': 'test@example.com',
            'password': 'testpass',
            'is_admin': 0
        })
        self.assertEqual(response.status_code, 302)
        # Verificar redirección a la raíz "/"
        self.assertEqual(response.location, '/')

    # Prueba de inicio de sesión correcto
    def test_login_correcto(self):
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/home')

    def test_login_incorrecto(self):
        response = self.client.post('/login', data={
        'username': 'testuser',
        'password': 'wrongpass'
        }, follow_redirects=True)  # Seguir redirección automáticament
        self.assertEqual(response.status_code, 200)  # Verificar estado OK después de redirección
        self.assertIn(b'Nombre de usuario o contrase\xc3\xb1a incorrectos.', response.data)


    # Prueba para la lista de usuarios (acceso admin)
    def test_usuarios(self):
        self.client.post('/submit', data={
            'username': 'admin',
            'dni': '87654321',
            'email': 'admin@example.com',
            'password': 'adminpass',
            'is_admin': 1
        })
        self.client.post('/login', data={
            'username': 'admin',
            'password': 'adminpass'
        })
        response = self.client.get('/usuarios')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Lista de Usuarios', response.data)



if __name__ == '__main__':
    unittest.main()