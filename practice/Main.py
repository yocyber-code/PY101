import isfat

weight = float(input())
height = float(input())

height = height / 100;
bmi = weight/height/height;
isfat.isfat(bmi)