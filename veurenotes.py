import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def veurenotes(allNotesNP, ownNotes, titol="Notes",display10=False, printImg=False):
    allNotes = list([note for note in allNotesNP if note not in ["np", "Np", "-", ""]])

    #if de cant find the note we are looking for, we look for the next biggest closest one
    for i in range(len(ownNotes)):
        if ownNotes[i] not in allNotes:
            j = 0
            while(allNotes[j] < ownNotes[i]): j += 1
            ownNotes[i] = allNotes[j]
      

    abandonaments = len(allNotesNP) - len(allNotes) 
    allNotes.sort()
    average = sum(allNotes) / len(allNotes)
    averageWithNP = sum(allNotes) / len(allNotesNP)

    # Creating the plot
    plt.figure(figsize=(10, 6))
    plt.plot(allNotes, marker='o', color='b')


    legend_handles = []
    legend_handles.append(mlines.Line2D([], [], color='none', marker='None', label=f'Nombre de gent: {len(allNotesNP)}'))
    legend_handles.append(mlines.Line2D([], [], color='b', marker='o', linestyle='-', label='totes les notes'))

    # Highlight and plot own notes in different color and marker style
    colors = [
    "green", "orange", "purple", "yellow",  
    "blue", "red", "cyan", "magenta",
    "black", "white", "grey", "lime",
    "maroon", "navy", "olive", "teal",
    "aqua", "fuchsia", "silver"
]


    for i, note in enumerate(ownNotes):
        if note in allNotes:
            note_index = allNotes.index(note)   # +1 as index starts from 1
            plt.scatter([note_index], [note], color=colors[i], marker='o', zorder=3) # Higher zorder
            
            percentage = ((note_index )/ (len(allNotes)-1)) * 100
            plt.text(note_index, note, f'{percentage:.2f}%', color="black", fontsize=8, verticalalignment='bottom')


            ranking_text = f' Top:{len(allNotes[note_index::])}'
            percentage_text = f'{percentage:.1f}%'
            legend_handles.append(mlines.Line2D([], [], color=colors[i], marker='o', linestyle='None', label=f'{ownNotes[i]}, sobre el : {percentage_text} {ranking_text}'))

        else:
            print(f"Note {note} in ownNotes not found in allNotes")
    
    percentatgeSuspesos = (len([note for note in allNotes if note < 5]) + abandonaments) /  len(allNotesNP) * 100
    legend_handles.append(mlines.Line2D([], [], color='none', marker='None', label=f'Suspesos: {percentatgeSuspesos:.2f}%'))
    percentatgeSobre9 = len([note for note in allNotes if note >= 9]) / len(allNotes) * 100
    legend_handles.append(mlines.Line2D([], [], color='none', marker='None', label=f'Gent sobre de 9: {percentatgeSobre9:.2f}%'))
    legend_handles.append(mlines.Line2D([], [], color='none', marker='None', label=f'Abandonaments: {abandonaments:.0f}'))

    plt.axhline(y=average, color='r', linestyle='-')
    legend_handles.append(mlines.Line2D([], [], color='red', linestyle='-', label=f'Mitjana: {average:.2f}'))
    legend_handles.append(mlines.Line2D([], [], color='none', linestyle='None', label=f'Mitjana Comptant NP: {averageWithNP:.2f}'))


    if printImg:
        titol2 = ''.join([word.capitalize() for word in titol.split()])
        plt.savefig(titol2 + ".png", format='png', dpi=300)

    if(display10):
        plt.ylim(0, 10)
    
    
    plt.yticks(range(1, round(max(allNotes))+1))  # left index
    plt.axhline(y=5, color='grey', linestyle='--', linewidth=1)
    plt.text(-7, 5, '', verticalalignment='center', color='grey')
    plt.legend(handles=legend_handles)
    plt.title(titol)
    plt.xlabel('')
    plt.ylabel('')
    plt.grid(True)
    plt.show()

    
