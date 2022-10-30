from flask import Flask, render_template, flash


#Criar objeto flask --> Váriavel que possui métodos do framework Flask.
app = Flask("Cheguei App", template_folder="html")

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def homePage():
    return render_template('index.html')

@app.route("/settings", methods=["GET"])
def settingsPage():
    return render_template('settings.html')

@app.route("/settings/restart")
def rebootPage():
    return "<h1> Rebooting Raspberry!!! </h1>"


app.run(host="0.0.0.0", debug=True)

