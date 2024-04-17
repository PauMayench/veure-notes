# Veure Notes

El script `veurenotes` permet visualitzar gràficament la distribució de les notes i analitzar estadístiques associades. Aquesta eina destaca les notes individuals dins del conjunt i ofereix informació estadística rellevant.

## Característiques

- Representació visual de la distribució de notes.
- Destacar notes individuals dins de la distribució.
- Càlcul i mostra de dades estadístiques com la mitjana de notes, percentatge de suspensos, entre altres.
- Possibilitat de personalitzar el títol i els límits de les notes mostrades.

## Instal·lació

Aquest script requereix Python i la biblioteca matplotlib. Assegura't de tenir Python instal·lat a la teva màquina i instal·la matplotlib utilitzant pip:

pip install matplotlib

## Ús
Per utilitzar l'script, necessites importar-lo i proporcionar-li una llista de notes. Així és com pots executar un exemple:

from veurenotes import veurenotes

# Llista de totes les notes, 'np' i '-' es tracten com a casos especials
all_notes_np = [8.7, 5, 6, 7, 'np', 8, 4, 1.4, 5, 6, 10, '-']
# Les teves notes individuals per destacar
own_notes = [6, 8.7]

# Genera el gràfic amb un títol
veurenotes(all_notes_np, own_notes, titol="Example Plot")



## Ús Avançat
Si necessites ajustar el rang visible del gràfic o guardar la imatge resultant, pots utilitzar les banderes display10 i printImg:

veurenotes(all_notes_np, own_notes, titol="Adjusted Plot", display10=True, printImg=True)


## Trucs
Per filtrar i editar llistes de notes ràpidament:

Copia totes les notes en un fitxer .txt en VSCode.
Utilitza Alt + Shift + Click de Ratolí per seleccionar columnes de text.
Això també es pot utilitzar per afegir comes o eliminar entrades,tambe pots afegir "," per a crear llistes de python rapidament

## Millores Futures
Afegir una funció de filtre per a no haver de filtar a ma al principi