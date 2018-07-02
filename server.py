import requests

while True:
    print("""
 #############################################
#                                             #
#      Server Admin Panel Finder v1.0         #
#                                             # 
#         Coded by Ahmet Ümit BAYRAM          #
#                                             #
 #############################################
    """)

    site = input("siteyi gir:")
    url = "https://api.viewdns.info/reverseip/?host="
    api_key = "&apikey=1390c310cd09636fa8085a63d5b6feffe0702c46&output=json"
    son_url = url + site + api_key
    responsec = requests.get(son_url)
    json_data = responsec.json()
    domain_liste = json_data["response"]["domains"]
    site_sayisi = json_data["response"]["domain_count"]
    son_liste = []

    i = 0
    dosya = open("./brute.txt", "r")
    a = dosya.read().split("\n")
    a.pop()
    while i < int(site_sayisi):
        for z in a:
            son_liste.append("http://www." + domain_liste[i]['name'] + z)
        i += 1
    for i in son_liste:
            try:
                req = requests.get(i)
                if req.status_code == 200 and ("unuttunuz" not in req.text) and ("Lost" not in req.text):
                    print(son_liste.index(i)+1,i, "panel bulundu!!!!!")
                elif req.status_code == 200 and "unuttunuz" in req.text:
                    print(son_liste.index(i)+1,i, "wordpress")
                elif req.status_code == 200 and "Lost" in req.text:
                    print(son_liste.index(i)+1,i, "wordpress")
                else:
                    print(son_liste.index(i)+1,i, "bulunamadı")
            except:
                    print(son_liste.index(i)+1,i, "bağlantı yok")
                    continue
            finally:
                    dosya.close()
