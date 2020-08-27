"""
Tujuan dibuatnya ini adalah membuat sistem rekomendasi dari
data yang didapat dari website myanimelist
"""
import sys
import time
import urllib.request
from bs4 import BeautifulSoup

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

def get_title(kode):
    url    = "https://myanimelist.net/anime/" + kode
    webUrl = urllib.request.urlopen(url)
    data   = webUrl.read()
    time.sleep(1)

    soup = BeautifulSoup(data, 'html.parser')
    title = soup.find_all("h1", class_="title-name")[0].string

    return title

def get_recommendation(anime_input_code):
    # 1. Generate situs berdasarkan kode anime, lalu mengambil data
    url    = "https://myanimelist.net/anime/" + anime_input_code
    webUrl = urllib.request.urlopen(url)
    data   = webUrl.read()

    # 2. Menganalisis data html dengan bs4 untuk memudahkan pencarian tag
    soup = BeautifulSoup(data, 'html.parser')
    arr = soup.find(id="anime_recommendation")

    # 3. Pencarian kode anime rekomendasi beserta mengambil jumlah users setiap anime
    anime_and_users = []
    arr2 = soup.find_all("a", class_="link bg-center")
    arr3 = soup.find_all("span", class_="users")

    # 4. Menyatukan temuan kode anime dan jumlah users
    for k in range(len(arr2)):
        compare_code = arr2[k]["href"].split("/")[-1].split("-")
        compare_code.remove(anime_input_code)
        code_anime = compare_code[0]
        users = arr3[k].string.split(" ")[0]
        anime_and_users.append([code_anime, int(users)])

    # 5. Mengembalikan kode anime rekomendasi beserta jumlah users dalam sebuah list
    return anime_and_users

def big_list_recommendation(arr_anime):
    anime_all_reco = {}
    for i in arr_anime :
        anime = get_recommendation(i)

        for i in anime:
            try:
                anime_all_reco[i[0]] = [anime_all_reco[i[0]][0] + i[1], anime_all_reco[i[0]][1] + 1 ]
            except:
                anime_all_reco[i[0]] = [i[1], 1]

    return anime_all_reco



# ==============================================================================
# if __name__ == '__main__':
# anime_all_reco = {}
# arr_anime = ["31240", "9253", "31043"]
#
# anime_all_reco = big_list_recommendation(arr_anime)
# for i in anime_all_reco:
#     uprint(get_title(i))
#     print(str(anime_all_reco[i][0]) + " | " + str(anime_all_reco[i][1]))
# ==============================================================================
# def big_list_recommendation(arr_anime):
#     anime_all_reco = {}
#     for i in arr_anime :
#         anime = get_recommendation(i)
#
#         for i in anime:
#             try:
#                 anime_all_reco[i[0]] = anime_all_reco[i[0]] + i[1]
#             except:
#                 anime_all_reco[i[0]] = i[1]
#
#     return anime_all_reco
# ==============================================================================


"""
Rezero s1 = 31240
Steins;gate = 9253
Konosuba = 30831

perhitungan extend :
x anime input x nilai vote user => jadi anime rekomendasi akan di kalikan dengan nilai
x jumlah user anime rekomendasi x nilai asli mal

Fitur tambahan rencana :
Judul anime
"""
