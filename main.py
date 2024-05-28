from shapes import Shape, rectangle, triangle

def Rec_Calc():
    width = int(input("Enter Rectangle Width: "))
    height = int(input("Enter Rectangle Height: "))
    rectangle1 = rectangle(width, height)
    print(f"\nRectangle Area = {rectangle1.area()}\nRectangle Perimeter = {rectangle1.perimeter()}")
    
def Tri_Calc():
    base = int(input("Enter Triangle Base: "))
    length = int(input("Enter a Triangle Length: "))
    length2 = int(input("Enter the other Triangle Length: "))
    triangle1 = triangle(base, length, length2)
    print(f"\nTriangle Perimeter = {triangle1.perimeter()}\n")
    choice3 = input("Type 1 to calculate area, 2 to calcualte height, or any key to exit ")
    if choice3 is "1":
        print("\n--AREA CALCULATOR--\n")
        print(f"Triangle Area = {triangle1.area()}")
    if choice3 is "2":
        print("\n--HEIGHT CALCULATOR--\n")
        print(f"Triangle Height = {triangle1.height()}")
        
print()
print()
print()
print("---SHAPE CALCULATOR---")
print()
print("1. Rectangle Calcutaor")
print("2. Triangle Calcutaor")
print()
choice = input("Select a Calculator type (Enter 1 or 2): ")

if choice == "1":
    Rec_Calc()
    
if choice == "2":
    Tri_Calc()




