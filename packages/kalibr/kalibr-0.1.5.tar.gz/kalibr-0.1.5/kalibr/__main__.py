# kalibr/__main__.py
from .kalibr_sdk import Kalibr

def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", help="Airtable API key")
    parser.add_argument("--base-url", default="https://jsonplaceholder.typicode.com")
    args = parser.parse_args()

    # Demo: wire up some actions
    k = Kalibr(args.base_url, api_key=args.api_key)
    k.add_action("get_posts", "/posts", "GET")
    k.add_action("create_post", "/posts", "POST", params={"title": "string", "body": "string"})
    k.deploy()

if __name__ == "__main__":
    main()
