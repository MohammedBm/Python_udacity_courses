from twilio.rest import TwilioRestClient

account_sid = "{{ AC827edb9e31c3eeb04f4fc3265788da3c }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ 945ab1d636b1e0a77bfadcaa119a4ab3 }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is Se7o?",
    to="+966557627080",    # Replace with your phone number
    from_="+18473069846") # Replace with your Twilio number

print(message.sid)


