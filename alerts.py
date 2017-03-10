import json, urllib, datetime, time, smtplib, requests
from datetime import timedelta
from twilio.rest import TwilioRestClient
from email.mime.text import MIMEText
accountSID = [your info]
authToken = [your info]
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = [your twilio number]
myCellPhone = [your cell number]


oidList = []
import arcrest
from arcrest.security import AGOLTokenSecurityHandler

username = [your username]
password = [your password]
sh = AGOLTokenSecurityHandler(username=username, password=password)

URL = [url to your feature layer]
fl = arcrest.agol.FeatureLayer(url=URL,securityHandler = sh, initialize = True)
# the creation date field requires tracking enabled
params = {'f': 'pjson', 'where': "1=1", 'outfields': 'OBJECTID, CreationDate', 'returnGeometry': 'false'}

sql= '1=1'
resFeats = fl.query(where=sql, out_fields="*")

for feat in resFeats:
    createDate = feat.get_value('CreationDate')

    createDate = int(str(createDate)[0:-3])
    t = datetime.datetime.now() - timedelta(hours=1)
    t = time.mktime(t.timetuple())
    if createDate > t:
        oidList.append(feat.get_value('OBJECTID'))

# To send email, press 1
SUBJECT = ''
TEXT = ''
FROM = 'mikerfuller@live.com'
TO = 'fuller@tmacog.org'
# Exit the program if there are no updates to share
if len(oidList) == 0:
    print("no new records")
    exit()
# Prepare message components if only 1 feature added
elif len(oidList) == 1:
    SUBJECT = 'New Feature Added'
    TEXT = str(len(oidList)) + " feature was added to [name of your layer]."
# Prepare message components if more than 1 feature added
elif len(oidList) > 1:
    SUBJECT = 'New Features Added'
    TEXT = str(len(oidList)) + " features were added to [name of your layer]."
# Send SMS message with update
message = twilioCli.messages.create(body=TEXT, from_=myTwilioNumber, to=myCellPhone)
# Create email message and parts
msg = MIMEText(TEXT)
msg['From'] = FROM
msg['To'] = TO
msg['Subject'] = SUBJECT

# Connect to email server and send email
with smtplib.SMTP([your smtp server], [your port]) as smtpObj:
    smtpObj.starttls()
    smtpObj.login([your email],[your password])
    smtpObj.send_message(msg)
