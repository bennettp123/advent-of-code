# 2015 day 7

The example in the instructions imply that the input is ordered such that
dependencies are set on lines above.

```
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
```

However, the actual input has lines out of order, and the instructions do not
mention ordering at all.

The simple parser assumes all needed values are available when parsing, so
we pre-process the input to ensure ordering.

