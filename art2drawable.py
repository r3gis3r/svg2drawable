#!/usr/bin/python
# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os, sys
import rsvg
from xml.dom.minidom import parse

import util


class AndroidProject:
  def __init__(self, directory):
    """
    Construct android project properties 
    which parse and retrieve serveral info about an android project 
    at a given directory path
    """
    # init
    self.root_dir = directory
    self.support_ldpi = False
    self.support_mdpi = False
    self.support_hdpi = False
    self.support_xhdpi = False
    # Parse the manifest file
    manifest = parse(os.path.join(self.root_dir, "AndroidManifest.xml"))
    supportScreen = manifest.getElementsByTagName('supports-screens')[0]
    ssattrs = supportScreen.attributes
    if ssattrs.has_key("android:smallScreens"):
      self.support_ldpi = (ssattrs.get("android:smallScreens").value.lower() == "true")
    if ssattrs.has_key("android:normalScreens"):
      self.support_mdpi = (ssattrs.get("android:normalScreens").value.lower() == "true")
    if ssattrs.has_key("android:largeScreens"):
      self.support_hdpi = (ssattrs.get("android:largeScreens").value.lower() == "true")
    if ssattrs.has_key("android:xlargeScreens"):
      self.support_xhdpi = (ssattrs.get("android:xlargeScreens").value.lower() == "true")

  def get_art_directory(self):
    """
    Retrieve directory where scalable art is stored
    """
    fdir = os.path.join(self.root_dir, "art")
    if not os.path.exists(fdir):
      raise Exception("Art path not found in this project")
    return fdir

  def get_res_directory(self):
    """
    Retrieve directory where bitmap res are stored
    """
    fdir = os.path.join(self.root_dir, "res")
    if not os.path.exists(fdir):
      raise Exception("Res path not found in this project")
    return fdir

def main():
  project = AndroidProject(os.getcwd())
  bdir = project.get_art_directory()
  scalable_dirs = [d for d in os.listdir(bdir) if d.startswith("scalable")]
  
  for sdir in scalable_dirs:
    formated_dir = sdir.replace("scalable", "drawable-%s")
    files = [f for f in os.listdir(os.path.join(bdir, sdir)) if f.endswith(".svg")]
    for f in files:
      file_path = os.path.join(bdir, sdir, f)
      in_svg = rsvg.Handle(file_path)
      svg_w = in_svg.get_property("width")
      svg_h = in_svg.get_property("height")
      print "In", file_path," : ", svg_w, "x", svg_h
      util.svg_to_drawables(file_path, project.get_res_directory(), mdpi_width=svg_w, mdpi_height=svg_h, folder_format=formated_dir, export_ldpi=project.support_ldpi, export_mdpi=project.support_mdpi, export_hdpi=project.support_hdpi, export_xhdpi=project.support_xhdpi)


if __name__ == "__main__":
	main()


