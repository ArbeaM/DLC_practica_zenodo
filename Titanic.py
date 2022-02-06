import matplotlib.pyplot as plt

data = pd.read_csv('titanic.csv', delimiter=',')
d1 = data[data['sex'] == 'male']
d2 = data[data['sex'] == 'female']

fig, ax = plt.subplots(1, 2)

ax[0].pie([sum(d1['survived'] == 1), sum(d1['survived'] == 0)], colors=['blue','orange'])
ax[0].set_title('Supervivencia de hombres')
ax[1].pie([sum(d2['survived'] == 1), sum(d2['survived'] == 0)], colors=['blue','orange'])
ax[1].set_title('Supervivencia de mujeres')
ax[1].legend(['Sobreviven', 'No sobreviven'], loc='upper right')
plt.show()
