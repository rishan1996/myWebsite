from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'You are home'

@app.route('/portfolio')
def portfolio():
    return 'You are on portfolio'

if __name__ == '__main__':
    app.run(debug=True)