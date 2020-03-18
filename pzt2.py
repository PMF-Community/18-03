# Zadatak 3. Napisati program koji od korisnika traži da unese petocifren
# broj. Program provjerava da li je uneseni broj petocifren, te ukoliko jeste,
# raˇcuna i ispisuje razliku njegove druge najve ́ce i njegove najmanje cifre.

broj=int(input("Unesi neki petocifren broj: "))

if broj<=10000 or broj>=99999:
    print("Broj nije petocifren.")
else:
    e=broj%10
    cetverocifrenBroj=broj//10

    d=cetverocifrenBroj%10
    trocifrenBroj=cetverocifrenBroj//10

    c=trocifrenBroj%10
    dvocifrenBroj=trocifrenBroj//10

    b=dvocifrenBroj%10
    jednocifrenBroj=dvocifrenBroj//10

    a=jednocifrenBroj%10

#maximum algorithm
if a>b and a>c and a>d and a>e:
    najveci=a
elif b>a and b>c and b>d and b>e:
    najveci=b
elif c>a and c>b and c>d and c>e:
    najveci=c
elif d>a and d>b and d>c and d>e:
    najveci=d
else:
    najveci=e

#minimum algorithm
if a<b and a<c and a<d and a<e:
    najmanji=a
elif b<a and b<c and b<d and b<e:
    najmanji=b
elif c<a and c<b and c<d and c<e:
    najmanji=c
elif d<a and d<b and d<c and d<e:
    najmanji=d
else:
    najmanji=e

print(najveci)
print(najmanji)

brojevi=[a,b,c,d,e]
brojevi.sort(reverse=True)
print(brojevi)

drugiNajveciBroj=brojevi[1]

razlikaBrojeva=drugiNajveciBroj-najmanji

print("Razlika brojeva je:",razlikaBrojeva)

#poenta liste je da se poredaju svi brojevi koji nisu najveci i najmanji
#znaci ako upisem 12345, u listu idu 234
# lista=[]
#
# if a < najveci and a>najmanji:
#     lista.append(a)
# elif b<najveci and b>najmanji:
#     lista.append(b)
# elif c<najveci and c>najmanji:
#     lista.append(c)
# elif d<najveci and d>najmanji:
#     lista.append(d)
# else:
#     lista.append(e)

# print(lista())
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
