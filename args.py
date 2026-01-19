def double_val(x, *args):
    for a in args:
        print( x * a )

double_val(2,9,8,4,5,6)


def func(x = 5, y = 3):
    print(x + y)
    
func(2)


def func2(*proben, **kwekwek):
    print(proben)
    print(kwekwek)
    
func2(1,2,3,4,x = 5, y = 3)
