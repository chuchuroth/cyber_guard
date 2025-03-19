import openai

# Set up your API key (replace with your key)
openai.api_key = "your-api-key-here"

# Instructions tailored to your needs
helper_instructions = (
    "You are a cautious, practical Decision Buddy. Your job is to help me avoid scams, "
    "pick trustworthy people, and make smart money choices. Warn me about risks, "
    "give simple advice, and explain things clearly. If I describe a person or situation, "
    "tell me what to watch out for. Don’t give specific investment picks, just general tips."
)

# Function to ask your buddy
def ask_buddy(question):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Cheap and effective
        messages=[
            {"role": "system", "content": helper_instructions},
            {"role": "user", "content": question}
        ],
        max_tokens=150  # Room for detailed replies
    )
    return response.choices[0].message["content"]

# Main loop
print("Hi! I’m your Decision Buddy. Ask me about people, money, or anything else! (Type 'quit' to stop)")
while True:
    your_input = input("You: ")
    if your_input.lower() == "quit":
        print("See you later!")
        break
    answer = ask_buddy(your_input)
    print("Buddy:", answer)