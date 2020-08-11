#exception handling
#Expection are errors those are handled



a=10
b=0
c=0

def excetionhandlinng():
    try:

        d=(a+b)/c
        print(d)
    except ZeroDivisionError:
        print("we cant not devided by zero")
    except TypeError:
        print("String value not accessble")
    except:
        print("Not possible ")

excetionhandlinng()

