import sys

gong_zi = int(sys.argv[1])

suo_de_e = gong_zi - 5000

if suo_de_e in range(0,3001):
    na_shui_e = suo_de_e * 0.03
    print('{:.2f}'.format(na_shui_e))
if suo_de_e in range(3001,12001):
    na_shui_e = suo_de_e * 0.1 - 210
    print('{:.2f}'.format(na_shui_e))
if suo_de_e in range(12001,25001):
    na_shui_e = suo_de_e * 0.2 - 1410
    print('{:.2f}'.format(na_shui_e))
if suo_de_e in range(25001,35001):
    na_shui_e = suo_de_e * 0.25 - 2660
    print('{:.2f}'.format(na_shui_e))
if suo_de_e in range(35001,55001):
    na_shui_e = suo_de_e * 0.3 - 4410
    print('{:.2f}'.format(na_shui_e))
if suo_de_e in range(55001,80001):
    na_shui_e = suo_de_e * 0.35 - 7160
    print('{:.2f}'.format(na_shui_e))
if suo_de_e > 80000:
    na_shui_e = suo_de_e * 0.45 - 15160
    print('{:.2f}'.format(na_shui_e))
