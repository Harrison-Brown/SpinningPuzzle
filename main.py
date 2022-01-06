import data

def cover(bottom, top):
    # Takes 2 equal length lists, bottom and top,
    # and replaces all bottom values with the non-null top values
    l = bottom.copy()
    for i in range(len(bottom)):
        if top[i] != None:
            l[i] = top[i]
    return l


class Ring:
    def __init__(self, array):
        # array is 4x12 array, None for holes
        self.array = array

    def rotate(self):
        # takes first number on each list and pushes to end
        self.array = [ l[1:] + l[:1] for l in self.array]

    def __str__(self):
        return '\n'.join([str(l) for l in self.array])

class Puzzle:
    def __init__(self, allrings):
        # self.allrings is list of arrays from data
        self.allrings = [Ring(ring) for ring in allrings]

    def solve(self):
        # rotates each ring once each other ring goes in a full circle
        for i in range(12**4):
            self.allrings[4].rotate()
            if i%12 == 0:
                self.allrings[3].rotate()
            if i%(12**2) == 0:
                self.allrings[2].rotate()
            if i%(12**3) == 0:
                self.allrings[1].rotate()
            if self.checksol():
                break

    def collapse(self):
        # Uses predefined cover function to collapse all rings into 1
        bottom = [ [None for i in range(12)] for j in range(4) ]
        for i in range(len(self.allrings)):
            top = self.allrings[i].array
            bottom = [ cover(bottom[j], top[j]) for j in range(len(top)) ]
        return bottom

    def checksol(self):
        # checks if each column on puzzle adds to 42
        collapsed = self.collapse()
        for x in range(len(collapsed[0])):
            s = sum(collapsed[i][x] for i in range(len(collapsed)))
            if s != 42:
                return False
        return True

    def __str__(self):
        s = ''
        for i in range(len(self.allrings)):
            s += f'Ring{i}:\n{self.allrings[i]}\n\n'
        return s

def main():
    p = Puzzle(data.allrings)

    p.solve()
    print(p)
    for x in p.collapse():
        print(x)


if __name__ == '__main__':
    main()
