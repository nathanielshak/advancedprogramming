# The Big O Runtime of Selection Sort is...


# O(n<sup>2</sup>)

## Why is that?

Well, let's look at the algorithm again.

**How many times do we loop through the list of numbers?**

Since we do this once for each element in the list, the answer to this is **n** times, where **n** is the number of elements in the list.

**How many items to we check per each loop?**

That's a trickier question. The first time, we will compare **n - 1** elements against the first one, then, we will check **n - 2** against the second, followed by **n - 3**, and so on. If we find the sum of all of these, it comes out to `n(n - 1) / 2` through an [arithmetic progression](https://en.wikipedia.org/wiki/Arithmetic_progression).

> If you don't understand the math, it's okay - just make sure you know it comes out to `n(n-1)/2` checks.

**Okay, but how does that come out to O(n<sup>2</sup>)?**

If we simplify out `n(n-1)/2`, we get:

(n<sup>2</sup> - n)/2

Remember that in Big O we don't care about constants, so we can ignore the 1/2, leaving us with:

n<sup>2</sup> - n

In Big O, we also don't care about any terms other than the biggest exponent one, so we can also ignore the n, leaving us with:

n<sup>2</sup>, so the Big O runtime is **O(n<sup>2</sup>)**.

[Back to the lesson!](README.md)