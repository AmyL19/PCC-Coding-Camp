# ===============================  EMPTY LISTS  ===============================

# a = []
# b = list()

# print(f"a is equal to b: {a == b}")
# print(f"the length of a is {len(a)}")
# print(f"the type of a and b are: {type(b)}")


# ===========================  LISTS AS CONTAINERS  ===========================

# list0 = [1, 2, 3, 4, 5]
# print(f"{list0} is a valid list")

# list1 = list(("a", "b", "c", "d", "e", "b"))
# print(f"{list1} is a valid list")

# list2 = [True, "False", 0]
# print(f"{list2} is a valid list")

# list3 = [(i**2) for i in range(3)]
# print(f"{list3} is a valid list")


# =============================  ACCESSING LISTS  =============================
# #       0    1    2    3    4    5
# lst = ["a", "b", "c", "d", "e", "f"]

# print(lst[0])               # a
# print(lst[7])               # out of range!
# print(lst[-1])              # f
# print(lst[-8])              # out of range!
# print(lst[:2])
# print(lst[3:])
# print(lst[1:5])
# print(lst[::2])
# print(lst[1:4:2])


# # ==============================  LIST FUNCTIONS  =============================

# list0 = [1, 2, 3, 4, 5]
# #              0    1    2  ...         5
# list1 = list(("a", "b", "c", "d", "e", "b"))
# list2 = [True, "False", 0]
# list3 = [(i**2) for i in range(3)] # 0 1 2

# print(len(list0))
# print(2 in list0)
# print(list1.count("b"))
# print(f"the first occurrence of 'b' is at index {list1.index('b')}")
# print(f"the next occurrence of 'b' is at index {list1.index('b', 2)}")

# modifying lists
# print([1, 2] + [3, 4])
# list0.append(6)
# print(list0)
# list2.insert(1, "blah")
# print(list2)

# list1.remove("b")             # remove the element
# print(list1)
# list3.pop()                   # deletes the index
# print(list3)

# list3[1] = 7
# print(list3)


# =========================  MONO-TYPE LIST FUNCTIONS  ========================

# print(min([5, -2, 9, 5]))
# print(max(["a", "b", "c", "d"]))
# print(sum([1, 2, 3, 4, 5]))
# print(sorted([5, -2, 9, 5]))


# =============================  LOOPS AND LISTS  =============================

# lst = [1, 2, 3, 4, 5, 6, 7, 8]

# for n in lst:
#     print(n)

# for i in range(len(lst)):
#     if i % 2 == 0:
#         print(lst[i])
