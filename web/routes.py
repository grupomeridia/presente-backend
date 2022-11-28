from flask import Flask, render_template, flash


#Criar objeto flask --> Váriavel que possui métodos do framework Flask.
app = Flask("Cheguei App")

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def homePage():
    return render_template('home.html')

@app.route("/settings", methods=["GET"])
def settingsPage():
    return render_template('settings.html')

@app.route("/settings/restart")
def rebootPage():
    return "<h1> Rebooting Raspberry!!! </h1>"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

app.run(host="0.0.0.0", debug=True)

