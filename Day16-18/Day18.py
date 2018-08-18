NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):

    new_name_list = [name.title() for name in names]
    new_name_list = list(set(new_name_list))

    return new_name_list


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    output_name = []
    for name in names:
        new_name = name.split()
        output_name.append(new_name[1] + " " + new_name[0])
    output_name2 = []
    for name in sorted(output_name, reverse=True):
        new_name = name.split()
        output_name2.append(new_name[1] + " " + new_name[0])
    return output_name2


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    first_names = [name.split()[0].title() for name in names]
    return_names = sorted(first_names, key=len)
    return return_names[0]

print(dedup_and_title_case_names(NAMES))
print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))

#Solution
#
# NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
#          'julian sequeira', 'sandra bullock', 'keanu reeves',
#          'julbob pybites', 'bob belderbos', 'julian sequeira',
#          'al pacino', 'brad pitt', 'matt damon', 'brad pitt']
#
#
# def dedup_and_title_case_names(names):
#     """Should return a list of names, each name appears only once"""
#     return list({name.title() for name in names})
#
#
# def sort_by_surname_desc(names):
#     """Returns names list sorted desc by surname"""
#     names = dedup_and_title_case_names(names)
#     return sorted(names,
#                   key=lambda x: x.split()[-1],
#                   reverse=True)
#
#
# def shortest_first_name(names):
#     """Returns the shortest first name (str)"""
#     names = dedup_and_title_case_names(names)
#     names = [name.split()[0] for name in names]
#     return min(names, key=len)