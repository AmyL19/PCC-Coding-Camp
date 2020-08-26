# LISTS

## Empty Lists

Lists are containers that can hold many items. Here are some examples of empty lists and their properties.

```python
a = []
b = list()

a == b                # True
len(a)                # 0
type(b)               # class: list
```


## Lists as containers

Here are some of the many ways to initialize lists. Lists in python are symbolized using square brackets: `[]`, but can also be initialized using the `list()` function or list comprehension notation. Additionally, as you can see, lists can hold anything; they don't all have to be of the same type.

```python
list0 = [1, 2, 3, 4, 5]
list1 = list(("a", "b", "c", "d", "e", "b"))
list2 = [True, "False", 0]
list3 = [(i**2) for i in range(3)]
```


## Accessing lists

Lists are accessed or sliced using square brackets (`[]`). You can use negative indices to access from the end of the list. Also, using the `:` inside the brackets lets you select a range. Using a number after the second colon indicates the step size. In total, the structure looks like this: `lst[start:end:step_size]`.

```python
lst = ["a", "b", "c", "d", "e", "f"]

lst[0]
lst[7]               # out of range!
lst[-1]
lst[-8]              # out of range!
lst[:2]
lst[3:]
lst[::2]
```


## List functions

Below are some examples of functions that you can perform on lists. Some examples include counting the length of the list, checking whether an item is in the list, counting the number of occurrences of an item in the list, finding the element in the list, and modifying the list in a variety of ways.

```python
list0 = [1, 2, 3, 4, 5]
list1 = list(("a", "b", "c", "d", "e", "b"))
list2 = [True, "False", 0]
list3 = [(i**2) for i in range(3)]

len(list0)                    # 5
2 in list0                    # True
list1.count("b")              # 2
list1.index('b')              # 1
list1.index('b', 2)           # 5

# modifying lists
[1, 2] + [3, 4]               # [1, 2, 3, 4]
list0.append(6)               # [1, 2, 3, 4, 5, 6]
list2.insert(1, "blah")       # [True, "blah", "False", 0]

list1.remove("b")             # ["a", "c", "d", "e"]
list3.pop()                   # [0, 1]

list3[1] = 7                  # [0, 7]
```


## Mono-type list functions

Below are some examples of functions that you can perform on lists if all members of the list are the same type. You can take the min or max, add up all the elements, and sort the list (think about why all elements need to be the same type to perform these types of operations). 

```python
min([5, -2, 9, 5])                  # -2
max(["a", "b", "c", "d"])           # "d"
sum[1, 2, 3, 4, 5]                  # 15
sorted([5, -2, 9, 5])               # [-2, 5, 5, 9]
```


## Loops and lists

Below are two ways to loop through lists. You can loop through the list directly, or loop through the indices. 

```python
lst = [1, 2, 3, 4, 5, 6, 7, 8]

for n in lst:
    print(n)

for i in range(len(n)):
    if i % 2 == 0:
        print(lst[i])
```
