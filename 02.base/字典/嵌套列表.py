a = [{"a": 1, "b": 2, "c": 3}, {"a": 11, "b": 22, "c": 33}]
d = {}
for key in a[0].keys():
    c = []
    for query in a:
        c.append(query.get(key))
    d[key] = c

print(d)

b = [query.get(key) for key in a[0].keys() for query in a]
m = [[query.get(key) for query in a] for key in a[0].keys()]
n = {key: [query.get(key) for query in a] for key in a[0].keys()}

print(b)
print(m)
print(n)

"""{'a': [1, 11], 'b': [2, 22], 'c': [3, 33]}
[1, 11, 2, 22, 3, 33]
[[1, 11], [2, 22], [3, 33]]
{'a': [1, 11], 'b': [2, 22], 'c': [3, 33]}
    """