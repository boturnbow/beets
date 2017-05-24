from subprocess import call

print("B2 contains Rock, Pop, Punk Rock.")

card_name = "B2"
card_dir = "/Volumes/%s/Music/" % card_name
query = "genre:rock, genre:pop, genre:punk rock"

call("beet stats %s" % query, shell=True)

# clean out directory instead of just syncing bc problems with sorting on sandisk
call("rm -rf %s*" % card_dir, shell=True)

# use convert plugin to move files using query
call("beet convert -y -d %s %s" % (card_dir, query), shell=True)

print("")
call("df -h /Volumes/%s/" % card_name, shell=True)
