from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# mysql+pymysql://root@localhost/python_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/python_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(70), unique = True)
    pais = db.Column(db.String(100))

    def __repr__(self):
        return "<Equipo %r>" % self.nombre

if __name__ == '__main__':
    app.run(debug=True)