# Example of while loop, break, continue, and else statement

# Print i as long as i is less than 6
i = 1
while i < 6:
  print(i)
  i += 1

# Exit the loop when i is 3 using break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# Continue to the next iteration if i is 3 using continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Print a message once the condition is false using else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
