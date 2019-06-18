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
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px 0;
                height: 120px 0;
            }}
        </style>
    </head>
    <body>
        <h2>Web Caesar</h2>

        <form method='post'>
            <label>Rotate by:</label>
            <input type='number' name='rotation'/>
            <br>

            <label>Type a message:</label>
            <textarea name='message'>{0}</textarea>
            <br>

            <input type='submit'/>
        </form>
    </body>
</html>
"""

def build_page(textarea_content):
    return header + form

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def post():
    message = request.form["message"]
    rotation = int(request.form["rotation"])
    encrypted_message = rotate_string(message, rotation)
    escaped_message = cgi.escape(encrypted_message)
    return form.format(escaped_message)

app.run()