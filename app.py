# All code by Ryan Islam
from flask import Flask, url_for, render_template, request, json
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'fbd1eefad885bf835e1d5ea884244221'

# Mail config settings
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ryanislam@hotmail.com'
app.config['MAIL_PASSWORD'] = 'ptvKTbXaZ71jt5KunjUo'
app.config['MAIL_DEFAULT_SENDER'] = "ryanislam@hotmail.com"

mail = Mail(app)

# Email Send/Reply/Confirmation
@app.route('/', methods=['POST'])
def send_email():
    user_email = request.form['user_email']
    user_message = request.form['user_message']
    usr_msg = Message('Customer - Contact Us', sender= f'{user_email}' , recipients= ['ryanislam@hotmail.com'])
    usr_msg.body = f'''{user_message}'''
    mail.send(usr_msg)
    msg = Message('We recieved your concerns', sender = 'ryanislam@hotmail.com', recipients = [user_email])
    msg.body = f''' Thank you { user_email }, we have recieved your email! You will receive a confirmation email from us within the next 2 days'''
    mail.send(msg)
    return index()

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

# Parameterized Request
@app.route('/hotel_list/<name>/<path:img>')
def hotelviewingalt(name,img):
    return render_template('hotel_viewing.html',name=name,img=img)

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

# Routing for Hotel Viewing
@app.route('/hotel_list')
def hotelviewing():
    return render_template('hotel_list.html', title='Viewing')

# Parameterized Request
@app.route('/hotel_list/<name>')
def hotelviewingsecond(name):
    return render_template('hotel_viewing.html',name=name)


print("-- DEBUG MODE ----")
app.run(debug = True, port= '5555')

#Waitress 
#import os
#from waitress import serve

#print("--PRODUCTION MODE ---")
#p = os.environ.get('PORT')
#serve(app, host='0.0.0.0', port=p)