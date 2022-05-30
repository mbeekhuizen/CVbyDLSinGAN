import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

if __name__ == '__main__':
    sns.set_theme(style="whitegrid")

    #Merged
    currDir = os.getcwd() + "/results/merged/"
    filesA = os.listdir(currDir + "alternating/")
    filesB = os.listdir(currDir + "interleaving/")
    alternating = []
    interleaving = []
    for file in filesA:
        alternating.append(np.load(currDir + "alternating/" + file))
    for file in filesB:
        interleaving.append(np.load(currDir + "interleaving/" + file))


    city13 = np.concatenate((alternating[0], alternating[1]))
    comic12 = np.concatenate((alternating[2], alternating[3]))
    doglion = np.concatenate((alternating[4], alternating[5]))
    grasshills = np.concatenate((alternating[6], alternating[7]))
    vulcanotrees = np.concatenate((alternating[8], alternating[9]))
    image = []
    for i in range(0, 22):
        if i >= 11:
            image.append("Image 2")
        else:
            image.append("Image 1")
    dictionary1 = {"City1 / City3": city13, "Comic1 / Comic2": comic12, "Dog / Lion": doglion,
                  "Grass / Hills": grasshills, "Vulcano / Trees": vulcanotrees, "SIFID": image}
    df1 = pd.DataFrame.from_dict(dictionary1)
    df2 = pd.melt(df1, value_vars=["City1 / City3", "Comic1 / Comic2", "Dog / Lion", "Grass / Hills", "Vulcano / Trees"], id_vars="SIFID")
    print(df2)
    #Plot 1
    fig, ax = plt.subplots(1, 2, figsize = (20, 8))
    sns.boxplot(data =df2, x="variable", y="value", hue= "SIFID", ax=ax[0])
    #sns.swarmplot(data=df2, x="variable", y="value", hue= "SIFID", ax= ax[0], dodge = True, palette = "Set2")
    ax[0].set_xlabel("Image")
    ax[0].set_ylabel("SIFID Score")
    ax[0].set_title("Distribution of alternating variant - 128x128")
    ax[0].set_ylim([0, 7])

    #Interleaving
    city13 = np.concatenate((interleaving[0], interleaving[1]))
    comic12 = np.concatenate((interleaving[2], interleaving[3]))
    doglion = np.concatenate((interleaving[4], interleaving[5]))
    grasshills = np.concatenate((interleaving[6], interleaving[7]))
    vulcanotrees = np.concatenate((interleaving[8], interleaving[9]))
    image = []
    for i in range(0, 22):
        if i >= 11:
            image.append("Image 2")
        else:
            image.append("Image 1")
    dictionary1 = {"City1 / City3": city13, "Comic1 / Comic2": comic12, "Dog / Lion": doglion,
                  "Grass / Hills": grasshills, "Vulcano / Trees": vulcanotrees, "SIFID": image}
    df1 = pd.DataFrame.from_dict(dictionary1)
    df2 = pd.melt(df1, value_vars=["City1 / City3", "Comic1 / Comic2", "Dog / Lion", "Grass / Hills", "Vulcano / Trees"], id_vars="SIFID")
    print(df2)

    #Plot2
    sns.boxplot(data =df2, x="variable", y="value", hue= "SIFID", ax=ax[1])
    ax[1].set_xlabel("Image")
    ax[1].set_ylabel("SIFID Score")
    ax[1].set_title("Distribution of interleaving variant - 128x128")
    ax[1].set_ylim([0, 7])
    plt.savefig("results/plots/altervsinter.png")
    plt.show()




    # fig, ax = plt.subplots(1, 2, figsize = (5, 10))
    #
    # aci13 = np.load("merged/alternating/alternating_city13_city1.npy")
    #






















    # animals = ['bird', 'cat', 'dog', 'lion']
    # cities = ['city1', 'city2', 'city3', 'city4']
    # comics = ['comic1', 'comic2', 'comic3', 'comic4']
    # landscapes = ['grassland', 'hills', 'lake', 'mountains']
    #
    # animal_32 = []
    # animal_64 = []
    # animal_128 = []
    # for animal in animals:
    #     animal_32.append(np.load(f'results/animal/{animal}_32.npy'))
    #     animal_64.append(np.load(f'results/animal/{animal}_64.npy'))
    #     animal_128.append(np.load(f'results/animal/{animal}_128.npy'))
    # city_32 = []
    # city_64 = []
    # city_128 = []
    # for city in cities:
    #     city_32.append(np.load(f'results/city/{city}_32.npy'))
    #     city_64.append(np.load(f'results/city/{city}_64.npy'))
    #     city_128.append(np.load(f'results/city/{city}_128.npy'))
    #
    # comic_32 = []
    # comic_64 = []
    # comic_128 = []
    # for comic in comics:
    #     comic_32.append(np.load(f'results/comic/{comic}_32.npy'))
    #     comic_64.append(np.load(f'results/comic/{comic}_64.npy'))
    #     comic_128.append(np.load(f'results/comic/{comic}_128.npy'))
    #
    # landscape_32 = []
    # landscape_64 = []
    # landscape_128 = []
    # for landscape in landscapes:
    #     landscape_32.append(np.load(f'results/landscape/{landscape}_32.npy'))
    #     landscape_64.append(np.load(f'results/landscape/{landscape}_64.npy'))
    #     landscape_128.append(np.load(f'results/landscape/{landscape}_128.npy'))
    #
    #
    # a32 = np.mean(np.array(animal_32), axis=1)
    # ci32 = np.mean(np.array(city_32), axis=1)
    # co32 = np.mean(np.array(comic_32), axis=1)
    # l32 = np.mean(np.array(landscape_32), axis=1)
    #
    # a64 = np.mean(np.array(animal_64), axis=1)
    # ci64 = np.mean(np.array(city_64), axis=1)
    # co64 = np.mean(np.array(comic_64), axis=1)
    # l64 = np.mean(np.array(landscape_64), axis=1)
    #
    # a128 = np.mean(np.array(animal_128), axis=1)
    # ci128 = np.mean(np.array(city_128), axis=1)
    # co128 = np.mean(np.array(comic_128), axis=1)
    # l128 = np.mean(np.array(landscape_128), axis=1)
    #
    # aAll = np.concatenate((a32, a64, a128), axis=0)
    # print(aAll)
    # ciAll = np.concatenate((ci32, ci64, ci128), axis=0)
    # coAll = np.concatenate((co32, co64, co128), axis=0)
    # lAll = np.concatenate((l32, l64, l128), axis=0)
    #
    # aAll = {'animals': aAll, 'cities': ciAll, 'comics': coAll, 'landscape': lAll}
    # df1 = pd.DataFrame.from_dict(aAll)
    # ax = sns.boxplot(data = df1)
    # ax = sns.swarmplot(data=df1, color = ".25")
    # ax.set_xlabel("Image")
    # ax.set_ylabel("SIFID Score")
    # ax.set_title("Distribution of SIFID score - Different domains on all image sizes")
    # plt.savefig("results/plots/domainsAll.png")
    # plt.show()

    #For individual categories
    # a32 = {'landscape1': landscape_32[0], 'landscape2': landscape_32[1], 'landscape3': landscape_32[2], 'landscape4': landscape_32[3]}
    # df1 = pd.DataFrame.from_dict(a32)
    # ax = sns.boxplot(data = df1)
    # ax = sns.swarmplot(data=df1, color = ".25")
    #
    # ax.set_xlabel("Image")
    # ax.set_ylabel("SIFID Score")
    # ax.set_title("Distribution of SIFID score - landscapes 32x32")
    # plt.savefig("results/plots/l32.png")
    # plt.show()