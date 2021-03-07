import numpy as np
# File: mystats.py

# define the is_iter function
def is_iter(v):
    v_is_iter = True
    try:
        iter(v)
    except:
        v_is_iter = False
    return v_is_iter

# define the mean function here
def mean(*args):
    '''return the mean value'''
    if len(args) == 0:
        return "Input invalid! Please check your Input"
    count = 0
    sum1 = 0
    for i in args:
        if is_iter(i):
            sum1 += sum(i)
            count += len(i)
        else:
            sum1 += i 
            count += 1
    return float(sum1/count)

# define the stddev function here
def stddev(*args):
    '''return the standard deviation for arguments input'''
    if len(args) == 0:
        return "Input Invalid! Please check your Input"
    mean1 = mean(*args)
    sum2 = 0
    count = 0
    for i in args:
        if is_iter(i):
            count += len(i)
            for j in i:
                sum2 += (j-mean1)**2
        else:
            sum2 += (i-mean1)**2
            count += 1
            
    return (sum2/(count - 1))**0.5

# define the median function here
def median(*args):
    if len(args) == 0:
        return "Input Invalid! Please check your Input"
    lst_temp = []
    for i in args:
        if is_iter(i):
            lst_temp += list(i)
        else:
            lst_temp.append(i)
    lst_temp.sort()
    len_tmp = int(len(lst_temp))
    if len_tmp % 2 == 0:
        return (lst_temp[int(len_tmp/2)] + lst_temp[int(len_tmp/2) - 1])/2
    else:
        return lst_temp[int(len_tmp/2)]

# define the mode function here
def mode(*args):
    if len(args) == 0:
        return "Input Invalid! Please check your Input"
    
    count_dict = {}
    for i in args:
        if is_iter(i):
            for j in i:
                if j in count_dict.keys():
                    count_dict[j] += 1
                else:
                    count_dict[j] = 0
        else:
            if i in count_dict.keys():
                count_dict[i] += 1
            else:
                count_dict[i] = 0
    
    max_count = max(count_dict.values())
    out = []
    for i in count_dict.keys():
        if count_dict[i] == max_count:
            out.append(i)

    return tuple(out)
    
    
    


# part (a)
# print('The current module is:', __name__)
# the current module is: __main__, which should be the module I am currently editing and testing

if __name__ == '__main__':
    # part (b)
    print('mean(1) should be 1.0, and is:', mean(1))
    print('mean(1,2,3,4) should be 2.5, and is:',
                                        mean(1,2,3,4))
    print('mean(2.4,3.1) should be 2.75, and is:',
                                        mean(2.4,3.1))
    print('mean() should FAIL:', mean())

    # part (c)
    print('mean([1,1,1,2]) should be 1.25, and is:',
                                   mean([1,1,1,2]))
    print('mean((1,), 2, 3, [4,6]) should be 3.2,' +
          'and is:', mean((1,), 2, 3, [4,6]))

    # part (d)
    # your code here
    for i in range(10):
        print("Draw", i, "from Norm(0,1):", np.random.randn())
    ls50 = [np.random.randn() for i in range(50)]
    print("Mean of", len(ls50), "values from Norm(0,1):", mean(ls50))

    ls10000 = [np.random.randn() for i in range(10000)]
    print("Mean of", len(ls10000), "values from Norm(0,1):", mean(ls10000))

    # part (e)
    # your code here
    np.random.seed(0)
    a1 = np.random.randn(10)
    print("a1:", a1)
    print("the mean of a1 is:", mean(a1))


    # part (f)
    # your code here
    print("the stddev of a1 is:", stddev(a1))

    # part (g)
    # your code here
    print("the median of a1 is:", median(a1))
    # part (h)
    # your code here
    print("mode(1, 2, (1, 3), 3, [1, 3, 4]) is:", mode(1, 2, (1, 3), 3, [1, 3, 4]))




