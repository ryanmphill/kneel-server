import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_metals, get_all_sizes, get_all_styles, get_all_orders, get_all_types
from views import get_single_metal, get_single_order, get_single_size, get_single_style
from views import create_order, get_single_type, delete_order, update_order

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    # Here's a method that takes the path of the request as an input.
    # It returns a tuple with the resource and id
    def parse_url(self, path):
        """Split the path into the resource and the id"""
        # Just like splitting a string in JavaScript. If the
        # path is "/metals/1", the resulting list will
        # have "" at index 0, "metals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

    def do_GET(self):
        """Handles GET requests to the server """

        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "metals":
            if id is not None:
                single_metal = get_single_metal(id)
                if single_metal is not None:
                    self._set_headers(200)
                    response = single_metal
                else:
                    self._set_headers(404)
            else:
                self._set_headers(200)
                response = get_all_metals()

        elif resource == "sizes":
            if id is not None:
                single_size = get_single_size(id)
                if single_size is not None:
                    self._set_headers(200)
                    response = single_size
                else:
                    self._set_headers(404)
            else:
                self._set_headers(200)
                response = get_all_sizes()

        elif resource == "styles":
            if id is not None:
                single_style = get_single_style(id)
                if single_style is not None:
                    self._set_headers(200)
                    response = single_style
                else:
                    self._set_headers(404)
            else:
                self._set_headers(200)
                response = get_all_styles()

        elif resource == "orders":
            if id is not None:
                single_order = get_single_order(id)
                if single_order is not None:
                    self._set_headers(200)
                    response = single_order
                else:
                    self._set_headers(404)
            else:
                self._set_headers(200)
                response = get_all_orders()

        elif resource == "types":
            if id is not None:
                single_type = get_single_type(id)
                if single_type is not None:
                    self._set_headers(200)
                    response = single_type
                else:
                    self._set_headers(404)
            else:
                self._set_headers(200)
                response = get_all_types()

        else:
            self._set_headers(404)
            response = "Invalid resource requested"

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server """

        content_len = int(self.headers.get('content-length', 0))

        # Convert JSON string to a Python dictionary
        post_body = json.loads(self.rfile.read(content_len))

        # Parse the URL
        (resource, _) = self.parse_url(self.path)

        # Initialize new item to post
        new_post = None
        response = {}

        if resource == "orders":
            new_post = create_order(post_body)
            self._set_headers(201)
            response = new_post
        else:
            self._set_headers(403)
            response = "POST operations only supported for orders"

        self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):
        """Handle put requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Update a single order in the list
        if resource == "orders":
            try_update = update_order(id, post_body)
            if try_update == "success":
                self._set_headers(204)
            else:
                self._set_headers(404)
        else:
            self._set_headers(403)

        # Empty response
        self.wfile.write("".encode())

    def do_DELETE(self):
        """Handle a DELETE request"""

        # Parse the URL
        (resource, id) = self.parse_url(self.path)


        # Delete a single order from the list
        if resource == "orders":
            try_delete = delete_order(id)
            if try_delete == "success":
                # Set a 204 response code
                self._set_headers(204)
            else:
                self._set_headers(404)
        # Encode empty response
        self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()



# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
