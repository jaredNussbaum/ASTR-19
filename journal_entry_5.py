import numpy as np
from astropy.table import Table

def gen_table():
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x)
    print(Table([x, y], names=["X", "Sin(X)"]))



if __name__ == "__main__":
    gen_table()
