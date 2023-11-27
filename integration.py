from scipy.integrate import quad, dblquad
from numpy import inf, exp


# Single
def s_int(function, l, u):
    
    """
    SINGLE INTEGRAL
    function: function to integrate. Wrap in quotation marks. Must be in form of "y=..."
    l / u: lower and upper bounds of integration. May not be a function. Do not wrap in quotation marks.
    """
    
    def integrand(x):
        return eval(function)

    return quad(integrand, l, u)[0]

# Double
def d_int(function, llx, ulx, lly, uly):

    """
    DOUBLE INTEGRAL
    function: function in terms of z. Enclosed in quotation marks.
    llx / ulx: x lower and upper bounds of integration (outer integral) - CANNOT BE VARIABLE. Is NOT enclosed in quotation marks.
    lly / uly: y lower and upper bounds of integration (inner integral) - CAN BE VARIABLE. Enclosed in quotation marks.
    
    """
    
    def integrand(y, x):
        return eval(function)
    
    def upper_limit_y(x):
        return eval(uly)
    
    def lower_limit_y(x):
        return eval(lly)

    return(dblquad(integrand, llx, ulx, lower_limit_y, upper_limit_y)[0])
