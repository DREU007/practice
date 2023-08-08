from gateway import find_all_matching


def find_the_cheapest_service(data, predicates=None): 
    # BEGIN (write your solution here) 
        matches = find_all_matching(data, predicates)
        return list(filter(lambda item: item['hotel']['cost'], matches))[0]
    # END
