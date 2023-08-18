def isfat(bmi):
    if bmi < 18.5:
        print("thin")
    elif bmi > 22.9:
        print("fat")
    else:
        print("normal")