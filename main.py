"""
Tujuan dibuatnya ini adalah membuat sistem rekomendasi dari
data yang didapat dari website myanimelist
"""
import sys
import urllib.request
from bs4 import BeautifulSoup


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


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


# def get_recommendation(anime_input_code):
#     # 1. Generate situs berdasarkan kode anime, lalu mengambil data
#     url    = "https://myanimelist.net/anime/" + anime_input_code
#     webUrl = urllib.request.urlopen(url)
#     data   = webUrl.read()
#
#     # 2. Menganalisis data html dengan bs4 untuk memudahkan pencarian tag
#     soup = BeautifulSoup(data, 'html.parser')
#     arr = soup.find(id="anime_recommendation")
#
#     # 3. Pencarian kode anime rekomendasi beserta mengambil jumlah users setiap anime
#     anime_and_users = {}
#     arr2 = soup.find_all("a", class_="link bg-center")
#     arr3 = soup.find_all("span", class_="users")
#
#     # 4. Menyatukan temuan kode anime dan jumlah users
#     for k in range(len(arr2)):
#         compare_code = arr2[k]["href"].split("/")[-1].split("-")
#         compare_code.remove(anime_input_code)
#         code_anime = compare_code[0]
#         users = arr3[k].string.split(" ")[0]
#         # anime_and_users.append([code_anime, int(users)])
#         anime_and_users[code_anime] = int(users)
#
#     # 5. Mengembalikan kode anime rekomendasi beserta jumlah users dalam sebuah list
#     return anime_and_users



# if __name__ == '__main__':

anime_all_reco = {}
rezero     = "31240"
steinsgate = "9253"
rezero     = get_recommendation(rezero)
steinsgate = get_recommendation(steinsgate)

for i in rezero:
    try:
        anime_all_reco[i[0]] = anime_all_reco[i[0]] + i[1]
    except:
        anime_all_reco[i[0]] = i[1]


print(anime_all_reco)

for i in steinsgate:
    try:
        anime_all_reco[i[0]] = anime_all_reco[i[0]] + i[1]
    except:
        anime_all_reco[i[0]] = i[1]
print("---------------")
print(anime_all_reco)

"""
Rezero s1 = 31240
Steins;gate = 9253
Konosuba = 30831

perhitungan extend :
anime input x nilai vote user => jadi anime rekomendasi akan di kalikan dengan nilai
jumlah user anime rekomendasi x nilai asli mal

Fitur tambahan rencana :
Judul anime
"""
