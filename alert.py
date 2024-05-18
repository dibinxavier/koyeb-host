from twilio.rest import Client

def sendTwilioMessage(message):
    account_sid_part1 = 'ACf349f16d4c1d424'
    account_sid_part2 = '53b115c4f78804831'
    account_sid = account_sid_part1 + account_sid_part2
    auth_token_part1 = 'b522abf69803a697'
    auth_token_part2 = 'dc4b8ba5038f5587'
    auth_token = auth_token_part1 + auth_token_part2
    print(f"auth_token: {auth_token}")
    fromNumber= '+16363227054'
    toNumber= '+918714812137'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=fromNumber,
        body=message,
        to=toNumber
    )
    message = client.messages(message.sid).fetch()
    if message is not None and message != "":
        print(f"Message sent successfully! - SID = {message.sid}")
        print(f"Message Status: {message.status}")

def scriptFromMainPage():
    try:
        message='Playoff 2 tickets available!'
        sendTwilioMessage(message)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print ("test success finally")

scriptFromMainPage()
