import FreeSimpleGUI as sg
import os
from SAVE_FILE_FIXER import ACNL_DREAM_FIXER as ACD
from SAVE_FILE_FIXER import checksum_fix_in_python as ACF
# Terrible code incoming but at least it's working :)

#########################################################################################################################
dossier_du_script = os.path.dirname(os.path.abspath(__file__))


acnl_decrypt_path = os.path.join(dossier_du_script, "ACNLDreamDecryptor.exe")
acnl_logo = os.path.join(dossier_du_script, "icon.ico")
#########################################################################################################################

### ONLY THE LAYOUT ###
sg.theme("Default 1")
layout = [ [sg.Text("Select the folder with your .bin files in it.")],
           [sg.Input(key='-BINFILEFOLDER-'), sg.FolderBrowse()],
           [sg.Text("Select the output folder for your new files.")],
           [sg.Input(key='-OUTPUTFOLDER-'), sg.FolderBrowse()],
           [sg.HorizontalSeparator()],
           [sg.Push(),sg.Button("Continue", size=14),sg.Button("Exit", size=14),sg.Push()]]


window = sg.Window('New Leaf Bin Files SEMI-FIXER', layout, icon=acnl_logo)
choix = ""

def select_version():
    global choix
    layout_selce = [[sg.Text("Select the region of your future garden_plus file (USAWA or EURWA)")],
                    [sg.Button("USA", key="-USA-", size=14), sg.Button("EUR", key='-EUR-', size=14), sg.Button("HELP", key='-HELP-', size=14)]]

    window_select = sg.Window(layout=layout_selce, title="SELECT YOUR REGION", icon="./Icon.ico", finalize=True, modal=True)

    while True:

        event_select, values_select = window_select.read()

        if event_select == sg.WIN_CLOSED:
            break

        if event_select == "-USA-":
            choix = "USA"
            break
        if event_select == "-EUR-":
            choix = "EUR"
            break
        if event_select == "-HELP-":
            sg.popup("How does this work ?\n",
            "You must select the same region as your save file.\n",
            "If you're playing one the USA verison of ACNLWA, The id is supposed to be 00198f00",
            "If you're playing one the EUR verison of ACNLWA, The id is supposed to be 00198e00",
            "It doesn't support the original version of ACNL and the JPN/KOR version (sorry :))",title="HELP",icon="./Icon.ico")

    window_select.close()
while True:

    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "Continue":
        dossier_avec_bin = values["-BINFILEFOLDER-"]
        Output_folder = values["-OUTPUTFOLDER-"]

        if not dossier_avec_bin or not Output_folder:
            sg.popup_error("ERROR", "Please Insert all the needed files for it to work. There wont be other verifications!!!")
            continue
            
        
        try:
            contenu_dossier = os.listdir(dossier_avec_bin)

            compteur = 0
            select_version()
            for fichier_nom in contenu_dossier:

                chemin_complet_dedans = os.path.join(dossier_avec_bin, fichier_nom)
                nom_du_fichier_sans_extension, extension_delaisse = os.path.splitext(fichier_nom)

                if os.path.isfile(chemin_complet_dedans):

                    if choix == "":
                        sg.popup_error("THERE WAS AN ERROR WHEN YOU SELECTED THE REGION, PLEASE RETRY")
                        break

                    nv_chemin_complet_sortie2 = os.path.join(dossier_du_script, "fichier_fix.dat")
                    with open(nv_chemin_complet_sortie2, 'wb') as f:
                        f.write(ACD.Fix_garden_plus_file(ACD.fixed_size_garden_plus_file(fichier_nom, dossier_avec_bin, choix),choix))

                    nv_chemin_complet_sortie3 = os.path.join(Output_folder, f"garden_plus({choix}WA)-({nom_du_fichier_sans_extension}).dat")
                    with open(nv_chemin_complet_sortie3, 'wb') as f:
                        f.write(ACF.fix_all_checksums(nv_chemin_complet_sortie2))
                    compteur +=1

                    #Deletes useless files
                    if os.path.exists(nv_chemin_complet_sortie2):
                        os.remove(nv_chemin_complet_sortie2)
            sg.popup(f"{compteur} files were converted !", title="Finished")
            break
        except Exception as e:
            sg.popup_error("Error", f"Informations : {e}")



window.close()