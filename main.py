#Function 1
''''
def list(n):
  a = []
  b = []
  if n.isdigit() == True:    #n.isdigit()
    n = input()
    a.append(n)
    print(a)
  elif n.isdigit == False:
    n = input()
    b.append(n)
    print(b)
  else: 
    print("What are you typing?")

n = [str(s) for s in input().split()]
print(list(n))
'''


#Function 2
a = [int(s) for s in input().split()]
for elem in a:
  print(elem, end = ' ')

for i in list:
  if i.isdigit == True:
    print("Yes")

def count(list_1):
  list_1 = []
  list_2 = []
  for i in list_1:
    if i.isdigit() == True:
      list_1.append(i)
      return list_1

list_1 = [(s) for s in input().split()]
print(count(list_1))




