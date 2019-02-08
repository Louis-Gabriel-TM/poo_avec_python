# **** Ces classes User et Admin ne sont pas utilisées ****


class User:
    ''' Utilisateur de l'application alumni
    '''
    def __init__(self):
        pass

    def create_record(self):
        ''' Créer une fiche étudiant :
        1. appel de l'interface pour renseigner les champs
        2. mise en base de la fiche
        '''
        pass

    def read_record(self):
        ''' Consulter une fiche étudiant :
        Récupérer la fiche étudiant et l'afficher
        '''
        pass


class Admin(User):
    ''' Administrateur (peut modifier et supprimer)
    '''
    def __init__(self):
        super.__init__(self)
        pass

    def modify_record(self):
        ''' Modifier une fiche étudiant
        '''
        pass

    def delete_record(self):
        ''' Supprimer une fiche étudiant
        '''
        pass
        