def readposint():
    try:
        number = int(input("Please enter positive integer number:"))
        if number <= 0:
            raise ValueError

    except TypeError:
        print("Incorrect data type entered")
    except ValueError:
        print("Incorrect value entered for positive integer")
    except KeyboardInterrupt:
        print("User aborted program")


readposint()