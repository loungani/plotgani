import numpy as np
import matplotlib.pyplot as plt

def PolynomialLeastSquares(x, y, degree):
    # Create A matrix
    A = np.empty([degree + 1, degree + 1])

    # Fill the A matrix
    for i in range(0, degree + 1):
        for j in range(0, degree + 1):
            sum = 0;
            for value in x:
                sum += np.power(value, i + j)
            A[i][j] = sum;

    # Create the b matrix
    b = np.empty([degree + 1, 1])
    for i in range(0, degree + 1):
        sum = 0;
        for idx in range(0, len(x)):
            sum += y[idx] * np.power(x[idx], i)
        b[i] = sum;
    return A, b

def systemSolve(A, b):
    return np.dot(np.linalg.inv(np.dot(A.T, A)),np.dot(A.T, b))

def printPolynomial(coef_list):
    polynomial_string = ''
    for i in range(0, len(coef_list)):
        polynomial_string += str(coef_list[i][0])
        polynomial_string += ('*x^' + str(i))
        if (i < (len(coef_list)-1)):
            polynomial_string += ' + '
    print(polynomial_string)

def getPredictFunction(coef_list):
    def f(value):
        sum = 0;
        for i in range(0, len(coef_list)):
            sum += coef_list[i][0]*np.power(value, i)
        return sum
    return f

def getSSR(x, y, predictFunction):
    sum = 0;
    for idx in range(0, len(x)):
        residual = predictFunction(x[idx]) - y[idx]
        sum += np.power(residual, 2)
    return sum


def plotLS(x, y, degree, stepSize):
    A, b = PolynomialLeastSquares(x, y, degree)
    coef_list = systemSolve(A, b)
    f = getPredictFunction(coef_list)

    ssr = np.around(getSSR(x, y, f), decimals=6)

    x_ls = np.arange(x[0], x[len(x) - 1] + stepSize, stepSize)
    y_ls = np.arange(x[0], x[len(x) - 1] + stepSize, stepSize)
    for idx in range(0, len(x_ls)):
        y_ls[idx] = f(x_ls[idx])

    plt.plot(x_ls, y_ls, color='blue')
    plt.scatter(x, y, color='red')
    plt.title('Polynomial of degree ' + str(degree) + ', SSR = ' + str(ssr))
    plt.show()