Introduction
============

The purpose of this project is to provide tools to ease things to transform svg graphics to android graphics with several resolutions.

It is compounded of 

* a little python utils library that one can use directly from a python cli (util.py)
* a command line tool to autogenerate files contained into art/scalable(-xxxx) folder of a project into res/drawable(-xxxx)-dpi folders. Size of svg files must be the target size in px of mdpi res. See CSipSimple project for a sample use.
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

Usage
-----
Library (util.py) :

To be completed

Command line tool (art2drawable.py) :

* Create art folder inside your project
* Create scalable folder inside art folder. Alternatively if you want your svg to target only one api version or filtering rule you can add the rule in the folder name. For example scalable-v11
* Put your svg files inside this directory. The dimension of the svg page will be what will be used as base dimension for mpdi size.
* Ensure that your AndroidManifest.xml does contains the supports-screen tag
* In command line go in the root folder of your android project and run art2drawable.py


The tool will automatically produce res corresponding to svg files into dpi folders announced as supported by your AndroidManifest.xml. 

It also take into account extra rules to scalable folder name.
For example a file is in a scalable-v11 folder is generated in mdpi inside drawable-mdpi-v11 folder.
