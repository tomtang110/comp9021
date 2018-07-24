def judge(a0,grid,double_bra,L=1,count=1):

    panduan1=panduan(double_bra,grid)
    if panduan1:
        a11=a0[0],b11=a0[1]
        a12 = a11+1
        b12 = b11 - 1
        n = L*2
        b13 = L + n -1
        L += 1
        new =[]
        a1=[a12,b12]
        for each_element in range(0,b13+1):
            new.append([a12,b12+each_element])
        judge(a1,grid,new,L,count)
        return count + judge(a1,grid,new,L,count)
    else:
        return 0

def panduan(n,grid):
    try:
        count_n=0
        n_len = len(n)
        for each in n:
            if grid[each[0]][each[1]] == 1:
                count_n += 1
            else:
                count_n += 0
        if n_len == count_n:
            return True
        else:
            return False
    except IndexError:
        return False


    

    
     