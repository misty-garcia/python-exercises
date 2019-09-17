def keep_long_words(strings):
    '''
    >>> keep_long_words(['ls', 'codeup', 'code', 'pip', 'bayes'])
    ['codeup', 'bayes']
    >>> keep_long_words(['cd', 'ls', 'pwd'])
    []
    >>> keep_long_words(['python', 'algorithm'])
    ['python', 'algorithm']
    '''
    string_list = []
    for x in strings:
        if len(x) > 4:
            string_list.append(x)
    return string_list

def make_model(cars):
    '''
    >>> cars = []
    >>> cars.append({'make': 'Toyota', 'model': 'Camry'})
    >>> cars.append({'make': 'Honda', 'model': 'Accord'})
    >>> cars.append({'make': 'Ford', 'model': 'Fiesta'})
    >>> cars.append({'make': 'Ford', 'model': 'F-150'})
    >>> make_model(cars)
    ['Toyota Camry', 'Honda Accord', 'Ford Fiesta', 'Ford F-150']
    '''
    car_list= []
    for car in cars:
        car_list.append(car['make'] + ' ' + car['model'])
    return car_list

def extract_time_components(time):
    '''
    >>> extract_time_components('21:30:00')
    {'hours': 21, 'minutes': 30, 'seconds': 0}
    >>> extract_time_components('09:01:53')
    {'hours': 9, 'minutes': 1, 'seconds': 53}
    '''
    time_list = time.split(':')
    time_dict = {}
    time_dict['hours'] = int(time_list[0])
    time_dict['minutes']= int(time_list[1])
    time_dict['seconds'] = int(time_list[2])
    return time_dict
    





