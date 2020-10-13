class node:
    def __init__(self, value):
        self.val = value
        self.next = None

class linkedList:
    def __init__(self):
        self.head = node(None)

    def push(self, value):
        itr = self.head
        if self.head.val == None:
            self.head.val = value
            return
        while itr.next != None:
            itr = itr.next
        else:
            new_node = node(value)
            itr.next = new_node
    
    def delete(self, node_value):
        if self.head == None:
            print("empty list cant delete")
            return
        itr = self.head
        previous = None
        if itr.val == node_value:
            head_pointer = self.head
            self.head = self.head.next
            del head_pointer
            return
        while itr != None:
            if itr.val != node_value:
                print(itr.val,node_value)
                previous = itr
            else:
                previous.next = itr.next
                del itr
                return
            if itr.next == None:
                print("Node not found {}".format(node_value))
                return
            itr = itr.next

    def traverse(self, node):
        if self.head == None:
            print("Linked List is emplty cant traverse")
            return
        if node == None:
            print()
            return
        else:
            print(node.val,end=" ")
            self.traverse(node.next)
    def middle_node(self):
        slow_ptr = self.head
        fast_ptr = self.head
        if slow_ptr==None:
            print("list is empty cant find middle")
            return
        while fast_ptr != None and fast_ptr.next != None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        print(slow_ptr.val)# if slow_ptr !=None else "list is empty cant find middle")

if __name__ == "__main__":
    linked_list = linkedList()
    list = list(input("Enter list: ")) #list = [1,'e','{',3,4,5,'7']
    for itr in list:
        linked_list.push(itr)

    linked_list.traverse(linked_list.head)
    linked_list.middle_node()
    linked_list.delete('1')
    linked_list.delete('3')
    linked_list.delete('4')
    linked_list.middle_node()
    linked_list.traverse(linked_list.head)

    # itr = linked_list.head
    # head_deleted = True
    # linked_list.delete('z')
    # while itr.next != None:
    #     if itr == linked_list.head and head_deleted:
    #         linked_list.delete(itr.val)
    #         head_deleted = False
    #     itr = itr.next
    # else:
    #     if itr != None:
    #         linked_list.delete(itr.val)