# Zooniverse-project-builder
Built on the Zooniverse Hack Day. Program that builds a project on the Zooninverse with a bank of images of a specified 'thing' uploaded as an image set. Sets project description as a wikipedia summary of the the 'thing' specified.

## Code Example

```
   $ python build.py
   What would you like to classify? cat
   Zooniverse username: example
   Password : ******
   Creating Project...
   Fectching images from google...
   Creating image set...
   Uploading images to Zooniverse...
   Complete.
```
Will result in a project being created in the project builder section of your zooniverse account. It will have images of cats uploaded to an image set, and a wikipedia summary of cats in the description of the project.

## Installation

You will need the [zooniverse panoptes-python-client](https://github.com/zooniverse/panoptes-python-client), and [wikipedia api for python](https://github.com/goldsmith/Wikipedia).

```
   $ pip install panoptes-client
   $ pip install wikipedia
```
