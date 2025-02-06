
# Given int array nums, k, return k most frequent elements, any order fine

def topKFreqElements(nums, k):
    top_freq_elms_dict = {}
    res = []

    for num in nums:
        if num not in top_freq_elms_dict:
            top_freq_elms_dict[num] = 0
        top_freq_elms_dict[num] += 1

    print("top_freq_elms_dict = ", top_freq_elms_dict)

    desc_top_freq_elms = sorted(top_freq_elms_dict.items(), key=lambda item: item[1], reverse=True)

    print("desc_top_freq_elms = ", desc_top_freq_elms)

    it = 0
    for key, value in desc_top_freq_elms:
        print("key = ", key)
        if it < k:
            res.append(key)
        else:
            break
        it += 1
    return res

def main():
    nums = [1,1,1,2,2,3]
    k = 2

    res = topKFreqElements(nums, k)
    print(res)

if __name__ == "__main__":
    main()