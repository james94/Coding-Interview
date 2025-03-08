from collections import defaultdict

# Perplexity AI assistance: https://www.perplexity.ai/search/can-you-solve-the-following-le-LS99sptyRF6e6lFyb3x9rA#0

# Leetcode Question: https://leetcode.com/problems/accounts-merge/

####
#   Clarifying Questions (Before Coding)
####
#
#   1. Understanding the Problem: Two accounts belong to the same person if they share at least
#       one email address. The name associated with each account must be the same for all merged
#       accounts.
#
#   2. Input and Output Format: input is a list of accounts where each account is a list of strings.
#       The first string is the name, and the rest are email addresses. The output should be a list
#       of merged accounts with the name followed by sorted email addresses.
#
####
#   Potential Solutions/Explanation of Data Structures & Algorithms
####
#
#   1. Union-Find Algorithm: can be used to group accounts that share common emails.
#
#   2. Hash Map: Useful for mapping emails to account indices to efficiently identify shared emails.
#
####
#   Solution Explanation
####
#
#   Step 1: Initialize Union-Find Structure
#       - Create a parent array where each account is initially its own parent
#       - Use a hash map to store the mapping of emails to account indices
#
#   Step 2: Iterate Through Accounts and Emails
#       - For each email in an account, check if it exists in the hash map.
#       - If it does, perform a union operation by setting the parent of the current account
#           to the parent of the account associated with the email
#       - If not, add the email to the hash map with its account index.
#
#   Step 3: Merge Accounts
#       - Use another hash map to group emails under their respective root parents
#       - For each account, find its root parent and add its emails to the set of emails for that parent
#
#   Step 4: Compile Merged Accounts
#       - For each unique root parent, create a merged account with the name and sorted emails
#
####
#    Big O Notation (While Coding)
####
#
#   Time Complexity: O(N * M * logM), where "N" is the number of accounts and "M" is the maximum
#       number of emails in an account. The log(M) factor comes from sorting emails.
#
#   Space Complexity: O(N * M), for storing the parent array and the hash maps
#
####
#   Potential Improvements (After Coding)
####
#
#   1. Optimize Storing: if the number of emails gets very large, consider using a more efficient
#       sorting algorithm or data structure like a balanced binary search tree
#
#   2. Reduce Memory Usage: Ensure that unnecessary data structures are cleared or reused to minimize memory footprint
#

def accountsMerge(accounts):
    # Helper function to find the root parent for any index
    def find(index: int) -> int:
        if parent[index] != index:
            parent[index] = find(parent[index])
        return parent[index]

    # The number of accounts
    num_accounts = len(accounts)

    # Initialize a list where the value at index i is the parent of i
    parent = list(range(num_accounts))

    # Dictionary to map each email to its account index
    email_to_account_id = {}

    # Assign parents for accounts with shared emails
    for account_id, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_account_id:
                # Union operation: set the parent of the current account to the account
                # already associated with this email
                parent[find(account_id)] = find(email_to_account_id[email])
            else:
                email_to_account_id[email] = account_id

    # Map each account index to a set of emails under the corresponding parent.
    emails_under_parent_account = defaultdict(set)
    for account_index, account in enumerate(accounts):
        for email in account[1:]:
            emails_under_parent_account[find(account_index)].add(email)

    # Compile the merged accounts: one per parent index
    merged_accounts = []
    for parent_index, emails in emails_under_parent_account.items():
        sorted_emails = sorted(emails)

        # Prepend the account name
        account_name = accounts[parent_index][0]
        merged_account = [account_name] + sorted_emails

        # Append the merged account to the result
        merged_accounts.append(merged_account)
    
    return merged_accounts

def main():
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    result = accountsMerge(accounts)
    print(result)

if __name__ == "__main__":
    main()