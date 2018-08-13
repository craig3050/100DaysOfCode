cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    new_list = cars['Jeep']
    myString = ", ".join(new_list)
    return myString

    """return a comma separated string of jeep models (original order)"""
    pass


def get_first_model_each_manufacturer():
    myString = []
    for item in cars:
        myString.append((cars[item][0]))
    return myString

    """return a list of matching models (original ordering)"""
    pass


def get_all_matching_models(grep='trail'):
    myString = []
    for item in cars:
        for item2 in cars[item]:
            if grep in item2:
                print(item2)
                myString.append(item2)
            print(item2)
    print(myString)
    return myString

    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    pass


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    pass

get_all_jeeps()
get_first_model_each_manufacturer()
get_all_matching_models()
