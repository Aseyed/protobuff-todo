from todo import todo_pb2
from hyper import HTTPConnection

conn = HTTPConnection(host='localhost', port=5000)
conn.request('GET', '/')
res = conn.get_response()

task = todo_pb2.Task()
data = task.ParseFromString(res.read())

print(f"task text: {task.text}")
print(f"task text: {task.done}")
