y_dev = {0: 2, 1: 3, 2: 4, 3: 2, 4: 3, 5: 0, 6: 7, 7: 8, 8: 9, 9: 0}

p = []
for i in range(10):
  p.append([])
print(p)
p[0] += [1]
print(p)
for i in range(10):
    p[y_dev[i]] += [i]
print(p)
