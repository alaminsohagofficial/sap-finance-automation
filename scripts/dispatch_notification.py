import json
import requests

# Load SMS Payload
with open('payloads/sms_002905.json') as f:
    sms_data = json.load(f)

# Example: Dispatching to SMS Gateway API
# sms_response = requests.post("https://api.your-sms-gateway.com/send", json=sms_data)
# print("SMS Status:", sms_response.status_code)

print(f"Ready to dispatch SMS to {sms_data['recipient']}...")
print(f"Message: {sms_data['message']}")
