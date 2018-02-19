#Finicky counter program
#loop with a break and continue

count = 0

while True:
  count += 1
  # end loop if count is greater than 10
  if count > 10:
      break
  #skip 5
  if count == 5:
      continue
  print count

raw_input("\n\nPress enter to exit")