import flask as fl
from flask import render_template
import requests


#===========| Код |===========#
app = fl.Flask(__name__)


@app.route('/')
def index():
    response = requests.get('https://api.github.com/users/rip6som/repos')
    print(f"GitHub API status: {response.status_code}")
    print(f"GitHub API response: {response.json()}")

    if response.status_code == 200:
        repos = response.json()
    else:
        repos = []
    return render_template('index.html', repos=repos)
#===========| Конец |===========#
if __name__ == '__main__':
    app.run(debug=True)