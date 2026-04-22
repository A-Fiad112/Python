import itertools


counter = itertools.count(10,2)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


data = [100,200,300,400]
daily_data = zip(itertools.count(),data)
# print(list(daily_data))

coun = itertools.count(start=5,step=-2.5)
# print(next(coun))
# print(next(coun))
# print(next(coun))

data = [100,200,300,400]
daily_deta = list(zip(range(10),data))
daily_deta = list(itertools.zip_longest(range(10),data))
# print(daily_deta)

cy = itertools.cycle(('on',"off",3))
print(next(cy))
# print(next(cy))
# print(next(cy))
# print(next(cy))

rp =itertools.repeat(2,times=3)
print(next(rp))
print(next(rp))
print(next(rp))
# print(next(rp))

squares = map(pow,range(10),itertools.repeat(2))
squares = itertools.starmap(pow,[(0,2),(1,2),(2,2),(3,2)])
print(next(squares))

# print(help(itertools.starmap))

letters=['a','b','c','d']
numbers=[1,2,3,4]
names=['john','doe','smith','jones']
selector = [True,False,True,True]

print(help(itertools.combinations))
# result = itertools.combinations(letters,2)
result = itertools.product(numbers,repeat=2)
result = itertools.combinations_with_replacement(numbers,2)
result = itertools.chain(letters,numbers,names)
result = itertools.islice(range(10),1,5,2)
result = itertools.compress(letters,selector)
result = itertools.filterfalse(letters,selector)
print(list(result))
