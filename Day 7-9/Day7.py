cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    new_word = ""
    for items in cars['Jeep']:
        new_word += items
        new_word += ", "
    print(new_word)
    return new_word

    """return a comma separated string of jeep models (original order)"""
    pass


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    pass


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    pass


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    pass

get_all_jeeps()

