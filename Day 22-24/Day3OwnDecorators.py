from functools import wraps



def add_text(element):
    def mydecorator(funct):
        @wraps(funct)
        def wrapper(*args, **kwargs):
            print(args)
            print(kwargs)
            result = funct(*args, **kwargs)
            return f'<{element}>{result}</{element}>'
        return wrapper
    return mydecorator


@add_text('start')
@add_text('end')
def get_text(number, text):
    number += 1
    return number, text

print(get_text(22, text='This is the existing filename'))