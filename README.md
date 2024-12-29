# Basic Setup for AI Agent Project

## Overview

This guide provides a step-by-step walkthrough to set up a Python project for building AI agents using OpenAI's API. The setup includes creating a virtual environment, installing dependencies, and implementing a simple text generation function. By following these steps, you can create a foundational structure for building more complex AI agents.

---

## Step 1: Create a Python Virtual Environment

1. **Open a Terminal:**
   - Navigate to your project directory or create a new one:
     ```bash
     mkdir ai_agent_project
     cd ai_agent_project
     ```

2. **Create a Virtual Environment:**
   - Use Python's `venv` module to create an isolated environment:
     ```bash
     python3 -m venv venv
     ```

3. **Activate the Virtual Environment:**
   - On macOS:
     ```bash
     source venv/bin/activate
     ```

4. **Verify the Environment:**
   - Ensure the virtual environment is active by checking the Python version:
     ```bash
     python3 --version
     ```

---

## Step 2: Install the OpenAI Package

1. **Install the Package:**
   - Use `pip` to install the OpenAI Python client library:
     ```bash
     pip install openai
     ```

2. **Verify Installation:**
   - Check the installed packages to confirm:
     ```bash
     pip list
     ```

---

## Step 3: Create a Basic Text Generation Function

1. **Create a Python File:**
   - Save the following code in a file called `openai_module.py`:
     ```python
     from openai import OpenAI
     import os
     from dotenv import load_dotenv

     # Load environment variables
     load_dotenv()

     # Create an instance of the OpenAI class
     openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

     def generate_text_basic(prompt: str, model="gpt-4", system_prompt: str = "You are a helpful AI assistant"):
         response = openai_client.chat.completions.create(
             model=model,
             messages=[
                 {"role": "system", "content": system_prompt},
                 {"role": "user", "content": prompt}
             ]
         )
         return response.choices[0].message.content

     def generate_text_with_conversation(messages, model="gpt-4"):
         response = openai_client.chat.completions.create(
             model=model,
             messages=messages
         )
         return response.choices[0].message.content
     ```

2. **Set Up Environment Variables:**
   - Create a `.env` file in the project directory to store your OpenAI API key:
     ```makefile
     OPENAI_API_KEY=your_api_key_here
     ```

   - Go to the [OpenAI Developer Platform](https://platform.openai.com/) to create your new API key:
![OpenAI Developer Platform](https://github.com/jason-victor1/basic-setup/blob/main/OpenAI%20Developer%20Platform.png?raw=true)


   - Install `python-dotenv` to load the `.env` file:
     ```bash
     pip install python-dotenv
     ```

   - Update the `openai_module.py` script to load environment variables:
     ```python
     from dotenv import load_dotenv
     load_dotenv()
     ```

---

## Step 4: Create a Test File Script

1. **Create a Python File:**
   - Save the following code in a file called `test.py`:
     ```python
     from openai_module import generate_text_basic

     prompt = "Explain the concept of AI agents in one sentence."

     response = generate_text_basic(prompt, model="gpt-4")

     print(response)
     ```

2. **Run the Script:**
   - Execute the script to test the text generation:
     ```bash
     python test.py
     ```

---

## Expected Output

If the setup is correct, the script will generate and print a response based on the input prompt:

```text
AI agents are autonomous entities that observe through sensors and act upon an environment using actuators based on artificial intelligence and machine learning to achieve specific goals.
```

---

## Key Concepts Explained in Context

- **Why Use a Virtual Environment?**
  - To isolate project dependencies and avoid conflicts with global packages.

- **Why Load Environment Variables?**
  - To securely manage sensitive information like API keys.

- **How the Function Works:**
  - The `generate_text_basic` function uses OpenAI’s `Completion.create` method to interact with a language model and return a generated response.

---

## Conclusion

This setup guide ensures you have a clean and functional environment to start building AI agents or other projects using the OpenAI API. By completing these steps, you will have a basic foundation to experiment with and expand on more complex AI workflows.
