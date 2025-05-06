# import numpy as np
# import matplotlib.pyplot as plt
# nimed = []
# korgused = []

# with open("maed.txt", "r", encoding="utf-8") as fail:
#     for rida in fail:
#         osad = rida.strip().split()
#         nimi = osad[0]
#         korgus = int(osad[1])
#         nimed.append(nimi)
#         korgused.append(korgus)
# np_korgused = np.array(korgused)
# keskmine = np.mean(np_korgused)
# maksimum = np.max(np_korgused)
# minimum = np.min(np_korgused)
# summa = np.sum(np_korgused)
# maks_index = np.argmax(np_korgused)
# min_index = np.argmin(np_korgused)
# koige_korgem = nimed[maks_index]
# koige_madalam = nimed[min_index]
# print("Statistika:")
# print(f"Keskmine kõrgus: {keskmine:.2f} m")
# print(f"Kõrgeim mägi: {koige_korgem} ({maksimum} m)")
# print(f"Madalaim mägi: {koige_madalam} ({minimum} m)")
# print(f"Kogukõrgus: {summa} m\n")
# nimed_np = np.array(nimed)
# sorted_index = np.argsort(-np_korgused)

# sorted_nimed = nimed_np[sorted_index]
# sorted_korgused = np_korgused[sorted_index]
# plt.figure(figsize=(12, 6))
# plt.bar(sorted_nimed, sorted_korgused, color='skyblue')
# plt.xlabel("Mäed")
# plt.ylabel("Kõrgus (m)")
# plt.title("Maailma kõrgeimad mäed (kahanevalt sorteeritud)")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig("maed_graafik.png")
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

with open("maed.txt","r")as file:
    lines=file.readlines()

nimed=[]
korgused=[]

for rida in lines:
    osad=rida.strip().split()
    nimi=" ".join(osad[:-1]).replace("_"," ")
    korgus=int(osad[-1])
    nimed.append(nimi)
    korgused.append(korgus)

korgused_np=np.array(korgused)
keskmine=np.mean(korgused_np)
min_korgus=np.min(korgused_np)
max_korgus=np.max(korgused_np)
summa=np.sum(korgused_np)

print("Keskmine kõrgus:",keskmine,"m")
print("Kõrgeim mägi:",nimed[np.argmax(korgused_np)],"-",max_korgus,"m")
print("Madalaim mägi:",nimed[np.argmin(korgused_np)],"-",min_korgus,"m")
print("Kogukõrgus:",summa,"m")

nimed_sorted=[x for _,x in sorted(zip(korgused,nimed),reverse=True)]
korgused_sorted=sorted(korgused,reverse=True)

plt.figure(figsize=(10,6))
plt.bar(nimed_sorted,korgused_sorted,color='skyblue')
plt.xticks(rotation=45,ha='right')
plt.ylabel('Kõrgus (m)')
plt.title('Maailma kõrgeimad mäed')
plt.tight_layout()
plt.savefig("maed_graafik.png")
plt.show()
plt.show()
