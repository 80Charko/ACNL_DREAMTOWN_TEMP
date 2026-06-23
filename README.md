# A WAY TO GET THE garden_plus OF A DREAM TOWN:
## WHAT YOU WILL NEED:
- A modded 3ds with [this](https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/releases/tag/v1.9.6-beta.1) version of vapecord
- A way to view the DataBase (I used https://sqliteviewer.app/)
- A working New Leaf Save (I only tested this with USAWA but it's supposed to work with any saves)
- [HxD](https://mh-nexus.de/en/hxd/) or an online Hex Editor.
- Acnl dream decryptor from https://github.com/Slattz/ACNL_Research/blob/master/Dream%20Town%20Downloading/ACNLDC/ACNLDreamDecryptor.exe

## DISCLAIMER
Make sure to backup your save before starting this tutorial. This is a temporary solution for those who really want to play into the dream town.<br>
Doing this tutorial will give you access to the town as if you were the creator. <br>
This tutorial is meant to be understandable for everyone, so mb if I say things that are just common sense.<br>
### Let's start.

# 1 Retrieve the city from the Pretendo archive
Go to https://archive.org/download/animal-crossing-new-leaf-dream-suite-archive then download the file named **datastore.sqlite**<br>
Once you have the file, open it in your in the database reader of your choice.<br> We will use [this](https://sqliteviewer.app/)<br>
Import the data.<br><img width="1792" height="497" alt="" src="https://github.com/user-attachments/assets/94ee7743-0bd0-49d4-9db0-4456483be816" />

The click on object and you will see a bunch of town<br>
<img width="1915" height="757" alt="" src="https://github.com/user-attachments/assets/9ad5f2fb-8b2a-4e70-9eec-f48372365ef7" />
Search for the town you'd like to visit and then write somewhere the **data_id** and the **version**.
<img width="1912" height="175" alt="" src="https://github.com/user-attachments/assets/c5957435-d364-4359-a1f6-9b936b049c12" />
*for this tutorial we will use PINK from LYON.*

Once you have everything, copy this link, "https://r2-acnl-public.pretendo.network/objects/DataID_vVersion.bin", and replace DataID with the data_id of your town and Version with the version you have.<br> *Ex. For LYON@PINK we have https://r2-acnl-public.pretendo.network/objects/1000117_v16.bin*<br>
Then paste it into your navigator and you'll have your bin file.

# 2 Fix the save file
You should have this in your folder. <br>
<img width="893" height="427" alt="" src="https://github.com/user-attachments/assets/caaa9db5-66bd-4cc6-b335-c528af6122c2" /><br>

Open ACNLDreamDecryptor.exe and put the name of your file in it and press ENTER. You will get something like DataID_vVersion.bin.dat<br>
<img width="952" height="497" alt="" src="https://github.com/user-attachments/assets/8645e22a-620a-4cee-8730-6250006395b7" /><br>

You might have noticed that the file wasn't the same size as our garden_plus.dat. ([Explaination](https://github.com/Slattz/ACNL_Research/blob/master/Dream%20Town%20Downloading/decrypting_dreams.txt))<br>
<img width="983" height="487" alt="" src="https://github.com/user-attachments/assets/875e390f-f09b-4356-bcc0-9d117612f234" /><br>
We will add some bytes to the now decrypted file to make it reach 551Ko. <br>
Now you will need to follow carefully what i'll do.<br>
1. Open both of your files on HxD and click on garden_plus.dat<br>
<img width="1415" height="736" alt="1-png" src="https://github.com/user-attachments/assets/7c60632f-9cb3-4db4-9718-5e0381ccc3e0" />

2. Copy everything from 00 to 70<br>
<img width="1406" height="718" alt="2-png" src="https://github.com/user-attachments/assets/7a81a2f0-f5d7-4bf0-8200-8100312e3643" />

3. Go to your decrypted file and paste everything you copied in front of the file<br>
<img width="1410" height="702" alt="3-png" src="https://github.com/user-attachments/assets/1174fd28-4bf5-4f59-814d-72b63d6e3659" /><br>

<img width="1407" height="706" alt="4-png" src="https://github.com/user-attachments/assets/df8c3090-4161-4ffc-991b-7d5e82b88fdf" /><br>

4. Then go back to your garden_plus file and right-click wherever you like, then click on ‘Select Block’.<br>
<img width="1376" height="705" alt="5-png" src="https://github.com/user-attachments/assets/86406ee6-8760-4f6e-bea9-9347646ef9fc" /><br>

5. Then put in Start 718F0 and on End whatever you want but a big number like mine. It will select everything.<br>
<img width="287" height="318" alt="6-png" src="https://github.com/user-attachments/assets/7a6cf670-d840-4e9c-bd58-fa4bf94ddb20" /><br>

6. Copy everything.<br>
<img width="1402" height="517" alt="8-png" src="https://github.com/user-attachments/assets/806042b5-2b36-4ad0-9c3f-7fc16ed2bab6" /><br>

7. Go back to your decrypted file then select the line 718F0 (dont copy it) and the paste on it everything you copied earlier.<br>
<img width="1413" height="702" alt="9-png" src="https://github.com/user-attachments/assets/cbdda970-1c26-4124-a16e-7e235e64e006" /><br>

8. You should have something like this. If it's not ending with the line 89AF0 then you did something wrong 💔.<br>
<img width="1403" height="707" alt="10-png" src="https://github.com/user-attachments/assets/2b6bcd5e-170b-44ec-8664-4cee2ec8f3c7" /><br>

9. Once you have everything, save the file and the you will be able to open it on save editor.<br>
<img width="1386" height="707" alt="11-png" src="https://github.com/user-attachments/assets/ec32723b-f2a9-4838-8cf4-b26c2bfae1d0" /><br>

10. You should have a file with either 550Ko or 551Ko it's fine either way.<br>
<img width="892" height="53" alt="12 png" src="https://github.com/user-attachments/assets/3da5fcd3-22fa-493d-9e96-f6496604dfc2" /> <br>

You will now be able to view the save file in the save editor but you wont be able to play with it since checksum is invalid (from my guess).<br>
**NOTE: If the save file has an invalid building in it, it wont load on the save editor.<br> Mine didn't open so I checked it on [NLSE](https://github.com/kwsch/NLSE) and it did have an invalid building (the photobooth was in the map)**.<br>
<img width="852" height="941" alt="BROSKI" src="https://github.com/user-attachments/assets/337d3077-da0c-4636-af47-7cf493bffa94" /><br>

Remove it and Tada you can modify it with save editor and even export the map! But as i said earlier you wont be able to play with the save file by itself.<br>
<img width="1920" height="1080" alt="13" src="https://github.com/user-attachments/assets/8db0b38e-2f00-41de-b74f-2effeb0c2416" /><br>
So that's why we will use vapecord.<br>

# 3 Play on the city !
*Note: I'll use citra for this tutorial but it'll be the same on a real 3ds*

Install this version of [vapecord](https://github.com/RedShyGuy/Vapecord-ACNL-Plugin/releases/tag/v1.9.6-beta.1) on your 3ds.<br>
I wont explain how to install it since there are a lot of tutorial out there.<br>
*Note: I'll use citra for this tutorial but it'll be the same on a real 3ds*<br>
**BACK UP YOUR SAVE BEFORE DOING THE NEXT PART**<br>

1. Copy this file.<br>
<img width="892" height="53" alt="12 png" src="https://github.com/user-attachments/assets/3da5fcd3-22fa-493d-9e96-f6496604dfc2" /> <br>
 
2. Paste it in your Vapecord folder in this specific path.<br>
**(your sd card)/Vapecord/(Your version (my save file was USA welcome Amiibo so USAWA))/Save**<br>
Paste your garden file on it.<br>
<img width="1853" height="982" alt="65" src="https://github.com/user-attachments/assets/33b9e370-3eb6-43c5-b94d-b719c9ef1694" /><br>

3. Then launch the game and stay on this screen.<br>
<img width="1377" height="625" alt="image" src="https://github.com/user-attachments/assets/454f822f-41dd-45d7-9ce1-1a3787261706" /><br>
4. Open Vapecord and select "Save codes" and follow the other images.<br>

<img width="822" height="157" alt="image" src="https://github.com/user-attachments/assets/1b67c07d-7d73-41f5-a254-cf06ec52f500" /><br>

<img width="807" height="512" alt="image" src="https://github.com/user-attachments/assets/ae1a6d5b-07f8-4057-b2d4-4a7c5ec0c512" /><br>

<img width="1293" height="572" alt="image" src="https://github.com/user-attachments/assets/e22cec62-9f68-4b4c-b441-fc00a3957f42" /><br>

<img width="1296" height="331" alt="image" src="https://github.com/user-attachments/assets/de590915-69a1-4123-9490-0eac04807793" /><br>

<img width="1287" height="606" alt="image" src="https://github.com/user-attachments/assets/4f4cb101-14dc-462c-bb38-1653e00881c1" /><br>

5. Then launch the game and wait till you're out of your house.<br>
*You might have noticed that Isabell said the right town name but you're still in your own town.* <br>
Redo the same steps as before<br>
<img width="1391" height="587" alt="image" src="https://github.com/user-attachments/assets/d4d86138-af9c-4b67-8d57-964ea4cb3b45" /><br>

<img width="822" height="157" alt="image" src="https://github.com/user-attachments/assets/1b67c07d-7d73-41f5-a254-cf06ec52f500" /><br>

<img width="807" height="512" alt="image" src="https://github.com/user-attachments/assets/ae1a6d5b-07f8-4057-b2d4-4a7c5ec0c512" /><br>

<img width="1293" height="572" alt="image" src="https://github.com/user-attachments/assets/e22cec62-9f68-4b4c-b441-fc00a3957f42" /><br>

<img width="1296" height="331" alt="image" src="https://github.com/user-attachments/assets/de590915-69a1-4123-9490-0eac04807793" /><br>

<img width="1287" height="606" alt="image" src="https://github.com/user-attachments/assets/4f4cb101-14dc-462c-bb38-1653e00881c1" /><br>

6. And also do this.<br>
<img width="822" height="552" alt="image" src="https://github.com/user-attachments/assets/22dfd755-d762-4397-92c9-f448fc161d78" /><br>

<img width="806" height="507" alt="image" src="https://github.com/user-attachments/assets/c21e2b2f-0df3-4ec0-abed-13c61d19f3d5" /><br>

7. Then faint !<br>
<img width="1391" height="585" alt="image" src="https://github.com/user-attachments/assets/86443bac-d819-47c8-994a-f1097499f88f" /><br>

8. You will wake up as the other player ! Wow.<br>
<img width="1392" height="580" alt="image" src="https://github.com/user-attachments/assets/38aca7a5-07f2-4e00-b833-8527f7db9361" /><br>
<img width="1386" height="577" alt="image" src="https://github.com/user-attachments/assets/06251200-de56-457b-b82a-2610fd6c6aed" /><br>

You can save now and restart the game and you will keep the town!<br>
<img width="1383" height="583" alt="image" src="https://github.com/user-attachments/assets/c30e3c3a-6e81-407e-ad02-2c42cee8f55d" /><br>


