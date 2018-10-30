# Beets config

* `Clip Sport` contains Wilco with 4 setlists, Decemberists with one setlist, Radiohead, Sharon Jones
* `B1` contains Alternative.
* `B2` contains Rock, Pop, Punk Rock.
* `M1` contains podcasts, smart playlists, all singles, plus Christian & Gospel, Classical, Holiday, Jazz, Soundtrack.
* `M2` contains Blues and R&B.
* `M3` contains Bluegrass and Folk.
* `M4` contains Country.
* `M5` contains Comedy, Electronic, Hip Hop/Rap, Latin, New Age, Reggae, World.

Sync player and cards with:

```
$ python ~/Library/Application\ Support/beets/player.py
$ python ~/Library/Application\ Support/beets/b1.py
$ python ~/Library/Application\ Support/beets/b2.py
$ python ~/Library/Application\ Support/beets/m1.py
$ python ~/Library/Application\ Support/beets/m2.py
$ python ~/Library/Application\ Support/beets/m3.py
$ python ~/Library/Application\ Support/beets/m4.py
$ python ~/Library/Application\ Support/beets/m5.py
```

Helpful

```
# upgrade beets
$ pip install --user --upgrade beets

albums added in last month
$ beet ls -a 'added:-1m..'

beet ls -af '$albumartist - $album : $genre' weezer
beet mod genre='Rock' 'pacific daydream'
```

itunes

Set prefs to not organize or copy
Add beets directory to Library
Won't refresh when you get new music, prob have to add again
