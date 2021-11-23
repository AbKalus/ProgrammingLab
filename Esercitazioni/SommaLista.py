def sum_list(the_list):
    acc=0
    for i in range(len(the_list)):
        acc = acc + the_list[i]
    return acc
print("Somma my_list: ", sum_list([1,2,3,4,5,6,7,8,9]))
#print("Somma my_list: {}".format(sum_list([1,2,3,4,5,6,7,8,9])))