def text_converter():
    print("=== Lowercase to Uppercase Text Converter ===")
    text = input("Enter text (lowercase or mixed): ")
    uppercase_text = text.upper()
    print(f"-> Converted Uppercase Output: {uppercase_text}")

if __name__ == "__main__":
    text_converter()