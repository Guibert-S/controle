# question 11 et 12 
from main import Note

def test_ajout():
  Note.vider()
  assert not(Note.instances) 
  Note('eleve1','math',12)
  assert Note.instances[0].eleve == 'eleve1' and Note.instances[0].matiere == 'math' and Note.instances[0].valeurs == 12

test_ajout()
# pas d erreur assert 

