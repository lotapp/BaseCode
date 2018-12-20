def application(env, start_response):
    print(env["PATH_INFO"])
    start_response("200 OK", [("Content-Type", "text/html")])
    return [f"<h1>Hello, {env["PATH_INFO"][1:] or "web"}!</h1>".encode("utf-8")]