from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  
from datetime import datetime
import os
import pandas as pd
import random
import re


date = datetime.today().strftime('%Y-%m-%d') 


# #Komputronik
# try:
#     # Konfiguracja przeglądarki
#     options = Options()
#     service = Service(executable_path="chromedriver.exe")
#     driver = webdriver.Chrome(service=service, options=options)

#     # Załadowanie pliku z ciasteczkami
#     import json
#     with open("cookies.json", "r") as file:
#         cookies = json.load(file)

#     links = {
#         'https://www.komputronik.pl/product/919834/sluchawki-samsung-galaxy-buds3-srebrne.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/784783/apple-airpods-3-gen-lightning-charging-case-.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/861792/sluchawki-apple-airpods-pro-2-gen-z-magsafe-usb-c.html': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/616063/apple-airpods-2-gen.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/836971/jbl-tune-770-bt-nc-czarny.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/818988/jbl-tune-520-bt-czarne.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/748451/technics-eah-a800e-k-czarny.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/876615/sluchawki-soundcore-liberty-4-nc-czarny.html': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/814360/sony-whch720nb-czarny.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/930296/sluchawki-apple-airpods-4-gen.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/930297/sluchawki-apple-airpods-4-gen-anc.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/878621/samsung-galaxy-tab-a9-8-7-128gb-szary-x110-.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/912943/tablet-huawei-matepad-11-5-s-wifi-8-256gb-szary-klawiatura-rysik.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/734199/apple-ipad-10-2-a13-wi-fi-64gb-gwiezdna-szarosc-9-gen-.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/819895/lenovo-tab-p11-2nd-gen-tb350fu-6-128gb-wifi-zabf0355pl-szary.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/898283/tablet-lenovo-yoga-tab-13-yt-k606f-8-128gb-wifi-za8e0027pl-czarny.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/916337/tablet-xiaomi-redmi-pad-pro-8-256gb-wifi-graphite-gray.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/878624/samsung-galaxy-tab-a9-11-0-128gb-szary-x210-.html': {'typ': 'Tablet', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/828020/lg-27un880p-b.html': {'typ': 'Monitor', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/816195/iiyama-red-eagle-gb2470hsu-b5-ips-165hz-flc.html': {'typ': 'Monitor', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/816196/iiyama-red-eagle-gb2770qsu-b5-ips-165hz-flc.html': {'typ': 'Monitor', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/802946/samsung-s27ag300nrx-27-va-full-hd-1ms-144hz-pivot.html': {'typ': 'Monitor', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/831494/asus-vy279hge-27-full-hd-ips-144hz-1ms-mprt-.html': {'typ': 'Monitor', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/901102/monitor-xiaomi-monitor-a27i.html': {'typ': 'Monitor', 'sklep': 'Komputronik'},
#         'https://www.komputronik.pl/product/927362/monitor-lg-27gs85q-b.html': {'typ': 'Monitor', 'sklep': 'Komputronik'}
#     }

#     # Inicjacja pustych list do przechowywania danych
#     ratings = []
#     device_names = []
#     stores = []
#     opinions_date = []
#     names = []
#     opinions_list = []

#     for link, other in links.items():
#         # Uruchomienie przeglądarki
#         driver.get(link)
#         # Maksymalizacja okna
#         driver.maximize_window()  
#         time.sleep(3)

#         # Dodanie pobranych ciasteczek
#         for cookie in cookies:
#             driver.add_cookie(cookie)

#         # Odświeżenie strony
#         driver.refresh() 
#         time.sleep(3)
        
#         # Pobranie nazwy urządzenia
#         try:
#             name = driver.find_element(By.XPATH, "//h1[@data-name='productName' and contains(@class, 'line-clamp-2') and contains(@class, 'font-headline') and contains(@class, 'font-bold')]")
#             name_text = name.text
#             device_names.append(name_text) 
#         except:
#             device_names.append(None) 
            
        
#         time.sleep(2)
#         # Przewijanie strony
#         driver.execute_script("window.scrollBy(0, 6450);")
#         time.sleep(3)

#         while True:
#                     try:
#                         # Znalezienie elementu
#                         show_more = driver.find_element(By.XPATH, "//u[contains(@class, 'text-base font-semibold') and contains(text(), 'Pokaż kolejne')] | //u[contains(@class, 'text-base font-semibold') and contains(text(), 'Pokaż kolejną')]")
#                         # Zlokalizowanie czy element jest widoczny w oknie przeglądarki
#                         window_view = driver.execute_script(
#                             "var rect = arguments[0].getBoundingClientRect();"
#                             "return rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight);",
#                             show_more
#                         )
                        
#                         # Operacja kliknięcia jeśli element jest widoczny
#                         if window_view:
#                             time.sleep(2)
#                             # Kliknięcie w element
#                             show_more.click()

#                     except:
#                         break 
#                     # Jeśli strona przewinie się za bardzo do dołu to wraca na górę
#                     current_scroll = driver.execute_script("return window.scrollY + window.innerHeight;")
#                     max_scroll = driver.execute_script("return document.documentElement.scrollHeight;")
#                     if current_scroll >= max_scroll:
#                         driver.execute_script("window.scrollBy(0, -2000);")
#                     # Scrollowanie w dół
#                     driver.execute_script("window.scrollBy(0, 300);")
#                     time.sleep(1)

#         time.sleep(3)

#         # Pobieranie treści opinii i ich ocen
#         opinion = driver.find_elements(By.XPATH, "//div[contains(@class, 'space-y-4') and contains(@class, 'p-6')]//div[contains(@class, 'wrap-text')]")
#         opinion_text = [review.text for review in opinion]
#         raitings = driver.find_elements(By.XPATH, "//div[contains(@class, 'space-y-4 p-6')]//div[contains(@class, 'star-rating inline-block text-2xl leading-none')]")
        
#         for raiting in raitings:
#             style = raiting.get_attribute('style')
            
#             mask_match = re.search(r'--mask: (\d+)px', style)
#             if mask_match:
#                 mask_value = float(mask_match.group(1))
#                 # Obsługa odczytu oceny z liczby pokolorowanych gwiazdek
#                 if mask_value == 24:
#                     ratings.append(1)
#                 elif mask_value == 84: 
#                     ratings.append(2.5)
#                 elif mask_value == 144: 
#                     ratings.append(4)
#                 elif mask_value == 156:
#                     ratings.append(4.5)
#                 elif mask_value == 180:
#                     ratings.append(5)
#                 else:
#                     ratings.append(None)
#             else:
#                 ratings.append(None)

#         for i in range(len(opinion_text)):
#             names.append(device_names[-1])
#             opinions_list.append(opinion_text[i])
#             stores.append(other['sklep']) 
#             opinions_date.append(None)

#     # Zamknięcie sesji
#     driver.quit()

#        # Utworzenie ramki danych
#     df = pd.DataFrame({
#         'Nazwa urzadzenia': names,
#         'Ocena': ratings,
#         'Opinia': opinions_list,
#         'Sklep': stores,
#         'Data opinii': opinions_date,
#         'Data pobrania': date
        
#     })
#     df

#     # Zapis do pliku csv
#     csv = 'monitoring_opinie_produktow.csv'

#     if os.path.exists(csv):
#         df.to_csv(csv, mode='a', index=False, header=False)
#     else:
#         df.to_csv(csv, mode='w', index=False, header=True)

# except:
#     pass





# Media Expert - opinie
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

    # Inicjacja pustych list do przechowywania danych
    opinions_date_list = []
    device_names = []
    stores = []
    raiting_list = []
    opinions_list = [] 


    for link, other in links.items():
        
        # Uruchomienie przegladarki
        driver.get(link)
        # Maksymalizacja okna
        driver.maximize_window()    
        time.sleep(5)
        
        # Pobranie nazw produktów
        try:
            name = driver.find_element(By.XPATH, "//h1[contains(@class, 'name is-title')]")
            name_text = name.text       
        except:
            pass

        time.sleep(4)

        # Osługa wyskakującego komunikatu
        try:
            close = driver.find_element(By.XPATH, "//span[contains(@class, 'is-text close is-regular')] | //button[contains(@class, 'dialog-close-btn')]")
            time.sleep(1)
            driver.execute_script("arguments[0].click();", close)
            time.sleep(2)
        except:
            pass
        
        # Obsługa wyskakującego komunikatu
        try:
            time.sleep(2)
            accept = driver.find_element(By.XPATH, "//button[contains(@id, 'onetrust-accept-btn-handler')]")
            accept.click()
        except:
            pass
        

        # Przewijanie strony
        try:
            scroll_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script(f"window.scrollTo(0, {scroll_height / 2});")
            time.sleep(3)
            scroll_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script(f"window.scrollTo(0, {scroll_height / 2});")
            time.sleep(5)
        except: 
            pass
        

        # try:
        #     time.sleep(2)
        #     close = driver.find_element(By.XPATH, "//span[contains(@class, 'is-text close is-regular')]")
        #     driver.execute_script(f"window.scrollTo(0, 150);")
        #     time.sleep(1)
        #     close.click()
        #     time.sleep(1)
        # except:
        #     pass

        # Sprawdzenie czy sa opinie
        try:
            opinion = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(text(), '/5') and number(substring-before(text(), '/5'))]"))
            )
            
        except:
            continue
        

        # try:
        #     ilosc = driver.find_element(By.XPATH, "//span[contains(@class, 'from')]")
        #     ilosc_text = ilosc.text
        #     ilosc_text = ''.join([char for char in ilosc_text if char.isdigit()])
        #     ilosc_text = int(ilosc_text) if ilosc_text else 1

        #     print(ilosc_text)
        # except:
        #     ilosc_text = 1
        #     print("zle")

            
        try:
            # Gdy jest kilka stron opinii
            while driver.find_element(By.XPATH, "//div[contains(@class, 'reviews-pagination pagination is-desktop')]//i[contains(@class, 'icon icon-arrow-1')][2][not(contains(@class, 'disabled'))]"):
                try:
                    # Przechodzenie po stronach opinii                    
                    next_page = driver.find_element(By.XPATH, "//div[contains(@class, 'reviews-pagination pagination is-desktop')]//i[contains(@class, 'icon icon-arrow-1')][2][not(contains(@class, 'disabled'))]")
                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_page)
                    time.sleep(1)
                    window_view = driver.execute_script(
                        "var rect = arguments[0].getBoundingClientRect();"
                        "return rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight);",
                        next_page
                    )
                    
                    # Pobranie treści opinii i ocen
                    try:
                        raitings = driver.find_elements(By.XPATH, "//div[contains(@class, 'rating-box')]//div[contains(@class, 'rating')]")
                        opinions = driver.find_elements(By.XPATH, "//div[contains(@class, 'review-content')]")
                        opinions_date = driver.find_elements(By.XPATH, "//span[contains(@class, 'date is-regular')]")
                        raitings_text = [raiting.text for raiting in raitings]
                        opinions_text = [opinion.text for opinion in opinions]
                        raitings_text = [text.split('/')[0].strip() for text in raitings_text if '/' in text]
                        opinions_date_text = [opinion_date.text for opinion_date in opinions_date] 

                        for i in range(len(raitings_text)):
                            device_names.append(name_text)
                            raiting_list.append(raitings_text[i]) 
                            opinions_list.append(opinions_text[i])
                            stores.append(other['sklep']) 
                            opinions_date_list.append(opinions_date_text[i])
                        
                    except:
                        pass
                    # Przejście do następnej strony poprzez kliknięcie
                    if window_view:
                        time.sleep(2)
                        next_page.click()
                    time.sleep(3)

                    
                except:
                    break
                
        # gdy jest jedna strona
        except:
            raitings = driver.find_elements(By.XPATH, "//div[contains(@class, 'rating-box')]//div[contains(@class, 'rating')]")
            opinion = driver.find_elements(By.XPATH, "//div[contains(@class, 'review-content')]")
            opinions_date = driver.find_elements(By.XPATH, "//span[contains(@class, 'date is-regular')]")
            raitings_text = [raiting.text for raiting in raitings]
            opinions_text = [opinion.text for opinion in opinions]
            raitings_text = [text.split('/')[0].strip() for text in raitings_text if '/' in text]
            opinions_date_text = [opinion_date.text for opinion_date in opinions_date] 

            for i in range(len(raitings_text)):
                device_names.append(name_text)
                raiting_list.append(raitings_text[i])
                opinions_list.append(opinions_text[i])
                stores.append(other['sklep']) 
                opinions_date_list.append(opinions_date_text[i])

    # Zakmnięcie sesji
    driver.quit()

    # Utworzenie ramki danych
    df = pd.DataFrame({
        'Nazwa urzadzenia': device_names,
        'Ocena': raiting_list,
        'Treść': opinions_list,
        'Sklep': stores,
        'Data opinii': opinions_date_list,
        'Data pobrania': date
    })

    df

    # Utworzenie pliku csv lub dodanie danych do istniejącego
    csv = 'monitoring_opinie_produktow.csv'

    if os.path.exists(csv):
        df.to_csv(csv, mode='a', index=False, header=False)
    else:
        df.to_csv(csv, mode='w', index=False, header=True)

except:
    pass








# # OleOle!
# try:
#     # Konfiguracja przeglądarki
#     options = Options()
#     service = Service(executable_path="chromedriver.exe")
#     driver = webdriver.Chrome(service=service, options=options)

#     links = {
#         'https://www.oleole.pl/sluchawki/samsung-galaxy-buds3-sm-r530nza-douszne-bluetooth-srebrny.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/sluchawki/apple-airpods-3-generacji-z-etui-ladujacym-lightning-mpny3zma.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/sluchawki/apple-airpods-pro-2-generacji-z-etui-magsafe-usb-c-dokanalowe-bluetooth-5-3.bhtml': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/sluchawki/apple-airpods-z-etui-ladujacym.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/sluchawki/jbl-sluch-nauszne-bt-jbl-tune-770nc-czarne.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/sluchawki/jbl-sluchawki-bt-nauszne-tune-520-bt-czarne.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/sluchawki/technics-sluchawki-nauszne-bt-eah-a800e-k-czarne.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/sluchawki/soundcore-liberty-4-nc-dokanalowe-bluetooth-5-3-czarny.bhtml': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/sluchawki/sony-wh-ch720-nauszne-czarny.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/sluchawki/apple-airpods-4-douszne-bluetooth-5-3-bialy.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/sluchawki/apple-airpods-4-z-aktywna-redukcja-halasu-douszne-bluetooth-5-3-bialy.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/ipad-i-tablety-multimedialne/samsung-tablet-galaxy-tab-a9-8-128gb-wifi-gray.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/ipad-i-tablety-multimedialne/huawei-tablet-matepad-s-11-5-8-256gb-klaw-pen3.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/ipad-i-tablety-multimedialne/apple-ipad-mini-2021-wi-fi-64gb-gwiezdna-szarosc.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/ipad-i-tablety-multimedialne/lenovo-tablet-p11-11-5-6gb-128gb-wifi-grey.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/ipad-i-tablety-multimedialne/lenovo-yoga-tab-13-yt-k606f-13-8-128gb-wi-fi.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/ipad-i-tablety-multimedialne/xiaomi-tablet-redmi-pad-pro-8-256ggb-graph-gray.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/ipad-i-tablety-multimedialne/samsung-tablet-galaxy-tab-a9-8-128gb-wifi-gray_1.bhtml': {'typ': 'Tablet', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/monitory-led-i-lcd/lg-monitor-27un880p-b.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/monitory-led-i-lcd/iiyama-monitor-gb2470hsu-b5.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/monitory-led-i-lcd/iiyama-monitor-gb2770qsu-b5.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/monitory-led-i-lcd/samsung-monitor-s27ag300nr.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/monitory-led-i-lcd/asus-monitor-vy279hge.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/monitory-led-i-lcd/xiaomi-monitor-a27i.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'},
#         'https://www.oleole.pl/monitory-led-i-lcd/lg-monitor-27gs85q-b.bhtml': {'typ': 'Monitor', 'sklep': 'OleOle!'}
#     }

#     # Inicjacja pustych list do przechowywania danych
#     opinions_date_list = []
#     device_names = []
#     stores = []
#     raiting_list = []
#     opinions_list = []

#     for link, other in links.items():
#         # Uruchomienie przeglądarki
#         driver.get(link)
#         # Maksymalizacja okna
#         driver.maximize_window()
        
#         # Obsługa komunikatów
#         time.sleep(3)
#         try:
#             accept = driver.find_element(By.XPATH, "//button[contains(@id, 'onetrust-accept-btn-handler')]")
#             accept.click()
#         except:
#             pass

#         # Pobranie nazw
#         try:
#             name = driver.find_element(By.XPATH, "//span[contains(@class, 'product-intro__title-text')]")
#             name_text = name.text
#         except:
#             device_names.append(None)  

#         # Sprawdzenie czy są opinie jeśli nie to następny produkt
#         try:
#                 opinion = driver.find_element(By.XPATH, "//div[contains(@class, 'product-information product-information--bigger')]//span[contains(@class, 'client-rate__rate')]")

#         except:
#                 continue
        
#         # Przewijanie strony
#         driver.execute_script("window.scrollBy(0, 900);")
#         time.sleep(5)

#         # Przejście do opinii
#         try:
#             time.sleep(5)
#             opinions_button = driver.find_element(By.XPATH, "//p[contains(@class, 'desktop-navigation__item desktop-navigation__item--opinions')]") 
#             driver.execute_script("arguments[0].click();", opinions_button)
#         except:
#             pass

        
#         try:
#             time.sleep(5)
#             # Wyświetlenie wszystkich opinii
#             opinions_all = driver.find_element(By.XPATH, "//div[contains(@class, 'opinions__cta ng-star-inserted')]//button") 
#             driver.execute_script("arguments[0].click();", opinions_all)
#             while True:
#                 try:
#                     time.sleep(8)
#                     scroll_element = driver.find_element(By.XPATH, "//eui-layer")
#                     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_element)
#                     time.sleep(4)
#                     # Wyświtelenie więcej opinii
#                     show_more = driver.find_element(By.XPATH, "//a[contains(@class, 'list-load-more__button cta ng-star-inserted')]")
#                     driver.execute_script("arguments[0].click();", show_more)
#                     time.sleep(2)
                
#                 except:
#                     break
            
#             # Pobranie danych
#             try:
#                 time.sleep(5)
#                 raitings = driver.find_elements(By.XPATH, "//div[contains(@class, 'opinions-layer ng-star-inserted')]//div[contains(@class, 'opinions-layer__opinions-boxes')]//span[contains(@class, 'client-rate__rate')]")
#                 opinions = driver.find_elements(By.XPATH, "//div[contains(@class, 'opinions-layer ng-star-inserted')]//div[contains(@class, 'opinions-layer__opinions-boxes')]//p[contains(@class, 'opinion-box__text')]")
#                 opinions_date = driver.find_elements(By.XPATH, "//span[contains(@class, 'opinion-box__date')]")
#                 time.sleep(5)
#                 raitings_text = [raiting.text for raiting in raitings]
#                 opinions_text = [opinion.text for opinion in opinions]
#                 opinions_date_text = [opinion_date.text for opinion_date in opinions_date] 
#                 for i in range(len(raitings_text)):
#                     device_names.append(name_text) 
#                     raiting_list.append(raitings_text[i])
#                     opinions_list.append(opinions_text[i])
#                     stores.append(other['sklep']) 
#                     opinions_date_list.append(opinions_date_text[i])
#             except:
#                 pass
                
#         # Pobranie danych gdy jest ich mało i nie ma przycisku więcej      
#         except:
#                 pass

        
#                 try:
#                     time.sleep(5)
#                     raitings = driver.find_elements(By.XPATH, "//div[contains(@class, 'opinion-box__content')]//span[contains(@class, 'client-rate__rate')]")
#                     opinions = driver.find_elements(By.XPATH, "//div[contains(@class, 'opinion-box__content')]//p[contains(@class, 'opinion-box__text opinion-box__text--truncated')]")
#                     opinions_date = driver.find_elements(By.XPATH, "//span[contains(@class, 'opinion-box__date')]")
#                     time.sleep(5)
#                     raitings_text = [raiting.text for raiting in raitings]
#                     opinions_text = [opinion.text for opinion in opinions]
#                     opinions_date_text = [opinion_date.text for opinion_date in opinions_date] 
#                     for i in range(len(raitings_text)):
#                         device_names.append(name_text)
#                         raiting_list.append(raitings_text[i])  
#                         opinions_list.append(opinions_text[i])
#                         stores.append(other['sklep']) 
#                         opinions_date_list.append(opinions_date_text[i])
#                 except:
#                     pass

        
#     # Zamknięcie sesji
#     driver.quit()
    
#     # Utworzenie ramki danych
#     df = pd.DataFrame({
#         'Nazwa urzadzenia': device_names,
#         'Ocena': raiting_list,
#         'Treść': opinions_list,
#         'Sklep': stores,
#         'Data opinii': opinions_date_list,
#         'Data pobrania': date
#     })

#     df

#     # Zapis do pliku csv
#     csv = 'monitoring_opinie_produktow.csv'

#     if os.path.exists(csv):
#         df.to_csv(csv, mode='a', index=False, header=False)
#     else:
#         df.to_csv(csv, mode='w', index=False, header=True)
# except:
#     pass







# # RTV Euro AGD
# try:
#     # Konfiguracja przeglądarki
#     options = Options()
#     service = Service(executable_path="chromedriver.exe")
#     driver = webdriver.Chrome(service=service, options=options)

#     links = {
#         'https://www.euro.com.pl/sluchawki/samsung-galaxy-buds3-sm-r530nza-douszne-bluetooth-srebrny.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/sluchawki/apple-airpods-3-generacji-z-etui-ladujacym-lightning-mpny3zma.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/sluchawki/apple-airpods-pro-2-generacji-z-etui-magsafe-usb-c-dokanalowe-bluetooth-5-3.bhtml': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/sluchawki/apple-airpods-z-etui-ladujacym.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/sluchawki/jbl-sluch-nauszne-bt-jbl-tune-770nc-czarne.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/sluchawki/jbl-sluchawki-bt-nauszne-tune-520-bt-czarne.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/sluchawki/technics-sluchawki-nauszne-bt-eah-a800e-k-czarne.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/sluchawki/soundcore-liberty-4-nc-dokanalowe-bluetooth-5-3-czarny.bhtml': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/sluchawki/sony-wh-ch720-nauszne-czarny.bhtml': {'typ': 'Słuchawki (nauszne)', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/sluchawki/apple-airpods-4-douszne-bluetooth-5-3-bialy.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/sluchawki/apple-airpods-4-z-aktywna-redukcja-halasu-douszne-bluetooth-5-3-bialy.bhtml': {'typ': 'Słuchawki (douszne)', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/ipad-i-tablety-multimedialne/samsung-tablet-galaxy-tab-a9-8-128gb-wifi-gray.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/ipad-i-tablety-multimedialne/huawei-tablet-matepad-s-11-5-8-256gb-wifi-g-key.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/ipad-i-tablety-multimedialne/apple-ipad-mini-2021-wi-fi-64gb-gwiezdna-szarosc.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/ipad-i-tablety-multimedialne/lenovo-tablet-p11-11-5-6gb-128gb-wifi-grey.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/ipad-i-tablety-multimedialne/lenovo-yoga-tab-13-yt-k606f-13-8-128gb-wi-fi.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/ipad-i-tablety-multimedialne/xiaomi-tablet-redmi-pad-pro-8-256ggb-graph-gray.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/ipad-i-tablety-multimedialne/samsung-tablet-galaxy-tab-a9-8-128gb-wifi-gray_1.bhtml': {'typ': 'Tablet', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/monitory-led-i-lcd/lg-monitor-27un880p-b.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/monitory-led-i-lcd/iiyama-monitor-gb2470hsu-b5.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/monitory-led-i-lcd/iiyama-monitor-gb2770qsu-b5.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/monitory-led-i-lcd/samsung-monitor-s27ag300nr.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/monitory-led-i-lcd/asus-monitor-vy279hge.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/monitory-led-i-lcd/xiaomi-monitor-a27i.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'},
#         'https://www.euro.com.pl/monitory-led-i-lcd/lg-monitor-27gs85q-b.bhtml': {'typ': 'Monitor', 'sklep': 'RTV Euro AGD'}
#     }

#     # Inicjacja pustych list do przechowywania danych
#     opinions_date_list = []
#     device_names = []
#     stores = []
#     opinions_list = []
#     raiting = []

#     for link, other in links.items():
#         # Uruchomienie przeglądarki
#         driver.get(link)
#         # Maksymalizacja okna
#         driver.maximize_window()        
#         time.sleep(3)

#         # Obsługa komunikatów
#         try:
#             accept = driver.find_element(By.XPATH, "//button[contains(@id, 'onetrust-accept-btn-handler')]")
#             accept.click()
#         except:
#             pass

#         # Pobranie nazw
#         try:
#             name = driver.find_element(By.XPATH, "//span[contains(@class, 'product-intro__title-text')]")
#             name_text = name.text
#         except:
#             device_names.append(None)  
        
#         # Sprawdzenie czy są opinie
#         try:
#                 opinion = driver.find_element(By.XPATH, "//div[contains(@class, 'product-information product-information--bigger')]//span[contains(@class, 'client-rate__rate')]")

#         except:
#                 continue
        
#         # Przewinięcie strony
#         driver.execute_script("window.scrollBy(0, 900);")
#         time.sleep(5)

#         # Wyświetlenie opinii
#         try:
#             time.sleep(5)
#             opinions_button = driver.find_element(By.XPATH, "//p[contains(@class, 'desktop-navigation__item desktop-navigation__item--opinions')]") 
#             driver.execute_script("arguments[0].click();", opinions_button)
#         except:
#             pass

#         # Pobranie opinii gdy jest ich dużo
#         try:
#             time.sleep(5)
#             opinions_all = driver.find_element(By.XPATH, "//div[contains(@class, 'opinions__cta ng-star-inserted')]//button") 
#             driver.execute_script("arguments[0].click();", opinions_all)
#             while True:
#                 # Wyświetlenie więcej opinii
#                 try:
#                     time.sleep(8)
#                     # Przewinięcie do samego dołu
#                     scrollable_element = driver.find_element(By.XPATH, "//eui-layer")
#                     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)
#                     time.sleep(4)
#                     show_more = driver.find_element(By.XPATH, "//a[contains(@class, 'list-load-more__button cta ng-star-inserted')]")
#                     driver.execute_script("arguments[0].click();", show_more)
#                     time.sleep(2)
                
#                 except:
#                     break
#             # Pobranie danych
#             try:
#                 time.sleep(5)
#                 raitings = driver.find_elements(By.XPATH, "//div[contains(@class, 'opinions-layer ng-star-inserted')]//div[contains(@class, 'opinions-layer__opinions-boxes')]//span[contains(@class, 'client-rate__rate')]")
#                 opinions = driver.find_elements(By.XPATH, "//div[contains(@class, 'opinions-layer ng-star-inserted')]//div[contains(@class, 'opinions-layer__opinions-boxes')]//p[contains(@class, 'opinion-box__text')]")
#                 opinions_date = driver.find_elements(By.XPATH, "//span[contains(@class, 'opinion-box__date')]")
#                 time.sleep(5)
#                 raitings_text = [raiting.text for raiting in raitings]
#                 opinions_text = [opinion.text for opinion in opinions]
#                 opinions_date_text = [opinion_date.text for opinion_date in opinions_date] 
#                 for i in range(len(raitings_text)):
#                     device_names.append(name_text)
#                     raiting.append(raitings_text[i])
#                     opinions_list.append(opinions_text[i])
#                     stores.append(other['sklep']) 
#                     opinions_date_list.append(opinions_date_text[i])
#             except:
#                 pass

                
#         # Pobranie danych gdy jest mało opinii        
#         except:
#                 time.sleep(3)
#                 try:
#                     time.sleep(5)
#                     raitings = driver.find_elements(By.XPATH, "//div[contains(@class, 'opinion-box__content')]//span[contains(@class, 'client-rate__rate')]")
#                     opinions = driver.find_elements(By.XPATH, "//div[contains(@class, 'opinion-box__content')]//p[contains(@class, 'opinion-box__text opinion-box__text--truncated')]")
#                     opinions_date = driver.find_elements(By.XPATH, "//span[contains(@class, 'opinion-box__date')]")
#                     time.sleep(5)
#                     raitings_text = [raiting.text for raiting in raitings]
#                     opinions_text = [opinion.text for opinion in opinions]
#                     opinions_date_text = [opinion_date.text for opinion_date in opinions_date] 
#                     for i in range(len(raitings_text)):
#                         device_names.append(name_text)
#                         raiting.append(raitings_text[i])
#                         opinions_list.append(opinions_text[i])
#                         stores.append(other['sklep']) 
#                         opinions_date_list.append(opinions_date_text[i])
#                 except:
#                     pass

        
#     # Zamknięcie sesji
#     driver.quit()

#     # Utworzenie ramki danych
#     df = pd.DataFrame({
#         'Nazwa urzadzenia': device_names,
#         'Ocena': raiting,
#         'Treść': opinions_list,
#         'Sklep': stores,
#         'Data opinii': opinions_date_list,
#         'Data pobrania': date
#     })

#     df

#     # Zapis do pliku csv
#     csv = 'monitoring_opinie_produktow.csv'

#     if os.path.exists(csv):
#         df.to_csv(csv, mode='a', index=False, header=False)
#     else:
#         df.to_csv(csv, mode='w', index=False, header=True)

# except:
#     pass






# # x-kom
# try:

#     # Wprowadzenie user-agentów
#     user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
#     'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36',
#     'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2820.59 Safari/537.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36'
#     ]

#     # Funkcja czyszcząca treść opinii z niepotrzebnych znaków
#     def clean_text(text):
#         if not text:
#             return ""
#         text = re.sub(r'<.*?>', ' ', text)
#         text = text.replace('"', "'").replace(';', ',')
#         text = text.replace('\n', ' ').replace('\r', ' ')
#         text = text.replace(' Zwiń', "")
#         return ' '.join(text.split())


#     links = {
#         'https://www.x-kom.pl/p/1264766-sluchawki-bezprzewodowe-samsung-galaxy-buds3-srebrne.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1070895-sluchawki-true-wireless-apple-airpods-3-generacji-lightning.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1180227-sluchawki-true-wireless-apple-airpods-pro-2-generacji-usb-c.html': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/490938-sluchawki-true-wireless-apple-airpods-2-generacji.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1163204-sluchawki-bezprzewodowe-jbl-tune-770nc-czarne.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1205701-sluchawki-bezprzewodowe-jbl-tune-520bt-czarny.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/724758-sluchawki-bezprzewodowe-technics-eah-a800-czarne.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1177895-sluchawki-bezprzewodowe-soundcore-liberty-4-nc-czarne.html': {'typ': 'Słuchawki (dokanałowe)', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1119463-sluchawki-bezprzewodowe-sony-wh-ch720n-czarne.html': {'typ': 'Słuchawki (nauszne)', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1278719-sluchawki-true-wireless-apple-airpods-4-generacji.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1278730-sluchawki-true-wireless-apple-airpods-4-generacji-z-aktywna-redukcja-halasu.html': {'typ': 'Słuchawki (douszne)', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1195773-tablet-8-samsung-galaxy-tab-a9-x110-wifi-8-128gb-szary.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1257581-tablety-11-huawei-matepad-115-s-wifi-8-256gb-space-greym-pencil-klawiatura.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/681239-tablet-10-apple-ipad-102-9gen-64gb-wi-fi-space-gray.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1126296-tablet-11-lenovo-tab-p11-6gb-128gb-android-12l-wifi-gen-2.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1226967-tablet-13-lenovo-yoga-tab-13-8gb-128gb-android-11-wifi.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1257753-tablet-12-xiaomi-redmi-pad-pro-8gb-256gb-graphite-gray.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1195785-tablety-11-samsung-galaxy-tab-a9-x210-wifi-8-128gb-szary.html': {'typ': 'Tablet', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1137559-monitor-led-27-265-284-lg-ultrafine-27un880p-b-ergo-4k.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1142195-monitor-led-24-235-264-iiyama-g-master-gb2470hsu-b5-red-eagle.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1142197-monitor-led-27-265-284-iiyama-g-master-gb2770qsu-b5-red-eagle.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1125894-monitor-led-27-265-284-samsung-odyssey-s27ag300nrx.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1144811-monitor-led-27-265-284-asus-vy279hge.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1208060-monitor-led-27-265-284-xiaomi-a27i.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
#         'https://www.x-kom.pl/p/1276734-monitor-led-27-265-284-lg-ultragear-27gs85q-b.html': {'typ': 'Monitor', 'sklep': 'x-kom'},
#     }
    
#     # Inicjacja pustych list do przechowywania danych
#     opinions_date_list =[]
#     raiting = []
#     device_names = []
#     stores = []
#     opinions_list = []
#     opinions_count = []  

    
#     for link, other in links.items():
#         # Losowanie user-agent
#         user_agent = random.choice(user_agents)
#         # Konfiguracja przeglądarki
#         options = Options()
#         options.add_argument(f'user-agent={user_agent}')
#         service = Service(executable_path="chromedriver.exe")
#         driver = webdriver.Chrome(service=service, options=options)
#         # Uruchomienie przeglądarki
#         driver.get(link)
#         time.sleep(6)

#         # Zarządzanie oknami
#         main_window = driver.current_window_handle
#         windows = driver.window_handles
#         if len(windows) > 1:
#             new_window = [window for window in windows if window != main_window][0]
#             driver.switch_to.window(new_window)
#         time.sleep(3)
        
#         # Obsługa komunikatów
#         try:
#             accept = driver.find_element(By.XPATH, "//button[contains(@class, 'parts__ButtonWrapper-sc-6adb784e-0 parts__AcceptButton-sc-22bd9b2d-9 kXIGaP jbQKAv')]")
#             accept.click()
#         except:
#             pass
#         time.sleep(3)
        
#         # Pobieranie nazw urządzeń
#         try:
#             try:
#                 name = driver.find_element(By.XPATH, "//h1[contains(@class, 'parts__Title-sc-2836f2a2-4 ekAhAJ')]")
#             except:
#                 try:
#                     name = driver.find_element(By.XPATH, "//h1[contains(@class, 'parts__Title-sc-2836f2a2-4 jTwNjC')]")
#                 except: 
#                     device_names.append(None)
#             name_text = name.text
#         except:
#             device_names.append(None)
        

#         time.sleep(3)
#         # Przejście do opinii
#         try:
#             op = driver.find_element(By.XPATH, "//span[contains(@class, 'parts__MenuItemText-sc-695441ce-3 eXdRHK') and contains(text(), 'Opinie')] | //span[contains(@class, 'parts__MenuItemText-sc-b23406eb-3 gAMmlx') and contains(text(), 'Opinie')]")
#             op.click()
#             time.sleep(3)
#         except:
#             pass

    
#         time.sleep(3)
#         # Przewijanie strony
#         driver.execute_script("window.scrollBy(0, 1200);") 
#         time.sleep(3)

#         # Przewiniecie do opinii
#         try:
#             while True:
#                 try:
#                     element = driver.find_element(By.XPATH, "//div[contains(@class, 'parts__CommentBodyWrapper-sc-1400db22-20 hsWNxj')]//p | //button[contains(@class, 'sc-iVCKna eNa-Dkb sc-kcuKUB hmVgvR parts__AddCommentModalButton-sc-eb57a5e0-3 dNAwxx')] | //div[contains(@class, 'parts__Text-sc-da9abc67-1 dVqzgO parts__CommentBody-sc-b5c8e9d8-21 YsAwC')]//p")
#                     driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
#                     window_view = driver.execute_script("var rect = arguments[0].getBoundingClientRect();""return rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight);",element)
#                     if window_view:
#                         break
                        
#                 except:
#                     pass

#         except:
#             pass
        
#         # Gdy są opinie
#         try:
#             driver.find_element(By.XPATH, "//div[contains(@class, 'parts__CommentBodyWrapper-sc-1400db22-20 hsWNxj')]//p | //div[contains(@class, 'parts__Text-sc-da9abc67-1 dVqzgO parts__CommentBody-sc-b5c8e9d8-21 YsAwC')]//p")
#             # Gdy nie ma przycisku do więcej opinii
#             try:
#                 time.sleep(3)
#                 driver.find_element(By.XPATH, "//div[contains(text(), 'Koniec opinii.')]")

#                 while True:
#                     try:
#                         # Rozwinięcie długich opinii
#                         show_more_content = driver.find_element(By.XPATH, "//span[contains(@class, 'parts__ReadMore')        and not(ancestor::span[@style='position:fixed;visibility:hidden;top:0;left:0' or contains(@style, 'position: fixed') and contains(@style, 'visibility: hidden')])       and contains(text(), '...')]")
#                         driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", show_more_content)

#                         time.sleep(1)
#                         window_view = driver.execute_script(
#                             "var rect = arguments[0].getBoundingClientRect();"
#                             "return rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight);",
#                             show_more_content
#                         )

#                         if window_view:
#                             time.sleep(2)
#                             show_more_content.click()
#                             time.sleep(3)
#                     except:
#                         break
#                 # Wybranie divow które zawierają opinie z treściami
#                 div_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'BoxFlex__Box-sc-bfe0bca9-0 dVvZQR parts__CommentBox-sc-1400db22-18 cJsUhM')]")

#                 # Pobranie treści i liczenie gwiazdek opinii
#                 for index, div in enumerate(div_elements, start=1):
#                     try:
#                         opinions = div.find_element(By.XPATH, ".//div[contains(@class, 'parts__CommentBodyWrapper-sc-1400db22-20 hsWNxj')]//p")
#                         opinion_date = div.find_element(By.XPATH, ".//div[contains(@class, 'parts__CommentDate-sc-1400db22-9 hSCZhg')]")
#                         stars = div.find_elements(By.XPATH, ".//*[name()='svg' and contains(@class, 'sc-bgqQcB hofwGb sc-kZwcoV glzWXZ')]")
#                         stars_count = len(stars)
#                         raiting.append(stars_count)
#                         try:
#                             opinions_text = clean_text(opinions.text)
#                         except:
#                             opinions_text = ""
#                         opinion_date_text = opinion_date.text
#                         opinions_date_list.append(opinion_date_text)
#                         opinions_list.append(opinions_text)
#                         device_names.append(name_text)
#                         stores.append(other['sklep'])
                        
#                     except:
#                         pass
#             # Gdy trzeba klikać przycisk rozwijający więcej opinii
#             except:
                
#                 while True:
#                     try:
                        
#                         try:
#                             # Rozwijanie listy opinii
#                             time.sleep(2)
#                             show_more = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'sc-iVCKna jjmzFq sc-kcuKUB buGPIy parts__MoreCommentsButton-sc-2abff0b6-0 kGFIsM')]")))
#                             driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", show_more)
#                             window_view = driver.execute_script(
#                                 "var rect = arguments[0].getBoundingClientRect();"
#                                 "return rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight);",
#                                 show_more
#                             )
                            
#                             if window_view:
#                                 time.sleep(3)
#                                 show_more.click()
#                                 time.sleep(2)
#                         except:
#                             show_more = driver.find_element(By.XPATH, "//div[contains(text(), 'Koniec opinii.')]")
#                             driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", show_more)
#                             window_view = driver.execute_script(
#                                 "var rect = arguments[0].getBoundingClientRect();"
#                                 "return rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight);",
#                                 show_more
#                             )
                            
#                             if window_view:
#                                 break
                        
#                     except:
#                         break

#                     time.sleep(0.5)

#                 while True:
#                     try:
#                         # Rozwijanie długich opinii
#                         time.sleep(2)
#                         show_more_content = driver.find_element(By.XPATH, "//span[contains(@class, 'parts__ReadMore')        and not(ancestor::span[@style='position:fixed;visibility:hidden;top:0;left:0' or contains(@style, 'position: fixed') and contains(@style, 'visibility: hidden')])       and contains(text(), '...')]")
#                         driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", show_more_content)

#                         time.sleep(1)
#                         window_view = driver.execute_script(
#                             "var rect = arguments[0].getBoundingClientRect();"
#                             "return rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight);",
#                             show_more_content
#                         )

#                         if window_view:
#                             time.sleep(2)
#                             show_more_content.click()
#                             time.sleep(3)
#                     except:
#                         break
#                 time.sleep(3)

#                 # Wyznaczenie divów z opiniami z treścią
#                 div_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'BoxFlex__Box-sc-bfe0bca9-0 dVvZQR parts__CommentBox-sc-1400db22-18 cJsUhM')]")
#                 for index, div in enumerate(div_elements, start=1):
#                     try:
#                         opinions = div.find_element(By.XPATH, ".//div[contains(@class, 'parts__CommentBodyWrapper-sc-1400db22-20 hsWNxj')]//p")
#                         opinion_date = div.find_element(By.XPATH, ".//div[contains(@class, 'parts__CommentDate-sc-1400db22-9 hSCZhg')]")
                        
#                         stars = div.find_elements(By.XPATH, ".//*[name()='svg' and contains(@class, 'sc-bgqQcB hofwGb sc-kZwcoV glzWXZ')]")

#                         stars_count = len(stars)
                        
#                         raiting.append(stars_count)
#                         try:
#                             opinions_text = clean_text(opinions.text)
#                         except:
#                             opinions_text = ""
#                         opinion_date_text = opinion_date.text
#                         opinions_date_list.append(opinion_date_text)
#                         opinions_list.append(opinions_text)
#                         device_names.append(name_text)
#                         stores.append(other['sklep'])
#                     except:
#                         pass
                
                
                    
#         except:
#             continue


        
#         time.sleep(4)


#         # Zamknięcie sesji
#         driver.quit()

#     # Utworzenie ramki danych
#     df = pd.DataFrame({
#         'Nazwa urzadzenia': device_names,
#         'Ocena': raiting,
#         'Treść': opinions_list,
#         'Sklep': stores,
#         'Data opinii': opinions_date_list,
#         'Data pobrania': date
#     })

#     df

#     #Zapis do pliku csv
#     csv = 'monitoring_opinie.csv'

#     if os.path.exists(csv):
#         df.to_csv(csv, mode='a', index=False, header=False, sep=',', encoding='utf-8-sig')
#     else:
#         df.to_csv(csv, mode='w', index=False, header=True, sep=',', encoding='utf-8-sig')
# except:
#     pass