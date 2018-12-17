from SimpleLinkedList import LinkedList
class Rack:

    def __init__(self, bag):
        self.rack = LinkedList()
        self.bag = bag
        self.initialize()

    def get_lenght(self):
        i = 0
        current = self.rack.head
        while current != None:
            i+=1
            current = current.get_next()
        return i

    def add_to_rack(self):
        self.rack.insert(self.bag.take_from_bag())

    def initialize(self):
        for i in range(7):
            self.add_to_rack()

    def get_rack_str(self):
        rack1 = self.rack.convert_to_arr()
        return ", ".join(str(item.get_letter()) for item in rack1)

    def get_rack_arr(self):
        rack1 = []
        rack1 = self.rack.convert_to_arr()
        return rack1

    def remove_from_rack(self, tile):
        self.rack.remove(tile)

    def get_rack_length(self):
        return len(self.rack)

    def replenish_rack(self):
        while self.get_lenght() < 7 and self.bag.get_remaining_tiles() > 0:
            self.add_to_rack()