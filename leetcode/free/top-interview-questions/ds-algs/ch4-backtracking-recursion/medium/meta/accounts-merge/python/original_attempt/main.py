
def accountsMerge(accounts):
    i = 0
    rows = len(accounts)

    recursiveMerge(accounts, rows, i)

def main():
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    result = accountsMerge(accounts)

if __name__ == "__main__":
    main()
