
from veurenotes import veurenotes

# Llista de totes les notes, 'np' i '-' es tracten com a casos especials
all_notes_np = [8.7, 5, 6, 7, 'np', 8, 4, 1.4, 5, 6, 10, '-']
# Les teves notes individuals per destacar
own_notes = [6, 8.7]

# Genera el gràfic amb un títol
veurenotes(all_notes_np, own_notes, titol="Example Plot")



#Ús Avançat
#Si necessites ajustar el rang visible del gràfic o guardar la imatge resultant, pots utilitzar les banderes display10 i printImg:

veurenotes(all_notes_np, own_notes, titol="Adjusted Plot", display10=True, printImg=True)