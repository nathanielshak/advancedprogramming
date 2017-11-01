# The Big O Runtime of Selection Sort is...


# O(N<sup>2</sup>)

## Why is that?

Well, let's look at the algorithm again.

**How many times do we loop through the list of numbers?**

Well, since we do this once for each element in the list, the answer to this is **N** times, where **N** is the number of elements in the list.

**How many items to we check per each loop?**

That's a trickier one. The first time, we will compare **N - 1** elements against the first one, then, we will check **N - 2**, followed by **N - 3**, and so on. If we find the sum for all of this, it comes out to `n(n - 1) / 2 ` through an [arithmetic progression](https://en.wikipedia.org/wiki/Arithmetic_progression).

> If you don't understand the math, it's okay - just make sure you know it comes out to n(n-1)/2 checks.
 
**Okay, but how does that come out to O(N<sup>2</sup>)?**

If we simplify out `n(n-1)/2`, we get:

(n<sup>2</sup> - n)/2

If you remember, in Big O, we don't care about constants, so we can ignore the 1/2, leaving us with:

n<sup>2</sup> - n

In Big O, we also don't care about any terms other than the biggest exponent one, so we can also ignore the n, leaving us with:

n<sup>2</sup>, which in Big O is: **O(N<sup>2</sup>)** 

[Back to the lesson!](README.md)