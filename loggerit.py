import logging
def logger():
    def decorator(func):
        def wrapper():
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
            logging.info(f"Function {func.__name__} is called ")
            func()
        return wrapper
    return decorator

def timeit():
    def decorator(func):
        def wrapper():
            import time
            start_time = time.time()
            result = func()
            end_time = time.time()
            logging.info(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute")
            return result
        return wrapper
    return decorator

def timeit2(number,repeat):
    def decorator(func):
        def wrapper():
            import timeit
            runs = timeit.repeat(func, number=number, repeat=repeat)
            logging.info(f"Function {func.__name__} took {sum(runs) / len(runs):.4f} seconds to execute")
        return wrapper
    return decorator