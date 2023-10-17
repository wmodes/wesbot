# app.py
# This file is the entry point for the Chatbot app.

# It creates the Chatbot app using the factory function in the `factory.py` file.
# It then starts the Flask app.

from factory import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)