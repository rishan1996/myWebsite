from flask import Flask, render_template
import re

app = Flask(__name__)


# Function to get the nav bar
def get_nav_bar(title):
	return render_template('navbar.html', title=title)


# Function to get the footer
def get_footer():
	return render_template('footer.html')


# Function to inset the active tag
def insert_active_tag(pattern, page_title):
	# String to hold the nav bar html
	nav_bar = get_nav_bar(page_title)

	# The pattern used to split the string
	regex_pattern = re.compile(pattern)

	# Find the position where the pattern is found
	split_pos = 0
	for m in re.finditer(regex_pattern, nav_bar):
		split_pos = m.start()

	# Split the string where pattern is found
	nav_bar1 = nav_bar[:split_pos]
	nav_bar2 = nav_bar[split_pos:]

	# Insert the active tag
	return nav_bar1 + 'id="active" ' + nav_bar2


# The home page
@app.route('/')
def home():
	# Get nav bar and insert the active tag
	nav_bar = insert_active_tag('href="/"', 'Home')

	return nav_bar + render_template('index.html') + get_footer()


# The portfolio page
@app.route('/portfolio')
def portfolio():
	# Get nav bar and insert the active tag
	nav_bar = insert_active_tag('href="portfolio"', 'Rishan\'s Portfolio')

	return nav_bar + render_template('portfolio.html') + get_footer()


# The about us page
@app.route('/aboutus')
def about_us():
	# Get nav bar and insert the active tag
	nav_bar = insert_active_tag('href="aboutus', 'About Us')

	return nav_bar + render_template('aboutUs.html') + get_footer()


# The contact us page
@app.route('/contactus')
def contact_us():
	# Get nav bar and insert the active tag
	nav_bar = insert_active_tag('href="contactus"', 'Contact Us')

	return nav_bar + render_template('contactUs.html') + get_footer()


# REMEMBER TO SET DEBUG TO FALSE WHEN PUBLISHED
# Launches the server
if __name__ == '__main__':
	app.run(debug=True)
