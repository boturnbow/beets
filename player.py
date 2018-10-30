from subprocess import call

print("Clip Sport contains Wilco with 4 setlists, Decemberists with one setlist, Radiohead, Sharon Jones.")

card_name = "Clip\ Sport"
card_dir = "/Volumes/%s/Music/" % card_name
query = "wilco, tweedy, decemberists, meloy, radiohead, sharon jones"

call("beet stats %s" % query, shell=True)

# clean out directory instead of just syncing bc problems with sorting on sandisk
call("rm -rf %s*" % card_dir, shell=True)

# move setlist m3u files to sandisk with windows line endings
call("cp /Users/bo/Music/beets/Setlists/*.m3u " + card_dir, shell=True)
call("unix2dos %s*" % card_dir, shell=True)

# 10/29/18 I just added the -a here to help with singles and featured
# will have to check later to see if it cleans things up, and what is misses
# use convert plugin to move files using query
call("beet convert -a -y -d %s %s" % (card_dir, query), shell=True)

print("")
call("df -h /Volumes/%s/" % card_name, shell=True)
