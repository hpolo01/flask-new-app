from flask import Flask, url_for,render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Renderiza la plantilla 'index.html' desde la carpeta 'templates'
    username="Heladio Polo"
    fecha=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html",username=username,fecha=fecha)

@app.route("/lenguaje")
def lenguaje():
    milenguaje=("PYTHON") 
    return render_template("lenguaje.html",milenguaje=milenguaje)   

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)


