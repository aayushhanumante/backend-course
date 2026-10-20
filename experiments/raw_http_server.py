import socket

server = socket.create_server(("127.0.0.1", 8000), family=socket.AF_INET)

while True:
    serveOn = server.accept()
    clientMsg = serveOn[0].recv(1024).decode()

    requestLine = clientMsg.split("\r\n", 1)[0]
    requestParts = requestLine.split()
    body = "Request received".encode("utf-8")
    content_length = len(body)
    
    if len(requestParts) == 3:
        method, request_target, http_version = requestParts
        ResponseMsg = (
            f"HTTP/1.1 200 OK\r\n"
            f"Content-Length: {content_length}\r\n"
            f"Connection: close\r\n"
            f"\r\n"
            ).encode("utf-8") + body
        
        serveOn[0].sendall(ResponseMsg) 
        serveOn[0].close()
    else:
        error_body = b"Bad Request"
        error_response = (
            f"HTTP/1.1 400 Bad Request\r\n"
            f"Content-Length: {len(error_body)}\r\n"
            f"Connection: close\r\n"
            f"\r\n"
        ).encode("utf-8") + error_body

        serveOn[0].sendall(error_response)
        serveOn[0].close()