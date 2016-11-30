import feedparser
import urllib
import re
import os

print "Starting..."
maindir = "*********" # This is the directory, where all the files will be stored.
torrdir = maindir + 'Torrents/' #Directory where downloaded torrents will go. Same one where your App will look for torrents
Showsdir = maindir + 'Shows.txt' #File containing all the shows you want to donload
rsslink = "********" #link to the rss feed
ShowsFile = open(Showsdir)
Shows = ShowsFile.read().splitlines()
ShowsFile.close

print "Looking For Shows : "
print Shows
print "Done Reading Shows..."
print ""

print "Getting RSS Feed..."
allfeeds = feedparser.parse(rsslink)
match = r's+\d+\d+e+\d+\d'

#Get all the feeds
for feed in allfeeds.entries:

	for line in Shows:
		title = str(feed.title.lower())
		show = str(line.lower())
		url = feed.link

		#Check if the title has any of the shows we are looking for
		if title.find(show) != -1 :
			print "Found Show..."
			outstring = re.findall(match,title)
			print title
			
			#Try to find S##E##. Error if we dont find
			if len(outstring) == 1:
				currepisode = outstring[0]

				if os.path.isfile(maindir + show + '.txt'):
					file = open(maindir + show + '.txt','r')
					Episodes = file.read().splitlines()
					file.close
				else:
					file = open(maindir + show + '.txt','w')
					Episodes = {}
					file.close
					

				#Check if the episode in feed is part of our text file already
				if currepisode in Episodes:
					print "WE ALREADY GOT IT BRO..."
				else:
					print "NEW EPISODE, DOWNLOADING AND ADDING TO FILE..."
					print "ANOTHER PENDING HOUR OF YOUR LIFE WASTED..."
					file = open(maindir + show + '.txt','a')
					file.write("\n" + currepisode)
					file.close
					print title
					testfile = urllib.URLopener()
					testfile.retrieve(url,torrdir + title + ".torrent")

			else:
				print "ERROR"

print "Finished"
