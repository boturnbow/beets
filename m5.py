from subprocess import call

print("M5 contains Comedy, Electronic, Hip Hop/Rap, Latin, New Age, Reggae, World.")

card_name = "M5"
card_dir = "/Volumes/%s/Music/" % card_name
query = "genre:Comedy, genre:Electronic, genre:'Hip Hop/Rap', genre:Latin, genre:New Age, genre:Reggae, genre:World"

call("beet stats %s" % query, shell=True)

# clean out directory instead of just syncing bc problems with sorting on sandisk
call("rm -rf %s*" % card_dir, shell=True)

# use convert plugin to move files using query
call("beet convert -y -d %s %s" % (card_dir, query), shell=True)

print("")
call("df -h /Volumes/%s/" % card_name, shell=True)
