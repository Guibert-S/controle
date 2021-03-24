
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
print(round(res),2)

#b/ calculez la moyenne de eleve1 en maths

res = 0
c=0
for x in notes: 
    if x[0]== 'eleve1' and x[1]=='math':
      res += x[2]
      c = c+1
res = res / c 
print(round(res,2))

notes_eleve1 = [note for note in notes if note[0] == 'eleve1']
print(notes_eleve1)

#c/ Créer une fonction "moyenne_tuples" qui calcule la moyenne de d'un élève dans une matière.
print("---")

def moyenne_tuple(notes, eleve=None, matiere=None):
    
    notes_eleve = [note for note in notes if note[0] == eleve] if eleve is not None else notes
    notes_eleve_matiere = [n for n in notes_eleve if n[1] == matiere] if matiere is not None else notes_eleve
    return round(sum([n[2] for n in notes_eleve_matiere])/len(notes_eleve_matiere),2)


# si on ajoute des erreurs, le programme plante ou le programme nous renvoi une 
# valeurs aberrante.


class Note:
  instances = []  
  def __init__(self, eleve, matiere, valeurs): 
    self.eleve = eleve
    self.matiere = matiere
    self.valeurs = valeurs

    Note.instances.append(self)


  def __str__(self):    # afficher
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeurs}')"
   
  def moyenne_Notes(*liste):
    res = round([sum(y) / len(liste) for y in zip(*liste)],2) 
    return res


  @classmethod 
  def vide(classe): # methode pour vide des 
    classe.instances = []
  
  @classmethod 
  def moyenne(classe): # methode pour calculer la moyenne
    return(sum(x.valeurs for x in classe.instances)/len(classe.instances))
  
 

print("---Demo---")
class Demo:
  classattr = 'defaut'
  def __init__(self, a):
    self.a = a


demo1 = Demo(1)
demo2 = Demo(2)

print(demo1.a)
print(demo2.a)
print(Demo.classattr)
print(demo1.classattr)
print(demo2.classattr)

Demo.classattr = 23

print(demo1.classattr)
print(demo2.classattr)

demo1.classattr = -1

print(Demo.classattr)
print(demo1.classattr)
print(demo2.classattr)

Demo.classattr = 14

print("--- Fin Demo---")

if __name__ == '__main__':
    note1 = ('eleve1', 'math', 13)
    note2 = ('eleve1', 'physique', 15)
    note3 = ('eleve1', 'math', 13)
    note4 = ('eleve1', 'eco', 12)
    note5 = ('eleve1', 'eco', 13)
    note6 = ('eleve1', 'math', 12)
    note7 = ('eleve2', 'math', 13)
    note8 = ('eleve2', 'math', 14)


notes = [note1, note2, note3, note4, note5, note6,note7,note8]

onote = Note('eleve1', 'maths', 13)
onote2 = Note('eleve5', 'maths', 15)
print(onote.eleve)
print(onote.matiere)
print(onote.valeurs)
Note.afficher(onote)
print(onote2.matiere)


print(sum(note[2] for note in notes_eleve1)/len(notes_eleve1))

notes_eleve1_math = [n for n in notes_eleve1 if n[1] == 'math']

print(sum(n[2] for n in notes_eleve1_math)/len(notes_eleve1_math))


print(moyenne_tuple(notes, 'eleve1', 'math'))


onote = Note('eleve1', 'maths', 13)


onotes = [Note(eleve, matiere,  valeurs) for eleve, matiere, valeurs in notes]
print(onotes)

onotes = [Note(*note) for note in notes]
print(onotes)
Note.vide()

onotes = [Note(*note) for note in notes]
print(onotes)
print(Note.moyenne())

#Question 11

from .main import Note

def tests_ajouts():

  notes = Note('xxx', 'yyy', 'zzz')
  print(notes)

  Note.vide()
  assert len(Note.instances) == 0
  Note(eleve = 'eleve1', matiere='math', valeurs=14)
  assert len(Note.instances) == 1 # on verifie 

#Question 12

assert  moyenne_tuple(14,eleve1,francais) == 14 























