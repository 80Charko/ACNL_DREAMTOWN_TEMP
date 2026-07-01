import subprocess
import os

##########################################################
# THIS IS REALLY A TEMPORARY WAY TO FIX THE GARDEN DAT ! #
##########################################################


Dossier_ou_le_script_est = os.path.dirname(os.path.abspath(__file__))
acnl_decryptor_path = os.path.join(Dossier_ou_le_script_est, "ACNLDreamDecryptor.exe")
# Juste un stockage du chemin du decrypteur

def fixed_size_garden_plus_file(fichie_a_decrypte, dossier_du_fichier_a_decrypter, Version):
    
    chemin_complet_fichier_a_decrypte = os.path.join(dossier_du_fichier_a_decrypter, fichie_a_decrypte)
    if Version == "USA":
        chemin_complet_fichier_decrypte = os.path.join(Dossier_ou_le_script_est, "USA_DATA.Dat")
    else:
        chemin_complet_fichier_decrypte = os.path.join(Dossier_ou_le_script_est, "EUR_DATA.Dat")

    nom_sans_extension, extension = os.path.splitext(fichie_a_decrypte)

    subprocess.run([acnl_decryptor_path],input=chemin_complet_fichier_a_decrypte, text=True)

    nouveau_chemin = os.path.join(dossier_du_fichier_a_decrypter, f"{nom_sans_extension}_decrypted.dat")

    ###### FIX POUR LES FICHIER (A CORRIGER!!!) ######
    decrypted_file = open(nouveau_chemin,"rb")
    dfile = decrypted_file.read()
    data_from_dfile = bytearray(dfile)

    garden_dat = open(chemin_complet_fichier_decrypte,"rb")
    Save_file = garden_dat.read()
    save_files_array = bytearray(Save_file)

    bytes_necessaires_deb = save_files_array[:0x80]
    bytes_necessaires_fin = save_files_array[0x71880:]
    fichier_final = bytes_necessaires_deb + data_from_dfile + bytes_necessaires_fin

    ### VERIFICATIONS FINALES EN CAS DE PROBLEME ###

    if len(fichier_final) > len(save_files_array):
        a_remove = len(fichier_final) - len(save_files_array)
        fichier_final = fichier_final[0:len(fichier_final)-a_remove]

    if len(fichier_final) < len(save_files_array):
        a_ajouter = len(save_files_array) - len(fichier_final)
        son = bytearray([0] * a_ajouter)
        fichier_final += son
    
    nouveau_garden_dat_chemin = os.path.join(Dossier_ou_le_script_est, "fixed_garden_for_region.dat")
    with open(nouveau_garden_dat_chemin,"wb") as New_Garden:
        New_Garden.write(fichier_final)

    decrypted_file.close()
    garden_dat.close()

    if os.path.exists(nouveau_chemin):
        os.remove(nouveau_chemin)
    
    return nouveau_garden_dat_chemin


def Fix_garden_plus_file(nv_fichier, choix):
    if choix == "USA":
        chemin_fichier_fixe = os.path.join(Dossier_ou_le_script_est, "USA_VERSION_FIXEE.dat")
        chemin_fichier_non_fixe = os.path.join(Dossier_ou_le_script_est, "USA_VERSION_NON_FIXEE.dat")
    else:
        chemin_fichier_fixe = os.path.join(Dossier_ou_le_script_est, "EUR_VERSION_FIXEE.dat")
        chemin_fichier_non_fixe = os.path.join(Dossier_ou_le_script_est, "EUR_VERSION_NON_FIXEE.dat")

    fichier_non_fonctionnel = bytearray(open(chemin_fichier_non_fixe, "rb").read()) # SAVE FILE NON FONCTIONNEL AVEC BYTES FIXés
    fichier_fonctionnel = bytearray(open(chemin_fichier_fixe, "rb").read()) # SAVE FILE POUR CHANGER LA REGION

    offset_differents_fonctionnel = {}
    offset_differents_non_fonctionnel = {}

    for offset in range(len(fichier_fonctionnel)):
        if fichier_fonctionnel[offset] != fichier_non_fonctionnel[offset]:
            offset_differents_fonctionnel[offset] = fichier_fonctionnel[offset]
            offset_differents_non_fonctionnel[offset] = fichier_non_fonctionnel[offset]

    chemin_save_file = nv_fichier
    autre_fichier_a_fix = bytearray(open(chemin_save_file, "rb").read())

    for item, value in offset_differents_fonctionnel.items():
        autre_fichier_a_fix[item] = value

    nouveau_garden_dat_chemin = os.path.join(Dossier_ou_le_script_est, "fixed_garden_for_region.dat")
    if os.path.exists(nouveau_garden_dat_chemin):
        os.remove(nouveau_garden_dat_chemin)

    return autre_fichier_a_fix

if __name__ == "__main__":
    #nv_chemin_complet_sortie2 = os.path.join(dossier_du_script, "fichier_fix.dat")
    #with open(nv_chemin_complet_sortie2, 'wb') as f:
        #f.write(Fix_garden_plus_file(fixed_size_garden_plus_file("USA_DATA.dat","1018230_43.bin")))

    #nv_chemin_complet_sortie3 = os.path.join(dossier_du_script, f"garden_plus.dat")
    #with open(nv_chemin_complet_sortie3, 'wb') as f:
        #f.write(fix_all_checksums(nv_chemin_complet_sortie2))
    print("salut")