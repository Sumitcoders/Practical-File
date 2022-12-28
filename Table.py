#h3kler

print("ENTER THE NUMBER")

a = int(input("=>"))
i = 1
print("Upto which number you want to find multiples?")
b = int(input("=>"))
if a == 0:
      print("0 multiplied by any number is zero mother fucker!")
elif a<0:
      print("please enter positive values")
else:
      pass
while i<=b:
      print(f"{a} X {i} = {a*i}")
      i = i+1
