"""Enregistrer en .pyw pour ne pas afficher l'executable"""

import pyscreenshot 
from time import sleep

def screen(a,b):
    for i in range(0,a):
        image = pyscreenshot.grab()
        image.save(f'{i}','png')
        sleep(b)

screen(3,1)
