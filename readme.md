This project requires Python 3.6 or higher, as well as the following Python packages:

NumPy
SciPy
Matplotlib
To install these packages, run the following command:
To use this project, import it in your Python code and call the relevant functions. For example, to solve a system of linear equations, you can use the solve_linear_system function:

python
Copy code
import numerical_computing as nc

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
x = nc.solve_linear_system(A, b)

or more information on the functions provided by this project, see the documentation in the doc/ directory. There, you'll find API documentation for each function, as well as examples of how to use them.

If you would like to contribute to this project, please follow the standard GitHub workflow:

Fork the repository
Create a feature branch
Make your changes and commit them
Push your changes to your fork
Submit a pull request
