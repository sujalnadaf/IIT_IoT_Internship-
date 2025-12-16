m1 = [
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12]
]
m2 = (
 (1, 1, 1, 1),
 (2, 2, 2, 2),
 (3, 3, 3, 3)
)
def matrix_ops(a, b):
 add = []
 sub = []
 for i in range(len(a)):
     add.append([a[i][j] + b[i][j] for j in range(len(a[0]))])
     sub.append([a[i][j] - b[i][j] for j in range(len(a[0]))])
 return add, sub
add_res, sub_res = matrix_ops(m1, m2)
print("Addition:", add_res)
print("Subtraction:", sub_res)
 