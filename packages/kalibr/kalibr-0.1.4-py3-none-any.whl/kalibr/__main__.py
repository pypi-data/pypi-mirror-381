# kalibr/__main__.py
from kalibr_sdk import Kalibr

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", help="Airtable API key")
    parser.add_argument("--base-url", default="https://api.airtable.com/v0/app12345/Contacts")
    args = parser.parse_args()

    k = Kalibr(args.base_url, api_key=args.api_key)
    k.add_action("add_contact", "/", "POST", params={"name": "string", "email": "string"})
    k.deploy()

if __name__ == "__main__":
    main()
