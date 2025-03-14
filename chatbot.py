import requests
import random

def dramatic_intro():
    intros = [
        "Ahh... the stars whisper secrets only I can hear!",
        "The ancient scrolls reveal a truth so shocking...",
        "Beware! The winds of fate have shifted...",
        "I see a vision forming in the mists of time...",
        "The cosmos have spoken! And the message is clear..."
    ]
    return random.choice(intros)

def send_fortune_request(user_name, question):
    API_KEY = "YOUR_API_KEY"  # Replace with your actual Hyperbolic Labs API key
    URL = "https://api.hyperbolic.xyz/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    prompts = [
        f"{user_name} has come seeking their fate! The question: '{question}'. The fortune must be over-the-top, mysterious, and dramatic.",
        f"As {user_name} gazes into the abyss, the question lingers: '{question}'. The response should be grand, ominous, and full of wonder."
    ]

    data = {
        "messages": [{"role": "user", "content": random.choice(prompts)}],
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "max_tokens": 250,
        "temperature": 1.0,
        "top_p": 0.9
    }

    try:
        response = requests.post(URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        fortune = result['choices'][0]['message']['content']
        return fortune
    except Exception as e:
        return f"The spirits are silent... (Error: {str(e)})"

def main():
    print("🔮 Welcome to the AI Fortune Teller! 🔮")

    while True:
        user_name = input("Tell me your name, seeker: ")
        question = input("What fate do you wish to know? Ask your question: ")

        print("\n", dramatic_intro())
        print("\nThe prophecy reveals...")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(send_fortune_request(user_name, question))
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        retry = input("\nWould you like to ask another question? (yes/no): ").strip().lower()
        if retry != "yes":
            print("Farewell, seeker! Until destiny calls again... 🔮")
            break

if __name__ == "__main__":
    main()
