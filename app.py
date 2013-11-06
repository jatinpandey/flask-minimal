
from flask import Flask, url_for, render_template, request, \
    redirect, abort, session, g, flash, Markup
from models import *
from flaskext.crf import csrf

app = Flask(__name__)
app.config.from_object('settings')
csrf(app)

@app.route('/')
def index():
    return "You are at the homepage!"

@app.route('/user/<username>')
def profile_page(username):
    return 'User: %s' %username

@app.route('/post/<int:post_id>') #Also float or path(accepts slashes)
def show_post(post_id):
    return 'Post %d' %post_id

@app.route('/lame-message/')
@app.route('/lame-message/<name>')
def converse(name=None):
    return render_template('hello.html', name=name)

@app.route('/redirect-to-<function>')
def pointless_redirect(function=None):
    return redirect(url_for(function))

@app.errorhandler(404)
def page_not_found(error):
    return render_template(('page_not_found.html'), 404)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']

@app.route('/login', methods=['GET', 'POST'])
def login_handler():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                        request.form['password']):
            return log_user_in(request.form['username'])
        else:
            error = "Invalid username/password!"
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run()


