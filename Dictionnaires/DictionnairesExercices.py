tel={"Utilisateur1":"0712345678","Utilisateur2":"0787654321","Utilisateur3":"0600000000","Utilisateur4":"0600000001","Utilisateur5":"070000001","Utilisateur6":"0244445555","Utilisateur7":"0787878898","Utilisateur8":"0235353535"}

# programme qui affiche le contenu du dictionnaire

m=list(tel.keys())
j=list(tel.values())
taille=0
print(f"Dans ce répertoire il y a {len(tel)} personnes\n\n--------------------------------------\n")
for k in range(len(m)):
    if len(m[k])>taille:
        taille=len(m[k])

for i in range(len(m)):
    n=" "
    for k in range(taille-len(m[i])):
        n+=" "
    print(m[i],n,j[i])
print("\n--------------------------------------")



# programme de recherche

def nom(nom):
    m=list(tel.keys())
    j=list(tel.values())
    for k in range(len(tel)):
        if m[k]==nom:
            k=str("Le numéro de ")+nom+(" est : ")+j[k]
            return k
    k=nom+str(" n'est pas dans le répertoire")
    return k

def num(num):
    m=list(tel.keys())
    j=list(tel.values())
    for k in range(len(tel)):
        if j[k]==num:
            k=str("La personne à qui appartient le numéro ")+num+(" est : ")+m[k]
            return k
    k=num+str(" n'est pas dans le répertoire")
    return k

n="Utilisateur1"
print(nom(n))
n="0600000000"
print(num(n))