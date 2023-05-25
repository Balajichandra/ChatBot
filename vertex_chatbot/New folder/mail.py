from flask import Flask
from flask_mail import Mail,Message
#from flask   import Mail, Message
app1 = Flask(__name__)
mail = Mail(app1) # instantiate the mail class
   
# configuration of mail
app1.config['MAIL_SERVER']='smtp.gmail.com'
app1.config['MAIL_PORT'] = 465
app1.config['MAIL_USERNAME'] = 'balajicena1995@gmail.com'
app1.config['MAIL_PASSWORD'] = '*********'
app1.config['MAIL_USE_TLS'] = False
app1.config['MAIL_USE_SSL'] = True
mail = Mail(app1)
   
# message object mapped to a particular URL ‘/’
@app1.route("/")
def index():
   msg = Message(
                'Hello',
                sender ='balajicena1995@gmail.com',
                recipients = ['balajiavinash66@gmail.com']
               )
   msg.body = 'Hello Flask message sent from Flask-Mail'
   with open("data.txt") as fp:  
      msg.attach("data.txt", "data/txt",fp.read())  
   mail.send(msg)
   return 'Mail Sent'
# print(file1.read())
if __name__ == "__main__":
    app1.run()        
       