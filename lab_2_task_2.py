import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Середнє значення
def get_mean (data):
    return np.mean(data)

# Медіана
def get_median (data):
    return np.median(data)

# Дисперсія
def get_variance (data):
    return np.var(data, ddof=1) # для незміщеної оцінки дисперсії

# Стандартне відхилення
def get_standard_deviation (data):
    return np.sqrt(get_variance (data))

group_A = np.array([85, 92, 78, 81, 89, 85, 91, 77, 84, 88])
group_B = np.array([79, 82, 85, 88, 75, 83, 90, 80, 87, 84])

mean_A = get_mean (group_A)
mean_B = get_mean (group_B)

median_A = get_median (group_A)
median_B = get_median (group_B)

variance_A = get_variance (group_A)
variance_B = get_variance (group_B)

std_A = get_standard_deviation (group_A)
std_B = get_standard_deviation (group_B)

print(f"\nОсновні характеристики заданих вибірок:"
      f"\nСереднє значення:"
      f"\n- Група студентів А: {mean_A}"
      f"\n- Група студентів B: {mean_B}"
      f"\nМедіана:"
      f"\n- Група студентів А: {median_A}"
      f"\n- Група студентів B: {median_B}"
      f"\nДисперсія:"
      f"\n- Група студентів А: {variance_A}"
      f"\n- Група студентів B: {variance_B}"
      f"\nСтандартне відхилення:"
      f"\n- Група студентів А: {std_A}"
      f"\n- Група студентів B: {std_B}")

t_statistic, p_value = ttest_ind(group_A, group_B)
print(f"\nРезультати t-тесту для порівняння середніх:"
      f"\nT-статистика: {t_statistic}"
      f"\nP-значення: {p_value}")
if p_value < 0.05:
    print("\nРізниця між середніми балами є значущою.")
else:
    print("\nСтатистично значущої різниці між середніми балами немає.")

def plot_histogram(data, label):
    plt.hist(data, color='green', edgecolor='black')
    plt.xlabel('Бали')
    plt.ylabel('Кількість')
    plt.title(f'Гістограма вибірки: {label}')
    plt.grid(axis='y')
    plt.show()

plot_histogram(group_A, "Група А")
plot_histogram(group_B, "Група Б")