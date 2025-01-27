Celem niniejszej pracy jest opracowanie systemu pozwalającego monitorować rynek i
analizować go pod względem zachowań konkurencji na platformach handlu internetowego.
Wstęp teoretyczny zawiera analizę konkurencji, w tym czynników i elementów,
na które warto zwracać uwagę oraz obszerny opis technologii i narzędzi możliwych do
wykorzystania w tym obszarze. Po analizie istniejących rozwiązań, zdecydowano się na
opracowanie własnego, dostosowanego do konkretnego przypadku zastosowania narzędzia.
Pierwszym elementem systemu jest wykorzystanie mechanizmu web scrapingu do
gromadzenia danych o zmianach cen konkurencji. Aby wdrożyć to rozwiązanie wykorzystany
został system Selenium WebDriver, w środowisku Python. Ekstrakcja danych
następuje z pięciu sklepów, z których pobierane są informacje dla tych samych produktów.
Bezpośrednia identyfikacja produktów na podstawie nazw nie była możliwa
z uwagi na różnice pomiędzy dostawcami, więc zaimplementowany został algorytm do
standaryzacji tych nazw, wykorzystujący algorytm oparty na odległości Levenshteina.
Cały powyższy proces został zautomatyzowany poprzez umieszczenie rozwiązania w
chmurze obliczeniowej. Plik z gotowymi danymi jest udostępniany, w taki sposób aby
mógł być pobrany przez program Power BI. Dane są oczyszczane, przekształcane i załadowywane
w celu dostarczenia interaktywnego interfejsu użytkownika, zawierającego
wizualizacje i inne rozwiązania do monitorowania zmian cen. Ostatnim etapem jest
odpowiednie wzbogacenie danych o nowe cechy wyliczone na podstawie istniejących
danych. Przeprowadzono wnikliwą analizę otrzymanych rezultatów i na podstawie odpowiedzi
na pytania badawcze sformułowano wnioski pozwalające poznać zachowania
i strategie cenowe konkurencji.
