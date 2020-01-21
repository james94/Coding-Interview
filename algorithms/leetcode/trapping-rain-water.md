# Trapping Rain Water

**Hard**

**Companies:** Amazon: 44, Goldman Sachs: 31, Microsoft: 23, Facebook: 13, Google: 11, Apple, Qualtrics, Bloomberg, Uber, Visa, Snapchat, Adobe, Oracle, ByteDance, Databricks, Wish, Affirm, Walmart Labs, Salesforce, Citadel, Yandex, Electronic Arts, Tableau

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![rainwatertrap.png](images/rainwatertrap.png)

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

## Solution

### C++

### Approach 1: Brute Force

**Intuition**

Do as directed in question. For each element in the array, we find the maximum level of water it can trap after the rain, which is equal to the minimum of maximum height of bars on both the sides minus its own height.

Runtime: **8 ms**

Memory Usage: **9.1 MB**

~~~cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int max_left = 0;
        int max_right = height.size()-1;
        int ans = 0;
        int max_index = 0;
        
        // get highest value in array, get it's index
        for(int i = 0; i<height.size(); i++)
        {
            if(height[i] > height[max_index])
            {
                max_index = i;
            }
        }
        
        // count trapped water from left to right up to max_index
        for(int i = 1; i<max_index; i++)
        {
            if(height[i] > height[max_left])
            {
                max_left = i;
            }
            else
            {
                ans += (height[max_left]-height[i]);
            }
        }
        
        // count trapped water from right to left up to max_index
        for(int i = height.size()-2; i>max_index; i--)
        {
            if(height[i] > height[max_right])
            {
                max_right = i;
            }
            else
            {
                ans += (height[max_right]-height[i]);
            }
        }
        return ans;
    }
};
~~~

**Complexity Analysis**

Time complexity: O(n^2). For each element of array, we iterate the left and right parts.

Space complexity: O(1) extra space.

### Approach 2: Dynamic Programming

**Intuition**

In brute force, we iterate over the left and right parts again and again just to find the highest bar size upto that index. But, this could be stored. Voila, dynamic programming.

The concept is illustrated as shown:

![traprainwater_dynamic_programming.png](images/traprainwater_dynamic_programming.png)

**Algorithm**

- Find maximum height of bar from the left end upto an index i in the array left_max.
- Find maximum height of bar from the right end upto an index i in the array right_max.
- Iterate over the height array and update ans:
    - Add `min(max_left[i], max_right[i])-height[i] to ans`

Runtime: **4 ms**

Memory Usage: **9.3 MB**

~~~cpp
class Solution {
public:
    int trap(vector<int>& height) {
        if(height.empty())
        {
            return 0;
        }
        
        int ans = 0;
        int size = height.size();
        vector<int> left_max(size);
        vector<int> right_max(size);
        // find max height of bar from left end up to an
        // index i in the array left_max
        left_max[0] = height[0];
        for(int i = 1; i < size; i++)
        {
            left_max[i] = max(height[i], left_max[i-1]);
        }
        
        // find max height of bar from right end up to an
        // index i in the array right_max
        right_max[size-1] = height[size-1];
        for(int i = size-2; i >= 0; i--)
        {
            right_max[i] = max(height[i], right_max[i+1]);
        }
        
        // count units of trapped rain water, get min value
        // from left_max and right_max at i, then subtract by
        // height at i, add to ans to get total trapped water
        for(int i = 1; i < size - 1; i++)
        {
            ans += min(left_max[i], right_max[i]) - height[i];
        }
        
        return ans;
    }
};
~~~

**Complexity Analysis**

Time complexity: O(n).

- We store the maximum heights upto a point using 2 iterations of O(n) each.
- We finally update ans using the stored values in O(n).

Space complexity: O(n) extra space.

- Additional O(n) space for left_max and right_max arrays than in Approach 1.

### Approach 3: Using Stacks

**Intuition**

Instead of storing the largest bar upto an index as in Approach 2, we can use stack to keep track of the bars that are bounded by longer bars and hence, may store water. Using the stack, we can do the calculations in only one iteration.

We keep a stack and iterate over the array. We add the index of the bar to the stack if bar is smaller than or equal to the bar at top of stack, which means that the current bar is bounded by the previous bar in the stack. If we found a bar longer than that at the top, we are sure that the bar at the top of the stack is bounded by the current bar and a previous bar in the stack, hence, we can pop it and add resulting trapped water to ans.

**Algorithm**

- Use stack to store the indices of the bars.
- Iterate the array
    - While stack is not empty and height[current]>height[st.top()]
    - It means that the stack element can be popped. Pop the top element as top.
    - Find the distance between the current element and the element at top of stack, which is to be filled. `distance=current−st.top()−1`
    - Add resulting trapped water to answer ans+=distance×bounded_height
- Push current index to top of the stack
- Move current to the next position

Runtime: **24 ms**

Memory Usage: **9.4 MB**

~~~cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        int current = 0;
        stack<int> st;
        
        // Use stack to store indices of the bars
        // iterate the array
        while(current < height.size())
        {
            // loop while stack isn't empty and current element > stack element
            while(!st.empty() && height[current] > height[st.top()])
            {
                cout << "current = " << current << endl;
                cout << "st.size() = " << st.size() << endl;
                // means the stack element can be popped, pop top element as top
                int top = st.top();
                cout << "stack top = " << top << endl;
                st.pop();
                if(st.empty())
                {
                    cout << "stack empty break" << endl;
                    break;                    
                }
                
                // find distance between current element and element at top of stack,
                // which is to be filled.
                int distance = current - st.top() - 1;
                cout << "distance = " << distance << endl;
                
                // find the bounded height bounded_height
                int bounded_height = min(height[current], height[st.top()]) - height[top];
                cout << "bounded_height = " << bounded_height << endl;
                
                // add resulting trapped water
                ans += distance*bounded_height;
            }
            // push current index to top of the stack
            // , then move current to next position
            st.push(current++);
        }
        return ans;
    }
};
~~~

**Complexity Analysis**

Time complexity: O(n).

- Single iteration of O(n) in which each bar can be touched at most twice(due to insertion and deletion from stack) and insertion and deletion from stack takes O(1) time.

- Space complexity: O(n). Stack can take upto O(n) space in case of stairs-like or flat structure.

### Approach 4: Using 2 Pointers

**Intuition**

As in Approach 2, instead of computing the left and right parts seperately, we may think of some way to do it in one iteration. From the figure in dynamic programming approach, notice that as long as `right_max[i]>left_max[i]` (from element 0 to 6), the water trapped depends upon the left_max, and similar is the case when `left_max[i]>right_max[i]` (from element 8 to 11). So, we can say that if there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction (from left to right). As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left). We must maintain `left_max` and `right_max` during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.

**Algorithm**

- Initialize left pointer to 0 and right pointer to size-1
- While left < right, do:
    - If height[left] is smaller than height[right]
        - If height[left]≥left_max, update left_max
        - Else add left_max−height[left] to ans
        - Add 1 to left
    - Else
        - If height[right]≥right_max, update right_max
        - Else add right_max-height[right] to ans
        - Subtract 1 from


Runtime: **4 ms**

Memory Usage: **9.2 MB**

~~~cpp
class Solution {
public:
    int trap(vector<int>& height) {
        // using 2 pointers
        int left = 0;
        int right = height.size() - 1;
        int ans = 0;
        int left_max = 0;
        int right_max = 0;
        
        // iterate the array while left pointer not reached right
        while(left < right)
        {
            // check is left height smaller than right height
            if(height[left] < height[right])
            {
                // check is left height bigger or equal to left height max,
                // if true, set left height max to left height
                // otherwise, add trapped water to total trapped water
                height[left] >= left_max ? (left_max = height[left]) : ans += (left_max - height[left]);
                // add 1 to left pointer
                ++left;
            }
            else
            {
                // check is right height bigger or equal to right height max,
                // if true, set right height max to right height
                // otherwise, add trapped water to total trapped 
                height[right] >= right_max ? (right_max = height[right]) : ans += (right_max - height[right]);
                // subtract 1 from right pointer
                --right;
            }
        }
        return ans;
    }
};
~~~

**Complexity analysis**

Time complexity: O(n). Single iteration of O(n).

Space complexity: O(1) extra space. Only constant space required for left, right, left_max and right_max.