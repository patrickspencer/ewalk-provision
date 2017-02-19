import fabric

def host_type():
    print(fabric.api.run('uname -s'))

def hello():
    print("Hello world!")
