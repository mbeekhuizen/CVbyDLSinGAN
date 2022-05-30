import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


if __name__ == '__main__':
    sns.set_theme(style="whitegrid")

    animals = ['bird', 'cat', 'dog', 'lion']
    cities = ['city1', 'city2', 'city3', 'city4']
    comics = ['comic1', 'comic2', 'comic3', 'comic4']
    landscapes = ['grassland', 'hills', 'lake', 'mountains']

    animal_32 = []
    animal_64 = []
    animal_128 = []
    for animal in animals:
        animal_32.append(np.load(f'results/animal/{animal}_32.npy'))
        animal_64.append(np.load(f'results/animal/{animal}_64.npy'))
        animal_128.append(np.load(f'results/animal/{animal}_128.npy'))
    city_32 = []
    city_64 = []
    city_128 = []
    for city in cities:
        city_32.append(np.load(f'results/city/{city}_32.npy'))
        city_64.append(np.load(f'results/city/{city}_64.npy'))
        city_128.append(np.load(f'results/city/{city}_128.npy'))

    comic_32 = []
    comic_64 = []
    comic_128 = []
    for comic in comics:
        comic_32.append(np.load(f'results/comic/{comic}_32.npy'))
        comic_64.append(np.load(f'results/comic/{comic}_64.npy'))
        comic_128.append(np.load(f'results/comic/{comic}_128.npy'))

    landscape_32 = []
    landscape_64 = []
    landscape_128 = []
    for landscape in landscapes:
        landscape_32.append(np.load(f'results/landscape/{landscape}_32.npy'))
        landscape_64.append(np.load(f'results/landscape/{landscape}_64.npy'))
        landscape_128.append(np.load(f'results/landscape/{landscape}_128.npy'))


    a32 = np.mean(np.array(animal_32), axis=1)
    ci32 = np.mean(np.array(city_32), axis=1)
    co32 = np.mean(np.array(comic_32), axis=1)
    l32 = np.mean(np.array(landscape_32), axis=1)
    
    a64 = np.mean(np.array(animal_64), axis=1)
    ci64 = np.mean(np.array(city_64), axis=1)
    co64 = np.mean(np.array(comic_64), axis=1)
    l64 = np.mean(np.array(landscape_64), axis=1)
    
    a128 = np.mean(np.array(animal_128), axis=1)
    ci128 = np.mean(np.array(city_128), axis=1)
    co128 = np.mean(np.array(comic_128), axis=1)
    l128 = np.mean(np.array(landscape_128), axis=1)

    aAll = np.concatenate((a32, a64, a128), axis=0)
    print(aAll)
    ciAll = np.concatenate((ci32, ci64, ci128), axis=0)
    coAll = np.concatenate((co32, co64, co128), axis=0)
    lAll = np.concatenate((l32, l64, l128), axis=0)
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
    a32 = {'landscape1': landscape_32[0], 'landscape2': landscape_32[1], 'landscape3': landscape_32[2], 'landscape4': landscape_32[3]}
    df1 = pd.DataFrame.from_dict(a32)
    ax = sns.boxplot(data = df1)
    ax = sns.swarmplot(data=df1, color = ".25")

    ax.set_xlabel("Image")
    ax.set_ylabel("SIFID Score")
    ax.set_title("Distribution of SIFID score - landscapes 32x32")
    plt.savefig("results/plots/l32.png")
    # plt.show()