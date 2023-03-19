from timedef import timedef

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
@timedef
def show(value: int):
    result = fibonacci(value)
    print(f"result fibonacci:{result}")

show(1)
show(10)
show(20)