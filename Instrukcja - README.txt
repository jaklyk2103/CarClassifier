Aby uruchomiæ projekt mobilnej apki trzeba mieæ zainstalowany React Native. W tym s¹ dwie œcie¿ki:
- Expo
- CLI

Szkic fabularny:
My mamy apkê w CLI, czyli w pe³noprawnym natywnym stylu, gdzie mamy wszystkie funkcjonalnoœci jakie oferuje React Native oraz ca³¹ kontrolê nad aplikacj¹, jak¹ oferuje React Native. Co do Expo, to taki l¿ejszy sposób na zaczêcie z React Native, razem z tym jest ca³e œrodowisko, program w którym mo¿na pisaæ i debuggowaæ aplikacjê, ale trochê ogranicza ona mo¿liwoœci, no i nie mamy wszystkich dostêpnych bibliotek, a co za tym funkcjonalnoœci smartfona, np. nie mo¿na w Expo u¿ywaæ Bluetooth.

Do sedna:

1. Instalacja React Native:
Wykonaæ kroki z tego, gdyby zajmowa³o Ci to du¿o czasu czy by³y jakieœ problemy to pisz, mi wszystko posz³o g³adko (polecam zainstalowaæ tego Chocolateya, bo to jedna linijka, a u³atwia):
https://facebook.github.io/react-native/docs/getting-started.html 

Aplikacje mo¿na uruchamiaæ albo przez emulator dostêpny dziêki Android Studio, albo na w³asnym smartfonie. (Moja opinia: emulator potrafi mocno muliæ, przez co wolê u¿ywaæ w³asnego smartfona, nie by³o u mnie z tym ¿adnych problemów, po prostu wpinasz USBa i ju¿ wszystko wykrywa.)

2. Development:

Good news: Po zainstalowaniu, je¿eli bêdziesz u¿ywaæ smartfona, a nie emulatora, to w normalnych warunkach nie musisz nawet tykaæ Android Studio, same pliki .js mo¿esz edytowaæ w dowolnym edytorze(oczywiœcie polecam Visual Studio Code), a aplikacjê uruchamiasz w terminalu/bashu/shellu poprzez komende "react-native run-android". 

Instalowanie bibliotek:

npm install <nazwa_biblioteki>
react-native link


react-native android-run wystarczy odpaliæ raz, ta komenda uruchamia taki serwer (nazywa siê chyba Metro), który obs³uguje komunikacjê z urz¹dzeniem w kwestii zmian w kodzie. Na samym urz¹dzeniu poprzez "shake" mo¿esz uruchomiæ ma³e menu i tam odpaliæ bodaj¿e "Live Reload", co pozwoli na automatyczne prze³adowywanie aplikacji po zapisaniu pliku .js z dowolnymi zmianami. (Niektóre zmiany w kodzie, np. w state komponentu wymagaj¹ rêcznego prze³adowania aplikacji, w tym ma³ym menu po "shake" jest te¿ opcja Reload.)