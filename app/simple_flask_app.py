from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenido a la home page'

@app.route('/hello')
def hello():
    return 'Hola mundo!'

@app.route('/goodbye')
def goodbye():
    return 'Adios mundo!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
