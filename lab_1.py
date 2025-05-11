import numpy as np
import matplotlib.pyplot as plt

# E(X) = Σ (x_i * P_i) (математичне сподівання)
def expectation(values, probabilities):
    return np.sum(np.multiply(values, probabilities))

# Var(X) = Σ [ (x_i - E(X))^2 * P_i ] (дисперсія)
def dispersion(values, probabilities, expectations):
    return np.sum(np.multiply((values - expectations)**2, probabilities))

# ΣP = 1 (обов'язкова нормалізація згідно з умовою)
def normalize (values):
    return values/np.sum(values)

array_values = np.array([1, 2, 3, 4, 5]) # Значення
array_before_normalization = np.array([10, 20, 30, 20, 20]) # Згідно з умовою не нормалізовані ймовірності

array_probability = normalize (array_before_normalization) # Нормалізовані ймовірності

E = expectation(array_values, array_probability) # Математичне сподівання

Var = dispersion(array_values, array_probability, E) # Дисперсія

Std = np.sqrt(Var) # Відхилення

# Консоль
print(f"\nЗначення X: {array_values}"
      f"\nНормалізовані ймовірності P: {array_probability}"
      f"\nМатематичне сподівання: {E}"
      f"\nДисперсія: {Var}"
      f"\nСтандартне відхилення: {Std}")

# Діаграма
plt.figure(figsize=(8, 5))
plt.bar(array_values, array_probability, color='green', edgecolor='black')
plt.xlabel("Значення X")
plt.ylabel("Ймовірність")
plt.title("Розподіл дискретної випадкової величини")
plt.grid(axis='y')
plt.show()