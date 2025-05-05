import numpy as np
import matplotlib.pyplot as plt
nimed = []
korgused = []

with open("maed.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.strip().split()
        nimi = osad[0]
        korgus = int(osad[1])
        nimed.append(nimi)
        korgused.append(korgus)
np_korgused = np.array(korgused)
keskmine = np.mean(np_korgused)
maksimum = np.max(np_korgused)
minimum = np.min(np_korgused)
summa = np.sum(np_korgused)
maks_index = np.argmax(np_korgused)
min_index = np.argmin(np_korgused)
koige_korgem = nimed[maks_index]
koige_madalam = nimed[min_index]
print("Statistika:")
print(f"Keskmine kõrgus: {keskmine:.2f} m")
print(f"Kõrgeim mägi: {koige_korgem} ({maksimum} m)")
print(f"Madalaim mägi: {koige_madalam} ({minimum} m)")
print(f"Kogukõrgus: {summa} m\n")
nimed_np = np.array(nimed)
sorted_index = np.argsort(-np_korgused)

sorted_nimed = nimed_np[sorted_index]
sorted_korgused = np_korgused[sorted_index]
plt.figure(figsize=(12, 6))
plt.bar(sorted_nimed, sorted_korgused, color='skyblue')
plt.xlabel("Mäed")
plt.ylabel("Kõrgus (m)")
plt.title("Maailma kõrgeimad mäed (kahanevalt sorteeritud)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("maed_graafik.png")
plt.show()
