import os.path
import re
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64

def get_messages():
    SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build("gmail", "v1", credentials=creds)

    results = service.users().messages().list(userId="me", labelIds=["SPAM"], maxResults=5).execute()
    messages = results.get("messages", [])
    if not messages:
        print("No messages found.")
    else:
        for msg in messages:
            message = service.users().messages().get(userId="me", id=msg["id"], format="full").execute()

            payload = message.get("payload", {})
            parts = payload.get("parts", [payload])

            for part in parts:
                if part["mimeType"] == "text/plain":
                    body_data = part["body"].get("data")
                    if not body_data:
                        continue

                    body = base64.urlsafe_b64decode(body_data).decode()
                    all_matches = re.findall(r"\b\d{6}\b", body)

                    if all_matches:
                        latest_otp = all_matches[-1]
                        # print(latest_otp)
                        return latest_otp
    return None

if __name__ == "__main__":
    get_messages()