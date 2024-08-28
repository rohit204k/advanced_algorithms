# Quick Sort
Quick sort algorithm is a sorting algorithm that sorts an array by recursively chosing a pivot element and sorting the sub arrays containing elements less than and greater than the pivor respectively. It works on the principle,that, upon choosing a pivot and creation of the subarrays, no two elements across the pivot (on either sides of the pivot) need to be compared, as all the elements in the subarrays (even though unsorted amongt themselves) are placed numerically in the correct order with respect to the pivot. It can be proved there will be atmost `nlogn` comparisons.

## Time Complexity

* Probability the `i-th` smallest element is compared the `j-th` smallest element of an array is equal to `2/(j - i + 1)`, where `i < j`.
* Let Z_ij = 1 if the 
* The time complexity can be derived using the Master's theorem where a=2, b=2, and α = 1.
* Time complexity, `T(n) = nlog(n)`