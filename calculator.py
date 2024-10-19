if __name__ == "__main__":
    print("Basic Calculator is ready!")
    
    while True:
        operation = input("Choose operation (add, subtract, multiply, divide) or 'exit' to quit: ")
        
        if operation == 'exit':
            break
            
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if operation == 'add':
            print(f"Result: {add(a, b)}")
        elif operation == 'subtract':
            print(f"Result: {subtract(a, b)}")
        elif operation == 'multiply':
            print(f"Result: {multiply(a, b)}")
        elif operation == 'divide':
            print(f"Result: {divide(a, b)}")
        else:
            print("Invalid operation. Please try again.")
