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

```
# mysecrets.py

OPENAI_API_KEY = "your-api-key-here"
```

Remember to keep your API key secure and do not share it in your repository for security purposes.

### OpenAI Chat Completion API

The Chatbot project leverages the OpenAI Chat Completions API to interact with the AI model (not to be confused with the earlier OpenAI Chat API). This API allows you to send a series of messages as input and receive a model-generated message as output. Messages are typically provided in an array format, with each message having a 'role' and 'content'.

Here's an example of the message format:

```
'messages': [
    {'role': 'system', 'content': 'You are a digital assistant.'},
    {'role': 'user', 'content': 'Tell me about your classes.'},
    {'role': 'assistant', 'content': 'I teach various classes, including Game Design Practicum, Creative Coding, and more.'},
]
```

Interestingly, the OpenAI Chat Completions API operates in a stateless manner, meaning it doesn't have any memory of previous interactions or visits. This implies that if you want the large language model to consider specific parts of the conversation in its response, you must provide that context explicitly in the conversation. Each message in the conversation, including 'system', 'user', and 'assistant' messages, plays a role in guiding the AI's understanding and response.

The 'system' message helps set the behavior or role of the assistant, while 'user' messages are the queries or prompts from the user. The 'assistant' message contains the AI's responses.

For more details and examples, refer to the [OpenAI Chat Completions API documentation](https://platform.openai.com/docs/guides/gpt/chat-completions-api).

### System Role and Domain-Specific Text
In this implementation, we employ the 'system' role for two primary purposes. The default system message that accompanies every API call instructs the large language model to flag responses when certain topics are mentioned. This flag "[[*topic*]]" corresponds to keys in the `domain_content` dictionary in the config, and is restricted by the values in `domain_topics_string`.

```
domain_topics_string = '"classes", "art", "research", or "community organizing". Any other topics should be flagged "other interests".'

domain_content = {
    "common": f"""
        Whenever the user touches on any of the topics in the following list, flag your response at the beginning with [[topic]] where topic is restricted to one of the following in-depth domains: {domain_topics_string}...

        Pretend you are Wes Modes, an artist and university instructor teaching new media, art, and game design...
    """

    "classes": """
        As a teacher, you are always interested in blurring the lines between teacher and learner....
    """
    # ...
```

When the API responds, the AI model includes "[[*topic*]]" as appropriate. The JavaScript code responsible for handling the response filters out the tag and sets a `domainFocus` variable for subsequent interactions.

On the next user input, the specific text associated with the domain is appended to the default system message. This provides domain-specific information, allowing it to provide contextually relevant responses aligned with the user's intended topic of discussion.

This approach enables the chatbot to engage in meaningful and domain-specific conversations, ensuring that the AI's responses are both accurate and contextually appropriate. Additionally, it helps reduce the size of the system message necessary to operate within OpenAI's token limits, enhancing the efficiency and effectiveness of the chatbot's interactions.

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
