import numpy as np

def omni_synthesis(dim=10, points=1000):
    """Simulate multidimensional synthesis without sklearn."""
    # Generate random input data
    X = np.random.rand(points, dim)
    y = np.sum(X, axis=1) + np.random.normal(0, 0.1, points)  # Synthetic target

    # Add bias term (intercept) to X
    X_bias = np.c_[np.ones(points), X]

    # Compute coefficients using Normal Equation: β = (XᵀX)⁻¹ Xᵀy
    beta = np.linalg.inv(X_bias.T @ X_bias) @ (X_bias.T @ y)

    # Predictions
    y_pred = X_bias @ beta

    # Compute R² score: 1 - SS_res / SS_tot
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - ss_res / ss_tot

    print(f"Omni Synthesis Accuracy (R²): {r2:.4f}")
    return r2

# Example run
if __name__ == "__main__":
    omni_synthesis()