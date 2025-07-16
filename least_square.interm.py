import numpy as np

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200 , -50, 5000, 100])    # coefficient values
 
def squared_error(X, y, c):
    sse = 0.0
    price = (X @ c)  # calculate the predicted price using matrix multiplication
    difference = price - y  # calculate the difference between predicted and actual prices
    difference *= difference  # square the differences 
    sse = float(np.sum(difference))  # sum the squared differences
    print(sse)

squared_error(X, y, c)
