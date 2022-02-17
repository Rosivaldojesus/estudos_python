# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def main():
    account_sid = 'AC1021e5def4f6911b48f8612a5ef789bb'
    auth_token = '2f5aea28a797877914550f9f41e6fe25'
    client = Client(account_sid, auth_token)


    number = int(input("Digite um valor inteiro: "))

    if number > 10:

        message = client.messages \
                        .create(
                             body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                             from_='+18596953499',
                             to='+5511942171085'
                         )

        print(message.sid)
    else:
        print("O número não atende a demanda!...")

if __name__ == '__main__':
    main()
