import matplotlib.pyplot as plt

left = [1, 2, 3, 4, 5]
height = [10, 11, 23, 36, 4]

tick_label = ['one', 'two', 'three', 'four', 'five']
plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['blue', 'orange'])

#x2 = [1, 2, 3, 4]
#y2 = [1, 2, 4, 4]

#plt.plot(x2, y2, label = 'Line 2') if I want to add an additional line to the graph

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph - Bar Chart')


# plt.legend()


plt.show()