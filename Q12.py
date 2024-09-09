import time
def decorator(fx):
    def inner(*args):
        start=time.time()
        fx(*args)
        end=time.time()
        print(f"the function ran at {end -start}")
        return fx
    return inner
@decorator
def func(n):
    print("checking the time to execute")
    
func(2)