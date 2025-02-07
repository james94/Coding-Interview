
def findAllCombinations(digits):
    map_digits_to_letter = {
        1: "",
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"]
    }
    
    result = []

    digits_list = list(digits)

    def find_combinations(digits):


def main():
    digits = "23"
    result = findAllCombinations(digits)

if __name__ == "__main__":
    main()