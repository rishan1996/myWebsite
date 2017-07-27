from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'You are home'

@app.route('/portfolio')
def portfolio():
    return 'You are on portfolio'

@app.route('/contactus')
def contactUs():
    return 'You are on contact us'

@app.route('/aboutus')
def aboutUs():
    return 'You are on about us'

if __name__ == '__main__':
    app.run(debug=True)