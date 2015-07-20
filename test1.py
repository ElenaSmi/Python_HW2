__author__ = 'Elena'
def my_function(l, n):

    result = []

    for i in range(len(l)):
        if (n - l[i]) in l and n/(n - l[i]) != 2:
            result.append([n - l[i], l[i]])
        elif l.count(n/2) > 1 and l[i] == n/2:
            result.append([n - l[i], l[i]])

    return result

print(my_function([6, 7, 6, 5, 10], 12))