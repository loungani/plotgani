import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def riemann_sum(a, b, f, n):
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,
                                   figsize=(10, 5))
    
    x = np.arange(a, b+0.001, 0.001)
    vfunc = np.vectorize(f)
    y = vfunc(x)
    
    partition = (b-a)/n
    
    area = 0
    for i in np.arange(0, n, 1):
        ax1.add_patch(patches.Rectangle((a+i*partition, 0), partition, f(a+i*partition), color='orange'))
        area += abs((partition*f(a+i*partition)))
    ax1.set_title('Lower sum: n=' + str(n) + ', Area=' + str(round(area, 3)))
    ax1.plot(x,y, color='blue')

    area = 0
    for i in range(0, n):
        ax2.add_patch(patches.Rectangle((a+i*partition, 0), partition, f(a+(i+1)*partition), color='red'))
        area += abs((partition*f(a+(i+1)*partition)))
    ax2.set_title('Upper sum: n=' + str(n) + ', Area=' + str(round(area, 3)))
    ax2.plot(x,y, color='blue')
    plt.show()