import vonage

def send_sms_notification(to_phone, message):
    client = vonage.Client(key='b16ca364', secret='oApPQzh3EZRQBthA')
    sms = vonage.Sms(client)

    responseData = sms.send_message({
        'from': 'VonageAPI',
        'to': to_phone,
        'text': message,
    })

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")


TEC_THRESHOLD = 20.0  
predicted_tec = 21.99


if predicted_tec > TEC_THRESHOLD:
    message = f'The predicted TEC value is {predicted_tec}. Communications might be affected.'
    user_phones = ['+919008295292']  
    for phone in user_phones:
        send_sms_notification(phone, message)
