import json
import requests
from http.server import BaseHTTPRequestHandler , HTTPServer

class DogApiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/api/dog':
            dog_api_url="https://dog.ceo/api/breeds/image/random"
            response=requests.get(dog_api_url).json()
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.send_header("Access-Control-Allow-Origin","*")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"not found")
            
def run(server_class=HTTPServer,handler_class=DogApiHandler,port=5000):
    server_address=("",port)
    httpd=server_class(server_address,handler_class)
    print(f"This is a dog api for my frontend at http://localhost:{port}")
    httpd.serve_forever()
    
if __name__=="__main__":
    run()