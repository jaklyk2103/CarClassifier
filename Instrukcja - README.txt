Aby uruchomi� projekt mobilnej apki trzeba mie� zainstalowany React Native. W tym s� dwie �cie�ki:
- Expo
- CLI

Szkic fabularny:
My mamy apk� w CLI, czyli w pe�noprawnym natywnym stylu, gdzie mamy wszystkie funkcjonalno�ci jakie oferuje React Native oraz ca�� kontrol� nad aplikacj�, jak� oferuje React Native. Co do Expo, to taki l�ejszy spos�b na zacz�cie z React Native, razem z tym jest ca�e �rodowisko, program w kt�rym mo�na pisa� i debuggowa� aplikacj�, ale troch� ogranicza ona mo�liwo�ci, no i nie mamy wszystkich dost�pnych bibliotek, a co za tym funkcjonalno�ci smartfona, np. nie mo�na w Expo u�ywa� Bluetooth.

Do sedna:

1. Instalacja React Native:
Wykona� kroki z tego, gdyby zajmowa�o Ci to du�o czasu czy by�y jakie� problemy to pisz, mi wszystko posz�o g�adko (polecam zainstalowa� tego Chocolateya, bo to jedna linijka, a u�atwia):
https://facebook.github.io/react-native/docs/getting-started.html 

Aplikacje mo�na uruchamia� albo przez emulator dost�pny dzi�ki Android Studio, albo na w�asnym smartfonie. (Moja opinia: emulator potrafi mocno muli�, przez co wol� u�ywa� w�asnego smartfona, nie by�o u mnie z tym �adnych problem�w, po prostu wpinasz USBa i ju� wszystko wykrywa.)

2. Development:

Good news: Po zainstalowaniu, je�eli b�dziesz u�ywa� smartfona, a nie emulatora, to w normalnych warunkach nie musisz nawet tyka� Android Studio, same pliki .js mo�esz edytowa� w dowolnym edytorze(oczywi�cie polecam Visual Studio Code), a aplikacj� uruchamiasz w terminalu/bashu/shellu poprzez komende "react-native run-android". 

Instalowanie bibliotek:

npm install <nazwa_biblioteki>
react-native link


react-native android-run wystarczy odpali� raz, ta komenda uruchamia taki serwer (nazywa si� chyba Metro), kt�ry obs�uguje komunikacj� z urz�dzeniem w kwestii zmian w kodzie. Na samym urz�dzeniu poprzez "shake" mo�esz uruchomi� ma�e menu i tam odpali� bodaj�e "Live Reload", co pozwoli na automatyczne prze�adowywanie aplikacji po zapisaniu pliku .js z dowolnymi zmianami. (Niekt�re zmiany w kodzie, np. w state komponentu wymagaj� r�cznego prze�adowania aplikacji, w tym ma�ym menu po "shake" jest te� opcja Reload.)