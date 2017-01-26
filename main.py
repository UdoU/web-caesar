import webapp2
import caesar

class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = "Hellooo World!"
        encryptedmessage = caesar.encrypt(message, 13)
        self.response.write(encryptedmessage)

class EncryptHandler(webapp2.RequestHandler):
    def get(self):
        message = "Hellooo World!"
        encryptedmessage = caesar.encrypt(message, 13)
        self.response.write(encryptedmessage)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/encrypt', EncryptHandler)
], debug=True)
