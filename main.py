from shapes import Shape, rectangle, triangle

def Rec_Calc():
    print("---Rectangle Calculator---")
    print()
    print("1. Calculate Perimeter")
    print("2. Calculate Area")
    def Rec_Peri():
        print()
        
        
    
    def Rec_Area():
        print()
    
def Tri_Calc():
    print("---Triangle Calculator---")
    print()
    print("1. Calculate Perimeter")
    print("2. Calculate Area")
    

print("---SHAPE CALCULATOR---")
print()
print("1. Rectangle Calcutaor")
print("2. Triangle Calcutaor")
user_input = input(("Select a Calculator type (Enter 1 or 2): "))

if user_input == 1:
    Rec_Calc()
    
if user_input ==  2:
    Tri_Calc()
    
else:
    print("Error, 1 or 2 not detected, enter 1 for rectangle, 2 for triangle")



