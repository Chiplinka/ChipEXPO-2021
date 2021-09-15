size = 3 # Размер квадратной матрицы 
par = size**2 + 1
for i in range(1, par):
    ia = ''
    ib = ''
    oa = ''
    ob = ''
    oc = 'c' + str(i)
    if i % size == 1:
        ia = "a" + str(i//size + 1)
    else:
        ia = "a{}{}".format(str(i - 1), str(i))
    if i <= size:
        ib = "b" + str(i)
    else:
        ib = "b{}{}".format(str(i - size), str(i))
    if (i + 1) % size == 1:
        oa = "a" + str(i)
    else:
        oa = "a{}{}".format(str(i), str(i + 1))
    if i % size == 0:
        oa = ''
    ob = "b{}{}".format(str(i), str(i + size))
    if i > par - size - 1:
        ob = ''
    print("pe pe{} (.clk(clk), .reset(reset), .in_a({}), .in_b({}), .out_a({}), .out_b({}), .out_c({}));".format(str(i), ia, ib, oa, ob, oc))





    