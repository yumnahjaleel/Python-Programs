import numpy as np

def train_linear_regression(x, y):
    # Calculate means using numpy's built-in functions
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Vectorized calculation of Slope (m)
    # This replaces the entire for-loop from the Java version
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean)**2)

    slope = numerator / denominator
    intercept = y_mean - (slope * x_mean)

    return slope, intercept

def main():
    print("--- Python Linear Regression (Vectorized) ---")
    
    # 1. Input Data
    # In Python, we usually work with lists or numpy arrays
    n = int(input("Enter number of data points: "))
    x_coords = []
    y_coords = []

    for i in range(n):
        val_x, val_y = map(float, input(f"Enter point {i+1} (x y): ").split())
        x_coords.append(val_x)
        y_coords.append(val_y)

    # Convert to NumPy arrays for vectorized math
    x = np.array(x_coords)
    y = np.array(y_coords)

    # 2. Train the model
    m, b = train_linear_regression(x, y)

    print(f"\nModel: y = {m:.4f}x + {b:.4f}")

    # 3. Prediction
    test_x = float(input("\nEnter an X value to predict Y: "))
    prediction = (m * test_x) + b
    print(f"Predicted Y: {prediction:.4f}")

if __name__ == "__main__":
    main()
