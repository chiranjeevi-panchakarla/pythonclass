x = 'global'


def outer():
    x = 'outer x'

    def inner():
        x = 'inner'
        print(x)

    inner()
    print(x)


outer()
print(x)
