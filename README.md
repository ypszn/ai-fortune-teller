# Hyperbolic Labs Chatbot
This repo contains a simple automated chatbot built using the [Hyperbolic Labs API](https://app.hyperbolic.xyz). The AI Fortune Teller Chatbot is a fun and mystical chatbot that predicts your future with dramatic, over-the-top responses. It uses the Hyperbolic Labs API to generate AI-powered fortune readings in a mysterious and engaging way.

## About Hyperbolic
[Hyperbolic Labs](https://hyperbolic.xyz) is an open-access AI platform that provides low-cost computing resources and inference services via their API.
* This project uses their language model (`meta-llama/Meta-Llama-3.1-8B-Instruct`) to generate responses to any question, showcasing the power of their tools for developers.
* Check out their [official documentation](https://docs.hyperbolic.xyz) for more details.

## Features
- Generates dramatic and mystical fortune responses.
- Uses Hyperbolic Labs API for AI-generated text.
- Supports unlimited questions with a retry option.
- Provides random mystical introductions for added effect.
- Built with Python and the `requests` library.

## Prerequisites
- Python 3.6+
- A [Hyperbolic API key](https://app.hyperbolic.xyz/settings) 

## Setup
1. **Install Packages**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install git screen python3 python3-pip python3-venv -y
   ```
2. **Clone the Repository**
   ```bash
   git clone https://github.com/ypszn/ai-fortune-teller.git
   cd ai-fortune-teller
   ```
   Create screen
   ```bash
   screen -S chatbot
   ```
4. **Install Dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux
   venv\Scripts\activate     # On Windows
   ```
   ```bash
   pip install requests
   ```
5. **Configure the API Key**

Replace the `YOUR_API_KEY_HERE` in `chatbot.py` with your own [Hyperbolic API Key](https://app.hyperbolic.xyz/settings):
   ```bash
nano chatbot.py
   ```
5. **Run the Chatbot**

Run the script
   ```bash
   python3 chatbot.py
   ```
* To minimize screen: `CTRL+A+D`
* To kill screen: `Ctrl+C` or command: `screen -XS chatbot quit`

## Usage
Example interaction:
```
🔮 Welcome to the AI Fortune Teller! 🔮
Tell me your name, seeker: Alex
What fate do you wish to know? Ask your question: Will I become rich?

Ahh... the stars whisper secrets only I can hear!

The prophecy reveals...
━━━━━━━━━━━━━━━━━━━━━━━
Ah, Alex... the universe stirs at your question. I see golden coins raining from the heavens, but beware! Riches come with great trials. A shadowy figure looms—perhaps a rival, or a lesson disguised as loss. Fortune smiles upon you, but only if you dare to seize the moment!
━━━━━━━━━━━━━━━━━━━━━━━

Would you like to ask another question? (yes/no): yes
```

## Notes
* Note the API usage limits and costs on your Hyperbolic Labs plan.
