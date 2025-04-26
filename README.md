## Praktyka Programowania - Laboratorium 1 Podejście TDD 

Podejście TDD (Test-Driven Development) w wielkim skrócie polega na napisaniu w pierwszej kolejności testów według wytycznych biznesowych ( w szczególności uwzględniając przypadki brzegowe tzw. edge/corner case'y) i następnie, po napisaniu testów przystąpienie do napisania funkcjonalności, która spełania wszystkie założenia testów.
Podejście to ma swoja wady jak i również zalety. Główną wadą tego podejścia jest duża czasochłonność, ponieważ testy same w sobie nie są funkcjonalnością biznesową, a ich wymyślenie z uwzglęnieniem przypadków brzegowych zajmuję dodatkowy czas. 
Są jednak również zalet takie jak:
- Napisana funkcjonalność będzie od początku przygotowana na przypadki brzegowe
- Programista na bierząco może sprawdzać feedback, czy jego implementacja jest zgodna z założeniami
- Możliwość łatwego wdrożenia innej osoby, po napisaniu testów jednostkowych, inna osoba, która implementuje funkcjoanlność jest w stanie łatwiej się wdrożyć
- Wczesne wykrycie błędów powoduje, że koszty nie rosną, jak w przypadku późniejszego ich wykrecia


W podanym zadaniu napisałem testy jednostkowe z wykorzystaniem biblioteki unittest, w IDE pyCharm

Projekt składa się z 2 klas:
Klasa główna z funkcją add, która przyjmuje String oddzielony przecinkami, lub znakiem nowej lini i funkcjami pomocnicznymi.
Klasa testowa zawierająca testy jednostkowe, od najprostszych przypadków do trudniejszych

Dobre praktyki:

Sama nazwa testu powinna wskazywać, co jest testowane, ale również dobrą praktyką jest stosowanie komentarzy powiązanych z dokumentacją.
Dobrą praktyką jest stosowanie konwencji BDD (Behavior Driven Development, inaczej given-when-then), która to konwencja dzieli testy na 3 części, oraz metoda powina być ujęta w konwencji should_***_when_*** np. should_return_zero_when_provided_empty_string

Inną dobrą praktyką jest stosowanie komentarzy, w konwencji, która definuje, co metoda przyjmuje oraz co zwraca 


