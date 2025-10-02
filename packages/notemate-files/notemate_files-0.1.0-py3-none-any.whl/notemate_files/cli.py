# notemate_files/cli.py
import os
import requests
import json
import getpass
from tqdm import tqdm
import argparse

# --- CONFIGURATION ---
BASE_URL = "http://127.0.0.1:5001" # Aapka Flask server ka URL
TOKEN_FILE = os.path.expanduser("~/.notemate_token")

# (save_token, load_token, login, upload_file_with_progress, upload functions yahan paste karein)
# ... poora uploader.py ka code yahan paste kar dein ...
# Example ke liye, main poora code yahan de raha hoon:

def save_token(token):
    with open(TOKEN_FILE, "w") as f:
        f.write(token)
    print("✅ Authentication token saved successfully!")

def load_token():
    if not os.path.exists(TOKEN_FILE):
        return None
    with open(TOKEN_FILE, "r") as f:
        return f.read().strip()

def login():
    print("--- NoteMate CLI Login ---")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/cli/login",
            json={"username": username, "password": password}
        )
        response.raise_for_status()
        data = response.json()
        
        if data.get("success"):
            save_token(data["token"])
        else:
            print(f"❌ Login failed: {data.get('error', 'Unknown error')}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")

def upload_file_with_progress(filepath, relative_path, token):
    try:
        file_size = os.path.getsize(filepath)
        filename = os.path.basename(filepath)
        
        with open(filepath, "rb") as f, tqdm(
            total=file_size,
            unit="B",
            unit_scale=True,
            desc=f"Uploading {filename}",
            ascii=True
        ) as pbar:
            response = requests.post(
                f"{BASE_URL}/api/cli/upload",
                files={"file": (filename, f)},
                data={"relative_path": relative_path},
                headers={"Authorization": f"Bearer {token}"},
            )
            pbar.update(file_size)

        response.raise_for_status()
        data = response.json()
        if not data.get("success"):
            print(f"\n❌ Error uploading {filename}: {data.get('error', 'Unknown server error')}")
        # Success message ab zaroori nahi, progress bar hi kaafi hai

    except FileNotFoundError:
        print(f"\n❌ File not found: {filepath}")
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Upload failed for {filename}: {e}")

def upload(path_to_upload):
    token = load_token()
    if not token:
        print("You are not logged in. Please run 'notemate-files login' first.")
        return

    abs_path = os.path.abspath(path_to_upload)

    if not os.path.exists(abs_path):
        print(f"❌ Path does not exist: {abs_path}")
        return

    if os.path.isfile(abs_path):
        print(f"Starting upload for single file: {os.path.basename(abs_path)}")
        upload_file_with_progress(abs_path, os.path.basename(abs_path), token)
    
    elif os.path.isdir(abs_path):
        print(f"Starting upload for directory: {os.path.basename(abs_path)}")
        all_files = []
        for root, _, files in os.walk(abs_path):
            for filename in files:
                all_files.append(os.path.join(root, filename))
        
        if not all_files:
            print("Directory is empty. Nothing to upload.")
            return
            
        print(f"Found {len(all_files)} files to upload.")
        for file_path in all_files:
            relative_path = os.path.relpath(file_path, os.path.dirname(abs_path))
            upload_file_with_progress(file_path, relative_path, token)
        print("\n🎉 Directory upload complete!")


def main():
    """CLI commands ko parse karta hai."""
    parser = argparse.ArgumentParser(description="NoteMate CLI Uploader")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # Login command
    parser_login = subparsers.add_parser("login", help="Authenticate with your NoteMate account.")
    
    # Upload command
    parser_upload = subparsers.add_parser("upload", help="Upload a file or directory.")
    parser_upload.add_argument("path", help="The path to the file or directory to upload.")

    args = parser.parse_args()

    if args.command == "login":
        login()
    elif args.command == "upload":
        upload(args.path)

if __name__ == "__main__":
    main()