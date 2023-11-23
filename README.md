# WesBot
An experiment with an AI-powered teaching assistant

## Description
We've kidnapped the university educator and artist, Wes Modes, digitized their brain, and placed them in a sophisticated, multi-layered recurrent neural network to provide you with a unique learning experience. WesBot is an AI-powered chatbot that brings Wes into the virtual realm where you can interact with them to get answers to your questions and guidance in the intricate world of new media, art, and game design. 

## Details
WesBot is powered by a carefully crafted technology stack that seamlessly blends different components to create an personalized chatbot experience. In this section, we'll delve into the core technologies that make WesBot tick, explore its project structure, configuration options, and its reliance on the OpenAI Chat Completions API for intelligent interactions. Additionally, we'll discuss the use of the 'system' role for domain-specific conversations and efficient operation within OpenAI's token limits. Let's start by examining the foundational technology stack.

### Technology Stack
WesBot utilizes a combination of technologies to provide a seamless chatbot experience. Here's an overview of the key components:

- **Flask:** Serving as the web foundation of WesBot, Flask manages routing, request handling, and facilitates communication with the chatbot.

- **Chatbot Class:** The heart of the server-side of the app, the Chatbot class interacts with the OpenAI API, processes user input, and generates responses.

- **JavaScript:** does much of the heavy lifting and takes charge of all front-end responsibilities. It not only handles the user interface but also manages user input and communicates with the Flask backend. JavaScript is responsible for real-time interactions with the chatbot, maintaining chat history, and managing tokens efficiently.

### Technology Stack Overview
Here's a concise breakdown:

- **Languages:** Python and JavaScript/jQuery
- **Framework:** Flask
- **API Integration:** OpenAI API
- **Web Server:** uWSGI

### Project Structure

Here's a quick overview of the primary directories and key files in the project:

- **/static:** Stores static files like JavaScript, CSS, and images for the web interface.
- **/templates:** Contains HTML templates used to render web pages.
- **/app.py:** The entry point for the Flask application, responsible for server setup and route management.
- **/factory.py:** Creates and configures the Flask app.
- **/chatbot.py:** Houses the `Chatbot` class, managing user interactions and responses.
- **/routes.py:** Defines web app routes and endpoints for handling user interactions.

### Configuration
In the config.py file, you'll find essential variables that fine-tune the chatbot's behavior. These variables are crucial for personalizing and customizing the chatbot's responses. Here are the key configuration variables:

- **model:** Specifies the AI language model used.
- **starter_content:** Defines the chatbot's initial message.
- **default_domain_focus:** Sets the default topic of conversation.
- **domain_topics_string:** Lists recognized conversation domains.
- **domain_content:** Details the chatbot's knowledge and approach for each domain.

These settings allow you to tailor the chatbot's responses to specific topics and make it more engaging for users.

### API Secrets
The project uses an `mysecrets.py` file to store sensitive information like API keys. However, this file is not included in the repository for security reasons. To obtain an OpenAI API key for your project, follow these steps:

1. Visit the [OpenAI website](https://beta.openai.com/signup/).
2. Sign up for an OpenAI account or log in if you already have one.
3. Once logged in, navigate to the API section to generate an API key.
4. Copy the generated API key and paste it into your `mysecrets.py` file as follows:

```py
# mysecrets.py

OPENAI_API_KEY = "your-api-key-here"
```

Remember to keep your API key secure and do not share it in your repository for security purposes.

### OpenAI Chat Completion API

The Chatbot project leverages the OpenAI Chat Completions API to interact with the AI model (not to be confused with the earlier OpenAI Chat API). This API allows you to send a series of messages as input and receive a model-generated message as output. Messages are typically provided in an array format, with each message having a 'role' and 'content'.

Here's an example of the message format:

```json
'messages': [
    {'role': 'system', 'content': 'You are a digital assistant.'},
    {'role': 'user', 'content': 'Tell me about your classes.'},
    {'role': 'assistant', 'content': 'I teach various classes, including Game Design Practicum, Creative Coding, and more.'},
]
```

Interestingly, the OpenAI Chat Completions API operates in a stateless manner, meaning it doesn't have any memory of previous interactions or visits. This implies that if you want the large language model to consider specific parts of the conversation in its response, you must provide that context explicitly in the conversation. Each message in the conversation, including 'system', 'user', and 'assistant' messages, plays a role in guiding the AI's understanding and response.

The 'system' message helps set the behavior or role of the assistant, while 'user' messages are the queries or prompts from the user. The 'assistant' message contains the AI's responses.

For more details and examples, refer to the [OpenAI Chat Completions API documentation](https://platform.openai.com/docs/guides/gpt/chat-completions-api).

### Retrieval-Augmented Generation via OpenAI Functions
In intricate conversational AI structures, Retrieval-Augmented Generation (RAG) combines precise information retrieval and context-based response creation. This setup bridges the gap between relevant, creative conversation from the model and accurate, factual data from a database.

The OpenAI API enables developers to define "executable" functions for the model that we can use to trigger our RAG. We send a list of functions that should be considered by the model with each API call, like this example that the model will use to lookup a person who comes up for the first time in the conversation:

```json
{ 
    functions: { "name": "lookup_person",
        "description": "Get information about a person mentioned in the prompt for the first time.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the person to look up, e.g. Benzy, mom."
                }
            },
            "required": ["name"]
        } 
    } 
}
```

The model does not execute functions on the API side, but merely specifies (via JSON) which function and any arguments that should be executed by the system. This is an example response from the model:

```json
{
  "id": "chatcmpl-123",
  ...
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": null,
      "function_call": {
        "name": "lookup_person",
        "arguments": "{ \"name\": \"Wes\"}"
      }
    },
    "finish_reason": "function_call"
  }]
}
```

Our back-end system has a custom lookup class that retrieves information requested by the model, first checking an index for definitive names, then querying the lookup table for specific data. The integration of functions like lookup_person enriches the AI's abilities to retrieve tailored information. Here's an example of structured data returned (as a string) from the Lookup class:

```json
{
    # ...
    "art75": "{\n  \"name\": \"ART75\",\n  \"aka\": [\"ART 75\", \"Intro to Digital Video Art\"],\n  \"type\": \"class\",\n  \"characteristics\": {\n    \"university\": \"SJSU\",\n    \"duration\": \"2017-18\",\n    \"description\": \"ART75, also known as Intro to Digital Video Art, is a course at SJSU introducing fundamental skills, software, and techniques used in digital video production. The course explores critical discourse and contemporary art theories related to digital video art.\"\n  }\n}",
    # ...
}
```

To help the model handle lookup data smoothly, system messages guide the model, suggesting functions for information retrieval and preventing repetitive data. Extensive training refines the model's understanding of function utilization, enriching generated responses.

```json
{"messages": [
    {"role": "system", "content": "Functions are enabled. Use 'lookup_person' for people, 'lookup_class' for named classes, 'lookup_project' for projects, and 'lookup_topic' for topics. Only look up things you don't already know. Don't repeat lookup information -- use your own words to answer the prompt. If no information is returned from a function call, invent something relevant. Don't mention looking up information or a database. Be cool, man."}, 
    # ... 
]}
```

These implementations empower the AI to retrieve and skillfully utilize information, fostering contextually informed conversations.

## Installation & Deployment
1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your-username/wesbot.git
    ```

1. Change to the project directory:

    ```
    cd wesbot
    ```

1. Create a virtual environment and activate it (optional but recommended):

    ```
    python -m venv venv
    source venv/bin/activate
    ```

1. Install the required packages using pip:

    ```
    pip install -r requirements.txt 
    ```

1. Set up your OpenAI API key by exporting it as an environment variable in your shell. For example, if you're using bash:

    ```
    export OPENAI_API_KEY=your-api-key-here  
    ```

### Testing

1. Launch Flask in debug mode from the root of the app with:

    ```
    python app.py
    ```

1. Test the flask app in your web browser at `http://127.0.0.1:5000/`

1. End with CTRL-C

### Launching Locally

1. If that's working, you're ready to start the application with uWSGI:

    ```
    uwsgi --http 127.0.0.1:5000 --wsgi-file wsgi.py --callable app 
    ```

1. Access the chatbot locally in your web browser at `http://127.0.0.1:5000/`

### Deploying on server

I use Gandi web hosting, and so these instructions will be similar, but possibly different for you. 

1. Set up the git repo in the control panel

1. Push the repo to the server:

```
git push gandi
```

1. Clean and deploy the app:

```
ssh [your_login]@[your_server_domain] clean default.git
ssh [your_login]@[your_server_domain] deploy default.git
```

Your AI-powered instructor, is ready to answer your questions and provide guidance in the world of new media, art, and game design.

Enjoy your learning journey with WesBot!

## License

This software is licensed under a [GNU General Public License 3.0 license](./LICENSE.md). 