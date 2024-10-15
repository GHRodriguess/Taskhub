class Session():
    def __init__(self, request):
        self.session = request.session

    def set(self, message, status):        
        self.session['message'] = message
        self.session['status'] = status
        self.session['updated'] = True

    def get(self):        
        message = self.session.pop('message', None)
        status = self.session.pop('status', None)
        self.session['updated'] = False
        return message, status

    def has_message(self):        
        return self.session.get('updated', False)