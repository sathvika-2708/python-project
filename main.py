size = int(input("Enter a number: ").strip())
def right_triangle_pattern(size):
    for i in range(1, size + 1):
        print(f"{size - i + 1} " * i)
    print()
right_triangle_pattern(size)
