'''
LEGB
Local, Enclosing, Global, Built-in
'''
x = 'global x'

# built in
x = min(2,1,4,5,7,8,.3)
print(x)
# Local
def test():
  x = 'local x'
  print(x)
test()
# Enclosing
def outer():
    # x = 'outer x'
    for b in range(3):
        x = 'outer {}'.format(b)

    def inner():
        # x = 'inner x'
        for c in range(4):
            x = 'inner {}'.format(c)
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)

outer()
print(x)
print(a)
