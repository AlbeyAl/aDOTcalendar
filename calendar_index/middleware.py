
class CalendarMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

        # __init__ called once at the beginning of web server.

    def __call__(self, request):
        path = request.path_info
        print("The path is: " + path)
        # query all events/to-dos for date requested, if authenticated.
        response = self.get_response(request)
        # code to execute on response

        return response