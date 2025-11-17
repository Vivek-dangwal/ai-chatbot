AI Chatbot with Memory and Calendar Access

This project is a simple chatbot that can save user information using a memory system, fetch calendar schedules, and chat through a Streamlit interface. The goal was to implement three main components: Mem0 for memory, MCP for tools, and Streamlit for the UI.

1. Project Overview

The chatbot performs three main functions:

Stores and retrieves user memories using the Mem0 memory client.

Provides meeting schedules through a calendar tool built with the MCP framework.

Offers a simple chat interface built with Streamlit.

The project is designed to demonstrate tool usage, state handling, and conversational interaction.

2. Project Structure
ai-chatbot/
│── app.py
│── bot.py
│── memory_manager.py
│── calendar_manager.py
│── sample_responses.txt
│── README.md
│── .env   (stores API key)

3. Installation and Setup
Step 1: Create a virtual environment
conda create -n chatbot python=3.10 -y
conda activate chatbot

Step 2: Install required packages
pip install streamlit mem0ai mcp python-dotenv

Step 3: Add Mem0 API key

Create a file named .env in the project folder and add:

MEM0_API_KEY=your_api_key_here

4. Running the Chatbot

Start the Streamlit app:

streamlit run app.py


This will open a browser window where you can chat with the bot.

5. Features
a) Memory System (using Mem0)

The bot can remember user details and recall them later.

Example commands:

Remember that I enjoy reading at night.
What do you remember?

b) Calendar System (using MCP)

A mock calendar tool returns basic meeting information.

Example commands:

What are my meetings today?
What are my meetings this week?

c) General Chat

The bot also supports normal conversation.

6. Sample Commands to Test

Here are some examples to verify the chatbot:

Hello
Remember that I like studying in the morning.
What do you remember?
What are my meetings today?
What are my meetings this week?

7. Sample Responses File

All sample chatbot responses are stored in the sample_responses.txt file, as required.

8. Notes

The calendar tool is a mock tool built for demonstration.

Memories are stored through the Mem0 API and persist across sessions.

The project is built purely for educational and assignment purposes.

9. Acknowledgments

Mem0 (memory system)

MCP Framework (tool structure)

Streamlit (frontend UI)