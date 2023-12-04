from flask import Flask, jsonify
from flask_cors import CORS  # For handling cross-origin requests
import requests
from flask import render_template
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
CORS(app)  # Enable CORS

# Include your get_number_of_owners function here

def get_number_of_owners(asset_contract_address, token_id, api_key):
    url = f"https://api.opensea.io/api/v1/asset/{asset_contract_address}/{token_id}/owners"
    headers = {"Accept": "application/json", "X-API-KEY": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        unique_usernames = set()
        for owner_info in data['owners']:
            username = owner_info['owner']['user']['username']
            if username:
                unique_usernames.add(username)
        print(f"Usernames for token ID {token_id}: {unique_usernames}")
        print(f"Number of unique usernames for token ID {token_id}: {len(unique_usernames)}")
        return len(unique_usernames)
    else:
        print(f"Error fetching data: {response.status_code}")
        return 0

@app.route('/get_nft_data')
def get_nft_data():
    # Example data fetching
    api_key = '04f1d6917de349caa2d1236eed4df99b'
    contract_address = "0xae2bc979178e97e0688384aab00055e67bea91ed"
    owner_counts = [get_number_of_owners(contract_address, token_id, api_key) for token_id in [1, 2, 3, 4, 5]]
    return jsonify(owner_counts)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
