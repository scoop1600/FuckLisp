class Person:

    parentList = []
    siblingList = []
    halfSiblingList = []


    def isParent(person1, person2):
        result = False

        if(person2.parentsList.contains(person1)):
            result = True

        return(result)


    def isSibling(person1, person2):
        result = False

