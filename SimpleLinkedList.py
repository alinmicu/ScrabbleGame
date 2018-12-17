from Node import Node

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def search2(self,data):
        current = self.head
        i = 0
        while current.get_data()!=data:
            current = current.get_next()
            i+=1
        if (current is None):
            return -1
        return i

    def swap(self,pos1,pos2):
        i = 0
        current = self.head
        while i < pos1:
            current = current.get_next()
            i+=1
        current2 = self.head
        i = 0
        while i < pos2:
            current2 = current2.get_next()
            i+=1
        aux = current.get_data()
        current.set_data(current2.get_data())
        current2.set_data(aux)
        print("aici")

    def remove(self,data):
        a = self.search2(data)
        self.deletepos(a)

    def get_lenght(self):
        i = 0
        current = self.head
        while current is not None:
            current = current.get_next()
            i+=1
        return i

    def deletepos(self, position):

        if self.head == None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.get_next()
            temp = None
            return
        for i in range(position - 1):
            temp = temp.get_next()
            if temp is None:
                break
                if temp is None:
                    return
        if temp.get_next() is None:
            return
        next = temp.get_next().get_next()
        #temp.next = None
        temp.next = next

    def insertpos(self, data, position):
        if (position == 0):
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
        else:
            current = self.head
            count = 0
            while (current != None):
                if (count == position - 2):
                    break
                else:
                    count += 1
                    current = current.get_next()
            newnode = Node(data)
            newnode.next = current.get_next()
            current.set_next(newnode)

    def convert_to_arr(self):
        array = []
        current = self.head
        while current is not None:
            array.append(current.get_data())
            current = current.get_next()
        #print(array)
        return array