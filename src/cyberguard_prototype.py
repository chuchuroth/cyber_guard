import openai

# Replace with your API key
openai.api_key = "your-api-key-here"

# CyberGuard’s instructions
cyber_instructions = (
    "You are CyberGuard, an AI Police Assistant. Your job is to detect scams, fraud, or illegal "
    "activity in online text. Look for red flags like quick money promises, urgent requests, "
    "or suspicious demands (e.g., 'send cash now'). Rate the text as 'Low', 'Medium', or 'High' "
    "risk. If Medium or High, suggest a pre-warning and investigation steps. Be clear and cautious."
)

# Function to analyze text
def analyze_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Cheap, effective model
        messages=[
            {"role": "system", "content": cyber_instructions},
            {"role": "user", "content": f"Analyze this text: '{text}'"}
        ],
        max_tokens=150  # Enough for a solid response
    )
    return response.choices[0].message["content"]

# Main loop to test it
print("Welcome to CyberGuard Prototype! Enter text to analyze (type 'quit' to stop):")
while True:
    user_input = input("Text: ")
    if user_input.lower() == "quit":
        print("CyberGuard shutting down...")
        break
    result = analyze_text(user_input)
    print("CyberGuard Report:\n", result)
    print("-" * 50)