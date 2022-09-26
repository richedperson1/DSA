class mapNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None


class map:
    def __init__(self) -> None:
        self.bucketSize = 5
        self.buckets = [None for i in range(self.bucketSize)]
        self.counts = 0

    def size(self):
        return self.counts

    def getHashCode(self, code):
        return abs(code) % self.bucketSize

    def rehashe(self):
        temp = self.buckets
        self.buckets = [None for i in range(self.bucketSize*2)]
        self.bucketSize = self.bucketSize*2
        self.counts = 0
        for head in temp:
            while head:
                self.insertData(head.key, head.val)
                head = head.next

    def getLoadFactorValue(self):
        return self.counts/self.bucketSize

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
        loadFactor = self.counts/self.bucketSize
        if loadFactor >= 0.7:
            self.rehashe()

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

    def deleteKey(self, key):
        hc = hash(key)
        index = self.getHashCode(hc)
        if self.buckets[index] == None:
            return "Index not founds"
        elif self.buckets[index].key == key:
            items = self.buckets[index]
            self.buckets[index] = self.buckets[index].next
            self.counts -= 1
            return items.key
        prev = None
        curr = self.buckets[index]
        head = curr
        while curr:
            if curr.key == key:
                prev.next = curr.next
                self.counts -= 1
                return curr.key
            prev = curr
            curr = curr.next
        self.buckets[index] = head
