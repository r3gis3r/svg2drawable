Introduction
============

The purpose of this project is to provide tools to ease things to transform svg graphics to android graphics with several resolutions.

It is compounded of 

* a little python utils library that one can use directly from a python cli (util.py)
* a command line tool to autogenerate files contains into art/scalable(-xxxx) folder of a project
into res/drawable(-xxxx)-dpi folders. Size of svg files must be the target size in px of mdpi res
See CSipSimple project for a sample use.
* a pyqt program to transform quickly svg files into drawables (svg2drawable.py)

Requirements
------------
Library (util.py) : 

* python
* python-cairo
* python-rsvg

Command line tool (art2drawable.py) :
* xml.dom.minidom

Graphic (svg2drawable.py):

* pyQt
