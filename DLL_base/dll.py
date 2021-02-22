
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
        if self.head == None:
            return
        
        temp = self.head
        if self.pos == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(self.pos - 1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None:
            return
        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next

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
        if self.pos == self.__len__():
            return
        else:
            self.pos += 1
        return

    def move_to_prev(self):
        if self.pos == 0:
            return
        else:
            self.pos -= 1
        return

    def move_to_pos(self, pos):
        if pos < 0 or pos > self.__len__():
            return
        else:
            self.pos = pos
        return

    def clear(self):
        if self.head == None:
            return
        elif self.head.next == None:
            self.head = None
            return
        else:
            while self.head.next != None:
                self.head = self.head.next
        self.head = None
        return

    def get_first_node(self):
        return self.head

    def get_last_node(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            return self.head
        else:
            temphead = self.head
            while temphead.next != None:
                temphead = temphead.next
            return temphead

    def partition(self, low, high):
        pivot = high
        i = low.prev
        ptr = low
        while ptr != high:
            if ptr.data <= pivot.data:
                i = low if i == None else i.next
                i.data, ptr.data = ptr.data, i.data
            ptr = ptr.next
        i = low if i == None else i.next
        i.data, pivot.data = pivot.data, i.data
        return i

    def sort(self):
        if(self.head == None):  
            return;  
        else:  
            #Current will point to head  
            current = self.head  
            while(current.next != None):  
                #Index will point to node next to current  
                index = current.next;  
                while(index != None):  
                    #If current's data is greater than index's data, swap the data of current and index  
                    if(current.data > index.data):  
                        temp = current.data;  
                        current.data = index.data;  
                        index.data = temp;  
                    index = index.next  
                current = current.next

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
    dll.insert("B1")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B2")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.partition(dll.get_first_node(), dll.get_last_node())
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.partition(dll.get_first_node(), dll.get_last_node())
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    
    """
    result = dll.get_first_node()
    if result != None:
        result = result.data
    print("first node: ", str(result))
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B3")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    result = dll.get_last_node()
    if result != None:
        result = result.data
    print("last node: ", str(result))
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    """