class MyListIterator:
    def __init__(self, head):
        self.myNode = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.myNode is None:
           raise StopIteration
        else: 
           data = self.myNode.data
           self.myNode = self.myNode.next
        return data