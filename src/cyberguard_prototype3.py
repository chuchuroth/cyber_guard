# update feature:
# Analyze URLs: Check sites like masscoin.vip for scam signs.
# Cross-Reference Companies: Flag "Qiming Tech" or similar fronts.
# Link to Blockchain/SEPA: Tie the URL to suspicious transactions for a fuller picture.
# Warn and Investigate: Alert users and suggest police steps based on this intel.



import openai
import requests

# Replace with your keys
openai.api_key = "your-openai-api-key-here"
etherscan_api_key = "your-etherscan-api-key-here"

# CyberGuard’s instructions with your scam context
cyber_instructions = (
    "You are CyberGuard, an AI Police Assistant. Detect scams in text, URLs, wallets, or IBANs. "
    "Look for red flags: fake investment promises, urgent demands, shady URLs (e.g., .vip domains), "
    "or suspicious companies. Rate risk as 'Low', 'Medium', or 'High'. Suggest pre-warnings and "
    "investigation steps. Example: I was scammed via 'https://masscoin.vip/#/user' (Qiming Tech, "
    "Chinese group in Dubai, 2023) promising big returns—linked to ETH wallets and SEPA IBAN "
    "LT783550020000012861."
)

# Check wallet (Ethereum)
def get_wallet_info(wallet):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={wallet}&startblock=0&endblock=99999999&sort=asc&apikey={etherscan_api_key}"
    try:
        response = requests.get(url).json()
        if response["status"] == "1":
            tx_count = len(response["result"])
            return f"Wallet {wallet} has {tx_count} transactions."
        return "No wallet data found."
    except:
        return "Error checking wallet."

# Check SEPA IBAN
def check_sepa_iban(iban):
    if iban.startswith("LT") and len(iban) == 20 and iban[4:9] == "35500":
        return "IBAN tied to UAB PAYRNET (Lithuania)—often used in scams."
    return "IBAN format valid but bank not identified."

# Basic URL check (expandable with APIs later)
def check_url(url):
    if ".vip" in url:
        return f"URL {url} uses a .vip domain—frequently tied to scams."
    return f"URL {url}—no specific scam data available yet."

# Analyze with OpenAI
def analyze_text(text, extra_info=""):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": cyber_instructions},
            {"role": "user", "content": f"Analyze: '{text}'. Extra info: {extra_info}"}
        ],
        max_tokens=200
    )
    return response.choices[0].message["content"]

# Main loop
print("CyberGuard v3: Enter text, wallet, IBAN, or URL (type 'quit' to stop):")
while True:
    user_input = input("Input: ")
    if user_input.lower() == "quit":
        print("Shutting down...")
        break
    extra_info = ""
    if user_input.startswith("0x") and len(user_input) == 42:
        extra_info = get_wallet_info(user_input)
    elif user_input.startswith("LT") and len(user_input) == 20:
        extra_info = check_sepa_iban(user_input)
    elif "http" in user_input:
        extra_info = check_url(user_input)
    result = analyze_text(user_input, extra_info)
    print("CyberGuard Report:\n", result)
    print("-" * 50)