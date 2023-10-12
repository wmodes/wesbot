from flask import Flask

app = Flask(__name__)

class Chatbot:
    def __init__(self):
        self.variable = None  # Initialize the variable

    def set_variable(self, value):
        self.variable = value

    def get_variable(self):
        return self.variable

chatbot = Chatbot()

@app.route('/set_variable/<value>')
def set_variable(value):
    chatbot.set_variable(value)
    return 'Variable set to ' + value

@app.route('/get_variable')
def get_variable():
    variable_value = chatbot.get_variable()
    return 'Variable value: ' + variable_value

if __name__ == '__main__':
    app.run(debug=True)
