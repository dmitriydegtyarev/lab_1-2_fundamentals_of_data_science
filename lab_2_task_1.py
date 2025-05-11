import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, chi2

# Середнє значення
def get_mean (data):
    return np.mean(data)

# Медіана
def get_median (data):
    return np.median(data)

# Дисперсія
def get_variance (data):
    return np.var(data, ddof=1) # для незміщеної оцінки дисперсії

# Довірчий інтервал для математичного сподівання
def confidence_interval_mean(data, confidence=0.95):
    n = len(data)
    mean = get_mean (data)
    variance = get_variance (data)
    t_value = t.ppf((1 + confidence) / 2, n - 1)
    margin_of_error = t_value * (np.sqrt(variance) / np.sqrt(n))
    return mean - margin_of_error, mean + margin_of_error

# Довірчий інтервал для дисперсії
def confidence_interval_variance(data, confidence=0.95):
    n = len(data)
    variance = get_variance (data)
    chi2_lower = chi2.ppf((1 - confidence) / 2, n - 1)
    chi2_upper = chi2.ppf((1 + confidence) / 2, n - 1)
    lower_bound = (n - 1) * variance / chi2_upper
    upper_bound = (n - 1) * variance / chi2_lower
    return lower_bound, upper_bound

# Масив даних з 20 елементів з data.gov.ua
values = np.array([4, 5, 3, 3, 5, 4, 1, 4, 3, 1, 3, 3, 1, 5, 3, 3, 2, 1, 5, 2])

# Статистичні показники
mean_value = get_mean (values)
median_value = get_median (values)
variance_value = get_variance (values)
ci_mean = confidence_interval_mean(values)
ci_variance = confidence_interval_variance(values)

print(f"\nОсновні характеристики вибірки:"
      f"\nСереднє значення: {mean_value}"
      f"\nМедіана: {median_value}"
      f"\nДисперсія: {variance_value}"
      f"\nДовірчий інтервал для середнього: {ci_mean}"
      f"\nДовірчий інтервал для дисперсії: {ci_variance}")

# Гістограма
# bins — кількість інтервалів
def plot_histogram(data, bins):
    plt.hist(data, bins=bins, color='green', edgecolor='black')
    plt.xlabel('Значення')
    plt.ylabel('Частота')
    plt.title('Гістограма вибірки')
    plt.grid(axis='y')
    plt.show()

plot_histogram(values, bins=10)