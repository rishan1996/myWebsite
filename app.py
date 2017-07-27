from flask import Flask, render_template
app = Flask(__name__)

#The home page
@app.route('/')
def home():
    return render_template('index.html')

#The portfolio page
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

#The contact us page
@app.route('/contactus')
def contactUs():
    return render_template('contactUs.html')

#The about us page
@app.route('/aboutus')
def aboutUs():
    return render_template('aboutUs.html')

#REMEBER TO SET DEBUG TO FALSE WHEN PUBLISHED
if __name__ == '__main__':
    app.run(debug=True)