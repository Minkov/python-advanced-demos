class Set:
    def __init__(self):
        self.capacity = 8
        self.count = 0
        self.internal_values = [None] * self.capacity

    def get_index(self, value):
        return abs(hash(value)) % self.capacity

    def add(self, value):
        self.check_resize()
        index = self.get_index(value)
        if not self.internal_values[index]:
            self.internal_values[index] = []
        if value in self.internal_values[index]:
            return

        self.internal_values[index].append(value)
        print(self.internal_values)
        self.count += 1

    def contains(self, value):
        index = self.get_index(value)
        return self.internal_values[index] and value in self.internal_values[index]

    def check_resize(self):
        if self.count < self.capacity * 0.7:
            return

        old_values = self.internal_values
        self.capacity *= 2
        self.internal_values = [None] * self.capacity
        self.count = 0
        for internal_list in old_values:
            if internal_list is None:
                continue
            for x in internal_list:
                self.add(x)


ss = Set()

ss.add('pesho')
[ss.add(i) for i in range(100)]
