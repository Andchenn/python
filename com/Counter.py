class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        # 返回下一个值直到当值大于high
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
