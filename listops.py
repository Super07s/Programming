my_list = [12, 45, 7, 34, 89, 23, 56, 78, 10, 67]

def print_list():
    print("List:", my_list)


def print_sum():
    print("Sum of all elements:", sum(my_list))

def print_largest():
    print("Largest element:", max(my_list))

def print_reverse():
    print("List in reverse order:", my_list[::-1])

def print_smallest():
    print("Smallest element:", min(my_list))

print_list()
print_sum()
print_largest()
print_reverse()
print_smallest()
