import matplotlib.pyplot as plt
from scipy import integrate
from numpy import *

# Polar Plot

def pplot(radius_function, theta_lower = 0, theta_upper = 2*pi):
    
    """
    radius_function: write a function in terms of 'r.' Wrap it in quotation marks.
    theta_lower / theta_upper: the bounds for theta. If left empty, default bounds are 0 -> 2pi.
    """

    # Polar Coordinates
    theta = linspace(theta_lower, theta_upper, 100) # Theta is a range from one value to another
    radius = eval(radius_function) # Change radius from string to something able to be evaluated

    # Formatting Graph
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, radius) # Plots theta vs radius
    ax.set_rmax(2)
    ax.set_rticks([1, 2, 3, 4, 5])  # Less radial ticks
    ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)

    # Plot
    ax.set_title("Polar Plot", va='bottom')
    plt.show()

# Polar Shade

def pshade(radius_function, theta_lower = 0, theta_upper = 2*pi):

    """
    radius_function: write a function in terms of 'r.' Wrap it in quotation marks.
    theta_lower / theta_upper: the bounds for theta. If left empty, default bounds are 0 -> 2pi.
    """
    
    # Theta
    
    theta = linspace(theta_lower, theta_upper, 100)

    # Radius
    
    rfunc = lambda theta: eval(radius_function) # Change string input into a "function"
        
    r = []
    for n in theta: # Make a list of radius points
        r.append(rfunc(n))

    r2 = [0 if i < 0 else i for i in r] 
        # Replace all negative points in list with 0. 
        # I ran into some problems with negative numbers that shouldn't exist. I think it is related to the way that
        # matplotlib.pyplot transposes cartesian graphs to polar

    # Formatting Graph

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_rmax(2)
    ax.set_rticks(arange(1, 100, 1))  # Less radial ticks
    ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)

    # Plot
    ax.fill_between(linspace(theta_lower, theta_upper, 100), 0, r2)
    fig.tight_layout()
    plt.show()

# Polar Integration
def polar_area(radius_function, tl=0, tu=2*pi, rl=0, ru=1):

    """
    radius_function: write a function in terms of 'r.' Wrap it in quotation marks.
    tl / tu: the bounds for theta. If left empty, default bounds are 0 -> 2pi.
    rl / ru: the bounds for radius. If left empty, default bounds are 0 -> 1.
    """
    
    def integrand(r, theta):
        return eval(("(" + radius_function) + ")*r")
  
    print(dblquad(integrand, tl, tu, rl, ru))