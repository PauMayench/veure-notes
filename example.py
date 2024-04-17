
from veurenotes import veurenotes

# Llista de totes les notes, 'np', '-', '', 'Np' es tracten com a no presentats i son equivalents
all_notes_np = [2.3, 6.0, 4.55, 5.51, 8.4, 4.91, 4.94, 0.22, 2.05, 5.79, 'np', 3.87, 9.15, 6.7, 3.84, 5.42, 5.24, 5.72, 3.42, 'np', 'np', 'np', 0.31, 1.5, 5.61, 6.37, 5.5, 4.32, 'np', 5.9, 3.72, 9.47, 2.01, 6.89, 5.8, 8.77, 6.82, 4.55, 4.23, 6.79, 6.51, 4.95, 4.68, 6.56, 7.46, 7.35, 9.70, 6.12, 6.86, 8.91, 6.95, 6.91, 'np', 6.12, 6.08, 5.76, 6.38, 5.3, 6.28, 3.5, 4.26, 5.45, 'np', 5.85, 4.42, 0.19, 6.01, 8.25, 0.86, 1.26, 4.9]

# Les teves notes individuals per destacar
own_notes = [6, 7.4]

# Genera el gràfic amb un títol
veurenotes(all_notes_np, own_notes, titol="Example Plot")



#Ús Avançat
#Si necessites ajustar el rang visible del gràfic o guardar la imatge resultant, pots utilitzar les banderes display10 i printImg:

veurenotes(all_notes_np, own_notes, titol="Adjusted Plot", display10=True, printImg=True)