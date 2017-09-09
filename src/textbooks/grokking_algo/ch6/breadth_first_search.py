from collections import deque



def search(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = searchqueue.popleft()
        if not person in searched:
            if person_is_seller(person):
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
