print("Loan Calculator")
print()
print("$1000 over 10 years at 5% APR")
amount = 1000
apr = 0.05
for i in range(10):
  amount+=(amount*apr)
  print("Year", i+1, "is",round(amount,2))
  
  