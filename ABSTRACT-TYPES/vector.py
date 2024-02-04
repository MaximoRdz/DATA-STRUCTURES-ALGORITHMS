import math


class Vector:
    """Multidimensional vector data structure."""

    def __init__(self, dim: int) -> None:
        self.dim = dim
        self.coordinates = [0 for _ in range(dim)]
    
    def __len__(self):
        return self.dim
    
    def __str__(self):
        return "(" + ",".join([str(c) for c in self.coordinates]) + ")"
    
    def __getitem__(self, i: int):
        return self.coordinates[i]
    
    def __setitem__(self, i: int, value):
        self.coordinates[i] = value

    def __add__(self, other):
        return [a+b for a, b in zip(self.coordinates, other.coordinates)]
    
    def __eq__(self, other):
        return all(a==b for a, b in zip(self.coordinates, other.coordinates))
    
    def dot(self, other):
        return sum([a*b for a, b in zip(self.coordinates, other.coordinates)])
    
    def cosine_distance(self, other):
        dot_product = self.dot(other)
        self_mod = math.sqrt(self.dot(self))
        other_mod = math.sqrt(other.dot(other))

        return dot_product / (self_mod * other_mod)


if __name__ == "__main__":
    myvector = Vector(3)
    myvector[0] = 2
    myvector[1] = 3
    myvector[2] = 7

    print(myvector)
    print("Length: ", len(myvector))
    print("Item 2: ", myvector[2])

    myvector2 = Vector(3)
    myvector2[0] = 2
    myvector2[1] = 5
    myvector2[2] = 6
    print(myvector2)


    print(myvector + myvector2)

    print("Equal: ", myvector == myvector2)
    print("Cosine distance: ", myvector.cosine_distance(myvector2))
    
