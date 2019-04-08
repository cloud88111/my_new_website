# Don't forget to "pip install requests"
# Could be "sudo pip install request"
import requests

# Get this from http://app.mailgun.com/app/dashboard
def sendmail(sendto,contact,message):
    sender = "name"
    domain_name = "domain"
    api_key = "key"
    
    send_table = {"UK":'nadelina.georgieva@ig.com',
                  "Germany":'nadelina.georgieva@ig.com',
                  "France":'nadelina.georgieva@ig.com'}
    
    def send_simple_message(sendto,contact,message):
        print("sending email")
        return requests.post(
                "https://api.mailgun.net/v3/{0}/messages".format(domain_name),
                auth=("api",api_key),  # authorisation token 
                data={
                        "from": "Nadleina <{0}@{1}>".format(sender, domain_name),
                        "to": [send_table[sendto]],
                        "subject": "email",
                        "text": message
                    },
                        #verify='C:\Users\georgin\Desktop\Python\zscaler.cer'
                )
    
    response = send_simple_message(sendto,contact,message)
    print(response.url)
    print(response.status_code)
    print(response.headers["content-type"])
    print(response.text)           