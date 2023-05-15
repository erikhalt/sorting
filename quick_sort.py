
def sort(lista,start,end):
    idx = start-1
    pivot = lista[end]
    for i in range(start,end):

        if pivot >= lista[i]:
            idx += 1
            if lista[i] == lista[idx]:
                pass
            if lista[i] < lista[idx]:
                lista[idx],lista[i] = lista[i],lista[idx]
                print(lista)
        else:
            pass
    return idx+1,lista
  

def quicksort(lista,start,end):
    
    if start < end:
        print(start,end)
        pivot,lista = sort(lista,start,end)
        quicksort(lista,start,pivot)
        quicksort(lista,pivot+1,end)


org_lista = [3,2,5,0,1,8,7,6,9,4]

quicksort(org_lista,0,(len(org_lista)-1))
