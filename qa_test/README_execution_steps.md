Installation steps to follow:

1. Clone the repository and go into the **qa_test** folder:
    * `git clone https://github.com/sudipsudip001/allOfAutomation.git`
    * `cd qa_test`
1. Install the requirements (You must have UV installed in your computer):
    * `uv sync`
1. For setting up gmail api:
    1. go to google console
    1. create project
    1. enable the API: API & Services > Library > search and enable Gmail API
    1. configure OAuth Consent Screen: APIs & Services > OAuth consent screen
    1. Create credentials: go to APIs & Services > Credentials, click + Create Credentials & select OAuth client ID.
    1. Choose Desktop app
    1. Download credentials, name it credentials.json and keep it inside qa_test folder.

1. Run the program using: `python signup_automation_script.py` command.

1. The demonstration video of the application can be found [here](https://youtu.be/8ztNYDXsYYk).