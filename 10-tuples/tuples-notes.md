# Tuples

Tuples are ...

- collections
- set of data
- **immutable**

## Access

```python
    oneTuple = ('a', 'b', 'c')
    print(oneTuple[0]) // a
    print(oneTuple[1]) // b
    print(oneTuple[2]) // c

    // Multiple assignments
    (first, second, third) = oneTuple
    print(first)  // a
    print(second) // b
    print(third)  // c
```

## Immutability

```python
    oneTuple = ('a', 'b', 'c')
    oneTuple[0] = 'x'    // ERROR
    oneTuple.sort()      // ERROR
    oneTuple.append()    // ERROR
    oneTuple.reverse()   // ERROR
```

## Reasons to use Tuples

1. Efficient - use less memory, better performance
   - use when list is temporary
   - use when items won't change

## Dictionaries

Dictionaries can be converted to tuples

```python
    newDictionary = dict()
    // ...
    tups = d.items()
```
