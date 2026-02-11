weight=int(input("Enter your weight: "))
unit=input("Enter your unit(Kg or L): ")
if unit in ["l"," L"]:
    weight*=0.453592
    print(f"Your weight is {weight} Kg")
elif unit in ["kg"," Kg","KG","kG"]:
    weight*=2.20462
    print(f"your weight is {weight} L")
else :
    print("Invalid unit")
