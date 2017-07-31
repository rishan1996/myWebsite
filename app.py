from flask import Flask, render_template

app = Flask(__name__)


# Function to get the nav bar
def get_nav_bar(title):
    return render_template('navbar.html', title=title)


# Function to get the footer
def get_footer():
    return render_template('footer.html')


# The home page
@app.route('/')
def home():
    temp = get_nav_bar('Home')
    # Split the nav bar string and insert the active tag on current page
    nav_bar1 = temp[:511]
    nav_bar2 = temp[511:]
    nav_bar = nav_bar1 + 'id="active" ' + nav_bar2
    return nav_bar + render_template('index.html') + get_footer()


# The portfolio page
@app.route('/portfolio')
def portfolio():
    temp = get_nav_bar('Rishan\'s Portfolio')
    # Split the nav bar string and insert the active tag on current page
    nav_bar1 = temp[:595]
    nav_bar2 = temp[595:]
    nav_bar = nav_bar1 + 'id="active" ' + nav_bar2
    return nav_bar + render_template('portfolio.html') + get_footer()


# The about us page
@app.route('/aboutus')
def about_us():
    temp = get_nav_bar('About Us')
    # Split the nav bar string and insert the active tag on current page
    nav_bar1 = temp[:660]
    nav_bar2 = temp[660:]
    nav_bar = nav_bar1 + 'id="active" ' + nav_bar2
    return nav_bar + render_template('aboutUs.html') + get_footer()


# The contact us page
@app.route('/contactus')
def contact_us():
    temp = get_nav_bar('Contact Us')
    # Split the nav bar string and insert the active tag on current page
    nav_bar1 = temp[:738]
    nav_bar2 = temp[738:]
    nav_bar = nav_bar1 + 'id="active" ' + nav_bar2
    return nav_bar + render_template('contactUs.html') + get_footer()

# REMEMBER TO SET DEBUG TO FALSE WHEN PUBLISHED
# Launches the server
if __name__ == '__main__':
    app.run(debug=True)



