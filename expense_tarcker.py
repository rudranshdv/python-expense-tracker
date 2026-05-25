print("---- Daily Expense Tracker ----")


Food = float(input("Enter food expenses: $"))
Transport = float(input("Enter transport expenses: $"))
Entertainment = float(input("Enter entertainment expenses: $"))
Other = float(input("Enter other expenses: $"))

Total = Food + Transport + Entertainment + Other


print(f"Food expenses are: ${Food}")
print(f"Transport expenses are: ${Transport}")
print(f"Entertainment expenses are: ${Entertainment}")
print(f"Other expenses are: ${Other}")
print(f"Total expenses are: ${Total}")