import unittest

"""
Count names with more than seven letters

Args:
     names_list (list): List of names to count.

Returns:
    int: Number of names with more than seven letters.
"""
def names(prenoms):
    more_than_seven = 0
    # Parcours de la liste des prénoms
    for prenom in prenoms:

        # Indiquer que le prénom a plus de 7 lettres, si oui alors on ajoute au compteur
        if len(prenom) > 7:
            more_than_seven += 1
            print("Prenom supérieur à 7 : " + prenom)
        # Indiquer que le prénom a 7 lettres ou moins
        else:
            print("Prenom inférieur ou égal à 7 : " + prenom)
    return more_than_seven

# Test pour verifier notre condition avec la fonction names
class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        # Liste de prénoms pour le test
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = names(prenoms=prenoms)
        # Test pour savoir s'il y a au moins 4 prénoms avec plus de 7 lettres
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()