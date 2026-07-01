import FreeSimpleGUI as sg
import random
import sqlite3
import os
import requests

dossier = os.path.dirname(os.path.abspath(__file__))
sqlite_file = os.path.join(dossier, "datastore.sqlite") # azy


###################### PARTIE SQLITE 3 (PAS TROP OPTI) ##########################
con = sqlite3.connect(sqlite_file)
cur = con.cursor()

stockage = cur.execute("SELECT name, data_id, version FROM objects")
son = stockage.fetchall()

def split_name_et_nom(info):
    """NE PRENDS PAS EN COMPTE LES VILLES QUI S'APPELLENT @@@@@@@@@@@@@@ !!!!"""
    ville, nom = "Anytown", "Anyone"
    if not "@" in info:
        return [info, "Anyone"]
    else:
        ville, nom = info.rsplit('@', 1)
    return [ville, nom]

DB = []
for i in range(len(son)):
   DB.append({  "id": i,
        "ville" : split_name_et_nom(son[i][0])[0],
        "nom" : split_name_et_nom(son[i][0])[1],
        "data_id" : son[i][1],
        "version" : son[i][2]
    })

con.close()
#############################################################################################
sg.theme("Default 1")
en_tetes = ["Id", "Town", "Name", "Version", "data_id"]
layout = [
    [sg.Text("Search for a town:"), 
     sg.Input(key="-TOWNSEARCH-", size=(20, 1), enable_events=True),
     sg.Text("Search for a name:"), 
     sg.Input(key="-NAMESEARCH-", size=(20, 1), enable_events=True),
     sg.Button(key="-RANDOMSAVE-",button_text='Random Towns',size=(20, 1)),
     sg.Text("Max rows:"),
     sg.Combo([50, 100, 200, 500, "All"], default_value=100, key="-LIMIT-", enable_events=True, size=(5, 1))
     ],
    [sg.Table(values=[], headings=en_tetes, max_col_width=35,
              auto_size_columns=True,
              display_row_numbers=False,
              justification='left',
              num_rows=22,
              key="-TABLEAU-",
              enable_events=True,
              expand_x=True)],
    [sg.HorizontalSeparator()],
    [sg.Text("NONE SELECTED", key="-SELECTION-", text_color="Green")],
    [sg.Button("Download", size=(20, 1)), 
     sg.Button("Selected towns",size=(20, 1)),
     sg.Button("About",size=(20, 1)), 
     sg.Button("Close",size=(20, 1))
     ]
]

window = sg.Window("ACNL DREAM TOWN DOWNLOADER", layout, finalize=True, icon="./Icon.ico")
villes_selectionnees = []
#########################################FIN DU LAYOUT########################""  
output_folder = None
def filtrer_et_mettre_a_jour(mode_random=False):
    """Filtre la base de données ou génère du random"""
    limite = values["-LIMIT-"]

    if str(limite).isdigit():
        nb_lignes = int(limite)
    elif not str(limite).isdigit():
        nb_lignes = 100
    
    if mode_random:
        #Dans le cas ou l'utilisateur tape un nombre plus grand que la base de donnée soit plus grand que 2XXXXXX - j'ai pas la valeur exact sur moi
        random_liste = random.sample(DB, min(nb_lignes, len(DB)))
        liste_des_randoms = []
        for user in random_liste:
            liste_des_randoms.append([user["id"], user["ville"], user["nom"], user["version"],user["data_id"]])
        return liste_des_randoms
    
    saisie_nom = values["-NAMESEARCH-"].lower()
    saisie_ville = values["-TOWNSEARCH-"].lower()
    
    resultats = []
    for user in DB:
        if saisie_nom in user["nom"].lower() and saisie_ville in user["ville"].lower():
            resultats.append([user["id"], user["ville"], user["nom"], user["version"],user["data_id"]])
    
    if limite != "All":
        if not str(limite).isdigit():
            limite = 100
        resultats = resultats[:int(limite)]
        
    return resultats

resultats_actuels = []
for user in DB[:100]:
    resultats_actuels.append([user["id"], user["ville"], user["nom"], user["version"],user["data_id"]])
window["-TABLEAU-"].update(values=resultats_actuels)


########################################################################################################
sle_town_open = False

def pop_up_villes_select():
    global sle_town_open
    sle_town_open = True
    global villes_selectionnees
    """Toutes les villes séléctionnées s'afficherons ici!"""
    layout_selection = [
        [sg.Text("SELECTED TOWNS (Click on it to remove the town)")],
        [sg.Table(values=villes_selectionnees, headings=en_tetes, max_col_width=35,
                  auto_size_columns=True, num_rows=15, key="-TABLEAUVILLESELECT-", 
                  enable_events=True, expand_x=True)],
        [sg.Button("Close", size=(15, 1))]
    ]
    window_sel = sg.Window(layout=layout_selection, title="YOUR SELECTED TOWNS", icon="./Icon.ico", finalize=True, modal=True)
    window_sel["-TABLEAUVILLESELECT-"].update(values=villes_selectionnees)

    while True:
        eventsel, valuessel = window_sel.read()
        
        if eventsel == "Close" or eventsel == sg.WIN_CLOSED:
            break

        if eventsel == "-TABLEAUVILLESELECT-":
            indices = valuessel["-TABLEAUVILLESELECT-"]
            if indices:
                indice_a_sup = indices[0]
                villes_selectionnees.pop(indice_a_sup)
                window_sel["-TABLEAUVILLESELECT-"].update(values=villes_selectionnees)
    window_sel.close()
    sle_town_open = False


def add_town(town):
    global villes_selectionnees
    if town not in villes_selectionnees:
        villes_selectionnees.append(town)

def download_towns():
    for villes in villes_selectionnees:
        data_id = str(villes[4]) # Exemple de DataID
        version = str(villes[3])
        urls = f"https://r2-acnl-public.pretendo.network/objects/{data_id}_v{version}.bin"
        try:
            response = requests.get(urls)

            if response.status_code == 200:
                nom_fichier = f"{data_id}_{version}.bin"
                fichier_final = os.path.join(output_folder, nom_fichier)

                with open(fichier_final, "wb") as f:
                    f.write(response.content)
                print("File successfully downloaded")
            else:
                print(f"Couldn't download this file {villes[4]}_v{villes[3]}.bin")
        
        except ConnectionError as e:
            print(f"Error: {e}")
        finally:
            print(f"Data for this town {villes[1]} - {villes[2]}")
            response.close()

def Download_pop_up():
    global output_folder
    layout_download = [[sg.Input(key='-FOLDER-'),sg.FolderBrowse()],
                       [sg.Button("Download", size=(20, 1), key='-DOWNCLICKED-'), sg.Button("Close",size=(20, 1)),sg.Push()],
                       [sg.Text(f"Last action : None", key="-NS-", text_color="Red")]]

    window_download = sg.Window(layout=layout_download, title="DOWNLOAD YOUR SELECTED TOWNS !", icon="./Icon.ico", finalize=True, modal=True)

    while True:

        event_down, value_down = window_download.read()

        if event_down in ("Close", sg.WIN_CLOSED):
            break
        
        if event_down == "-DOWNCLICKED-":
            output_folder = value_down["-FOLDER-"]
            window_download["-NS-"].update("Last action : Downloading...")
            if output_folder:
                download_towns()
                window_download["-NS-"].update("Last action : All your files have been downloaded")
            else:
                window_download["-NS-"].update("PLEASE INPUT A VALID OUTPUT FOLDER")

    window_download.close()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "Close":
        break

    if event == "Selected towns":
        if not sle_town_open:
            pop_up_villes_select()
        
    if event == "About":
        sg.popup("ACNL Dream Town Downloader\nA temporary solution ;d.") 

    if event == "-RANDOMSAVE-":
        random_towns = filtrer_et_mettre_a_jour(mode_random=True)
        resultats_actuels = random_towns
        window["-TABLEAU-"].update(values=random_towns)
    
    if event in ("-TOWNSEARCH-","-NAMESEARCH-","-LIMIT-"):
        towns = filtrer_et_mettre_a_jour(mode_random=False)
        resultats_actuels = towns
        window["-TABLEAU-"].update(values=towns)

    if event == "-TABLEAU-":
        indices_selectionnes = values["-TABLEAU-"]
        
        if indices_selectionnes and resultats_actuels:
            donnee_stockee = resultats_actuels[indices_selectionnes[0]]
            add_town(donnee_stockee)
            print(donnee_stockee[0])
            window["-SELECTION-"].update(f"SELECTED DATA : Town-> {donnee_stockee[1]}, Name-> {donnee_stockee[2]}")
    
    if event == "Download":
        Download_pop_up()

window.close()