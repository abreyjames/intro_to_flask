from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome'

@app.route('/Niki')
def niki():
    return 'Welcome Niki'

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)

