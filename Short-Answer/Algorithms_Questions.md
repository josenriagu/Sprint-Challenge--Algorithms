# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0 #-> O(1)
    while (a < n * n * n): #-> O(n) * O(1)
      a = a + n * n #-> O(1)
```

```python
b)  sum = 0 #-> O(1)
    for i in range(n): #-> O(n)
      j = 1 #-> O(1)
      while j < n: #-> O(logn)
        j *= 2 #-> O(1)
        sum += 1 #-> O(1)
```

```python
c)  def bunnyEars(bunnies):
      if bunnies == 0: #-> O(1)
        return 0 #-> O(1)

      return 2 + bunnyEars(bunnies-1) #-> O(n)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

`I will utilize Binary Search, which is faster than Linear Search`

- determine the `middle` of the building using n//2 `#-> O(1)`
- assign `f` to middle `#-> O(1)`
- assign `high` to highest floor - `n` `#-> O(1)`
- assign `low` to ground floor - `0` `#-> O(1)`
- initialize a while loop (`while middle > 1`) `#-> O(logn)`

  - get to the middle and drop egg `#-> O(1)`
  - if the egg breaks: `#-> O(1)`

    - re-assign `high` to `middle` (we need to descend) `#-> O(1)`
    - re-assign `middle` to `(middle - lower) // 2` ( half of the lower half of the building) `#-> O(1)`
    - re-assign `f` to `middle` as usual `#-> O(1)`

  - else if it doesn't break, `#-> O(1)`
    - re-assign `low` to middle ( we need to ascend) `#-> O(1)`
    - re-assign `middle` to `(high - middle) // 2` ( half of the upper half of the building) `#-> O(1)`
    - re-assign `f` to `middle` as usual `#-> O(1)`
  - half the total height of the building with n/2 and the loops starts afresh with this new height `#-> O(1)`

- when the loop breaks, return `f`, which points to the middle of the last loop
