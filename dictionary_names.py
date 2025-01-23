import re
import pandas as pd
import shutil
import numpy as np
from datetime import datetime
import os

# Pobranie danych z plików csv
files = ['monitoring_cen_komputronik.csv', 'monitoring_cen_mediaexpert.csv', 'monitoring_cen_oleole.csv', 'monitoring_cen_rtv.csv', 'monitoring_cen_xkom.csv']
# Łączenie plików w ramki dnaych oraz zbudowanie listy ramek danych
data = []
for name in files:
    df = pd.read_csv(name)
    data.append(df)

# Połączenie ramek danych
df = pd.concat(data, ignore_index=True)

# Zmiana niektórych wyrażeń pozwalająca poprawić działanie
def replacement_expression(text):
    # Zmiana fraz z ANC
    expression = {
        "z aktywną redukcją szumów": "ANC",
        "z aktywną redukcją hałasu": "ANC"
    }
    
    # Zamiana liczb rzymskich na arabskie
    numbers = {
        'I': '1',
        'II': '2',
        'III': '3'
    }
    
    # Zamiana wyrażeń na "ANC"
    for text_old, text_new in expression.items():
        text = text.replace(text_old, text_new)
    
    # Zamiana cyfr rzymskich na arabskie
    for number_type_1, number_type_2 in numbers.items():
        text = re.sub(r'\b' + number_type_1 + r'\b', number_type_2, text)

    return text

# Funkcja normalizująca nazwę
def normalize_name(name):
    # Zastosowanie zamian z wczesniejszych funkcji: zamiana niektórych słów na "ANC" i liczebników
    name = replacement_expression(name.lower())
    # Usunięcie znaków specjalnych zachowując cyfry i znaki +, ', "
    return re.sub(r'[^a-zA-Z0-9+\"\' ]+', ' ', name).strip() 

# Funkcja zwracająca cyfry z nazwy
def select_number(name):
    # d - cyfry od 0 do 9
    return re.findall(r'\d+', name)

# Funkcja sprawdzająca obecność słowa "pro" w nazwie
def pro(name):
    return 'pro' in name.lower()

# Funkcja rozdzielająca nazwę na oddzielne słowa
def word_set(name):
    normalized_name = normalize_name(name)
    return set(normalized_name.split())

# Funkcja dopasowania za pomocą odległości Levenshteina
def levenshtein_distance(name_1, name_2):
    m = len(name_1)
    n = len(name_2)
    matrix = np.zeros((n+1, m+1))
    matrix[0] = range(0, m + 1)
    matrix[:, 0] = range(0, n + 1)
    name_1_split = list(name_1)
    name_2_split = list(name_2)
    for i in range(1,m+1):
        for j in range(1, n+1):
            if name_1_split[i-1] == name_2_split[j-1]:
                cost = 0
            else:
                cost = 1
            matrix[j,i] = min(matrix[j-1,i]+1, matrix[j, i-1]+1, matrix[j-1,i-1] + cost)
    return matrix[-1][-1]
        


# Funkcja dopasowująca nazwy do ich słownikowych nazw
def match_levenshtein(original_name, dictionary_names):
    original_words = word_set(original_name)
    original_numbers = select_number(original_name)
    original_pro = pro(original_name)
    best_match = None
    best_count = 0
    best_number_match = False
    best_pro_match = False

    for dictionary_name in dictionary_names:
        dictionary_words = word_set(dictionary_name)
        dictionary_number = select_number(dictionary_name)
        dictionary_pro = pro(dictionary_name)
        
        # Porównanie cyfr
        number_match = len(set(original_numbers).intersection(dictionary_number)) > 0
        pro_match = original_pro == dictionary_pro

        # Badanie czy są cyfry lub pro
        if number_match or pro_match:
            if not best_number_match and not best_pro_match:
                best_match = dictionary_name
                best_count = len(original_words.intersection(dictionary_words))
                best_number_match = number_match
                best_pro_match = pro_match
            elif (best_number_match and number_match) or (best_pro_match and pro_match):
                # Jeśli cyfry lub "pro" są zgodne to sprawdzanie dalej na podstawie liczby takich samych słów
                matched_count = len(original_words.intersection(dictionary_words))
                if matched_count > best_count:
                    best_count = matched_count
                    best_match = dictionary_name
                elif matched_count == best_count:
                    # Jeśli taki sam wynik to dopasowanie odległością Levenshteina
                    distance = levenshtein_distance(original_name, dictionary_name)
                    if best_match is not None:
                        best_distance = levenshtein_distance(original_name, best_match)
                        if distance < best_distance:
                            best_match = dictionary_name
        else:
            # Jeśli nie ma dopasowania cyfr oraz słowa pro to normalne porównanie bez priorytetu
            matched_count = len(original_words.intersection(dictionary_words))
            if matched_count > best_count and not (best_number_match or best_pro_match):
                best_count = matched_count
                best_match = dictionary_name
            elif matched_count == best_count and not (best_number_match or best_pro_match):
                # Jeśli taki sam wynik to dopasowanie odległością Levenshteina
                distance = levenshtein_distance(original_name, dictionary_name)
                if best_match is not None:
                    best_distance = levenshtein_distance(original_name, best_match)
                    if distance < best_distance:
                        best_match = dictionary_name

    return best_match if best_count > 0 else original_name


# Pobranie nazw urządzeń z ramki danych
original_names = df['Nazwa urzadzenia'].tolist()

# Wprowadzenie listy słownikowej nazw
dictionary_names = [
    "Samsung Galaxy Buds 3",
    "Apple AirPods 3 gen (Lightning Charging Case)",
    "Apple AirPods Pro 2 gen MagSafe",
    "Apple AirPods 2 gen",
    "JBL Tune 770 BT NC",
    "JBL Tune 520 BT",
    "Technics EAH-A800E-K",
    "Soundcore Liberty 4 NC",
    "Sony WHCH720 ANC",
    "Apple AirPods 4 gen",
    "Apple AirPods 4 gen ANC (z aktywną redukcją hałasu)",
    "Samsung Galaxy Tab A9 (X110) 128GB",
    "Huawei MatePad 11.5\" S 8/256GB + klwiatura + rysik",
    "Apple iPad 10.2\" A13 (9.gen) 64GB",
    "Lenovo TAB P11 2 gen (TB350FU) 6/128GB",
    "Lenovo Yoga Tab 13 (YT-K606F) 8/128GB",
    "Xiaomi Redmi Pad Pro 8/256GB",
    "Samsung Galaxy Tab A9+ (X210) 128GB",
    "LG UltraFine 27UN880P-B - 27\"",
    "iiyama G-Master GB2470HSU-B5 Red Eagle - 23.8\"",
    "iiyama G-Master GB2770QSU-B5 Red Eagle - 27\"",
    "Samsung Odyssey G30A LS27AG300NRXEN - 27\"",
    "ASUS VY279HGE - 27\"",
    "Xiaomi A27i - 27\"",
    "LG UltraGear 27GS85Q-B - 27\""
]

# Inicjacja pustej listy do przechowywania danych
new_names = []

# Testowanie funkcji dopasowania
for name in original_names:
    match = match_levenshtein(name, dictionary_names)
    new_names.append(match)

# Zamiana nazw na nowe
df["Nazwa urzadzenia"] = new_names

# Zapis do pliku csv
# Inicjacja nazwy pliku i folderu
csv = 'monitoring_cen.csv'
archive_folder = 'archiwum_cen'

# Sprawdzenie czy folder do przechowywania danych archiwalnych istnieje - zabezpieczenie przed tratą danych
if not os.path.exists(archive_folder):
    os.makedirs(archive_folder)

# Zapis do pliku głównego i do archiwum
if os.path.exists(csv):
    archive_name = f"monitoring_cen_{datetime.now().strftime('%Y-%m-%d')}.csv"
    shutil.copy(csv, os.path.join(archive_folder, archive_name))
    df.to_csv(csv, mode='w', index=False, header=True)
else:
    df.to_csv(csv, mode='w', index=False, header=True)
