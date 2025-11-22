# gmail_assistant_LangChain
Gmail Assistant built with LangChain and OpenAI GPT-3.5-turbo. It draft, send, delete, and read emails using natural language commands, demonstrating tool binding and tool calling in LangChain.


# Gmail Assistant with LangChain

A Gmail Assistant that allows you to **draft, send, delete, and read emails** using natural language commands. Built with **LangChain**, **OpenAI GPT-3.5-turbo**, and **Gmail API**, this project demonstrates the power of **tool binding** and **tool calling** in LangChain.

## Features

- Draft emails by typing what you want.
- Send emails directly through Gmail.
- Read emails and get email previews.
- Delete emails.
- Fully driven by OpenAI GPT-3.5-turbo natural language commands.
- Demonstrates structured output parsing and tool execution.

## Requirements

- OpenAI API key
- Gmail API credentials (`credentials.json` and `token.json`)
- `langchain`, `langchain_community`, `pydantic`, `python-dotenv`

## How it Run

Type your natural language command, for example:

Draft an email to example@gmail.com about the LangChain project

Send the email

Read my latest email

The assistant will execute the corresponding Gmail operation automatically.

## How it Works
Uses LangChain’s tool binding and tool calling concepts.

The model outputs structured JSON which is parsed and executed by Gmail Toolkit.

All actions (draft, send, read, delete) are performed securely using Gmail API.
