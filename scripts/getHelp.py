#!/usr/bin/python3

""" Do not forget to add 
<Directory /var/www/cgi-bin>
  AllowOverride None
  Options ExecCGI
  Order allow,deny
  Allow from all
</Directory>

to /etc/apache2/apache2.conf
"""

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
name     = form.getvalue('firstname')
email    = form.getvalue('email')
address  = form.getvalue('address')
city     = form.getvalue('city')
state    = form.getvalue('state')
zip_code = form.getvalue('zip')

if name == None:
    name = "cmdln-test"
    email = "cmdln-test"
    address = "cmdln-test"
    city = "cmdln-test"
    state = "cmdln-test"
    zip_code = "cmdln-test"

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Getting help</title>")
print ("</head>")
print ("<body>")

body_text = "TODO text support"

body_html = (
"Getting help <b>for:</b><br>" +
"<table>"+
"<tr><td>name:</td><td>"+name+"</tr>"+
"<tr><td>email:</td><td>"+email+"</tr>"+
"<tr><td>address:</td><td>"+address+"</tr>"+
"<tr><td>city:</td><td>"+city+"</tr>"+
"<tr><td>state:</td><td>"+state+"</tr>"+
"<tr><td>zip_code:</td><td>"+zip_code+"</tr>"+
"</table><br>"+
"<b>From:</b> TODO:$VOLUNTEER<br>"+
"&nbsp<br>"
"Standby for the materials you need in your mailbox!"
)
print(body_html)

print ("</body>")
print ("</html>")



#!/usr/bin/python3
import smtplib, ssl 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

volunteer_email='sean.head@gmail.com'
volunteer_email='lonoami@gmail.com'
receiver_email=volunteer_email
sender_email = "vbuggertest@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email
message.attach(MIMEText(body_text, "plain"))
message.attach(MIMEText(body_html, "html"))

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
password = "********"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)

    server.sendmail(sender_email,volunteer_email, message.as_string())
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()

