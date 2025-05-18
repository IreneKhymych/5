import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_function(expr, x_range, output_folder):
    x = np.linspace(x_range[0], x_range[1], 400)
    allowed_names = {"x": x, "np": np, "sin": np.sin, "cos": np.cos, "exp": np.exp, "log": np.log, "sqrt": np.sqrt, "tan": np.tan}

    try:
        y = eval(expr, {"__builtins__": {}}, allowed_names)
    except Exception as e:
        raise ValueError(f"Помилка у виразі: {e}")

    plt.figure()
    plt.plot(x, y)
    plt.title(f"Графік: y = {expr}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    img_path = os.path.join(output_folder, "plot.png")
    plt.savefig(img_path)
    plt.close()
    return img_path
