from wsgiref.simple_server import make_server

def aplicacao(environ, start_responsew):
    status = "200 OK"
    headers = [("Content-Type", "text/html;charset=utf-8'")]
    start_response(status, headers)
    return [b"<h1>Olá, Mundo!</h1>"]

make_server("", 5000, aplicacao)