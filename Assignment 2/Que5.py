def print_binary(num):
    binary = bin(num)[2:]  
    print("Binary representation:", binary)
n = int(input("Enter a number: "))
print_binary(n)
