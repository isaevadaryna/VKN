import child
import numpy as np
kids = np.array([["Микола", "Савченко", "2016"],
            ["Марина", "Кравченко","2019"],
            ["Андрій", "Вишнивеський","2019"],
            ["Світлана", "Левицька","2016"]], dtype=str)
#age1 = child.child.set_age(kids)
#age = child.child.get_age(age1)
children = []
#L = len(kids)
for i in range(4):
    child1 = child.child(kids[i][0],kids[i][1],kids[i][2])
    children.append(child1)
for elem in children:
    age = elem.get_age()
    if age == 6:
        print("Йде до першого класу")
    if age == 3:
        print("Йде до садочка")