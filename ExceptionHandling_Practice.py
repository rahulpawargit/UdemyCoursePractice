
def exceptionHandling():
    try:
        Dict={"make":'Honda', "Model":'i250', "Year":'2019' }
        print(Dict["color"])
        # print(Dict["Year"])



    except KeyError:
          print("Keyerror Catched")
          raise

    except:
          print("Exeption catched")
    else:
        print("There is no error")
    finally:
        print("It will execute always")




exceptionHandling()
