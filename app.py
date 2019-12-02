#All code by Ryan Islam
from flask import Flask, url_for, render_template, request, json
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'fbd1eefad885bf835e1d5ea884244221'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ryanislam@hotmail.com'
app.config['MAIL_PASSWORD'] = 'passwordplaceholder'

# Placeholder for mail retreival from contact us page
#   mail = Mail(app)
#   @app.route('/process_email', methods=['POST'])
#   def process_email():
#   msg = Message('Test', sender='testaccount@gmail.com', recipients=['your@email.com'])
#   msg.body = 'This is a test email' #Customize based on user input
#   mail.send(msg)
#   return 'done'

#Error 404 Page
@app.errorhandler(404)
def err_404(error):
    return render_template( '404.html'), 404

#Routing for Index page
@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')

#Routing for Register page
@app.route('/register')
def register():
    return render_template('register.html', title='Registration')

#Routing for About Us Page
@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

#Routing for Contact Us Page
@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')

#Routing for Data Page
@app.route('/data')
def data():
    return render_template('data.html', title='Data')


# print("-- DEBUG MODE ----")
# app.run(debug = True, port= '5555')

import os
from waitress import serve

print("--PRODUCTION MODE ---")
p = os.environ.get('PORT')
serve(app, host='0.0.0.0', port=p)