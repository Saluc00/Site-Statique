import argparse
import markdown2
import re
import os
from os.path import splitext

# Detecte s'il y a la présence d'une URL
link_patterns=[(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]

# Intégration du head dans les variables ci dessous
head = "<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset='utf-8'/>\n\t<title>"+ "YES ! J'ai REUSSSIII !!!!" +"</title>\n\t<link rel='stylesheet' type='text/css' href='main.css'/>\n</head>\n<body>\n"
finHead = "</body>\n</html>"

def convert(md_input, html_output):
    # Ouvre le fichier .md
    malist = os.listdir(f'./'+md_input)
    for i in malist:
        f = open(f'./{md_input}/{i}', "r")
        html = markdown2.markdown(f.read(), extras=["link-patterns"] ,link_patterns=link_patterns)
        nomFichier = os.path.splitext(i)[0]
        # Affiche que tel fichier est bien convertie ! :D
        print(f'Le fichier "{nomFichier}" à bien été convertie !')
        # Genere / Modifie le fichier html
        html_file = open(f'./{html_output}/{nomFichier}.html', 'w')
        # Ecrit le debut du head
        html_file.write(head)
        # Ecrit le fichier .md convertie
        html_file.write(html)
        #Ecrit les denieres balises (</body> et </html>)
        html_file.write(finHead)

# Element graphique sympa :D
print('''                                                                                                
           ,,                                                   ,,                              
 .M"""bgd  db   mm                .M"""bgd mm            mm     db                              
,MI    "Y       MM               ,MI    "Y MM            MM                        s             
`MMb.    `7MM mmMMmm .gP"Ya      `MMb.   mmMMmm  ,6"Yb.mmMMmm `7MM  ,dW"Yvd `7MM  `7MM  .gP"Ya  
  `YMMNq.  MM   MM  ,M'   Yb       `YMMNq. MM   8)   MM  MM     MM ,W'   MM   MM    MM ,M'   Yb 
.     `MM  MM   MM  8M""""""     .     `MM MM    ,pm9MM  MM     MM 8M    MM   MM    MM 8M"""""" 
Mb     dM  MM   MM  YM.    ,     Mb     dM MM   8M   MM  MM     MM YA.   MM   MM    MM YM.    , 
P"Ybmmd" .JMML. `Mbmo`Mbmmd'     P"Ybmmd"  `Mbmo`Moo9^Yo.`Mbmo.JMML.`MbmdMM   `Mbod"YML.`Mbmmd' 
                                                                         MM                     
                                                                       .JMML.                   
''')
print('Bienvenue sur l\'invite de commande du generateur de site statique.\nVeuillez entrer -i [FICHIER .MD] -u [FICHIER HTML] !\n\n')
    
parser = argparse.ArgumentParser()

# Création des commandes du CLI
parser.add_argument("-i", '--input',help='Inserer le chemin du fichier .md')
parser.add_argument("-u", '--output',help='Inserer le chemin du fichier .html')
args = parser.parse_args()

print(f'Confirmation de la conversion de l\'intégrité des fichiers de "{args.input}" en fichiers html dans "{args.output}" \n\n')

# Appel de la fonction qui convertit le fichié demandé
convert(args.input, args.output)