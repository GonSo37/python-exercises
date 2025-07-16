import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([
    [3000, 200, -50, 5000, 100],     # <-- цей має бути найкращий
    [1000, 100, -20, 3000, 50],
    [2500, 150, -30, 4000, 90]
])

def find_best(X, y, c):
    smallest_error = np.inf
    best_index = -1
    index = 0
    for coeff in c:
        predicition = X @ coeff
        diference = predicition - y
        squared_error = np.sum(diference ** 2)
    
        if squared_error < smallest_error:
            smallest_error = squared_error
            best_index = index
        print ("Set %d: Squared Error = %.2f" % (index, squared_error))
        index += 1

    print("the best set is set %d" % best_index)


find_best(X, y, c)
