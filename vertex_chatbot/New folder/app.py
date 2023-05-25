from flask import Flask,render_template,request,jsonify,send_file
from chat import get_response
from flask import Flask
from flask_mail import Mail,Message
global file1

#1st app_file
app = Flask(__name__)

#print(file1.read())
@app.get("/")
def index_get():
    return render_template('base.html')
"""
@app.get("/download")
def download_file():
    p = "file1.pdf"
    return send_file(p,as_attachment=True)
"""
@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    file1 =  open("data.txt","a")
    file1.write("Bot : ")
    file1.write(text)
    file1.write("\n")
    response = get_response(text)
    file1.write("User : ")
    file1.write(response)
    file1.write("\n")
    message = {"answer":response}
    return jsonify(message)

open('data.txt', 'w').close() 

# print(file1.read())
if __name__ == "__main__":
    app.run()
"""
# mail sending app2
app1 = Flask(__name__)
mail = Mail(app1) # instantiate the mail class
   
# configuration of mail
app1.config['MAIL_SERVER']='smtp.gmail.com'
app1.config['MAIL_PORT'] = 465
app1.config['MAIL_USERNAME'] = 'balajicena1995@gmail.com'
app1.config['MAIL_PASSWORD'] = 'tn18ab9058'
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
   with app.open_resource("data.txt") as fp:  
      msg.attach("data.txt", "data/txt",fp.read())  
   mail.send(msg)
   return 'Mail Sent'
if __name__ == "__main__":     
    app1.run()
"""  
  
