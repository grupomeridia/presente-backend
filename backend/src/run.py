from application import create_app
from waitress import serve

app = create_app('settings.py')
serve(app, host="0.0.0.0", port=5000)