
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

notes_enregistrees  = []  
class Note:
  # question 7
  instances  = [] 
  def __init__(self, eleve, matiere, valeurs): 
    self.eleve = eleve
    self.matiere = matiere
    self.valeurs = valeurs

    Note.instances.append(self)
    notes_enregistrees.append(self)
  # question 6

  def __str__(self):    # afficher
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeurs}')"
   
  #question 8
  def moyenne_Notes(self):
    res = sum([x.valeurs for x in notes_enregistrees])  / len(notes_enregistrees) 
    return res

  # question 10 
  @classmethod 
  def vider(classe): 
    classe.instances = []
  
  @classmethod 
  def moyenne(classe): # methode pour calculer la moyenne
    return(sum(x.valeurs for x in classe.instances)/len(classe.instances))
  
 
# question 5 

onote = [Note(note[0],note[1],note[2]) for note in notes]
print(onote)

print('----')

# question 8 test

print(onote[0].moyenne_Notes())














