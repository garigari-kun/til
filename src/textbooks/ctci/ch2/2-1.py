"""

Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a templarary buffer is not allowed


"""


from linked_list import LinkedList





def setup():
    values = [
        4, 8, 15, 16, 23, 42, 15, 32, 23, 56, 2
    ]
    linked_list = LinkedList()
    for value in values:
        linked_list.add(value)

    print(linked_list)
    remove_duplicates(linked_list)



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

    return linked_List

if __name__ == "__main__":
    setup()
