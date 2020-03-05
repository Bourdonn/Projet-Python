Bonjour à tous, 
Vous trouverez sur Moodle dans le dossier Python/2020_Projet des fichiers de tests unitaires.
 Ces fichiers vous présentent 3 classes que vous devez implémenter dans le cadre de votre projet.
 -> La classe Robot qui modélise un robot aspirateur et testée dans le fichier Test_Robot.py
    Elle a au moins 2 attributs color, un caractère et index un entier, correspondant à la position "1D" du robot = x * n_y + y si x et y sont les coordonnées 2D du robot et n_y la largeur en y de la salle.
    Elle a au moins 2 méthodes: can_move(aspiR, direction) et compute_move(aspiR, direction)), avec direction un caractère "N", "S", "E" ou "W"
 -> La classe Room qui modélise la pièce et testée dans le fichier Test_Room.py
    Elle a au moins une méthode: has_wall(index, direction) qui retourne True ou False si pour la case à la position "1D" index, il y a un mur dans la direction concernée.

 -> La classe AspiR qui modélise la pièce et testée dans le fichier Test_AspiR.py
    Elle a au moins 2 méthodes: clean() qui calcule un chemin optimal et check_cleaning(path) qui vérifie que le chemin path permet au robot de bien passer partout.
