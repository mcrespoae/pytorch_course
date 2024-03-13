import torch
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    a = torch.linspace(0, 2*np.pi, 100)
    b = torch.sin(a)

    plt.plot(a, b)
    plt.show()