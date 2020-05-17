import numpy as np 
import matplotlib.pyplot as plt 
import scipy.stats

def array_gen(n):
    c_row =n/2
    c_col = n/2
    arr = np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            val = max( abs(c_row - i)*2/n, abs(c_col-j)*2/n )
            arr[i][j] = (scipy.stats.norm(loc =0, scale=0.8).pdf(val)*2*255)
    return arr

def reflect_img():
    n =1000
    arr = array_gen(n)
    plt.figure(figsize=(8,8))
    ax = plt.gca()
    ax.axis([0,n-1,0,n-1])
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    im = ax.imshow(arr, cmap='gray', vmin=0, vmax=255)
    plt.savefig('reflect.png')
    plt.show()
    
    pass

if __name__=='__main__':
    reflect_img()