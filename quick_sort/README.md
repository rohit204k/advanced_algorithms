# Quick Sort
Quick sort algorithm is a sorting algorithm that sorts an array by recursively chosing a pivot element and sorting the sub arrays containing elements less than and greater than the pivor respectively. It works on the principle,that, upon choosing a pivot and creation of the subarrays, no two elements across the pivot (on either sides of the pivot) need to be compared, as all the elements in the subarrays (even though unsorted amongt themselves) are placed numerically in the correct order with respect to the pivot. It can be proved there will be atmost `nlogn` comparisons.

## Time Complexity

* Probability the `i`<sup>th</sup> smallest element is compared the `j`<sup>th</sup> smallest element of an array is equal to `2/(j - i + 1)`, where `i < j`.
* Let Z<sub>ij</sub> = 1 if the `i`<sup>th</sup> smallest element is compared the `j`<sup>th</sup> smallest element.
* Total number of comparisons is ∑<sub> 1 <= i < j <= n </sub>Z<sub>ij</sub>.
* Expected number of comparisons is E[∑<sub> 1 <= i < j <= n </sub>Z<sub>ij</sub>] = ∑<sup>n</sup><sub>j=2</sub> ∑<sup>j</sup><sub>k=2</sub> 2/k.
* The above term is simplified to `O(nlogn)`. For detailed explanation, refer [Prof. Andrew McGregor's lecture slides](https://people.cs.umass.edu/~mcgregor/611S24/lec13.pdf).
* Time complexity, `T(n) = nlog(n)`.