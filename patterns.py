#    1)
#     *
#    ***
#   *****
#  *******
# *********

for i in range(5):
        print(" " * (5 - i - 1) + "*" * (2 * i + 1))

        


#        2)
# * * * * * 
# * * * *
# * * *
# * *
# *
for i in range(5):
    print("* " * (5 - i))



#        3)
# * * * * * 
# *       *
# *       *
# *       *
# * * * * *
for i in range(5):
    for j in range(5):
        if i == 0 or i == 5 - 1 or j == 0 or j == 5 - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#        4)
#     * 
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

for i in range(5):
    print(" " * (5 - i - 1) + "* " * (i + 1))
for i in range(5 - 1):
    print(" " * (i + 1) + "* " * (5 - i - 1))



#      5)
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
for i in range(5):
    coef = 1
    for j in range(1, 5 - i + 1):
        print(" ", end="")
    for k in range(0, i + 1):
        print("", coef, end="")
        coef = coef * (i - k) // (k + 1)
    print()

#         6)
#     *
#    **
#   ***
#  ****
# *****
for i in range(5):
        print(" " * (5 - i - 1) + "*" * (i + 1))

#       7)
# 1 2 3 4 5 
# 5 4 3 2 1
# 1 2 3 4 5
# 5 4 3 2 1
for i in range(1, 4 + 1):
    if i % 2 == 0:
        for j in range(5, 0, -1):
            print(j, end=" ")
    else:
        for j in range(1, 5 + 1):
            print(j, end=" ")
    print()