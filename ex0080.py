lista = []

for cont in range (0,5):
    vl= int( input('digite um valor: ') )
    ele = 0
    if len(lista)==0:
        lista.append(vl)
    else:
        for i in lista:
            if vl <= i:
                lista.insert(ele,vl)
                break
            ele+=1
        else:
            lista.append(vl)

print(lista)