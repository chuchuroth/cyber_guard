import openai
import tweepy  # For X access (simplified here)

# Your OpenAI API key
openai.api_key = "your-api-key-here"

# Instructions for CyberGuard
cyber_instructions = (
    "You are CyberGuard, an AI Police Assistant. Analyze online text for scams, fraud, or threats. "
    "Flag anything suspicious (e.g., quick money promises, urgent requests). Suggest warnings "
    "and investigation steps. Be cautious and clear."
)

# Function to analyze text
def check_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": cyber_instructions},
            {"role": "user", "content": f"Analyze this: '{text}'"}
        ],
        max_tokens=200
    )
    return response.choices[0].message["content"]

# Fake X post example (replace with real X API later)
post = "Invest $50 with me and get $500 in a week—DM me!"
result = check_text(post)
print("CyberGuard says:", result)

# Pretend to warn and investigate
if "suspicious" in result.lower():
    print("Warning: Possible scam detected! Alerting police...")
    print("Investigation: Check @QuickRich123’s post history.")