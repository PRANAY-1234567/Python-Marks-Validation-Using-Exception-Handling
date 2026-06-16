try:
    marks = int(input("Enter the marks (0-100) : "))

    if marks < 0 or marks > 100:
        raise Exception("Invalid marks")

    print("Valid marks entered")

except Exception as e:
    print("Error :", e)
