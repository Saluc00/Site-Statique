import argparse
import markdown2
import os

def convert(md_input, html_output):
    # Ouvre le fichier .md
    input_file = open(md_input, "r")
    html = markdown2.markdown(input_file.read())
    # Genere / Modifie le fichier html
    if '.html' in html_output:
        html_file = open(html_output, 'w')
    if '.html' not in html_output:
        html_file = open(f'{html_output}.html', 'w')
    html_file.writelines(html)

print('''                                                                                                
           ,,                                                   ,,                              
 .M"""bgd  db   mm                .M"""bgd mm            mm     db                              
,MI    "Y       MM               ,MI    "Y MM            MM                                     
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
parser.add_argument("-i", '--input',help='Inserer le chemin du fichier .md')
parser.add_argument("-u", '--output',help='Inserer le chemin du fichier .html')
args = parser.parse_args()
if False:
    print('Merci d"inscrire "-i [VOTRE FICHIER .MD] -u [NOM DU FICHIER HTML]"')
elif args.input and args.output:
    print('md : ' + args.input + ' html : ' + args.output)
else:
    pass
f = open(args.input, 'a')
convert(args.input, args.output)
