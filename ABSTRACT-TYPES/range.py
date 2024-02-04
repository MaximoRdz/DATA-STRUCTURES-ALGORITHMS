

class Range:

    def __init__(self, start, end, step=1):
        self.start = start         
        self.end = end
        self.step = step

    def iterable(self):
        current = self.start
        while current < self.end:
            yield current
            current += self.step

    def __len__(self):
        return (self.end - self.start + self.step - 1) // self.step
    
    def __getitem__(self, i: int):
        if not (0 <= i < len(self)):
            print("Index out of range.")
            return None
        return self.start + i * self.step
    
    def __str__(self):
        return ",".join(
            [str(i) for i in self.iterable()]
            )
    
    def sum(self):
        ans = 0
        for i in self.iterable():
            ans += i
        return ans


if __name__ == "__main__":
    r = Range(5, 10, 2)
    print(5, 10, 2)
    print("Length: ", len(r))

    print("i = 0: ", r[0])

    print("str: ", r)

    print("sum: ", r.sum())
    



