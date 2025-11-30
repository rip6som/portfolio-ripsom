import flask as fl
from flask import render_template
import requests


#===========| Код |===========#
app = fl.Flask(__name__)


@app.route('/')
def index():
    response = requests.get('https://api.github.com/users/rip6som/repos')
    repos = response.json()
    return render_template('index.html', repos=repos)

#===========| Конец |===========#
if __name__ == '__main__':
    app.run(debug=True)