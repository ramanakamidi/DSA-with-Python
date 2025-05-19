class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def traverse(self):
        if self.head==None:
            print("Linkedlist is empty")
            return 
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("Null")
    def insertbeg(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
        
    def insertend(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
    
    def insert_bef_speci(self,value,specifiedValue):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            return
        temp=self.head
        if self.head.data==specifiedValue:
            new_node.next=self.head
            self.head=new_node
            return 
        prev=None
        while temp.data!=specifiedValue and temp!=None:
            prev=temp
            temp=temp.next
        if temp is None:
            print(f"Error: {specifiedValue} not found in the list.")
            return
        new_node.next=temp
        prev.next=new_node
            
    def insert_aft_speci(self,value,specifiedValue):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            return
        temp=self.head
        if self.head.data==specifiedValue:
            new_node.next=self.head.next
            self.head.next=new_node
            return
        while temp!=None and temp.data!=specifiedValue:
            temp=temp.next
        if temp is None:
            print(f"Error: {specifiedValue} not found in the list.")
            return
        new_node.next=temp.next
        temp.next=new_node
        
               
       
        
        
ob1=Linkedlist()
ob1.insertbeg(3)
ob1.insertend(0)
ob1.insertbeg(8)
ob1.insertend(7)
ob1.insert_bef_speci(19,8)
ob1.insert_aft_speci(20,90)
ob1.traverse()
value=0
while value!=-1:
    value=int(input("enter value : "))
    if value == -1:
        break
    ob1.insertend(value)
ob1.traverse()