names = ['david', 'lila', 'miriam', 'chana']
name_lengths = {
    name: (lambda x: len(x), name) for name in names
    #why is this not then (lambda x: len(x), name) for name in names??
    #doing so causes chaos and says "{'Eli': <filter object at 0x000001CADB7BBE50>..." hmmmm
}
print("Name lengths:", name_lengths)