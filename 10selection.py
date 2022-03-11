from tkinter.ttk import LabeledScale


number = 200
if number < 100:
    print("A szám kissebb, mint száz")
print("end")

number = 5
if number < 0:
    print("negatív")
elif number == 0:
    print("nulla")
    print("szám")
else:
    print("pozitív")

number2 = 5
if number2 % 2 == 0:
    print("páros")
else:
    ("páratlan")

numbers = [5, 2, -1, 0, 7, -3]
result1 = 0
for num in numbers:
    if num > 0:
        print(num)
        result1 += num
print(result1)
