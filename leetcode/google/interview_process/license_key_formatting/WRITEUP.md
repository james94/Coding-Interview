# License Key Formatting (Solution)

We will go through a step-by-step explanation:

## Data Structure Choice

We use a `std::string` as our primary data structure. It's efficient for this problem because it allows dynamic resizing and provides fast access to characters.

## Memory Pre-allocation

We reserve memory for the result string upfront to avoid multiple reallocations during the process.

## Removing Dashes & Converting to Uppercase

- We use `std::copy_if` to remove dashes
- We use `std::transform` to convert to uppercase
- We iterate from the end of the string to simplify the grouping process later

## Insert Dashes

- We insert dashes from right to left, which allows us to maintain the correct grouping without worrying about the potentially shorter first group.

## Reversing the Result

Since we built the string in reverse, we need to reverse it at the end.

## Time Complexity: O(n)

`n` is the length of the input string. We perform a linear scan of the input and a constant number of operations per character.

## Space Complexity: O(n)

O(n) as we create a new string to store the result.

## Software Infrastructure Perspective

1. **Modularity**: the solution is encapsulated in a class, making it easy to integrate into larger systems.

2. **Efficiency**: we use C++20 standard library functions for better performance.

3. **Memory Management**: we pre-allocate memory to reduce the number of reallocations.

4. **Readability**: the code is structured in a way that each step is clear and separate.

## Resources

- While exploring how to solve this problem, I had assistance from Perplexity AI on how to solve it from a software design and development perspective: https://www.perplexity.ai/search/you-are-a-software-engineer-ai-xdA48g27RCynedwEOVu17Q
