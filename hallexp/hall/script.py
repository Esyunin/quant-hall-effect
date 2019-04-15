import pandas as pd 
import matplotlib.pyplot as plt

Parazite = pd.read_csv('Parazite_hall.tsv', delimiter = '\t')
pz_I = Parazite['Iobr,mA'].tolist()
pz_U = Parazite['U_h,mV'].tolist()

# plt.figure(0)

# plt.plot(pz_I,pz_U,'-',color = 'red')
# plt.grid(which = 'both')


mA1 = pd.read_csv('task 5.5(2mA).tsv', delimiter = '\t')
mA1_I = mA1['I_h-field,A'].tolist()
mA1_Eh = mA1['E_Hall,mV'].tolist()


plt.figure(1)
plt.grid(which = 'both')
plt.title('Iobr = 2mA')
plt.xlabel('E_hall,mV')
plt.ylabel('I_h,A')
plt.plot(mA1_Eh,mA1_I)

H1 = pd.read_csv('task 5.6(0.75A).tsv', delimiter = '\t')
H1_i = H1['Iobr,mA'].tolist()
H1_Eh = H1['E_Hall,mV'].tolist()

plt.figure(2)
plt.grid(which = 'both')
plt.title('H~600 gs')
plt.xlabel('E_hall,mV')
plt.ylabel('Iobr,mA')
plt.plot(H1_Eh,H1_i)


plt.show()