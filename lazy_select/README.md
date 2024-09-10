# Lazy Select
The lazy select algorithm is a randomized algorithm that computes the `k`-th smallest element in a typically large set of elements. The naive approach requires the set to be sorted first. When `n` is very large, say 2**16 or even larger, the sorting will take `O(nlogn)` steps which is very high. The lazy select approach computes the same in `O(n)` steps. 

## Algorithm
1. Given set `S` with `n = 2m` elements. 
2. Create another set `R` by sampling elements from `S` with a probability `1/n**(0.25)`
3. Sort `R`
4. Compute `a` and `b` using the formulas given below.
5. Let `S'` be a set such `S = {y ∈ S : a < y < b}` and let `t` be number of elements in `S` which are smaller than `a`.
6. Sort `S'`
7. Return `S[t - k - 1]`

### Compute a and b

* a = `(n**(0.75))/2 - 5*(n**(0.5))` -th smallest element in R
* b = `(n**(0.75))/2 + 5*(n**(0.5))` -th smallest element in R

## Time Complexity
1. Computing `R` takes `O(n)` steps.
2. Sorting `R` takes `|R|log(|R|)` steps, but note that `|R| << n`.
3. Computing `S` and `t` takes `O(n)` steps.
4. Sorting `S'` takes `|S'|log(|S'|)` steps, but note that `|S'| << n`.
5. Therefore, all the steps will take atmost `O(n)` steps.

## Correctness Analysis
The correctness of the algorihtm involves a mathematical proof, and can be found in detail from [Prof. Andrew McGregor's lecture slides](https://people.cs.umass.edu/~mcgregor/611S24/lec16.pdf).