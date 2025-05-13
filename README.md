
# OpenAI SDK + Responses API Demo

This repository demonstrates how to use the OpenAI SDK with the new `responses` API for building AI-powered applications.

Unlike the traditional `chat.completions` API, the `responses` API handles memory management for you. You no longer need to resend the full chat history to maintain context—just pass the `response_id` to continue the conversation.

## What's Covered

- Installing and setting up the OpenAI SDK
- Using `.env` files to manage your API key securely
- Sending prompts using `responses.create()`
- Comparing `chat.completions` and `responses`
- Understanding how `response_id` enables contextual memory

## Watch the Full Walkthrough

Check out the full video here:  
**OpenAI SDK: A Game Changer for Building AI Apps**  
https://youtu.be/DmpbZbMS9NI

## Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/openai-sdk-demo.git
   cd openai-sdk-demo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your API key:
   ```
   OPENAI_API_KEY=sk-...
   ```

4. Run the script:
   ```bash
   python main.py
   ```

## Requirements

- Python 3.8 or higher
- `openai`
- `python-dotenv`

## Feedback

Found this helpful or have suggestions? Leave a comment on the video or open an issue in this repository.
