# Maximum Subarray

**Easy**

_Companies_: ***0-6 months:*** Amazon: 24, Google: 18, Microsoft: 17, LinkedIn: 12, Facebook: 9, Apple: 8, Adobe: 6, Oracle: 5, Expedia: 2, Yahoo: 2, Zillow: 2, JPMorgan: 2, Morgan Stanley: 2, Asana: 2, Atlassian: 2, Walmart Labs: 2; ***6 months - 1 year:*** Bloomberg: 7, Paypal: 5, eBay:4, SAP: 4, Cisco: 3, ByteDance: 3, Alibaba: 2, Intel: 2, Uber: 2; ***1 year - 2 years:*** Two Sigma: 6, Goldman Sachs: 3, Capital One: 3, NetEase: 2, Evernote: 2, Citadel: 2, Nvidia: 2, Wayfair: 2

_Related Topics_: Array, Divide and Conquer, Dynamic Programming

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

~~~
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
~~~

**Follow up:**

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Solution

### C++

### Approach 1: Brute Force

The brute force approach is simple. Loop through each element i and then loop through each element j = i+1 to find the contiguous subarray whose sum has the largest sum.

**C++ Code**

Runtime: **556 ms**

Memory Usage: **9.2 MB**

~~~cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0;
        int largest_sum = INT_MIN;
        
        // test edge case: if nums size == 1, then 1st elm is largest sum
        if(nums.size() == 1) {
            return nums[0];
        }
        
        for(int i = 0; i < nums.size(); i++) {
            sum = 0;
            sum += nums[i];
            for(int j = i+1; j < nums.size(); j++) {
                if(sum > largest_sum) {
                    largest_sum = sum;
                }
                sum += nums[j];
            }
            // test edge case: if there are only 2 elements, check is 2nd
            // element sum greater than largest sum
            if(sum > largest_sum) {
                largest_sum = sum;
            }
        }
        return largest_sum;
    }
};
~~~

**Complexity Analysis**

Time Complexity: O(n^2). For each element i, we try to find the contiguous subarray with the largest sum by looping through the rest of the array j = i+1, which takes O(n) time. Thus, the time complexity is O(n^2). 

Space complexity : O(1).

### Approach 2: Divide and Conquer

**Intuition**

The problem is a classical example of divide and conquer approach, and can be solved with the algorithm similar with the merge sort.

Let's follow here a solution template for the divide and conquer problems :

Define the base case(s).

Split the problem into subproblems and solve them recursively.

Merge the solutions for the subproblems to obtain the solution for the original problem.

**Algorithm**

maxSubArray for array with n numbers:

If n == 1 : return this single element.

left_sum = maxSubArray for the left subarray, i.e. for the first n/2 numbers (middle element at index (left + right) / 2 always belongs to the left subarray).

right_sum = maxSubArray for the right subarray, i.e. for the last n/2 numbers.

cross_sum = maximum sum of the subarray containing elements from both left and right subarrays and hence crossing the middle element at index (left + right) / 2.

Merge the subproblems solutions, i.e. return max(left_sum, right_sum, cross_sum).

**C++ Code**

Runtime: **20 ms**

Memory Usage: **9.3 MB**

~~~cpp
class Solution {
public:
    int crossSum(vector<int> &nums, int left, int right, int p) {
        // check does nums contain a single element, return it
        if(left == right) return nums[left];
        
        // get max left sum
        int left_subsum = INT_MIN;
        int curr_sum = 0;
        for(int i = p; i > left - 1; --i) {
            curr_sum += nums[i];
            left_subsum = max(left_subsum, curr_sum);
        }
        
        // get max right sum
        int right_subsum = INT_MIN;
        curr_sum = 0;
        for(int i = p+1; i < right+1; ++i) {
            curr_sum += nums[i];
            right_subsum = max(right_subsum, curr_sum);
        }
        // add max left subsum to max right subsum, then return it 
        return left_subsum + right_subsum;
    }
    
    int helper(vector<int> &nums, int left, int right) {
        // check does nums contain a single element, return it
        if(left == right) return nums[left];
        
        int p = (left+right)/2;
        
        // get maxSubArray for left subarray for first n/2 + middle index
        int left_sum = helper(nums, left, p);
        // get maxSubArray for right subarray for first n/2 numbers
        int right_sum = helper(nums, p+1, right);
        // get max sum of subarray containing elements from both left and right subarrays
        // crossing the middle element
        int cross_sum = crossSum(nums, left, right, p);
        // merge subproblem solutions to return largest sum of subarray
        return max(max(left_sum, right_sum), cross_sum);
    }
    
    int maxSubArray(vector<int>& nums) {
        return helper(nums, 0, nums.size()-1);
    }
};
~~~

**Complexity Analysis**

Time complexity : \mathcal{O}(N \log N). Let's compute the solution with the help of master theorem T(N) = aT\left(\frac{b}{N}\right) + \Theta(N^d). The equation represents dividing the problem up into aa subproblems of size \frac{N}{b} in \Theta(N^d) time. Here one divides the problem in two subproblemes a = 2, the size of each subproblem (to compute left and right subtree) is a half of initial problem b = 2, and all this happens in a \mathcal{O}(N) time d = 1. That means that \log_b(a) = d and hence we're dealing with case 2 that means \mathcal{O}(N^{\log_b(a)} \log N) = \mathcal{O}(N \log N) time complexity.

Space complexity : \mathcal{O}(\log N) to keep the recursion stack.