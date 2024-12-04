import numpy as np
import matplotlib.pyplot as plt

def julia(c, z, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Childrens' input for a name and two numbers. The numbers are randomly drawn
def get_numbers():
    name = input("Enter your name: ")
    
    real_c = float(input("Enter the real part of c (e.g., -0.7): "))
    imag_c = float(input("Enter the imaginary part of c (e.g., 0.27015): "))
    
    return name, complex(real_c, imag_c)

# Main function to generate the Julia Set
def generate_ornament():
    name, c = get_numbers()
    z_init = complex(0, 1)  # Fixed starting value
    max_iter = 256
    width, height = 800, 800
    x_min, x_max, y_min, y_max = -2.0, 2.0, -2.0, 2.0

    img = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            real = x_min + (x / width) * (x_max - x_min)
            imag = y_min + (y / height) * (y_max - y_min)
            img[y, x] = julia(c, complex(real, imag), max_iter)
    
    plt.imshow(img, extent=[x_min, x_max, y_min, y_max], cmap='plasma')
    plt.suptitle(f"{name}'s Julia Set", fontsize=16)
    plt.title(f"With c = {c} and fixed start z = {z_init}")

    # Save the image as NAME.pdf
    plt.savefig(f"{name}.pdf")
    print(f"Image saved as {name}.pdf")

    # Display the image
    plt.show()

# Start the program
generate_ornament()
