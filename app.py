from flask import Flask, render_template

app = Flask(__name__)


# Function to get the nav bar
def get_nav_bar(title):
    return '''<html>
    <head>
    <!--Load the stylesheet-->
    <link rel="stylesheet" type="text/css" href="/static/css/mainStyle.css">

    <!--Set the page title in the tab-->
        <title>
			''' + title + '''
        </title>
    </head>
        <div id="navbarWrapper">
            <div id="navbar">
                <ul>
                <!--Set the links in the nav bar-->
                    <li class="navitem"><a href="/">Home</a></li>
                    <li class="navitem"><a href="portfolio">Portfolio</a></li>
                    <li class="navitem"><a href="aboutus">About Us</a></li>
                    <li class="navitem"><a href="contactus">Contact Us</a></li>
                </ul>
            </div>
        </div>
    </html>'''


# The home page
@app.route('/')
def home():
    return render_template('index.html')


# The portfolio page
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


# The contact us page
@app.route('/contactus')
def contact_us():
    return render_template('contactUs.html')


# The about us page
@app.route('/aboutus')
def about_us():
    temp = get_nav_bar('About Us')
    nav_bar1 = temp[:549]
    nav_bar2 = temp[549:]
    nav_bar = nav_bar1 + 'id="active" ' + nav_bar2
    return nav_bar + render_template('aboutUs.html')

# REMEMBER TO SET DEBUG TO FALSE WHEN PUBLISHED
# Launches the server
if __name__ == '__main__':
    app.run(debug=True)



