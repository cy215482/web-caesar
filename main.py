from caesar import rotate_string
from flask import Flask, request
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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.rotate_character(message, rotation)
        escaped_message = cgi.escape(encrypted_message)
        content = build_page(escaped_message)
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

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
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
    </body>
</html>