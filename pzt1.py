uB = int(input("Unesi neki trocifren broj: "))

#sredi ovaj uslov nekad pls
if uB<100 | uB>999:
    print('Greska!')
else:
    zCTB=uB%10
    sTBZJC=uB//10
    pCTB=sTBZJC%10
    jB=sTBZJC//10

if  jB-pCTB==1 or jB-zCTB \
 or pCTB-jB==1 or pCTB-zCTB \
 or zCTB-jB==1 or zCTB-pCTB==1:
 print("Broj je dobar!")
else:
    print("Broj nije dobar!")



# print(jB)
# print(pCTB)
# print(zCTB)

#unosBroja = uB
#zCTB - zadnja cifra trocifrenog broja
#sTBZJC - skracen trocifreni broj za jednu cifru
#jB - jednocifren broj
