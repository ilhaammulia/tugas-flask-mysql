from flask import Flask, render_template
from models import MBukuTelepon

app = Flask(__name__)


@app.route('/')
def index():
    model = MBukuTelepon()
    container = []
    container = model.selectDB()
    return render_template('index.html', container=container)


if __name__ == '__main__':
    app.run(debug=True)
