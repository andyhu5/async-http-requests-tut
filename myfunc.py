import loggerit

@loggerit.logger()
def foo():
    print("Hello, world!")

@loggerit.timeit()
@loggerit.logger()
@loggerit.timeit2(1, 5)
def bar():
    import time
    time.sleep(2)
    print("Goodbye, world!")    
    
if __name__ == "__main__":
    foo()
    bar()
    