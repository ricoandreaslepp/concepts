for i in range(10):
  if i==2:
    print("1. break")
    break
else:
  print("1. executed the whole loop")
  
for i in range(10):
  pass
else:
  print("2. executed the whole loop")
  
  
# useful in nested loops:
for i in range(15):
  
  for j in range(3):
    
    print(f"i, j {i, j}")
    if i==3 and j==2:
      break
      
  else:
    continue
  break
