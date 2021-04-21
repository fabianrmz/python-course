from LinkedList import LinkedList, Node

def __main__():

    print("Test linked list")

    myList = LinkedList()
    myList.add(5)
    myList.add(35)
    myList.add(45)
    myList.add(4)
    myList.print_list()

    print('size =', str(myList.size))
    myList.remove(35)
    myList.print_list()
    print(myList.find(25))
    print(myList.find(5))
    print('size =', str(myList.size))

    print('Root:', myList.root)


__main__()
