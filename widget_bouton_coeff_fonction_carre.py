"""
Tracé de la courbe d'équation y=a.x²+b
influence des coefficients a et b
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib import rcParams

#rcParams["text.usetex"]=True

#Création de la figure et de la zone graphique
fig1=plt.figure()
axe1=fig1.add_subplot(111)      
axe1.set_xlim(-5,5)
axe1.set_xticks([i for i in range(-5,6)])
axe1.set_ylim(-150,150)

#positionnement des contours
axe1.spines["left"].set_position("zero")
axe1.spines["bottom"].set_position("zero")
axe1.spines["right"].set_color("none")
axe1.spines["top"].set_color("none")

#marge de droite pour placer les boutons
plt.subplots_adjust(right=0.8)


#Liste contenant les valeurs initiales des coefficients a=0 et b=0
#ces valeurs seront modifiées par des fonctions en utilisant des méthodes de liste
#la modifications par une fonction d'une variable (de type float) extérieure à la fonction n'est pas possible?!!??
#c'est pourquoi des listes ont été crées....
coeff_a=[0]
coeff_b=[0]

#tracé de la courbe d'équation y=a.x²+b
X=np.arange(-5,5.1,0.1)
Y=X*X*coeff_a[0]+coeff_b[0]
courbe,=axe1.plot(X,Y)


#zones des 2 boutons pour le coeff a
axe2=fig1.add_axes([0.8,0.78,0.05,0.05])
axe3=fig1.add_axes([0.8,0.7,0.05,0.05])
axe1.text(5.2,135,"a",fontsize=12,fontweight="bold",color="red")
#zones des 2 boutons pour le coeff b
axe4=fig1.add_axes([0.86,0.78,0.05,0.05])
axe5=fig1.add_axes([0.86,0.7,0.05,0.05])
axe1.text(6.1,135,"b",fontsize=12,fontweight="bold",color="green")

#boutons pour a
bouton1=Button(axe2,"+")
bouton2=Button(axe3,"-")
#boutons pour b
bouton3=Button(axe4,"+")
bouton4=Button(axe5,"-")

#Affichage de l'équation y=a.x²+b
affichage_texte1=axe1.text(4.8,60,r"$y=$", fontsize=8)
affichage_texte2=axe1.text(5.38,60,coeff_a[0], fontsize=12,fontweight="bold",color="red")
affichage_texte3=axe1.text(6,60,r"$.x$", fontsize=8)
affichage_texte4=axe1.text(6.4,60,r"$+$", fontsize=12,fontweight="bold",color="green")
affichage_texte5=axe1.text(6.7,60,coeff_b[0], fontsize=12,fontweight="bold",color="green")


def func1(event):
    if coeff_a[0]<10:
        coeff_a[0]=coeff_a[0]+1             #modification de la variable extérieure coeff_a par des méthodes de liste.
        Y1=X*X*coeff_a[0]+coeff_b[0]   
        courbe.set_ydata(Y1)
        affichage_texte2.set_text(coeff_a[0])
        plt.draw()
bouton1.on_clicked(func1)


def func2(event):
    if coeff_a[0]>-10:
        coeff_a[0]=coeff_a[0]-1
        Y1=X*X*coeff_a[0]+coeff_b[0]    
        courbe.set_ydata(Y1)
        affichage_texte2.set_text(coeff_a[0])
        plt.draw()
bouton2.on_clicked(func2)


def func3(event):
    if coeff_b[0]<150:
        coeff_b[0]=coeff_b[0]+10
        Y1=X*X*coeff_a[0]+coeff_b[0]    
        courbe.set_ydata(Y1)
        affichage_texte5.set_text(abs(coeff_b[0]))
        if coeff_b[0]<0:
            affichage_texte4.set_text(r"$-$")
        else:
            affichage_texte4.set_text(r"$+$")
        plt.draw()
bouton3.on_clicked(func3)


def func4(event):
    if coeff_b[0]>-150:
        coeff_b[0]=coeff_b[0]-10
        Y1=X*X*coeff_a[0]+coeff_b[0]    
        courbe.set_ydata(Y1)
        affichage_texte5.set_text(abs(coeff_b[0]))
        if coeff_b[0]<0:
            affichage_texte4.set_text(r"$-$")
        else:
            affichage_texte4.set_text(r"$+$")
        plt.draw()
bouton4.on_clicked(func4)

fig1.show()
