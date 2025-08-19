def triangle(a,b,c):
    if (a + b > c) and (b + c > a) and (c + a > b):
             print('Triangle can be formed')
             if (a**2)==(b**2)+(c**2) or (b**2)==(c**2)+(a**2) or (c**2)==(a**2)+(b**2):
                    print('Right angled Triangle')
             elif a==b==c:
                    print('Isosceles Triangle')
             elif a==b or b==c or c==a:
                    print('Scalene Triangle')
    else:
            print('Triangle cannot be formed')
triangle(3,4,5)