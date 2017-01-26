import webapp2
import caesar
def build(content):
    header = "<h2>Enter your text:</h2>"
    message = "Enter your text..."
    rotation = "<input type='number' name='rotation'/>"
    textarea = "<textarea name='message'>" + content + "</textarea>"
    submit = "<input type='submit'/>"
    form = header + "<form method='post'>" + textarea + "<br>" + "Key:" + rotation + "<br>" + submit + "</form>"
    return form
    

class MainHandler(webapp2.RequestHandler):
    
    def get(self):
        form = build("")
        self.response.write(form)

    def post(self):
        message = self.request.get("message")
        key = int(self.request.get("rotation"))
        encryptedmessage = caesar.encrypt(message, 13)
        form = build(encryptedmessage)
        self.response.write(form)
        




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
