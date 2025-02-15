# Anthropic Blog Post Agent Tutorial

This tutorial shows you how to build an AI agent that:
- Searches for information on a given topic using DuckDuckGo.
- Summarizes the collected information.
- Generates a short blog post using Anthropic's language model.

## Features

- **Search & Summarize**: Automatically retrieves and condenses web data.
- **LLM-Powered Blog Post**: Generates concise and engaging blog posts.
- **Logging**: Displays runtime logs to help you follow the agent's activity.
- **Exponential Backoff**: Handles API overload gracefully by increasing the delay between retries.

## Prerequisites

- Python 3.8 or later.
- An LLM API key.

## Setup Instructions

1. **Clone the Repository or Download the Code**

   ```bash
   git clone https://github.com/Pitcocy/ai-agent-tutorial
   cd ai-agent-tutorial
   ```

2. **Create a Virtual Environment and Activate It**

   **For Linux/macOS:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   **For Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **macOS Specific Setup (Optional Extra Details)**

   - **Install Homebrew** (if you haven't already):
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - **Install Python3 using Homebrew** (if needed):
     ```bash
     brew install python
     ```
   - Then create the virtual environment as shown above:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Environment Variables**

   Create a file named `.env` in the project root (if it doesn't already exist) and add your Anthropic API key:
   ```env
   LLM_API_KEY=YOUR_ACTUAL_API_KEY_HERE
   ```
   Replace `YOUR_ACTUAL_API_KEY_HERE` with your actual Anthropic API key.

## Running the Agent

Run the main script using Python:

```bash
python blog_agent.py
```


