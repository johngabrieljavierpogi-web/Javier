import math

def triangle_calculator():
    print("=== Triangle Calculator ===")
    try:
        base = float(input("Enter base (b): "))
        height = float(input("Enter height (h): "))
        
        if base < 0 or height < 0:
            print("Dimensions cannot be negative.")
            return

        area = 0.5 * base * height
        # Estimated perimeter assuming an isosceles triangle configuration
        hypotenuse = math.sqrt((base / 2) ** 2 + height ** 2)
        perimeter = base + (2 * hypotenuse)
        
        print(f"-> Area: {area:.2f}")
        print(f"-> Estimated Perimeter: {perimeter:.2f}")
    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    triangle_calculator()