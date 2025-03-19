# investigate blockchain-based cryptocurrency scams
# pull blockchain data using Etherscan’s free API (a public Ethereum explorer) and let OpenAI analyze it



import openai
import requests

# Replace with your keys
openai.api_key = "your-openai-api-key-here"
etherscan_api_key = "your-etherscan-api-key-here"

# CyberGuard’s instructions
cyber_instructions = (
    "You are CyberGuard, an AI Police Assistant. Detect scams in cryptocurrency transactions. "
    "Analyze wallet addresses and transaction data for red flags like new wallets, quick fund moves, "
    "or scam patterns (e.g., 'send $100, get $200'). Rate risk as 'Low', 'Medium', or 'High'. "
    "Suggest pre-warnings and investigation steps. Use blockchain data if provided."
)

# Function to get wallet data from Etherscan
def get_wallet_info(wallet):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={wallet}&startblock=0&endblock=99999999&sort=asc&apikey={etherscan_api_key}"
    try:
        response = requests.get(url).json()
        if response["status"] == "1":
            tx_count = len(response["result"])
            return f"Wallet {wallet} has {tx_count} transactions."
        return "No data found for this wallet."
    except:
        return "Error checking wallet—try later."

# Function to analyze with OpenAI
def analyze_text(text, wallet_info=""):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": cyber_instructions},
            {"role": "user", "content": f"Analyze this: '{text}'. Blockchain info: {wallet_info}"}
        ],
        max_tokens=200
    )
    return response.choices[0].message["content"]

# Main loop
print("CyberGuard Prototype v2: Enter text or a wallet address (type 'quit' to stop):")
while True:
    user_input = input("Input: ")
    if user_input.lower() == "quit":
        print("CyberGuard shutting down...")
        break
    # Check if it’s a wallet address (starts with 0x and 42 chars)
    if user_input.startswith("0x") and len(user_input) == 42:
        wallet_info = get_wallet_info(user_input)
        result = analyze_text("Check this wallet for scam activity.", wallet_info)
    else:
        result = analyze_text(user_input)
    print("CyberGuard Report:\n", result)
    print("-" * 50)