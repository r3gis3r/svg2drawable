#!/usr/bin/python

from os import path, mkdir

# TODO : safe import with warnings
import cairo, rsvg, StringIO

def svg_to_png(in_path, out_path, width=48, height=48):
	"""
	Transform svg file into a png file at defined size
	Use the svg document bound as detected by rsvg library
	
	in_path -- path of the svg input file
	out_path -- where to save the file
	width -- target png width
	height -- target png height
	"""
	# Get input handle
	in_svg = rsvg.Handle(in_path)
	svg_w = in_svg.get_property("width")
	svg_h = in_svg.get_property("height")
	# Create output cairo surface
	surf = cairo.SVGSurface(StringIO.StringIO(), width, height) 
	svgctx = cairo.Context(surf)
	# Rescale context to fit 
	# TODO : take more scale type options here
	# TODO : support +1px border for 9 patches
	svgctx.scale(width/float(svg_w), height/float(svg_h))
	# Render file in cairo context
	in_svg.render_cairo(svgctx)
	
	# Save file
	surf.write_to_png(out_path)
	surf.finish()

# Define available densities
DENSITIES = [
	{
	"name" : "ldpi",
	"scale" : 0.75,
	"export_default" : True
	},
	{
	"name" : "mdpi",
	"scale" : 1.0,
	"export_default" : True
	},
	{
	"name" : "hdpi",
	"scale" : 1.5,
	"export_default" : True
	},
	{
	"name" : "xhdpi",
	"scale" : 2,
	"export_default" : False,
	}
	#TODO : add tvdpi?
]

def svg_to_drawables(in_path, out_path, out_name=None, 
                     mdpi_width=48, mdpi_height=48, folder_format = "drawable-%",
		     **kargs):
	"""
	Render svg into drawable folders (drawable-ldpi, hdpi, mdpi...)

	in_path -- path of the svg input file
	out_path -- path where drawable-xxx should go
	mdpi_width, mdpi_height -- width and height for reference output size
	
	use export_xxx (ex: export_mdpi=True/False) to enable a particular export size
	"""
	#Cleanup out_name 
	if out_name is None:
		out_name = path.splitext(path.basename(in_path))[0]
	if not out_name.endswith(".png"):
		out_name += ".png"

	for density in DENSITIES:
		dname = density["name"]
		dscale = density["scale"]
		#Should we process this density?
		process_density = density["export_default"]
		export_key = "export_%s" % ( dname, )
		if kargs.has_key(export_key):
			process_density = kargs[export_key]
		if process_density:
			out_folder_path = path.join(out_path, folder_format % dname)
			if not path.exists(out_folder_path):
				mkdir(out_folder_path)
			out_file_path = path.join(out_folder_path, out_name)
			print "Export : ", out_file_path
			svg_to_png(in_path, out_file_path, 
				   mdpi_width * dscale, mdpi_height * dscale)



