KOSTROVOK_FEE = 0.12 
BOOKKING_CONVERT_RATE = 75


    # BEGIN (write your solution here)
SERVICE_FEE = {
        'kostrovok': lambda cost: cost + cost * KOSTROVOK_FEE,
        'book-king': lambda cost: cost *  BOOKKING_CONVERT_RATE
}
CONFIG = {'min': -float('inf'), 'max': float('inf')}

def find_all_matching(data, predicates):
    predicates = CONFIG | predicates
    matching_hotels = []
    for service_data in data:
        service = service_data['service']
        for hotel in service_data['hotels']:
            _data = {}
            for k, v in hotel.items():
                if k == 'cost':
                    _data[k] = SERVICE_FEE.get(service, lambda x: x)(v)
                else:
                    _data[k] = v
            if predicates['max'] < _data['cost'] < predicates['min']:
                continue
            h_data = {'hotel': _data, 'service': service}
            matching_hotels.append(h_data)
    return matching_hotels
    # END 
