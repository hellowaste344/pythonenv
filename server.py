import falcon.asgi

app = falcon.asgi.App()

class Site:
    async def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.text = "Greetings!"
    async def on_post(self, req, resp):
        resp.status = falcon.HTTP_401
        resp.text = "You are not authenticated"

app.add_route("/home", Site())
app.add_route("/blog", Site())

# gunicorn server:app
# uvicorn server:app