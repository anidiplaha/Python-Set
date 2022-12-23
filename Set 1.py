s = set() # creates an empty set
s.add(10) # add an element
s.add(20)
s.add(30)
s
{10, 20, 30}
primeNums = {2, 3, 5, 7}
s.update(primeNums) # update set with another set

s1=set()
s1.add(2)
s1.add(3)
s1.add(20)
s1.add(30)
{2, 3, 20,30}
s1.remove(2) # remove an element
s1
{3, 20, 5, 7, 10, 30}

print(s)
print(s1)
