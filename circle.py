import math

def circle_calculator():
    print("=== Circle Properties Calculator ===")
    try:
        radius = float(input("Enter radius (r): "))
        if radius < 0:
            print("Radius cannot be negative.")
            return
        
        area = math.pi * (radius ** 2)
        circumference = 2 * math.pi * radius
        
        print(f"-> Area: {area:.2f}")
        print(f"-> Circumference: {circumference:.2f}")
    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    circle_calculator()