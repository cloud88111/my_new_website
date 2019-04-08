# Don't forget to "pip install requests"
# Could be "sudo pip install request"
import requests

# Get this from http://app.mailgun.com/app/dashboard
sender = "nadelina" #sender name is the name it will come from like nadelina@jeganathan.co.uk 
domain_name = "sandbox1d4c0da5cdf34bfba2a2a8b53e863fbc.mailgun.org"
api_key = "d4ebbbdc4a378933e8c13e8a2eacf679-985b58f4-3091d3f8"

send_table = {"UK":'nadelina.georgieva@ig.com',
              "Germany":'nadelina.georgieva@ig.com',
              "France":'nadelina.georgieva@ig.com'}

def send_simple_message(sendto,contact,message):
    return requests.post(
            "https://api.mailgun.net/v3/{0}/messages".format(domain_name),
            auth=("api",api_key),  # authorisation token 
            data={
                    "from": "Nadleina <{0}@{1}>".format(sender, domain_name),
                    "to": [send_table[sendto]],
                    "subject": "Alert email",
                    "text": message + '/n Call me back on ' + str(contact) + 'please!'
                },
                    #verify='C:\Users\georgin\Desktop\Python\zscaler.cer'
            )
    
sendto = 'UK'
contact = '07525056730'
message = 'My husband is beating me!'
response = send_simple_message(sendto,contact,message)
                    