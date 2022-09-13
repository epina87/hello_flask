from flask import Flask

app = Flask(__name__)


@app.route("/hola") 
def primeraentrada():
    return "Hola, mundo"

@app.route("/adios")
def salida():
    return "Hasta luego, Mari Carmen!!!" 

@app.route("/dobe/<int:numero>")
def doble(numero):
    return str(numero * 2)