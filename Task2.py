# Task 2 of Assignment 5 - Demonstrating List Slicing

org_list = [i for i in range(1,11)]         # creation of list
print(f"Original List: {org_list}")

ext_list = org_list[0:5]                    # extraction of first five elements from list
print(f"Extracted first five elements of list: {ext_list}")

rev_ext_list = ext_list[::-1]               # reversal of extracted list
print(f"Reversed extracted list: {rev_ext_list}")

# end of program