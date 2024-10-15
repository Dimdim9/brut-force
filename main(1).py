import random
def aleatoire ():
    pwd=""
    for i in range(4):
        pwd=pwd+str(random.randint(0,9))
    with open("test_python.txt", "w") as fichier:
        fichier.write(pwd)
    return pwd

tentative=5
mdp='ANIS1234'
while tentative>0:
    pwd=input('entrez votre mot de passe:')
    if mdp==pwd:
        print ("le mot de passe est correct")
        break
    elif pwd!=mdp:
        print('le mot de passe est incorrect')
        tentative=tentative-1
        print ("il vous reste",tentative,"essais")
        if tentative==0:
            print('on vous hack')
            aleatoire()'''
            













