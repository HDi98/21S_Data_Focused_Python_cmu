import numpy as np
# File: mystats.py

# define the mean function here
def mean(n, *args):
    def get_ttl(x):
        try:
            return sum(x)
        except:
            return x
    def get_numel(x):
        try:
            return len(x)
        except:
            return 1

    ttl = get_ttl(n)
    numel = get_numel(n)

    for arg in args:
        ttl += get_ttl(arg)
        numel += get_numel(arg)
    return ttl / numel

# define the stddev function here
def stddev(n, *args):
    numerator = 0
    denominator = 0
    x_bar = mean(n, *args)
    all_args = [n]
    all_args.extend(args)
    for arg in all_args:
        try:
            denominator += len(n)
            numerator += sum((np.array(list(n)) - x_bar) ** 2)
        except:
            denominator += 1
            numerator += arg
    try:
        return (numerator / (denominator-1)) ** 0.5
    except:
        print("Sample standard deviation needs more than 1 number")
        return None

# define the median function here
def median(n, *args):
    def is_iterable(x):
        try:
            iter(x)
            return True
        except:
            return False
    elements = []
    all_args = [n]
    all_args.extend(args)
    for arg in all_args:
        elements.extend(arg) if is_iterable(arg) else elements.append(arg)
    if len(elements) % 2 == 1:
        # odd number of elements
        return sorted(elements)[len(elements) // 2]
    else:
        # even number of elements
        x1 = sorted(elements)[len(elements) // 2 - 1]
        x2 = sorted(elements)[len(elements) // 2]
        return (x1 + x2) / 2

# define the mode function here
def mode(n, *args):
    counts = {}
    all_args = [n]
    all_args.extend(args)
    for arg in all_args:
        try:
            for e in arg:
                counts[e] = counts.get(e, 0) + 1
        except:
            counts[arg] = counts.get(arg, 0) + 1
    sorted_elements = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    results = []
    for i in range(len(sorted_elements)):
        if i == 0:
            results.append(sorted_elements[i][0])
        else:
            if sorted_elements[i][1] == sorted_elements[i-1][1]:
                results.append(sorted_elements[i][0])
                continue
            break
    return tuple(results)

if __name__ == '__main__':
    # part (a)
    print('The current module is:', __name__)
    # Below is the output of this print statement:
    # The current module is: __main__

    # part (b)
    print('mean(1) should be 1.0, and is:', mean(1))
    print('mean(1,2,3,4) should be 2.5, and is:',
                                        mean(1,2,3,4))
    print('mean(2.4,3.1) should be 2.75, and is:',
                                        mean(2.4,3.1))
    # print('mean() should FAIL:', mean())

    # part (c)
    print('mean([1,1,1,2]) should be 1.25, and is:',
                                   mean([1,1,1,2]))
    print('mean((1,), 2, 3, [4,6]) should be 3.2,' +
          'and is:', mean((1,), 2, 3, [4,6]))

    # part (d)
    for i in range(10):
        print("Draw", i, "from Norm(0,1):",
                np.random.randn())
    ls50 = [np.random.randn() for _ in range(50)]
    print("Mean of", len(ls50), "values from Norm(0,1):", mean(ls50))
    ls10000 = [np.random.randn() for _ in range(10000)]
    print("Mean of", len(ls10000), "values from Norm(0,1):", mean(ls10000))

    # part (e)
    np.random.seed(0)
    a1 = np.random.randn(10)
    print("a1:", a1) # should display an ndarray of 10 values
    print("the mean of a1 is:", mean(a1))

    # part (f)
    print("the stddev of a1 is:", stddev(a1))

    # part (g)
    print("the median of a1 is:", median(a1))
    print("median(3, 1, 5, 9, 2):", median(3, 1, 5, 9, 2))

    # part (h)
    print("mode(1, 2, (1, 3), 3, [1, 3, 4]) is:",
            mode(1, 2, (1, 3), 3, [1, 3, 4]))
