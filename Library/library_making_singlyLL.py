#Singly linked list

class node:
  def __init__(self,e,n):
   self.element=e
   self.next=n

class linkedlist:
  def __init__(self,a):
    self.head=None
    tail=None
    for i in a:
      newN=Node(i,None)
      if self.head==None:
        self.head=newN
        tail=newN
      tail.next=newN
      tail=newN

  def forwardPrint(self):
    head=self.head
    while head!=None:
      print(head.element)
      head=head.next

  def backwardPrint(self):
     head=self.head
     while head!=None:
       head=head.next
       print(head.element)

  def countNode(self):
      c=0
      head=self.head
      while head!=None:
        c+=1
        head=head.next
      return c

  def nodeAt(self,idx):
     if (idx<0) or (idx>self.countNode()):
      return None
     else:
      c=0
      head=self.head
      while head!=None:
       if c==idx:
        return head
       c=c+1
       head=head.next

  def get(self, idx):
    if (idx<0) or (idx>self.countNode()):
      return None
    else:
     c=0
    head = self.head
    while head!=None:
      if  c==idx:
        return head.element
      c+=1
      head = head.next
    return None

  def set(self, idx, elem):
    if (idx<0) or (idx>self.countNode()):
      return None
    else:
      c=0
      temp=0
      head=self.head
      while head!=None:
       if c==idx:
         temp=head.element
         head.element=elem
         return temp
       c=c+1
       head=head.next

  def indexOf(self, elem):
    c=0
    head=self.head
    while head!=None:
      if head.element==elem:
        return c
      c=c+1
      head=head.next
    return -1   #if elem doesn't exist in the list

  def contains(self, elem):
    c=0
    head=self.head
    temp=False
    while head!=None:
      if elem==head.element:
        return True
      c+=1
      head=head.next
    return False

  def copyList(self):
    copyL=Node(self.head.element, None)
    tail=copyL
    n=self.head.next
    while n!=None:
        newN=Node(n.element, None)
        tail.next=newN
        tail=newN
        n=n.next
    return copyL

  def reverseList(self):
    revH = Node(self.head.element,None)
    n=self.head.next
    while n!=None:
        newN=Node(n.element, None)
        newN.next=revH
        revH=newN
        n = n.next
    return revH

  def rotateLeft(self):
    temp=self.head
    self.head=self.head.next
    tail=self.head
    while tail.next!=None:
      tail=tail.next
    tail.next=temp
    temp.next=None

  def rotateRight(self):
    tail=self.head
    while tail.next.next!=None:
        tail=tail.next
    tail.next.next=self.head
    self.head=tail.next
    tail.next=None

  def insert(self, elem, idx):
    size= self.countNode()
    if idx==0:
      newN= Node(elem,self.head)
      self.head = newN
    elif 0<idx<=size:
      prev_node=self.nodeAt(idx-1)
      n= Node(elem,prev_node.next)
      prev_node.next=n
    else:
      print("Invalid Index")

  def remove(self, idx):
    n= self.countNode()
    if idx>n-1 or idx< 0:
        return None
    if idx==0:
        rmv= self.head.element
        self.head=self.head.next
        return rmv
    elif 1<=idx<n:
        tail=self.nodeAt(idx)
        prev = self.nodeAt(idx-1)
        rmv = prev.next.element
        prev.next = tail.next
        return rmv