
note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]
# pour run python main.py

print(notes)
#Question 4 a/ calculez la moyenne de eleve1 
# cd c16_03
res = 0
c = 0
for x in notes: 
    if x[0]== 'eleve1':
      res += x[2]
      c = c+1
res = res / c
print(res)

#b/ calculez la moyenne de eleve1 en maths

res = 0
c=0
for x in notes: 
    if x[0]== 'eleve1' and x[1]=='math':
      res += x[2]
      c = c+1
res = res / c 
print(res)

#c/ Créer une fonction "moyenne_tuples" qui calcule la moyenne de d'un élève dans une matière.
print("---")
def moyenne_tuples(notes,eleve,matiere):
 
  if eleve == none and matiere = none:
    res = 0 
    c = 0 
    for x in notes:
      res +=x[2]
      c = c+1 
    res = res/ c 
    return res

  else :
  res = 0
  c=0
  for x in notes: 
    if x[0]== eleve and x[1]== matiere:
      res += x[2]
      c = c+1
  res = res / c 
  return res


# si on ajoute des erreurs, le programme plante ou le programme nous renvoi une 
# valeur aberrante.


#Question 5/ Reprenez la liste de notes pour créer une nouvelle liste onotes qui seront des instance de Note


#Question 6/ On aimerai bien pouvoir directement afficher une note en utilisant print(note) plutot que note.affiche. Ajouter une méthode dans la classe Note

class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)

  def __call__(self, *args, **kwargs):
        return self._type(*args, **kwargs)

onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)



