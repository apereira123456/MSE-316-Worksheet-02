import matplotlib.pyplot as plt
import numpy as np

E = np.linspace(0,4 * 10**(-20),1000)

k_B = 1.381 * 10**(-23)
E_F = 2 * 10**(-20)
T_1 = 0
T_2 = 100
T_3 = 200

F_1 = 1 / (1 + np.exp((E - E_F) / (k_B * T_1)))
F_2 = 1 / (1 + np.exp((E - E_F) / (k_B * T_2)))
F_3 = 1 / (1 + np.exp((E - E_F) / (k_B * T_3)))

fig = plt.figure(figsize=(6, 7)) 
frame = plt.gca()
frame.axes.get_xaxis().set_ticks([])

plt.ylabel('F(E)')

plt.subplot(3,1,1)
plt.plot(E, F_1, 'b', label='T=0K')
plt.plot([2 * 10**(-20),2 * 10**(-20)], [0,1], 'k--', label='')
plt.title('Fermi Plots')
plt.legend()
plt.xlabel('E_F')
frame = plt.gca()
frame.axes.get_xaxis().set_ticks([])

plt.subplot(3,1,2)
plt.plot(E, F_2, 'r', label='T=100K')
plt.plot([2 * 10**(-20),2 * 10**(-20)], [0,1], 'k--', label='')
plt.legend()
plt.xlabel('E_F')
plt.ylabel('F(E)')
frame = plt.gca()
frame.axes.get_xaxis().set_ticks([])

plt.subplot(3,1,3)
plt.plot(E, F_3, 'g', label='T=200K')
plt.plot([2 * 10**(-20),2 * 10**(-20)], [0,1], 'k--', label='')
plt.legend()
plt.xlabel('E_F')
frame = plt.gca()
frame.axes.get_xaxis().set_ticks([])

plt.savefig('q2.png', dpi=300)