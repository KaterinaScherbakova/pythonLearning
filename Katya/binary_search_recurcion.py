sort_list = [1,2,5,9,15,32,55,68,99]
found= 32

def bin(sort_list, found, left, rigth):
    if left==rigth:
        return left if sort_list[left] == found else 'Такого числа нет в списке!'
    middle = (left + rigth) // 2
    if found > sort_list[middle]:
        return bin(sort_list,found, middle+1, rigth)
    elif found < sort_list[middle]:
        return bin(sort_list, found, left, middle-1)
    return middle

print(f'Индекс искомого числа = {bin(sort_list,found,0,len(sort_list)-1)}')
print(bin(sort_list,-32,0,len(sort_list)-1)) # если числа нет в списке