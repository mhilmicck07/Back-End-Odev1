boy = float(input('Boyunuz(m): '))
kilo = float(input('Kilonuz(kg): '))

endeks = round(float(kilo / (boy * boy)),1)
print(endeks,'kg/m2')

if endeks < 18.5:
    print('Zayıfsın. Biraz kilo al!')
elif endeks >= 18.5 and endeks < 24.9:
    print('Normal Kilodasın')
elif endeks >=25.0 and endeks < 29.9:
    print('Hafif Kilolusun. Biraz az ye de zayıfla')
elif endeks >= 30.0 and endeks < 34.9:
    print('1.Derece Obezsin! Kilo vermen şart!!!')
elif endeks >= 35.0 and endeks < 39.9:
    print('2.Derece Obezsin! Ağır yaşamlar vol.1!')
elif endeks >= 40.0:
    print('3.Derece Obezsin! Ağır yaşamlar vol.2!')
else:
    print('Çok cahilsin keşke ölsen')