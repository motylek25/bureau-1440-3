def A_40():
    f = [1, 3]  
    A = [1, 3]  
    while len(A) < 40:
        next_val = 5 * f[-1] + f[-2]
        f.append(next_val)
        if next_val % 2 != 0:
            A.append(next_val)   
    return A[39]
res = A_40()  
print(res)
