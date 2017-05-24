from subprocess import call

print("M1 contains podcasts, smart playlists, all singles, plus Christian & Gospel, Classical, Holiday, Jazz, Soundtrack.")

card_name = "M1"
card_dir = "/Volumes/%s/Music/" % card_name
query = "playlist::'.+', singleton:true, genre:'Christian & Gospel', genre:Classical, genre:Holiday, genre:Jazz, albumtype:soundtrack"

call("beet stats %s" % query, shell=True)

# clean out directory instead of just syncing bc problems with sorting on sandisk
call("rm -rf %s*" % card_dir, shell=True)

# update all smart playlists
call("beet splupdate", shell=True)

# move m3u files to sandisk with windows line endings
call("cp /Users/bo/Music/beets/Playlists/*.m3u " + card_dir, shell=True)
call("unix2dos %s*" % card_dir, shell=True)

# use convert plugin to move files using query
call("beet convert -y -d %s %s" % (card_dir, query), shell=True)

# copy podcasts over - they're not in beets library
call("cp /Users/bo/Music/beets/Podcasts/*" + " /Volumes/%s/Podcasts/" % card_name, shell=True)

print("")
call("df -h /Volumes/%s/" % card_name, shell=True)
