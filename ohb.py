
def print_formatted(number) -> int:
    for i in range(1,number+1):
        o = octal_number(i)
        h = hex_number(i)
        b = binary_number(i)
        print("{:5d} {:5d} {:>5} {:5d}".format(i, o, h, b))

def octal_number(number):
    res = int(number / 8);
    if res >= 8:
        res = octal_number(res)
    return res * 10 + (number % 8)

def hex_number(number) -> str:
    lib = {0 : 0, 1 : 1, 2: 2, 3 : 3, 4 : 4, 5: 5, 6: 6, 7 : 7, 8 : 8, 9 : 9, 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    res = int(number / 16) 
    if res >= 16:      
        res = hex_number(res)  
    return str(lib[res] if lib[res] != 0 else '') + str(lib[number % 16])

def binary_number(number):
    res = int(number / 2) 
    if res >= 2:      
        res = binary_number(res)  
    return res * 10 + number % 2   
 


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    