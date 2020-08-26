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

# <div class="anime-slide-block" id="anime_recommendation" data-json=\'{"width":702,"btnWidth":40,"margin":8}\'>
# <li class="btn-anime" style="width:90px" title="Steins;Gate"><a class="link bg-center" href="https://myanimelist.net/recommendations/anime/9253-31240" style="width:90px;height:140px;"><span class="title fs10">Steins;Gate</span><span class="users">93 Users</span><img alt="Steins;Gate" border="0" class="image lazyload" data-src="https://cdn.myanimelist.net/r/90x140/images/anime/5/73199.jpg?s=845a91477804f22f90e5a37faa1d76a6" data-srcset="https://cdn.myanimelist.net/r/90x140/images/anime/5/73199.jpg?s=845a91477804f22f90e5a37faa1d76a6 1x,https://cdn.myanimelist.net/r/180x280/images/anime/5/73199.jpg?s=0e8d9c7f7140a5583adfaf1556635774 2x" height="140" src="https://cdn.myanimelist.net/images/spacer.gif" width="90"/></a></li>

arr3 = soup.find_all("a", class_="link bg-center")
for k in arr3:
    uprint(k["href"])

# Belum : jumlah user
