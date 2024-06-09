# Question 5: Clustering Theory
# Python code to compute the geometric median of a set of points

import math

def GeometricMedian(points):
    # Initialize the median to the centroid
    median = [0.0, 0.0]
    for point in points:
        median[0] += point[0]
        median[1] += point[1]
    median[0] /= len(points)
    median[1] /= len(points)
    # Iteratively move the median to the geometric median
    while True:
        # Compute the weight of each point
        weights = []
        totalWeight = 0.0
        for point in points:
            weight = 1.0 / math.sqrt((point[0] - median[0])**2 + (point[1] - median[1])**2)
            weights.append(weight)
            totalWeight += weight
        # Compute the weighted sum of the points
        weightedSum = [0.0, 0.0]
        for i in range(len(points)):
            weightedSum[0] += points[i][0] * weights[i]
            weightedSum[1] += points[i][1] * weights[i]
        weightedSum[0] /= totalWeight
        weightedSum[1] /= totalWeight
        # If the weighted sum is the same as the median, we are done
        if (weightedSum[0] == median[0] and weightedSum[1] == median[1]):
            break
        # Otherwise, update the median
        median = weightedSum
    return median

# Test the function
points = [(0.6, 0.8), (0.8, 0.6), (-0.8, 0.6)]
print(GeometricMedian(points))