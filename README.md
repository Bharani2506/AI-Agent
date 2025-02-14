# 🚀 AI Shopping Agent using LLMs

## Overview
This project explores how **AI agents** powered by **LLMs (Large Language Models)** can be used to automate online shopping. Using an open-source project called **Browse Use**, we deployed a local AI agent to browse e-commerce websites, add products to the cart, and proceed to checkout.

## Features
- 🤖 **AI-powered shopping assistant** using **Gemini AI** via Google Studio (free for students!)
- 🛒 Automated browsing, cart management, and checkout simulation
- 🏗️ Built using **LangChain** for agentic workflows
- 💡 Learn how LLMs interact with web-based tasks

## Setup & Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `pip` package manager
- API access to **Gemini AI** (via Google AI Studio)

### Installation Steps
```sh
# Clone this repository
git clone https://github.com/yourusername/ai-shopping-agent.git
cd ai-shopping-agent

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup
Create a `.env` file and add your Google AI Studio API key:
```sh
API_KEY=your_google_api_key
```

## How It Works
1. The AI agent is initialized using **LangChain** and connected to **Gemini AI**.
2. The agent browses an online store (e.g., FC Barcelona official store) and selects a predefined item.
3. It adds the product to the cart, verifies the selection, and proceeds to checkout.
4. The process stops before making a real payment (we like our wallets intact 💸😅).

## Demo Example
We tested this by ordering a **Barcelona UCL kit (Pedri 8 - Player Version)** from the official store:
✅ Browsed the store 🛍️  
✅ Added the kit to cart 👕  
✅ Checked the cart 🛒  
✅ Proceeded to payment (but didn't pay! 😅)  

## Acknowledgments
Huge thanks to [Gregor Zunic](https://x.com/gregpr07) & [Magnus Müller](https://x.com/mamagnus00) for their amazing open-source project **Browse Use**, which made this experiment possible! 🙌

## Future Enhancements
- 🛠️ Integrate **more LLMs** (GPT, Claude, Mistral, etc.)
- 🌍 Expand functionality to multiple online stores
- 💳 Simulate secure payment process (without actual transactions!)

## Contributors
👨‍💻 **Praveen** – [LinkedIn](https://linkedin.com/in/praveen)  

## License
This project is open-source and available under the **MIT License**.

---

💡 **Want to contribute?** Feel free to fork the repo, submit pull requests, or reach out with ideas!
