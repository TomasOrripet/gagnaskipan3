
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
        
    def get_value(self): # tes
        return self.data

    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    
    def setData(self,newdata):
        self.data=newdata
        
    def move_to_next(self,newnext):
        self.next=newnext
    
    def move_to_prev(self,newprev):
        self.prev=newprev
    
class LinkedList:
    def __init__(self,node):
        self.head=node
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            if cur_node.next==None:
                self.tail=cur_node

  
    def first(self):
        return self.head
    
    def last(self):
        return self.tail    
        
    def before(self,p):
        return p.prev
        
    def after(self,p):
        return p.next  
        
    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
    
    def __len__(self):
        cur_node=self.head
        counter=1
        while cur_node.next !=None:
            counter+=1
            cur_node=cur_node.next   
        return counter  
    
    
    def __str__(self):
        result = "["
        node = self.head
        if node != None:
            result += str(node.data)
            node = node.next
            while node:
                result += ", " + str(node.data)
                node = node.next
        result += "]"
        return result    
        
    def insertAfter(self,p,v):
        v.prev=p
        v.next=p.next
        (p.next).prev=v
        p.next=v
        return v
    
    def insertBefore(self,p,v):
        v.next=p
        v.prev=p.prev
        (p.prev).next=v
        p.prev=v
        return v
        
    def remove(self,p):
        t=p.data
        (p.prev).next=p.next
        (p.next).prev=p.prev
        return t


if __name__ == "__main__":
    #create tests here if you want
    A=Node(1)
    B=Node(2)
    C=Node(3)
    D=Node(4)
    E=Node(5)
    A.move_to_next(B)
    B.move_to_prev(A)
    B.move_to_next(C)
    C.move_to_prev(B)
    L=LinkedList(A)
    L.insertAfter(B,D)
    L.insertBefore(B,E)
    L.remove(B)
    print(L)
    print(A.get_value())
    print(len(L))
        
