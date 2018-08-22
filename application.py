###########################################################################
#Hamish Nicholson
#Personal Website Backend Source Code
###########################################################################
from flask import *

# app configurations
application = Flask(__name__)
# home page
@application.route('/')
def index():
    return render_template('index.html')

# Still working on the blog section
# @app.route('/blog.html')
# def blog():
# 	return render_template('blog.html')

# @app.route('/blog-single.html')
# def blog_single():
# 	return render_template('blog-single.html')

# app call
if __name__ == '__main__':
    application.run(debug = False, ssl_context='adhoc')