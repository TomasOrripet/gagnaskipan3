
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.pos = 0
        return

    def insert(self, data):
        new_node = Node(data)
        if self.pos == 0:
            if self.head == None:
                self.head = new_node
                return
            elif self.head.next == None:
                self.head.next = self.head
                self.tail = self.head
                self.tail.next = None
                self.head = new_node
                new_node.next = self.tail
                return
        
            new_node.next = self.head
            self.head = new_node

        elif (self.pos == 1):
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:    
            temp = self.head
            for i in range(1, self.pos):
                if(temp != None):
                    temp = temp.next   
            if temp != None:
                new_node.next = temp.next
                new_node.prev = temp
                temp.next = new_node  
                if (new_node.next != None):
                    new_node.next.prev = new_node        
        return 


        

    def remove(self):
        t= self.head.data
        (self.head.prev).next=self.head.next
        (self.head.next).prev=self.head.prev
        return t

    def get_value(self):
        if self.pos == 0:
            value = self.head
        elif self.pos == 1:
            value = self.head.next
        else:
            temphead = self.head
            for i in range(0, self.pos):
                if temphead != None:
                    temphead = temphead.next
            value = temphead
            
        if value == None:
            return None
        else:     
            return value.data

    def move_to_next(self):
        self.pos += 1
        return

    def move_to_prev(self):
        self.pos -= 1
        
        return

    def move_to_pos(self, pos):
        for i in range(0,pos):
            self.head = self.head.next
        node = self.head.data
        return node

    def clear(self):
        pass

    def get_first_node(self):
        return self.head

    def get_last_node(self):
        pass

    def partition(self, low, high):
        pass

    def sort(self):
        pass

    def __len__(self):
        cur_node=self.head
        counter=1
        if cur_node == None:
            return 0
        else:
            while cur_node.next !=None:
                counter+=1
                cur_node=cur_node.next   
            return counter

    def __str__(self):
        string = ""
        node = self.head
        while node != None:
            string += str(node.data) + " "
            node = node.next
        return string

if __name__ == "__main__":
    #create tests here if you want
    dll = DLL()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("D")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("E")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("1")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("2")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("3")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("4")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("VALUE")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(8)
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
