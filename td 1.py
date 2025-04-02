tirage = ['a','r','b','g','e','s','c','j']
f = open('frenchssaccent.dic','r')
dico=[] #on initialise le dictionnaire de tout les mots possibles
mots= [] #on initialise la liste des mots compatibles avec le tirage
maxi= ''

for mot in f:
    dico.append(mot[0:len(mot)-1]) #on ajoute au dictionnaire tout les mots du documents, en enlevant le dernier élément qui symbolise un retour à la ligne

# Exercice 2
for mot in dico: #on va chercher, afin de simuler le principe du scrabble, à éliminer les lettres possibles dès qu'on les a sélectionnées dans le mot.
    clone=tirage.copy() #Pour cela, on clône d'abord le tirage afin de ne pas risquer d'altérer les possibilités
    copier=True
    for j in mot:
        if j in clone:
            clone.remove(j) #lorsqu'une lettre du mot étudié est compatible, on l'enlève des lettres restantes grâce à la fonction remove
        else:
            copier=False #dès lors qu'une lettre du mot étudié n'est pas ou plus disponible, on supprime la possibilité de conserver le mot étudié dans la liste mots
            break #dès lors que le mot est incompatible, on arrête son étude et on passe au mot suivant grâce à la fonction break
    if copier:
        mots.append(mot) #on ajoute le mot étudié à la liste des mots compatibles

for mot in mots:
    if len(mot)>len(maxi): #on compare la "longueur" des mots, soit le nombre de lettres composant chaques mots
        maxi=mot
print("le mot compatible de longueur maximale est :",maxi)
#Exercice 3
# On utilise un dictionnaire afin d'implémenter des poids aux lettres
tirage_Ex3 = {'a':1,'r':1,'b':3,'g':2,'e':1,'s':1,'c':3,'j':8}
mots_Ex3= [] #on initialise les mêmes variables qu'à l'exercice précédent
maxi_Ex3= ['',0] #on initialise le mot maximum comme une liste, avec le poids associé au maximum
for mot in dico:
    clone=tirage.copy() #de la même manière que précédemment, on cherche à trouver tout les mots qui contiennent que des éléments de la liste
    copier=True
    for j in mot:
        if j in clone:
            clone.remove(j)
        else:
            copier=False
            break
    if copier:
        mots_Ex3.append(mot)

for mot in mots_Ex3:
    s=0
    for j in mot:
        s+=tirage_Ex3[j] #on calcule le 'poids' du mot possible avant de le comparer au maximum actuel
    if s>maxi_Ex3[1]:
        maxi_Ex3[0]=mot #si le poids actuel est plus grand, on remplace maxi par le mot et son poids associé
        maxi_Ex3[1]=s
print("le mot compatible de meilleur score est:",maxi_Ex3)