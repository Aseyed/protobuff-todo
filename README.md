# python-toto
#### This is a todo app with python language based on gRPC protocol and twisted framework

## pre-requirements
* make a virtual env
    * `virtualenv venv`
* install requirements from requirements file
    * `pip install -r requirements.txt`
* make sure `protoc` is installed

## run the program
* make proto file in python
    * if you changed the todo.proto file do these; else jump to next level      
    * `cd todo`
    * `protoc -I . todo.proto --python_out=plugins=grpc:.`
* run server
    * `cd server` 
    * `python app.py`
* run client
    * `cd client`
    * `python client.py`s