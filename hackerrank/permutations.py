# Python program to print all
# the possible combinations

def comb(L):
    n = 2
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):

                # check if the indexes are not
                # same
                if (i!=j and j!=k and i!=k):
                    if(L[i] + L[j] + L[k] != n):
                        print(L[i], L[j], L[k])

# Driver Code
comb([1, 1, 1])
