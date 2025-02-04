# Took about 20 minutes
# Time Complexity: O(n+m)
# Space Complexity: O(n^2 + m)?
def groupAnagram(strs):
    sorted_strs_dict = {}
    result = []
    for str_item in strs:
        print(f"str_item = {str_item}")
        sorted_str = "".join(sorted(str_item))
        if sorted_str not in sorted_strs_dict:
            sorted_strs_dict[sorted_str] = []

        print(f"sorted_str = {sorted_str}")
        sorted_strs_dict[sorted_str].append(str_item)

    for key, value in sorted_strs_dict.items():
        print(f"Dict Anagram: {key} = {value}")
        result.append(value)

def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = groupAnagram(strs)

if __name__ == "__main__":
    main()
    