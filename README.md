# Walking Pad Stream Widget
![Screenshot of the widget](https://i.imgur.com/Muab187.png)
![Screenshot of the small widget](https://i.imgur.com/pOLzp6E.png)



# Setup
Hier wird kurz beschrieben wie man das Widget ans Laufen und die Verbindung zum Walking Pad hinbekommt.

## Get Token and IP

### IP
IP des Gerätes im lokalen Netzwerk. Am besten über den Router herausfinden. Kommt auf den Router an.

### Token
Siehe https://python-miio.readthedocs.io/en/latest/discovery.html#tokens-from-mi-home-logs.
1. Gerät mit der originalen MiiHome-App einrichten
2. MiiHome-App Version 5.4.49 auf Google suchen und installieren
3. Einloggen
4. Wenn nicht vorhanden -> Gerät einrichten
5. Mit einem Android File Browser zu `SmartHome/logs/plug_DeviceManager` navigieren
6. Die zuletzt erstellte Datei in dem Ordner öffnen und nach 'Token' suchen
7. Token kopieren
8. Neuste MiiHome-App von Google Play installieren
9. ????
10. Profit

## Tool
1. Den letzten Release von dieser Seite (https://github.com/Trojan13/walking-pad-obs-widget/releases/) herunterladen
2. IP und Token in der Config.txt anpassen
3. Config.txt und wstest.exe müssen in dem gleichen Ordner liegen
4. Wstest.exe ausführen



## OBS
In OBS eine neue Quelle hinzufügen. 'Browser Quelle' aussuchen.
![Browser Quelle in OBS](https://i.imgur.com/ihrxZLF.png)

'Lokale Datei' auswählen und `widget.html` wählen. Breite auf `320` und Höhe auf `90`setzen.
![Einstellungen der Browser Quelle](https://i.imgur.com/TDyVfMq.png)


