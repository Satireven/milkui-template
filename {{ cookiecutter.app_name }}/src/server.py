import bottle
from os import path

STATIC_FOLDER = path.join(path.dirname(__file__), 'public')
ALLOW_TYPES = ['html', 'js', 'css', 'png', 'jpg', 'ico', 'webp']

app = bottle.Bottle()

# single page app
@app.route('/')
@app.route('/index.html')
def index():
    return bottle.static_file('index.html', root = STATIC_FOLDER)

# static files
@app.route(f'/<path:re:.*\\.({"|".join(ALLOW_TYPES)})>')
def static(path):
    return bottle.static_file(path, root = STATIC_FOLDER)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)