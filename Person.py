import sys

class Person:

    def __init__(self, name, parent1, parent2):
        self.name = name
        self.parent1 = parent1
        self.parent2 = parent2

    def get_name(self):
        return self.name

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def set_parent1(self, p):
        self.parent1 = p

    def set_parent2(self, p):
        self.parent2 = p

    def find_parent(self, p):
        if self.get_parent1().get_name() is p.get_name():
            return True
        elif self.get_parent2().get_name() is p.get_name():
            return True
        else:
            return False

    def find_sibling(self, p):
        rents = [self.get_parent1().get_name(), self.get_parent2().get_name()]

        if p.get_parent1().get_name() in rents and p.get_parent2().get_name() in rents:
            return True
        else:
            return False

    def find_half(self, p):
        rents = [self.get_parent1().get_name(), self.get_parent2().get_name()]
        if bool(p.get_parent1().get_name() in rents) != bool(p.get_parent2().get_name() in rents):
            return True
        elif self.find_sibling(p):
            return False

    def ancestors(self):
        fam = ""

        if self.get_parent1() is None:
            fam = fam
        elif self.get_parent2() is None:
            fam = fam
        else:
            if self.get_parent1() is not None:
                fam += self.get_parent1().get_name() + "\n"
                fam += self.get_parent1().ancestors()
            if self.get_parent2() is not None:
                fam += self.get_parent2().get_name() + "\n"
                fam += self.get_parent2().ancestors()
        return fam

    def find_ancestor(self, ancestor):
        ancs = self.ancestors().split()
        if ancestor.get_name() in ancs:
            return True
        else:
            return False

    def find_cousin(self, other):
        common = False
        direct = False
        result = False

        a = self.ancestors().split()
        b = other.ancestors().split()

        for name in a:
            if name in b:
                common = True

        if other.get_name() in a:
            direct = True

        elif self.get_name() in b:
            direct = True

        if common is True and direct is False:
            result = True
        return result

    def find_related(self, other):
        result = False
        common = False
        direct = False

        a = self.ancestors()
        b = other.ancestors()

        first_anc = a.split()
        second_anc = b.split()

        for name in first_anc:
            if name in second_anc:
                common = True

        if other.get_name() in first_anc:
            direct = True
        elif self.get_name() in second_anc:
            direct = True

        if common is True or direct is True or (common is True and direct is True):
            result = True
        return result


def alph(x):
    result = ""
    words = x.split()
    words.sort()
    for p in words:
        result += p + "\n"

    return result


x = 0
dict = {}
splits = []
people = []

for line in sys.stdin:
    data = line.rstrip()
    splits = data.split(" ")
    # splits[0] - query, splits[1] - parent1, splits[2] - parent2, (splits[3] - child)
    for i in range(len(splits)):
        splits[i] = splits[i].strip()

    if splits[0] == "E":
        # Event
        if len(splits) == 3:
            print(splits[0] + " " + splits[1] + " " + splits[2])

            if splits[1] not in dict:
                p1 = Person(splits[1], None, None)
                people.append(p1)
                dict[p1.get_name()] = p1
            else:
                p1 = dict.get(splits[1])

            if splits[2] not in dict:
                p2 = Person(splits[2], None, None)
                people.append(p2)
                dict[p2.get_name()] = p2
            else:
                p2 = dict.get(splits[2])

        elif len(splits) >= 4:
            print(splits[0] + " " + splits[1] + " " + splits[2] + " " + splits[3])

            if splits[1] not in dict:
                p1 = Person(splits[1], None, None)
                people.append(p1)
                dict[p1.get_name()] = p1
            else:
                p1 = dict.get(splits[1])

            if splits[2] not in dict:
                p2 = Person(splits[2], None, None)
                people.append(p2)
                dict[p2.get_name()] = p2
            else:
                p2 = dict.get(splits[2])

            if splits[3] not in dict:
                p3 = Person(splits[3], p1, p2)
                dict[p3.get_name()] = p3
                people.append(p3)

            else:
                p3 = dict.get(splits[3])
                p3.set_parent1(p1)
                p3.set_parent2(p2)

    if splits[0] is "X":
        # IS questions
        if splits[2] == "parent":
            child = dict.get(splits[3])
            parent = dict.get(splits[1])

            try:
                if child.find_parent(parent) is True:
                    print("X " + parent.get_name() + " parent " + child.get_name())
                    print("Yes\n")
                else:
                    print("X " + parent.get_name() + " parent " + child.get_name())
                    print("No\n")
            except:
                print("X " + splits[1] + " parent " + splits[3])
                print("No\n")

        elif splits[2] == "sibling":
            sib1 = dict.get(splits[3])
            sib2 = dict.get(splits[1])
            try:
                if sib2.find_sibling(sib1) is True:
                    print("X " + sib2.get_name() + " sibling " + sib1.get_name())
                    print("Yes\n")
                else:
                    print("X " + sib2.get_name() + " sibling " + sib1.get_name())
                    print("No\n")
            except:
                print("X " + splits[1] + " sibling " + splits[3])
                print("No\n")

        elif splits[2] == "half-sibling":
            sib1 = dict.get(splits[3])
            sib2 = dict.get(splits[1])
            try:
                if sib1.find_half(sib2) is True:
                    print("X " + sib2.get_name() + " half-sibling " + sib1.get_name())
                    print("Yes\n")
                else:
                    print("X " + sib2.get_name() + " half-sibling " + sib1.get_name())
                    print("No\n")
            except:
                print("X " + splits[1] + " half-sibling " + splits[3])
                print("No\n")

        elif splits[2] == "ancestor":
            person = dict.get(splits[3])
            anc = dict.get(splits[1])
            try:
                if person.find_ancestor(anc) is True:
                    print("X " + anc.get_name() + " ancestor " + person.get_name())
                    print("Yes\n")
                else:
                    print("X " + anc.get_name() + " ancestor " + person.get_name())
                    print("No\n")
            except:
                print("X " + splits[1] + " ancestor " + splits[3])
                print("No\n")

        elif splits[2] == "cousin":
            cousin1 = dict.get(splits[3])
            cousin2 = dict.get(splits[1])
            try:
                if cousin1.find_cousin(cousin2) is True:
                    print("X " + cousin2.get_name() + " cousin " + cousin1.get_name())
                    print("Yes\n")
                else:
                    print("X " + cousin2.get_name() + " cousin " + cousin1.get_name())
                    print("No\n")
            except:
                print("X " + splits[1] + " cousin " + splits[3])
                print("No\n")

        elif splits[2] == "unrelated":
            person1 = dict.get(splits[3])
            person2 = dict.get(splits[1])
            try:
                if person1.find_related(person2) is False:
                    print("X " + person2.get_name() + " unrelated " + person1.get_name())
                    print("Yes\n")
                else:
                    print("X " + person2.get_name() + " unrelated " + person1.get_name() )
                    print("No\n")
            except:
                print("X " + splits[1] + " unrelated " + splits[3])
                print("Yes\n")


    elif splits[0] is "W":
        # WHO questions
        if splits[1] == "parent":
            try:
                child = dict.get(splits[2])
                result = child.get_parent1().get_name() + "\n" + child.get_parent2().get_name()
                print("W parent " + splits[2])
                print(alph(result))
            except:
                print("W parent " + splits[2])

        elif splits[1] == "sibling":
            sib = dict.get(splits[2])
            result = ""
            for p in people:
                try:
                    if sib.find_sibling(p) is True:
                        if p.get_name() != sib.get_name():
                            result += p.get_name() + "\n"
                except:
                    result = result
            print("W sibling " + splits[2])
            print(alph(result))

        elif splits[1] == "half-sibling":
            half = dict.get(splits[2])
            result = ""
            for p in people:
                try:
                    if half.find_half(p) is True:
                        if half.get_name() != p.get_name():
                            result += p.get_name() + "\n"
                except:
                    result = result
            print("W half-sibling " + splits[2])
            print(alph(result))

        elif splits[1] == "ancestor":
            anc = dict.get(splits[2])
            try:
                result = anc.ancestors()
                print("W ancestor " + splits[2])
                print(alph(result))
            except:
                print("W ancestor " + splits[2])

        elif splits[1] == "cousin":
            cousin = dict.get(splits[2])
            curr = False
            result = ""
            for p in people:
                try:
                    curr = cousin.find_cousin(p)
                    if curr is True and cousin.get_name() != p.get_name():
                        result += p.get_name() + "\n"
                except:
                    result = ""
            print("W cousin " + splits[2])
            print(alph(result))

        elif splits[1] == "unrelated":
            rel = dict.get(splits[2])
            curr = False
            result = ""
            if rel is None:
                for p in people:
                    result += p.get_name() + "\n"
            else:
                for p in people:
                    curr = rel.find_related(p)
                    if curr is False and rel.get_name() != p.get_name():
                        result += p.get_name() + "\n"
            print("W unrelated " + splits[2])
            print(alph(result))
