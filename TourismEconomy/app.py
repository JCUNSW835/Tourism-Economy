# To make this work, first install Flask:
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade flask

from flask import Flask
app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')
            # we don't currently have templates,
            # but the idea is Flask can simplify development
            # of new pages with emplates

# the below line is using a Python decorator- and this wraps a functions and modifies its behaviour
# sungle/below can be thought of as the 'base URL'
# specifying how to handle a particular URL request
# / is the default base URL
@app.route('/')
def root():
    return app.send_static_file('index.html')
    # index.html is very common naming convention for the 'base'/
    # 'first' HTML file that should be homepage.
# so within a single site, we can have multiple 'sub routes' - e.g pages
# examples
# www.google.com
# wwww.google.com/images
# www.google.com/signin/authenticator etc

# boilerplate code that protects users from invoking the script
# when they didn't necessarily mean to
# More broadly: as we start to work with mutiple Python files，
# and import functions from other files, it's important

if __name__ == "__main__":
    app.run(port = 8000)