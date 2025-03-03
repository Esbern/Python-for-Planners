'''
to run this server. 
open codespace
click termonal
type cd project_example/ toi change to the esampel folder
type pip install flask to install the flask web module
type  python web_app.py to start the app
'''
from flask import Flask

app = Flask(__name__)

def generate_output():
    result = ""  # Create an empty string to store the output
    for i in range(2, 11, 3):
        result += f"{i}\n"  # Append each number followed by a newline
    return result

@app.route('/')
def home():
    output = generate_output().replace("\n", "<br>")  # Format for HTML
    return f"<h1>Loop Output</h1><p>{output}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
