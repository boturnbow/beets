from subprocess import call

print("M3 contains Bluegrass and Folk.")

card_name = "M3"
card_dir = "/Volumes/%s/Music/" % card_name
query = "genre:bluegrass, genre:folk"

call("beet stats %s" % query, shell=True)

# clean out directory instead of just syncing bc problems with sorting on sandisk
call("rm -rf %s*" % card_dir, shell=True)

# use convert plugin to move files using query
call("beet convert -y -d %s %s" % (card_dir, query), shell=True)

print("")
call("df -h /Volumes/%s/" % card_name, shell=True)
