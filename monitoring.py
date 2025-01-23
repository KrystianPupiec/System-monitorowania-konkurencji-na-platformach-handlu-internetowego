from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime
import pandas as pd
import os

import random

report = pd.DataFrame(columns=["Sklep", "Opis", "Data"])
date = datetime.today().strftime('%Y-%m-%d')


# Komputronik
try:
    # Konfiguracja przeglądarki
    options = Options()
    options.add_argument("--headless")
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)


    links = {
        'https://www.komputronik.pl/product/919834/sluchawki-samsung-galaxy-buds3-srebrne.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/784783/apple-airpods-3-gen-lightning-charging-case-.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/861792/sluchawki-apple-airpods-pro-2-gen-z-magsafe-usb-c.html': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/616063/apple-airpods-2-gen.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/836971/jbl-tune-770-bt-nc-czarny.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/818988/jbl-tune-520-bt-czarne.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/748451/technics-eah-a800e-k-czarny.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/876615/sluchawki-soundcore-liberty-4-nc-czarny.html': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/814360/sony-whch720nb-czarny.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/930296/sluchawki-apple-airpods-4-gen.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/930297/sluchawki-apple-airpods-4-gen-anc.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/878621/samsung-galaxy-tab-a9-8-7-128gb-szary-x110-.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/912943/tablet-huawei-matepad-11-5-s-wifi-8-256gb-szary-klawiatura-rysik.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/734199/apple-ipad-10-2-a13-wi-fi-64gb-gwiezdna-szarosc-9-gen-.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/819895/lenovo-tab-p11-2nd-gen-tb350fu-6-128gb-wifi-zabf0355pl-szary.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/898283/tablet-lenovo-yoga-tab-13-yt-k606f-8-128gb-wifi-za8e0027pl-czarny.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/916337/tablet-xiaomi-redmi-pad-pro-8-256gb-wifi-graphite-gray.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/878624/samsung-galaxy-tab-a9-11-0-128gb-szary-x210-.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/828020/lg-27un880p-b.html': {'typ': 'Monitor', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/816195/iiyama-red-eagle-gb2470hsu-b5-ips-165hz-flc.html': {'typ': 'Monitor', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/816196/iiyama-red-eagle-gb2770qsu-b5-ips-165hz-flc.html': {'typ': 'Monitor', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/802946/samsung-s27ag300nrx-27-va-full-hd-1ms-144hz-pivot.html': {'typ': 'Monitor', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/831494/asus-vy279hge-27-full-hd-ips-144hz-1ms-mprt-.html': {'typ': 'Monitor', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/901102/monitor-xiaomi-monitor-a27i.html': {'typ': 'Monitor', 'sklep': 'Komputronik'},
        'https://www.komputronik.pl/product/927362/monitor-lg-27gs85q-b.html': {'typ': 'Monitor', 'sklep': 'Komputronik'}
    }

    device_names = []
    device_types = []  
    stores = []
    prices = []
    opinions = []
    opinions_count = []  
    availability = []  


    for link, other in links.items():

        # Uruchomienie przeglądarki
        driver.get(link)
        
        # Wprowadzenie opóżnienia o 2 sekundy
        time.sleep(2)
        
        # Pobranie nazw urządzeń
        try:
            name = driver.find_element(By.XPATH, "//h1[@data-name='productName' and contains(@class, 'line-clamp-2') and contains(@class, 'font-headline') and contains(@class, 'font-bold')]")
            name_text = name.text
            device_names.append(name_text) 
        except:
            device_names.append(None) 
        

        # Pobranie cen
        try:
            price = driver.find_element(By.XPATH, "//div[contains(@class, 'text-3xl') and contains(@class, 'font-bold') and contains(@class, 'leading-8')]")
            price_text = price.text
            prices.append(price_text) 
        except:
            prices.append(None) 

        
        # Pobranie średniej oceny i liczbę opinii
        try:
                opinion = driver.find_element(By.XPATH, "//div[contains(@class, 'text-center') and contains(@class, 'leading-4') and contains(@class, 'text-[2.625rem]')]")
                opinion_text = opinion.text
                opinions.append(opinion_text)
                opinion_count = driver.find_element(By.XPATH, "//div[contains(@class, 'flex') and contains(@class, 'space-x-2') and .//i[contains(@class, 'i-messages')]]/span")
                opinion_count_text = opinion_count.text
                opinions_count.append(opinion_count_text)
        except:
                opinions.append(None) 
                opinions_count.append('0')

        # Sprawdzenie dostępności produktu
        try:
            availability_product = driver.find_element(By.XPATH, "//div[contains(text(), 'Produkt tymczasowo niedostępny.')] | //div[contains(text(), 'Archiwum')]")
            availability.append(0) 
        except:
            availability.append(1) 
        

        # Dodanie typu urządzenia i sklepu 
        device_types.append(other['typ']) 
        stores.append(other['sklep'])  
            
    # Zakończenie sesji
    driver.quit()

    # Utworzenie ramki danych
    df = pd.DataFrame({
        'Nazwa urzadzenia': device_names,
        'Cena (zł)': prices,
        'Ocena': opinions,  
        'Liczba ocen': opinions_count,
        'Czy dostepny': availability,
        'Typ urzadzenia': device_types,
        'Sklep': stores
    })

    # Operacje na danych - zmiana typu, usunięcie niepotrzebnych słów i znaków
    df['Data'] = date
    df['Cena (zł)'] = df['Cena (zł)'].str.replace(' ', '').str.replace('zł', '')
    df['Liczba ocen'] = df['Liczba ocen'].str.extract('(\d+)')
    df = df.replace(',', '.', regex=True)
    print(df)

    # Zapis do pliku csv
    csv = 'monitoring_cen_komputronik.csv'

    if os.path.exists(csv):
        df.to_csv(csv, mode='a', index=False, header=False)
    else:
        df.to_csv(csv, mode='w', index=False, header=True)

except:
    # Dodanie wiersza do pliku csv z informacją o błędzie i wskazanie produktu gdzie błąd nastąpił
    row = ["Komputronik", f"Błąd przy wykonywaniu dla produktu: {device_names[-1]}", date]
    report.loc[len(report)] = row
    csv = 'raport.csv'
    if os.path.exists(csv):
        report.to_csv(csv, mode='a', index=False, header=False)
    else:
        report.to_csv(csv, mode='w', index=False, header=True)


# Media Expert
try:
    # Konfiguracja przeglądarki
    options = Options()
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    links = {
        'https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-douszne-samsung-buds-3-anc-wodoodporne-srebrny': {'typ': 'Słuchawki (douszne)', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-douszne-apple-airpods-iii-bialy-etui-z-lightning': {'typ': 'Słuchawki (douszne)', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-bluetooth-apple-airpods-pro-2-tws-usb-c-dokanalowe-biale': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-bluetooth-apple-airpods-ii-dokanalowe-z-ladowarka-biale': {'typ': 'Słuchawki (douszne)', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-bluetooth-jbl-tune-770-anc-nauszne-czarne': {'typ': 'Słuchawki (nauszne)', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-nauszne-jbl-tune-520bt-czarny': {'typ': 'Słuchawki (nauszne)', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-nauszne-technics-eah-a800-czarny': {'typ': 'Słuchawki (nauszne)', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-dokanalowe-soundcore-liberty-4-nc-czarny': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-nauszne-sony-whch720nb-czarny': {'typ': 'Słuchawki (nauszne)', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-bluetooth-apple-airpods-4': {'typ': 'Słuchawki (douszne)', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/telewizory-i-rtv/sluchawki/wszystkie-sluchawki/sluchawki-bluetooth-apple-airpods-4-z-aktywna-redukcja-halasu': {'typ': 'Słuchawki (douszne)', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/tablety-i-e-booki/tablety/tablet-samsung-galaxy-tab-a9-8-7-8-128-gb-wi-fi-szary': {'typ': 'Tablet', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/tablety-i-e-booki/tablety/tablet-huawei-matepad-s-11-5-8-256-gb-wi-fi-szary-rysik-klawiatura': {'typ': 'Tablet', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/tablety-i-e-booki/tablety/tablet-apple-ipad-10-2-2021-mk2k3fd-a-a13-8gb-64gb-wifi-10-2-ipados-grey': {'typ': 'Tablet', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/tablety-i-e-booki/tablety/tablet-lenovo-tab-p11-2-gen-tb350fu-11-5-6-128-gb-wi-fi-szary-rysik': {'typ': 'Tablet', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/tablety-i-e-booki/tablety/tablet-lenovo-yoga-tab-13-yt-k606f-13-8-128-gb-wi-fi-czarny': {'typ': 'Tablet', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/tablety-i-e-booki/tablety/tablet-xiaomi-redmi-pad-pro-12-1-8-256-gb-wi-fi-szary': {'typ': 'Tablet', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/tablety-i-e-booki/tablety/tablet-samsung-galaxy-tab-a9-11-8-128-gb-wi-fi-szary': {'typ': 'Tablet', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/monitory-led/monitor-lg-ultrafine-27un880p-b-27-3840x2160px-ips': {'typ': 'Monitor', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/monitory-led/monitor-iiyama-g-master-gb2470hsu-b5-23-8-1920x1080px-ips-165hz-0-8-ms': {'typ': 'Monitor', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/monitory-led/monitor-iiyama-g-master-gb2770qsu-b5-27-2560x1440px-ips-165hz-0-5-ms': {'typ': 'Monitor', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/monitory-led/monitor-led-samsung-27-ls27ag300nrxen-odyssey-g3': {'typ': 'Monitor', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/monitory-led/monitor-asus-vy279hge-27-1920x1080px-ips-144hz-1-ms': {'typ': 'Monitor', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/monitory-led/monitor-xiaomi-a27i-27-1920x1080px-ips-100hz': {'typ': 'Monitor', 'sklep': 'Media Expert'},
        'https://www.mediaexpert.pl/komputery-i-tablety/monitory-led/monitor-lg-ultragear-27gs85q-b-27-2560x1440px-ips-180hz-1-ms-gtg': {'typ': 'Monitor', 'sklep': 'Media Expert'}
    }


    device_names = []
    device_types = [] 
    stores = []
    prices = []
    opinions = []
    opinions_count = []  
    availability = []  



    for link, other in links.items():
        # Przypadek gdy strona z produktem przestaje istnieć
        # if link == 'https://www.mediaexpert.pl/komputery-i-tablety/tablety-i-e-booki/tablety/tablet-lenovo-tab-p11-2-gen-tb350fu-11-5-6-128-gb-wi-fi-szary-rysik':
        #     device_names.append('Tablet LENOVO Tab P11 2 gen. TB350FU 11.5"" 6/128 GB Wi-Fi Szary + Rysik')
        #     device_types.append('Tablet')
        #     stores.append('Media Expert')
        #     prices.append('None')
        #     opinions.append('None')
        #     opinions_count.append(0)
        #     availability.append(0)
        #     continue

        # Uruchomienie przeglądarki
        driver.get(link)
        # Zmaksymalizowanie okna przeglądarki
        driver.maximize_window()    
        # Wprowadzenie opóźnienia o 5 sekund
        time.sleep(5)


        try:
            # Obsługa przypadku z zarchiwizowanym produktem
            archiwum = driver.find_element(By.XPATH, "//div[contains(@class, 'heading') and contains(text(), 'Produkt archiwalny')]")
            name = driver.find_element(By.XPATH, "//h1[contains(@class, 'title is-title')]")
            name_text = name.text
            device_names.append(name_text)
            prices.append(0)  
            opinions.append(None)
            availability.append(0)
            opinions_count.append(0)
            device_types.append(other['typ'])  
            stores.append(other['sklep'])  

        except:
            # Pobranie nazw urządzeń
            try:
                name = driver.find_element(By.XPATH, "//h1[contains(@class, 'name is-title')]")
                name_text = name.text
                device_names.append(name_text) 
            except:
                device_names.append(None)  
             
            # Pobranie cen
            try:
                # Oczekiwanie na załadowanie elementu
                price_whole = WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class, 'whole')]"))
                )

                price_cents = WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class, 'cents')]")))

                pricesp = []

                for i, whole_element in enumerate(price_whole):
                    whole_price = whole_element.text.strip()

                    if i < len(price_cents):  
                        cents_price = price_cents[i].text.strip()
                    else:
                        cents_price = "00"  

                    full_price = f"{whole_price}.{cents_price}"
                    pricesp.append(full_price)
                    
                if pricesp:
                    prices.append(pricesp[-2])
                    price_temp = []  
                    price_temp.append(pricesp[-2])                
                else:
                    price_temp = []  
                    prices.append(None)  
                    price_temp.append('None')

            except:
                price_temp = []  
                price_temp.append('None')
                prices.append(None)  


            # Pobranie średniej oceny
            try:
                # przewijanie strony do połowy wysokości okna dwa razy
                scroll_height = driver.execute_script("return document.body.scrollHeight")
                driver.execute_script(f"window.scrollTo(0, {scroll_height / 2});")
                time.sleep(3)
                scroll_height = driver.execute_script("return document.body.scrollHeight")
                driver.execute_script(f"window.scrollTo(0, {scroll_height / 2});")
                time.sleep(3)

                opinion = WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(text(), '/5') and number(substring-before(text(), '/5'))]"))
                )
                time.sleep(3)
                for element_opinion in opinion[:1]:  
                    text = element_opinion.text.split('/')[0].strip()
                    if text:  
                        opinions.append(text)
            except:
                opinions.append(None)

            # Pobranie liczby opinii
            try:
                time.sleep(3)
                opinion_count_elements = WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(text(), ' opinii') and number(substring-before(text(), ' opinii'))]"))
                )
                time.sleep(3)
                for element_opinion_count in opinion_count_elements[:1]:  
                    text = element_opinion_count.text.split(' ')[0].strip()
                    if text:  
                        opinions_count.append(text)
            except:
                opinions_count.append('0')

            # Sprawdzenie dostępności produktu
            try:
                if price_temp[0] == 'None': 
                    availability.append(0)  
                else:
                    availability.append(1) 
            except:
                availability.append(0)

            # Dodanie typu urządzenia i sklepu
            device_types.append(other['typ'])  
            stores.append(other['sklep']) 
            
    # Zamknięcie sesji
    driver.quit()

    # Utworzenie ramki danych
    df = pd.DataFrame({
        'Nazwa urzadzenia': device_names,
        'Cena (zł)': prices,
        'Ocena': opinions,  
        'Liczba ocen': opinions_count,
        'Czy dostepny': availability,
        'Typ urzadzenia': device_types,
        'Sklep': stores
    })

    # Operacje na danych - zmiana typu, usunięcie niepotrzebnych słów i znaków
    df['Data'] = date
    df['Cena (zł)'] = df['Cena (zł)'].str.replace(' ', '').str.replace('zł', '').str.replace('\u202f', '')
    df['Liczba ocen'] = df['Liczba ocen'].str.extract('(\d+)')
    df = df.replace(',', '.', regex=True)
    print(df)

    # Zapis do pliku csv
    csv = 'monitoring_cen_mediaexpert.csv'

    if os.path.exists(csv):
        df.to_csv(csv, mode='a', index=False, header=False)
    else:
        df.to_csv(csv, mode='w', index=False, header=True)   
except:
    # Dodanie wiersza do pliku csv z informacją o błędzie i wskazanie produktu gdzie błąd nastąpił
    row = ["Media Expert", f"Błąd przy wykonywaniu dla produktu: {device_names[-1]}", date]
    report.loc[len(report)] = row
    csv = 'raport.csv'
    if os.path.exists(csv):
        report.to_csv(csv, mode='a', index=False, header=False)
    else:
        report.to_csv(csv, mode='w', index=False, header=True)



# OleOle!
try:
    # Konfiguracja przeglądarki
    options = Options()
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    links = {
        'https://www.oleole.pl/sluchawki/samsung-galaxy-buds3-sm-r530nza-douszne-bluetooth-srebrny.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/sluchawki/apple-airpods-3-generacji-z-etui-ladujacym-lightning-mpny3zma.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/sluchawki/apple-airpods-pro-2-generacji-z-etui-magsafe-usb-c-dokanalowe-bluetooth-5-3.bhtml': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/sluchawki/apple-airpods-z-etui-ladujacym.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/sluchawki/jbl-sluch-nauszne-bt-jbl-tune-770nc-czarne.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/sluchawki/jbl-sluchawki-bt-nauszne-tune-520-bt-czarne.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/sluchawki/technics-sluchawki-nauszne-bt-eah-a800e-k-czarne.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/sluchawki/soundcore-liberty-4-nc-dokanalowe-bluetooth-5-3-czarny.bhtml': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/sluchawki/sony-wh-ch720-nauszne-czarny.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/sluchawki/apple-airpods-4-douszne-bluetooth-5-3-bialy.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/sluchawki/apple-airpods-4-z-aktywna-redukcja-halasu-douszne-bluetooth-5-3-bialy.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/ipad-i-tablety-multimedialne/samsung-tablet-galaxy-tab-a9-8-128gb-wifi-gray.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/ipad-i-tablety-multimedialne/huawei-tablet-matepad-s-11-5-8-256gb-klaw-pen3.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/ipad-i-tablety-multimedialne/apple-ipad-mini-2021-wi-fi-64gb-gwiezdna-szarosc.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/ipad-i-tablety-multimedialne/lenovo-tablet-p11-11-5-6gb-128gb-wifi-grey.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/ipad-i-tablety-multimedialne/lenovo-yoga-tab-13-yt-k606f-13-8-128gb-wi-fi.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/ipad-i-tablety-multimedialne/xiaomi-tablet-redmi-pad-pro-8-256ggb-graph-gray.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/ipad-i-tablety-multimedialne/samsung-tablet-galaxy-tab-a9-8-128gb-wifi-gray_1.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/monitory-led-i-lcd/lg-monitor-27un880p-b.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/monitory-led-i-lcd/iiyama-monitor-gb2470hsu-b5.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/monitory-led-i-lcd/iiyama-monitor-gb2770qsu-b5.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/monitory-led-i-lcd/samsung-monitor-s27ag300nr.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/monitory-led-i-lcd/asus-monitor-vy279hge.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/monitory-led-i-lcd/xiaomi-monitor-a27i.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'},
        'https://www.oleole.pl/monitory-led-i-lcd/lg-monitor-27gs85q-b.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'}
    }

    # Inicjacja pustych list do przechowywania danych
    device_names = []
    device_types = []  
    stores = []
    prices = []
    opinions = []
    opinions_count = []  
    availability = [] 

    for link, other in links.items():
        # Konfiguracja przeglądarki
        driver.get(link)
        # Maksymalizacja okna przeglądarki
        driver.maximize_window()
        
        time.sleep(2)
        
        # Pobranie nazw urządzeń
        try:
            name = driver.find_element(By.XPATH, "//span[contains(@class, 'product-intro__title-text')]")
            name_text = name.text
            device_names.append(name_text)  
        except:
            device_names.append(None)  
        
        # Pobranie cen
        try:
            price_whole_part = driver.find_element(By.XPATH, "//span[contains(@class, 'price-template__large--total')]")
            price_whole_part_text = price_whole_part.text

            try:
                price_cents_part = driver.find_element(By.XPATH, "//span[contains(@class, 'price-template__large--decimal')]")
                price_cents_part_text = price_cents_part.text
            except:
                price_cents_part_text = '00'

            price_text = f"{price_whole_part_text},{price_cents_part_text}"
            prices.append(price_text) 
        except:
            prices.append(None) 

        # Pobranie średniej oceny i liczby opinii
        try:
                opinion = driver.find_element(By.XPATH, "//span[contains(@class, 'client-rate__rate')]")
                opinion_text = opinion.text
                opinions.append(opinion_text)
                opinion_count = driver.find_element(By.XPATH, "//span[contains(@class, 'client-rate__opinions')]")
                opinion_count_text = opinion_count.text
                opinions_count.append(opinion_count_text)
        except:
                opinions.append(None) 
                opinions_count.append('0')

        # Sprawdzenie dostępności produktu
        try:
            availability_product = driver.find_element(By.XPATH, "//span[contains(text(), ' Produkt tymczasowo niedostępny ')] | //span[contains(text(), ' Produkt nie jest już dostępny w naszym sklepie ')]")
            availability.append(0)
        except:
            availability.append(1)

        # Dodanie typu urządzenia i sklepu
        device_types.append(other['typ'])  
        stores.append(other['sklep'])  
            
    # Zamknięcie sesji
    driver.quit()

       # Utworzenie ramki danych
    df = pd.DataFrame({
        'Nazwa urzadzenia': device_names,
        'Cena (zł)': prices,
        'Ocena': opinions, 
        'Liczba ocen': opinions_count,
        'Czy dostepny': availability,
        'Typ urzadzenia': device_types,
        'Sklep': stores
    })
    
    # Operacje na danych - zmiana typu, usunięcie niepotrzebnych słów i znaków
    df['Data'] = date
    df['Cena (zł)'] = df['Cena (zł)'].str.replace(' ', '').str.replace('zł', '')
    df['Liczba ocen'] = df['Liczba ocen'].str.extract('(\d+)')
    df = df.replace(',', '.', regex=True)
    print(df)

    # Zapis do pliku csv
    csv = 'monitoring_cen_oleole.csv'

    if os.path.exists(csv):
        df.to_csv(csv, mode='a', index=False, header=False)
    else:
        df.to_csv(csv, mode='w', index=False, header=True)   
except:
    # Dodanie wiersza do pliku csv z informacją o błędzie i wskazanie produktu gdzie błąd nastąpił
    row = ["OleOle!", f"Błąd przy wykonywaniu dla produktu: {device_names[-1]}", date]
    report.loc[len(report)] = row
    csv = 'raport.csv'
    if os.path.exists(csv):
        report.to_csv(csv, mode='a', index=False, header=False)
    else:
        report.to_csv(csv, mode='w', index=False, header=True)



# RTV Euro AGD
try:
    # Konfiguracja przeglądarki
    options = Options()
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    links = {
        'https://www.euro.com.pl/sluchawki/samsung-galaxy-buds3-sm-r530nza-douszne-bluetooth-srebrny.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/sluchawki/apple-airpods-3-generacji-z-etui-ladujacym-lightning-mpny3zma.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/sluchawki/apple-airpods-pro-2-generacji-z-etui-magsafe-usb-c-dokanalowe-bluetooth-5-3.bhtml': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/sluchawki/apple-airpods-z-etui-ladujacym.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/sluchawki/jbl-sluch-nauszne-bt-jbl-tune-770nc-czarne.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/sluchawki/jbl-sluchawki-bt-nauszne-tune-520-bt-czarne.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/sluchawki/technics-sluchawki-nauszne-bt-eah-a800e-k-czarne.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/sluchawki/soundcore-liberty-4-nc-dokanalowe-bluetooth-5-3-czarny.bhtml': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/sluchawki/sony-wh-ch720-nauszne-czarny.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/sluchawki/apple-airpods-4-douszne-bluetooth-5-3-bialy.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/sluchawki/apple-airpods-4-z-aktywna-redukcja-halasu-douszne-bluetooth-5-3-bialy.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/ipad-i-tablety-multimedialne/samsung-tablet-galaxy-tab-a9-8-128gb-wifi-gray.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/ipad-i-tablety-multimedialne/huawei-tablet-matepad-s-11-5-8-256gb-wifi-g-key.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/ipad-i-tablety-multimedialne/apple-ipad-mini-2021-wi-fi-64gb-gwiezdna-szarosc.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/ipad-i-tablety-multimedialne/lenovo-tablet-p11-11-5-6gb-128gb-wifi-grey.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/ipad-i-tablety-multimedialne/lenovo-yoga-tab-13-yt-k606f-13-8-128gb-wi-fi.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/ipad-i-tablety-multimedialne/xiaomi-tablet-redmi-pad-pro-8-256ggb-graph-gray.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/ipad-i-tablety-multimedialne/samsung-tablet-galaxy-tab-a9-8-128gb-wifi-gray_1.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/monitory-led-i-lcd/lg-monitor-27un880p-b.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/monitory-led-i-lcd/iiyama-monitor-gb2470hsu-b5.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/monitory-led-i-lcd/iiyama-monitor-gb2770qsu-b5.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/monitory-led-i-lcd/samsung-monitor-s27ag300nr.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/monitory-led-i-lcd/asus-monitor-vy279hge.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/monitory-led-i-lcd/xiaomi-monitor-a27i.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'},
        'https://www.euro.com.pl/monitory-led-i-lcd/lg-monitor-27gs85q-b.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'}
    }


    # Inicjacja pustych list do przechowywania danych
    device_names = []
    device_types = []
    stores = []
    prices = []
    opinions = []
    opinions_count = []  
    availability = [] 

    for link, other in links.items():
        # Uruchomienie przeglądarki
        driver.get(link)
        # Maksymalizacja okna przeglądarki
        driver.maximize_window()    
        time.sleep(2)
        
        # Pobranie nazw urządzeń
        try:
            name = driver.find_element(By.XPATH, "//span[contains(@class, 'product-intro__title-text')]")
            name_text = name.text
            device_names.append(name_text) 
        except:
            device_names.append(None)
        
        # Pobranie cen
        try:
            price_whole_part = driver.find_element(By.XPATH, "//span[contains(@class, 'price-template__large--total')]")
            price_whole_part_text = price_whole_part.text

            try:
                price_cents_part = driver.find_element(By.XPATH, "//span[contains(@class, 'price-template__large--decimal')]")
                price_cents_part_text = price_cents_part.text
            except:
                price_cents_part_text = '00'

            try:
                price_text = f"{price_whole_part_text},{price_cents_part_text}"
            except:
                price_text = price_whole_part_text

            prices.append(price_text)
        except:
            prices.append(None)

        # Pobranie średniej oceny i liczbę opinii
        try:
            # Przewijanie strony
            scroll_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script(f"window.scrollTo(0, {scroll_height / 1.7});")
            time.sleep(3)            
            opinion = driver.find_element(By.XPATH, "//span[contains(text(), ' Napisz pierwszą opinię ')]")
            opinions.append(None) 
            opinions_count.append('0')
        except:
            try:
                    driver.find_element(By.XPATH, "//span[contains(@class, 'opinions-header__title')]")
                    opinion = driver.find_element(By.XPATH, "//span[contains(@class, 'client-rate__rate')]")
                    opinion_text = opinion.text
                    opinions.append(opinion_text)
                    opinion_count = driver.find_element(By.XPATH, "//span[contains(@class, 'client-rate__opinions')]")
                    opinion_count_text = opinion_count.text
                    opinions_count.append(opinion_count_text)
            except:
                    opinions.append(None)
                    opinions_count.append('0')
            
        # Sprawdzenie dostępności produktu
        try:
            availability_product = driver.find_element(By.XPATH, "//span[contains(text(), ' Produkt tymczasowo niedostępny ')] | //span[contains(text(), ' Ten produkt dostępny jest tylko w wybranych sklepach ')] | //span[contains(text(), ' Produkt nie jest już dostępny w naszym sklepie ')]")
            availability.append(0)
        except:
            availability.append(1)

        # Dodanie typu urządzenia i sklepu
        device_types.append(other['typ'])
        stores.append(other['sklep']) 
            
    # Zamknięcie sesji
    driver.quit()

       # Utworzenie ramki danych
    df = pd.DataFrame({
        'Nazwa urzadzenia': device_names,
        'Cena (zł)': prices,
        'Ocena': opinions,
        'Liczba ocen': opinions_count,
        'Czy dostepny': availability,
        'Typ urzadzenia': device_types,
        'Sklep': stores
    })

    # Operacje na danych - zmiana typu, usunięcie niepotrzebnych słów i znaków
    df['Data'] = date
    df['Cena (zł)'] = df['Cena (zł)'].str.replace(' ', '').str.replace('zł', '')
    df['Liczba ocen'] = df['Liczba ocen'].str.extract('(\d+)')
    df = df.replace(',', '.', regex=True)
    print(df)

    # Zapis do pliku csv
    csv = 'monitoring_cen_rtv.csv'

    if os.path.exists(csv):
        df.to_csv(csv, mode='a', index=False, header=False)
    else:
        df.to_csv(csv, mode='w', index=False, header=True) 
except:
    # Dodanie wiersza do pliku csv z informacją o błędzie i wskazanie produktu gdzie błąd nastąpił
    row = ["RTV Euro AGD", f"Błąd przy wykonywaniu dla produktu: {device_names[-1]}", date]
    report.loc[len(report)] = row
    csv = 'raport.csv'
    if os.path.exists(csv):
        report.to_csv(csv, mode='a', index=False, header=False)
    else:
        report.to_csv(csv, mode='w', index=False, header=True)




# x-kom
try:
    #Wprowadzenie wybranych nagłówków user-agent
    user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2820.59 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36'
    ]



    links = {
        'https://www.x-kom.pl/p/1264766-sluchawki-bezprzewodowe-samsung-galaxy-buds3-srebrne.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1070895-sluchawki-true-wireless-apple-airpods-3-generacji-lightning.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1180227-sluchawki-true-wireless-apple-airpods-pro-2-generacji-usb-c.html': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/490938-sluchawki-true-wireless-apple-airpods-2-generacji.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1163204-sluchawki-bezprzewodowe-jbl-tune-770nc-czarne.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1205701-sluchawki-bezprzewodowe-jbl-tune-520bt-czarny.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/724758-sluchawki-bezprzewodowe-technics-eah-a800-czarne.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1177895-sluchawki-bezprzewodowe-soundcore-liberty-4-nc-czarne.html': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1119463-sluchawki-bezprzewodowe-sony-wh-ch720n-czarne.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1278719-sluchawki-true-wireless-apple-airpods-4-generacji.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1278730-sluchawki-true-wireless-apple-airpods-4-generacji-z-aktywna-redukcja-halasu.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1195773-tablet-8-samsung-galaxy-tab-a9-x110-wifi-8-128gb-szary.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1257581-tablety-11-huawei-matepad-115-s-wifi-8-256gb-space-greym-pencil-klawiatura.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/681239-tablet-10-apple-ipad-102-9gen-64gb-wi-fi-space-gray.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1126296-tablet-11-lenovo-tab-p11-6gb-128gb-android-12l-wifi-gen-2.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1226967-tablet-13-lenovo-yoga-tab-13-8gb-128gb-android-11-wifi.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1257753-tablet-12-xiaomi-redmi-pad-pro-8gb-256gb-graphite-gray.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1195785-tablety-11-samsung-galaxy-tab-a9-x210-wifi-8-128gb-szary.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1137559-monitor-led-27-265-284-lg-ultrafine-27un880p-b-ergo-4k.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1142195-monitor-led-24-235-264-iiyama-g-master-gb2470hsu-b5-red-eagle.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1142197-monitor-led-27-265-284-iiyama-g-master-gb2770qsu-b5-red-eagle.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1125894-monitor-led-27-265-284-samsung-odyssey-s27ag300nrx.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1144811-monitor-led-27-265-284-asus-vy279hge.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1208060-monitor-led-27-265-284-xiaomi-a27i.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
        'https://www.x-kom.pl/p/1276734-monitor-led-27-265-284-lg-ultragear-27gs85q-b.html': {'typ': 'Monitor', 'sklep': 'x-kom'}
    }


    # Inicjacja pustych list do przechowywania danych
    device_names = []
    device_types = []
    stores = []
    prices = []
    opinions = []
    opinions_count = []  
    availability = [] 

    for link, other in links.items():
        # Losowanie user-agent
        user_agent = random.choice(user_agents)
        # Konfiguracja przeglądarki
        options = Options()
        options.add_argument(f'user-agent={user_agent}')
        service = Service(executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)

        # Uruchomienie przeglądarki
        driver.get(link)
        time.sleep(3)

        # Zarządzanie oknami przeglądarki
        main_window = driver.current_window_handle
        windows = driver.window_handles
        if len(windows) > 1:
            new_window = [window for window in windows if window != main_window][0]
            driver.switch_to.window(new_window)
        time.sleep(2)
        
        # Pobranie nazw urządzeń
        try:
            try:
                name = driver.find_element(By.XPATH, "//h1[contains(@class, 'parts__Title-sc-2836f2a2-4 ekAhAJ')]")
            except:
                try:
                    name = driver.find_element(By.XPATH, "//h1[contains(@class, 'parts__Title-sc-2836f2a2-4 jTwNjC')]")
                except: 
                    device_names.append(None)
            name_text = name.text
            device_names.append(name_text)
        except:
            device_names.append(None)
        
        
        # Pobranie cen
        try:
            try:
                time.sleep(5)
                price = driver.find_element(By.XPATH, "//span[contains(@class, 'sc-jnqLxu cjLwnY parts__Price-sc-53da58c9-2 hbVORa')]")
                price_text = price.text
                prices.append(price_text)
            except:
                time.sleep(5)
                price = driver.find_element(By.XPATH, "//span[contains(@class, 'sc-emqRaN cfSJSM parts__Price-sc-53da58c9-2 hbVORa')]")
                price_text = price.text
                prices.append(price_text)
        except:
                prices.append(None)

        # Pobranie średniej oceny i liczby opinii
        try:
                opinion = driver.find_element(By.XPATH, "//span[contains(@class, 'parts__Rating-sc-8400f50a-1 kXsCwx')]")
                opinion_text = opinion.text
                opinions.append(opinion_text)
                opinion_count = driver.find_element(By.XPATH, "//div[contains(@class, 'parts__RatingReviews-sc-8400f50a-5 gnTmfI')]")
                opinion_count_text = opinion_count.text
                opinions_count.append(opinion_count_text)
        except:
                opinions.append(None)
                opinions_count.append('0')

        # Sprawdzenie dostępności produktu
        try:
            try:
                availability_product = driver.find_element(By.XPATH, "//span[contains(text(), 'Czasowo niedostępny')] | //span[contains(text(), 'Produkt wycofany')] | //span[contains(text(), 'Chwilowo niedostępny')]")
                availability.append(0)
            except:
                try:
                    availability_product = driver.find_element(By.XPATH, "//span[contains(text(), 'Wycofany')]")
                    availability.append(0)
                except:
                    availability.append(1)
            
        except:
            pass

        # Dodanie typu urządzenia i sklepu
        device_types.append(other['typ'])
        stores.append(other['sklep'])

    # Zamknięcie sesji
    driver.quit()

       # Utworzenie ramki danych
    df = pd.DataFrame({
        'Nazwa urzadzenia': device_names,
        'Cena (zł)': prices,
        'Ocena': opinions,
        'Liczba ocen': opinions_count,
        'Czy dostepny': availability,
        'Typ urzadzenia': device_types,
        'Sklep': stores
    })

    # Operacje na danych - zmiana typu, usunięcie niepotrzebnych słów i znaków
    df['Data'] = date
    df['Cena (zł)'] = df['Cena (zł)'].str.replace(' ', '').str.replace('zł', '')
    df['Liczba ocen'] = df['Liczba ocen'].str.extract('(\d+)')
    df = df.replace(',', '.', regex=True)
    print(df)

    # Zapis do pliku csv
    csv = 'monitoring_cen_xkom.csv'

    if os.path.exists(csv):
        df.to_csv(csv, mode='a', index=False, header=False)
    else:
        df.to_csv(csv, mode='w', index=False, header=True) 
except:
    # Dodanie wiersza do pliku csv z informacją o błędzie i wskazanie produktu gdzie błąd nastąpił
    row = ["x-kom", f"Błąd przy wykonywaniu dla produktu: {device_names[-1]}", date]
    report.loc[len(report)] = row
    csv = 'raport.csv'
    if os.path.exists(csv):
        report.to_csv(csv, mode='a', index=False, header=False)
    else:
        report.to_csv(csv, mode='w', index=False, header=True)