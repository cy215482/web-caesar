from caesar import rotate_string
from flask import Flask, request
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px 0;
                height: 120px 0;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
    </body>
</html>
"""

def build_page(textarea_content):
    rot_label = "<label>Rotate by:</label>"
    rotation_input = "<input type='number' name='rotation'/>"

    message_label = "<label>Type a message:</label>"
    textarea = "<textarea name='message'>" + textarea_content + "</textarea>"

    submit = "<input type='submit'/>"
    form = ("<form method='post'>" +
        rot_label + rotation_input + "<br>" + message_label + textarea + "<br>" + submit + "</form>")

    header = "<h2>Web Caesar</h2>"

    return header + form

@app.route("/")
def index():
    return build_page("")

@app.route("/", methods=['POST'])
def post():
    message = request.form["message"]
    rotation = int(request.form["rotation"])
    encrypted_message = rotate_string(message, rotation)
    escaped_message = cgi.escape(encrypted_message)
    content = build_page(escaped_message)
    return (content)

app.run()