from application import create_app

app = create_app('settings.py')
app.run(debug=True, host="0.0.0.0")