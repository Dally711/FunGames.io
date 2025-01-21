def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER

    return num not in grille[row]


def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER

    for row in grille:

        if row[col] == num:

            return False

    return True


def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    # A COMPLETER

    debRow, debCol = 3*(row//3), 3*(col//3)

    for i in range(3):

        for j in range(3):

            if grille[debRow + i][debCol + j] == num:

                return False

        return True

    
def verifierGagner(grille):
    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''
    
   # A COMPLETER

    for row in grille:

      if 0 in row:

          return False

    return True


def verifierValide(grille, row, col, num):
   ''' (list, int, int, int) ->  bool
   * verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
   * Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
   '''
   
   # A COMPLETER
   
   return (verifierLigne(grille, row, num) + verifierCol(grille, col, num) + verifierSousGrille(grille, row, col, num))
