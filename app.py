# All code by Ryan Islam
from flask import Flask, url_for, render_template, request, json
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'fbd1eefad885bf835e1d5ea884244221'

# Mail config settings
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ryanislam@hotmail.com'
app.config['MAIL_PASSWORD'] = 'passwordplaceholder'
app.config['MAIL_DEFAULT_SENDER'] = "ryanislam@hotmail.com"

# mail = Mail(app)

# Mail retreival from contact us page
# @app.route('/process_email', methods=['GET','POST'])
# def process_email():
# name=request.form['name']
# password=request.form['password']
# email=request.form['email']
# msg = Message("Email confirmation", recipients=[email])
# msg.html=render_template('index.html',name=name,password=password,email=email)
# msg.body = 'Confirming Email'
# mail.send(msg)
# return render_template('index.html',title='Home',msg="Thank you {name}, you have successfully registered. Please check your email inbox at {email}.")

# Parameterized Rqeuest
# @app.route('/', methods=['GET', 'POST'])
# def parse_request():
#     data = request.data

# Error 404 Page
@app.errorhandler(404)
def err_404(error):
    return render_template( '404.html'), 404

# Routing for Index page
@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')

# Routing for Register page
@app.route('/register')
def register():
    return render_template('register.html', title='Registration')

# Routing for About Us Page
@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

# Routing for Contact Us Page
@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')

# Routing for Data Page
@app.route('/data')
def data():
    return render_template('data.html', title='Data')


# print("-- DEBUG MODE ----")
# app.run(debug = True, port= '5555')

# Waitress 
import os
from waitress import serve

print("--PRODUCTION MODE ---")
p = os.environ.get('PORT')
serve(app, host='0.0.0.0', port=p)