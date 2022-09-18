import win32api
from flask import Flask, render_template, request
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/SendMail',methods=["POST"])
def SendMail():
    print("Python Injection being completed")
    print("""
________                                                             .__     
\______ \   ____     ____   ___________  _______  ____  __ __   ____ |  |__  
 |    |  \ /  _ \   /    \ /  _ \_  __ \ \_  __ \/  _ \|  |  \_/ ___\|  |  \ 
 |    `   (  <_> ) |   |  (  <_> )  | \/  |  | \(  <_> )  |  /\  \___|   Y  \
/_______  /\____/  |___|  /\____/|__|     |__|   \____/|____/  \___  >___|  /
        \/              \/                                         \/     \/ 
""")

    output = request.get_json()
    print("Value of mail=" + str(output))
    sender_email = "god237056@gmail.com"
    receiver_email = "alvaro.cadenas@students.st-patricks.com"
    password = "uqsggclyyhtlfpft"
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # Create the plain-text and HTML version of your message
    text = """\
    Hola,
    Cadenitas
    """
    html = """\
    <html>
      <body>
        <p>Hola<br>
           ADIOS<br>
           <a href="https://drive.google.com/drive/u/0/search?q=type:video"</a> 
        </p>
      </body>
    </html>
    """
    
    
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    
    message.attach(part1)
    message.attach(part2)
    
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
       
