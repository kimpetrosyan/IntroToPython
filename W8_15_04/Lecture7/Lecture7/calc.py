import pretty_print



def calculate_cube(x):
    return x**3

def calculate_square(x):
    return x**2

def main():
    x1 = calculate_square(2)
    pretty_print.simple_print(x1)
    
    x2 = calculate_cube(4)
    pretty_print.pro_print(x2)
    
if __name__ == '__main__':
    main()