"""
print(2+2)
nombres = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for nombre in nombres:
    print(nombre)
for nombre in range(16):
    print(nombre * 2)
for nombre in range(0, 31, 2):
    print(nombre)
liste_invites=["Paul","Pierre","Jean","Marie"]
for invite in liste_invites:
    print("Bienvenu " + invite)
    print ("Au revoir " + invite)
    print ("Merci " + invite)
    """

"""
def fonction_recursive(x):
    if x ==0:
        print('x est nul')
    else:
        print(x)
        nouveau_x = x-1
        fonction_recursive(x=nouveau_x)
fonction_recursive(10)

def ma_fonction(param):
    variable = param + 3
    return variable

resultat = ma_fonction(param=5)
print resultat
"""
"""
def ma_fonction(param):
    variable = param + 3
    print variable

resultat = ma_fonction(param=5)
print resultat
"""
"""
def ma_fonction(param):
    variable = param * 2
    return variable

resultat = ma_fonction(param=5)
print resultat
"""
"""
def ma_fonction(x):
    print(x*2)

ma_fonction(5)
"""
"""
def ma_fonction(liste):
    print len(liste)
    return len(liste)


glope = [1, 2, 3, 4]

ma_fonction(liste=glope)
resultat = ma_fonction(liste=glope)
print resultat

"""
"""
def build_list():
    new_list = ()
for compteur in range(5):
    new_list.append(False)
new_list.append(True)
for compteur in range(3):
    new_list.append(False)


new_list = build_list()
if new_list == [False, False, False, False, False, True, False, False, False]:
    print("test OK")
else:
    print ("test KO")

def print_state(repr3):
    state_str = ''

    for element in repr3:
        if element == True:
            state_str = state_str + '1'
        else:
            state_str = state_str + '-'

    print(state_str)
    return

state = [False, False, False, True, False, False, False, False, False, False, ]
print_state(repr3=state)

other_state = [True, False, False, False, False, False, False, False, False, False, ]
print_state(repr3=other_state)

next_state = [False, False, False, False, False, False, False, False, True, ]
print_state(repr3=next_state)

"""
"le personnage est dans la 3e collone de la 6e ligne"



position_personnage = (3, 6)

etat_des_salles = [
[False, False, False, False, False, False, False, False, ],
[False, False, False, False, False, False, False, False, ],
[False, False, False, False, False, False, False, False, ],
[False, False, False, False, False, False, False, False, ],
[False, False, False, False, False, False, False, False, ],
[False, False, True, False, False, False, False, False, ],
[False, False, False, False, False, False, False, False, ],
[False, False, False, False, False, False, False, False, ],
[False, False, False, False, False, False, False, False, ],
[False, False, False, False, False, False, False, False, ],
]

affichage_jeu = """----------
----------
----------
----------
----------
--+-------
----------
----------
----------
----------
----------"""

print(affichage_jeu)


''''
print(2+2)
print"bonjour""aurevoir"
print{"rouge":"objet",
"vert":"animal",
"jaune":"humain"}
print[2,3,4,7,8]
liste_invites = ["Marcel","Paul","Marie"]
for invite in liste_invites:
    print("Bienvenu " + invite)
ma_variable = 2
if ma_variable+2<6:
    print("plus petit")
else:
    print("plus grand")
{
(8,30):{
"lieu":"universite",
"cours":"programmation",
},
(9):{
"lieu":"universite",
"cours":"chinois",
},
}
for compteur in range(10):
    print(compteur)
print"universite"
ma_liste = [1,2,5,6]
ma_liste[3] = 5
troisieme_element=ma_liste[3]
print len(ma_liste)
liste_personnes = ["Lily","Samuel","Camille","Olivier"]
for personne in liste_personnes:
    print("Bonjour " + personne)
for i in range(0, 30, 2):
    print(i)
for a in range(10, 0, -1):
    print(a)
    def ma_fonction(param):
        variable=param+3
        return ma_variable
        print ma_variable
print(2+2)""""
'''

from kbhit import KBHit

kb = KBHit()

print('Hit any key, or ESC to exit')
def print_state(repr3):
    state_str = ''

    for element in repr3:
        if element == True:
            state_str = state_str + '1'
        else:
            state_str = state_str + '-'

    print(state_str)
    return

def build_list(etat_position):
    new_list = []
    for compteur in range(etat_position):
        new_list.append(False)
    new_list.append(True)
    for compteur in range(3):
        new_list.append(False)
    return new_list

etat_nombre = 5

while True:

    if kb.kbhit():
        caractere = kb.getch()
        caractere_ord = ord(caractere)
        print(caractere)
        print(caractere_ord)
        if caractere_ord == 27: # ESC
            break
        print(caractere)

        if caractere == "d":
            etat_nombre = etat_nombre + 1
            etat_list = build_list(etat_nombre + 1)
            print(etat_list)

        if caractere == "g":
            etat_nombre = etat_nombre - 1
            etat_list = build_list(etat_nombre - 1)
            print(etat_list)


            print_state(etat_list)


kb.set_normal_term()
