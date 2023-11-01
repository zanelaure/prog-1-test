#Meiteņu un zēnu skaita histogramma.
import matplotlib.pyplot as plt

skaits = [12, 15] #meiteņu un zēnu kopskaits
kategorijas = ['Meitenes','Zēni']

plt.figure(figsize=(8,6))
plt.bar(kategorijas, skaits, color = ['pink','blue'])

plt.title('Meiteņu un zēnu skaits')
plt.xlabel('Kategorijas')
plt.ylabel('Skaits')

plt.show()