# WesBot

## Description
We've kidnapped the university educator and artist, Wes Modes, digitized their brain, and placed them in a sophisticated, multi-layered recurrent neural network to provide you with a unique learning experience. WesBot is an AI-powered chatbot that brings Wes into the virtual realm where you can interact with them to get answers to your questions and guidance in the intricate world of new media, art, and game design. 

## Technology
- Python
- Flask
- OpenAI API
- uWSGI

## Installation
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



## Testing

1. Launch Flask in debug mode from the root of the app with:

    ```
    python app.py
    ```

1. Test the flask app in your web browser at `http://127.0.0.1:5000/`

1. End with CTRL-C

## Launching Locally

1. If that's working, you're ready to start the application with uWSGI:

    ```
    uwsgi --http 127.0.0.1:5000 --wsgi-file wsgi.py --callable app 
    ```

1. Access the chatbot locally in your web browser at `http://127.0.0.1:5000/`

## Deploying on server

I use Gandi web hosting, and so these instructions will be similar, but possibly different for you. 

1. Set up the git repo in the control panel

1. Push the repo to the server:

```
git push gandi
```

1. Clean and deploy the app:

```
ssh [your_login]@[your_server_domain] deploy default.git
ssh [your_login]@[your_server_domain] clean default.git
```

Your AI-powered instructor, is ready to answer your questions and provide guidance in the world of new media, art, and game design.

Enjoy your learning journey with WesBot!