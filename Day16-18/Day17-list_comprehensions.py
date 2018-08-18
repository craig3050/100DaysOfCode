

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def reverse_names(names):
    for name in names:
        new_name = name.split()
        print(new_name[1] + " " + new_name[0])

def gen_name():
    for name in NAMES:
        yield name


new_names = [name.title() for name in NAMES]
print(new_names)
reverse_names(new_names)


pairs = gen_name()
for _ in range(10):
    print(f'{next(pairs)} teams up with {next(pairs)}')
