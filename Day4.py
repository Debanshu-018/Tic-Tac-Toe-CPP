# Q.1
rows = 5
for i in range(1,rows + 1):
    print("*" * i)
#   output
# *
# **
# ***
# ****
# *****

# Q.2
rows = 5

for i in range(rows, 0, -1):
    print("*" * i)
#   OUTPUT
# *****
# ****
# ***
# **
# *

# Q.3
rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

# OUTPUT
#     *
#    **
#   ***
#  ****
# *****

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Q.4
 
# OUTPUT
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5    






































































































































