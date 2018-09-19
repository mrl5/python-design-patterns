# -*- coding: utf-8 -*-


class Handler:
    """Abstract Handler"""
    def __init__(self, successor):
        self._successor = successor # Define who is the next handler

    def handle(self, request):
            handled = self._handle(request) #If handled, stop here
            # Otherwise, keep going
            if not handled:
                self._successor.handle(request)    

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')


# Inherits from the abstract handler
class ConcreteHandler1(Handler):
    """Concrete handler 1"""
    def _handle(self, request):
        # Provide a condition for handling
        if 0 < request <= 10:
            print("Request {} handled in handler 1".format(request))
            # Indicates that the request has been handled
            return True


class DefaultHandler(Handler): # Inherits from the abstract handler
    """Default handler"""
    def _handle(self, request):
        """If there is no handler available"""
        #No condition checking since this is a default handler
        print("End of chain, no handler for {}".format(request))
        return True # Indicates that the request has been handled


# Using handlers
class Client:
    def __init__(self):
        # Create handlers and use them in a sequence you want
        # Note that the default handler has no successor
        self.handler = ConcreteHandler1(DefaultHandler(None))

    # Send your requests one at a time for handlers to handle
    def delegate(self, requests):
        for request in requests:
                self.handler.handle(request)


# Create a client
c = Client()

# Create requests
requests = [2, 5, 30]

# Send the requests
c.delegate(requests)
