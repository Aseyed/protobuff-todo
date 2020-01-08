# %%
from todo import todo_pb2
from twisted.web import server
from twisted.web.resource import Resource
from twisted.web.static import File
from twisted.internet import reactor, endpoints


# %%
class Listener(Resource):
    isLeaf = True

    @staticmethod
    def render_GET(request):
        task = todo_pb2.Task()
        task.text = 'Hello There!'
        task.done = True
        return task.SerializeToString()


# %%
if __name__ == "__main__":
    site = server.Site(Task())
    server = endpoints.serverFromString(
        reactor,
        # "ssl:port=5000:privateKey=key.pem:certKey=cert.pem",
        "tcp:5000",
    )
    server.listen(site)
    reactor.run()

# %%

