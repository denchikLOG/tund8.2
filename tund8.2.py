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

def loe_andmed_failist(maed.txt):
    nimed=[]
    kõrgused=[]
    with open(maed.txt,'r') as f:
        for rida in f:
            osa=rida.strip().split(',')
            nimed.append(osa[0])
            kõrgused.append(int(osa[1]))
    return nimed,kõrgused

def arvuta_statistika(kõrgused):
    keskmine=np.mean(kõrgused)
    kõrgeim=np.max(kõrgused)
    madalaim=np.min(kõrgused)
    kogusumma=np.sum(kõrgused)
    return keskmine,kõrgeim,madalaim,kogusumma

def loo_graafik(nimed,kõrgused,sorteeritud=False):
    if sorteeritud:
        sorted_indices=np.argsort(kõrgused)[::-1]
        nimed=np.array(nimed)[sorted_indices]
        kõrgused=np.array(kõrgused)[sorted_indices]
    plt.figure(figsize=(10,6))
    plt.bar(nimed,kõrgused,color='skyblue')
    plt.xlabel('Mägi')
    plt.ylabel('Kõrgus (meetrites)')
    plt.title('Mägedes kõrgused')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('maed_graafik.png')
    plt.show()

def main():
    failinimi='maed.txt'
    nimed,kõrgused=loe_andmed_failist(maed.txt)
    keskmine,kõrgeim,madalaim,kogusumma=arvuta_statistika(kõrgused)
    print(f'Keskmine kõrgus: {keskmine:.2f} meetrit')
    print(f'Kõrgeim mägi: {nimed[kõrgused.index(kõrgeim)]} ({kõrgeim} meetrit)')
    print(f'Madalaim mägi: {nimed[kõrgused.index(madalaim)]} ({madalaim} meetrit)')
    print(f'Kogusumma (kõrgused kokku): {kogusumma} meetrit')
    loo_graafik(nimed,kõrgused)
    loo_graafik(nimed,kõrgused,sorteeritud=True)

if __name__ == '__main__':
    main()
