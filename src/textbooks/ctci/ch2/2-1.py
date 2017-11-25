"""

Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a templarary buffer is not allowed


"""


from linked_list import LinkedList








# O(n)
def remove_duplicates(linked_list):
    values_dict = {}
    current_node = linked_list.root
    prev_node = None
    while current_node:
        if current_node.value in values_dict:
            if prev_node:
                prev_node.next = current_node.next
        else:
            values_dict[current_node.value] = True
        prev_node = current_node
        current_node = current_node.next

    return linked_list


# O(n^2)
def remove_duplicates_without_ds(linked_list):
    current_node = linked_list.root
    prev_node = None

    while current_node:
        starting_node = current_node.next
        found = False
        while starting_node:
            if current_node.value == starting_node.value:
                found = True
            starting_node = starting_node.next
        if found:
            if prev_node:
                prev_node.next = current_node.next

        prev_node = current_node
        current_node = current_node.next

    return linked_list



def setup():
    values = [
        4, 8, 15, 16, 23, 42, 15, 32, 23, 56, 2
    ]
    linked_list = LinkedList()
    for value in values:
        linked_list.add(value)

    print(linked_list)
    print(remove_duplicates(linked_list))


def setup_ver2():
    print("Setup2-------------------------------\n")
    values = [
        4, 8, 15, 16, 23, 42, 15, 32, 23, 56, 2
    ]
    linked_list = LinkedList()
    for value in values:
        linked_list.add(value)

    print(linked_list)
    print(remove_duplicates_without_ds(linked_list))



if __name__ == "__main__":
    setup()
    setup_ver2()
