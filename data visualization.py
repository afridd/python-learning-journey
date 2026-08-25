import matplotlib.pyplot as plt
plt.style.use("dark_background")

sizes = [89, 80, 90, 100, 75]
labels = ["Tamil", "English", "Maths", "Science", "Social"]
plt.pie(sizes, labels=labels, autopct="%.2f")
plt.show()

plt.plot([1, 2, 3, 4])
plt.show()