# 2015 day 7

The example in the instructions implies that input is ordered such that
dependencies are never undefined, as long as the input is processed from
top to bottom:

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

The final solution uses a mix of regular expressions for dependency ordering,
and substring comparison for the actual logic. A more elegant solution might
use regex for everything, but I've left it with a mix becuase:

1. it works, and
2. it permits expressions like `x AND NOT y` or `x AND y OR z`, which are
   undefined in the requirements. However, these expressions will probably
   need to be pre-ordered to ensure dependencies are met, since the regex
   does not handle these extensions.
