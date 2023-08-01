from sympy.parsing.latex import parse_latex
from sympy import latex
from process_latex import process_sympy


# sample latex string
latex_string = r"\frac{1}{2} \int_{-\infty}^{\infty} x^{2} \mathrm{d} x"

# convert latex string to sympy expression
sympy_expr = process_sympy(latex_string)

#create a image of the expression
from sympy import preview
preview(sympy_expr, viewer='file', filename='sympy.png', euler=False)


