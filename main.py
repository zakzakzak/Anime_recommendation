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


url    = "https://myanimelist.net/anime/31240"
webUrl = urllib.request.urlopen(url)
data   = webUrl.read()

soup = BeautifulSoup(data, 'html.parser')
arr = soup.find(id="anime_recommendation")

anime_and_vote = []
arr2 = soup.find_all("a", class_="link bg-center")

arr3 = soup.find_all("span", class_="users")

for k in range(len(arr2)):
    compare_code = arr2[k]["href"].split("/")[-1].split("-")
    compare_code.remove("31240")
    code_anime = compare_code[0]
    vote = arr3[k].string.split(" ")[0]
    anime_and_vote.append([code_anime, vote])

for i in anime_and_vote:
    print(i)
