#code starts here
import sys


class Person:
    name = ""
    parent1 = None
    parent2 = None

    def __init__(self, name, parent1, parent2):
        self .name = name
        self.parent1 = parent1
        self.parent2 = parent2

    def get_name(self):
        return self.name

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def parents(self):
        return self.parent1.get_name + " " + self.parent2.get_name

    def set_parent1(self, p):
        self.parent1 = p

    def set_parent1(self, p):
        self.parent2 = p

    def find_parent(self, p):
        result = False
        if self.parent1.get_name is p.get_name:
            result = True
        if self.parent2.get_name is p.get_name:
            result = True
        return result
    #missing other parent

    def find_sibling(self, p):
        result = False
        rents = self.parents
        if p.get_parent1 in rents:
            if p.get_parent2 in rents:
                result = True
        return result

    def find_half(self, p):
        result = False
        rents = self.parents
        if p.get_parent1.get_name in rents:
            result = False
        elif p.getParent2.get_name in rents:
            result = False
        elif self.siblingQ(self, p):
            result = False
        return result

    def ancestors(self):
        fam = ""

        if self.parent1 is None:
            fam = fam
        elif self.parent2 is None:
            fam = fam
        else:
            if self.parent1 is not None:
                fam += self.parent1.get_parent1.get_name + " "
                fam += self.get_parent1.ancestors
            if self.parent2 is not None:
                fam += self.get_parent2.get_name + " "
                fam += self.get_parent2.ancestors
        return fam
    # may be missing return statement

    def find_ancestor(self, anc):
        result = False
        a = self.ancestors
        if anc.get_name in a:
            result = True
        return result

    def find_cousin(self, other):
        common = False
        direct = False
        result = False

        a = self.ancestors
        b = other.ancestors

        for name in a:
            if name in b:
                common = True

        if other.get_name in a:
            direct = True
        elif self.get_name in b:
            direct = True
        if common is True & direct is True:
            result = True
        return result

    def find_related(self, other):
        result = False
        common = False
        direct = False

        a = self.ancestors
        b = other.ancestors

        for name in a:
            if name in b:
                common = True
        if other.get_name in a:
            direct = True
        elif self.get_name in b:
            direct = True
        if direct is True | common is True | (direct is True & common is True):
            result = True
        return result

x = 0
dic = {}
splits = []
people = []

while x != 1:
    data = sys.stdin.readline()
    splits = data.split(" ")
    # splits[0] - query, splits[1] - parent1, splits[2] - parent2, (splits[3] - child)
    print(splits)

    if splits[0] is "E":
        # Event
        if len(splits) is 3:

            if splits[1] not in dic:
                p1 = Person(splits[1], None, None)
                people.append(p1)
                dic[p1.get_name()] = p1
            else:
                p1 = dic.get(splits[1])

            if splits[2] not in dic:
                p2 = Person(splits[2], None, None)
                people.append(p2)
                dic[p2.get_name()] = p2
            else:
                p2 = dic.get(splits[2])

        else:

            if splits[1] not in dic:
                p1 = Person(splits[1], None, None)
                people.append(p1)
                dic[p1.get_name()] = p1
            else:
                p1 = dic.get(p1.get_name())

            if splits[2] not in dic:
                p2 = Person(splits[2], None, None)
                people.append(p2)
                dic[p2.get_name()] = p2
            else:
                p2 = dic.get(p2.get_name())

            if splits[3] not in dic:
                newP = Person(splits[3], p1, p2)
                people.append(newP)
                dic[newP.get_name()] = newP
            else:
                p3 = dic.get(splits[3])
                p3.set_parent1(p1)
                p3.set_parent2(p2)
        print("here")

    elif splits[0] is "X":
        # IS questions
        if splits[2] is "parent":
            child = dic.get(splits[3])
            parent = dic.get(splits[1])

            if parent.find_parent(child) is True:
                print("X " + child.get_name() + " parent " + parent.get_name() + "\nYes")
            else:
                print("X " + child.get_name() + " parent " + parent.get_name() + "\nNo")
        print("Here")
    # elif splits[0] is "W":
        # WHO questions

