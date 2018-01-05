simple_graph = {}
simple_graph['you'] = ['Alice', 'Bob', 'Claire']
# print(simple_graph)


simple_graph2 = {}
simple_graph2['you'] = ['Alice', 'Bob', 'Claire']
simple_graph2['Bob'] = ['Anuj', 'Peggy']
simple_graph2['Alice'] = ['Peggy']
simple_graph2['Peggy'] = []
# print(simple_graph2)


from collections import deque
search_queue = deque()
search_queue += simple_graph2['you']
searched = []


def person_is_seller(name):
    return name[-1] == 'm'


while search_queue:
    person = search_queue.popleft()
    if not person in searched:
        if person_is_seller(person):
            print("{} is sellor".format(person))
            return True
        else:
            if simple_graph2.get(person):
                search_queue += simple_graph2[person]
                searched.append(person)
print('could not find any seller.sorry')
return False
