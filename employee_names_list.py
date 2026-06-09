# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Employee Names List
# DATE WRITTEN: 10/21/2020
# UPDATED:      2026 — SYNTAX ERROR FIX: line 58 had print("SORTED LIST", "^60"))
#                      missing format() and had extra ) — fixed to
#                      print(format("SORTED LIST", "^60")). Fixed typo
#                      "positve" → "positive". Renamed to snake_case.
#
# PURPOSE: Illustrate how to create and use an array/list by storing
#          employee names entered by the user, displaying them unsorted,
#          then sorting and displaying them in alphabetical order.
#
# KEY CONCEPTS:
#   - Defining a list: name = [""] * size
#   - Populating a list with a WHILE loop using an index
#   - list.sort() — sorts the list alphabetically in ascending order
#   - format() with centering — format("text", "^60") centers in 60 chars

# ============================================================
# Define the number of elements that will be saved in the name list
# Input for number of elements in the list

print("How many names will be entered into this list?")

# Validate that size is a positive integer
while True:
    try:
        size = int(input())
    except ValueError:
        print("WRONG DATA TYPE — Enter a positive whole number.\n")
        continue
    else:
        if size <= 0:
            print("NEGATIVE VALUE ENTERED — Enter a positive whole number.\n")
            continue
        else:
            break  # Valid input received

# ============================================================
# Declare variables
# Initialize the name list — pre-filled with empty strings
name = [""] * size

# Initialize loop control variable / index
count = 0

# ============================================================
# WHILE LOOP — build or populate the name list
while count < size:
    print("Enter name #" + str(count + 1) + ":")
    name[count] = input()   # Store each name at the current index position
    count = count + 1       # Update index to move to the next position

# ============================================================
# Display the UNSORTED list

# Reset count back to 0 for display loop
count = 0

# Display column header for unsorted list
print(format("UNSORTED LIST", "^60"))
print("~" * 60)

# Reset count back to 0
count = 0

# WHILE LOOP — display each name in the unsorted list
while count < size:
    print(format(name[count], "^60s"))   # Display name centered in 60 characters
    count = count + 1
print("~" * 60)

# ============================================================
# Sort the list alphabetically using built-in sort method
name.sort()  # Built-in function/method to sort list in ascending order

# ============================================================
# Display the SORTED list

# Display column header for sorted list — FIXED: was missing format()
print(format("SORTED LIST", "^60"))
print("~" * 60)

# Reset count back to 0
count = 0

# WHILE LOOP — display each name in the sorted list
while count < size:
    print(format(name[count], "^60"))   # Display name centered in 60 characters
    count = count + 1
print("~" * 60)

# END PROGRAM
