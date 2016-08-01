###############################################################################
# Peter McGill 29.07.2016                                                     #
# build.py - code to build a project on the Zooniverse, with images of a      #
# specified thing pulled from a google search. Requires Zooniverse             #
# panoptes_client and wikipedia python api                                    #
###############################################################################

from panoptes_client import Project, Panoptes, SubjectSet, Subject
from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import getpass
import wikipedia


# ask user for login and object they want to classify
thing = raw_input("What would you like to classify? ")
user = raw_input("Zooniverse username: ")
password = getpass.getpass("password: ")

print 'Creating Project...'

#create project
Panoptes.connect(username=str(user), password=str(password))
p = Project()
p.display_name= 'Help find out about all the' + str(thing) + '\'s'

#add wikipedia summary to project description
p.description= wikipedia.summary(str(thing),sentences=1)
p.primary_language='en'
p.private=True
p.save()

print 'Fectching images from google...'

# get images
def get_soup(url,header):
  return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),"lxml")

image_type = thing
query = str(thing)
query= query.split()
query='+'.join(query)
url=url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
header = {'User-Agent': 'Mozilla/5.0'}
soup = get_soup(url,header)

images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
#print images
for img in images:
  raw_img = urllib2.urlopen(img).read()
  #add the directory for your image here
  DIR="images/"
  cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
  f = open(DIR + image_type + "_"+ str(cntr)+".jpg", 'wb')
  f.write(raw_img)
  f.close()

print 'Creating image set...'

# create the subject set.
subject_set = SubjectSet()
subject_set.links.project = p
subject_set.display_name = "Images of " + thing + '\'s'
subject_set.save()

print 'Uploading images to Zooniverse...'

# add all images to subject set
for i in range(1,21):
    subject = Subject()
    subject.links.project = p
    subject.add_location('images/' + str(thing) + '_' + str(i)+'.jpg')
    subject.save()
    subject_set.add(subject)

print 'Complete.'
