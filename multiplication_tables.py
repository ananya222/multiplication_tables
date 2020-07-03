def mul_table(which_number,how_many,i):
    product=i*which_number
    print(str(i)+'*'+str(which_number)+'='+str(product))
    i=i+1
    if(i>how_many):
        return
    else:
        mul_table(which_number,how_many,i)

which_number=10
how_many=10
i=0
mul_table(which_number,how_many,i)
