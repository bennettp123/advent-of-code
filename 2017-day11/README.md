# 2017 day 11

The coordinates here are essentially the same as [day 3](http://adventofcode.com/2017/day/3),
except in addition to moving N/S/E/W, you can also move diagonally NE/SW.

More details [here](https://gamedev.stackexchange.com/questions/44812/finding-shortest-path-on-a-hexagonal-grid).

# What the user sees: hex grid

```
  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
```

# Internal representation: square grid

```
   | n | ne
 --+---+--
nw |   | se
 --+---+--
sw | s |
```

Moving N/NE/NW/SE/SW/S each has the same distance cost.

With these coordinates, the algorithm to determine the shortest path to origin
is:

```
if x > 0 and y > 0:
       min(x, y) + max(x, y) - min(x, y)

if x < 0 and y < 0:
    same distance as if they were both positive

else:
    x + y
```

The first case is equivalent to max(x, y), making the algorithm:

```
if x > 0 and y > 0:
    max(x, y)

if x < 0 and y < 0:
    abs(min(x, y))

else:
    x + y
```

