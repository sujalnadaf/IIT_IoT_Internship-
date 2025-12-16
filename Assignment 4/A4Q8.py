data = ((10, 10, 10, 12),
 (30, 45, 56, 45),
 (81, 80, 39, 32),
 (1, 2, 3, 4))
averages = []
for col in zip(*data):
 averages.append(sum(col) / len(col))
print(averages)