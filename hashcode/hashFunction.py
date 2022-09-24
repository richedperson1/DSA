class mapNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None


class map:
    def __init__(self) -> None:
        self.bucketSize = 20
        self.buckets = [None for i in range(self.bucketSize)]
        self.counts = 0

    def size(self):
        return self.counts

    def getHashCode(self, code):
        return abs(code) % self.bucketSize

    def insertData(self, key, val, functionCode=None):
        if functionCode != None:
            index = functionCode
        else:
            hc = hash(key)
            index = self.getHashCode(hc)
        curr = self.buckets[index]
        head = curr
        while head != None:
            if head.key == key:
                head.val = val
                return
            head = head.next
        newNode = mapNode(key, val)
        newNode.next = curr
        self.buckets[index] = newNode
        self.counts += 1

    def search(self, key):
        hc = hash(key)
        index = self.getHashCode(hc)

        if self.buckets[index]:
            head = self.buckets[index]
            curr = head
            while curr:
                if curr.key == key:
                    return curr.val
                curr = curr.next
            return "Not preset"
        return "Not present"
