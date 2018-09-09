from functools import wraps


def make_html(element):
    def mydecorator(funct):
        @wraps(funct)
        def wrapper(*args, **kwargs):
            result = funct(*args, **kwargs)
            return f'<{element}>{result}</{element}>'
        return wrapper
    return mydecorator


@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text

print(get_text())