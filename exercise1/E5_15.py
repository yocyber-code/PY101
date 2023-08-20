import math
w = int(input())
h = int(input())
monsteller = math.sqrt(w*h/3600)
dubois = 71.84 * (w**0.425) * (h**0.725) / 10000
boyd = 0.0003207 * (h**0.3) * ((1000*w)**(0.7285 - (0.0188 * (3 + math.log10(w)))))
print(monsteller)
print(dubois)
print(boyd)
