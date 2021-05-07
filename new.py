import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from sys import platform
import vdf, zipfile, getpass, json, ntpath, re
from datetime import date
from os.path import expanduser, isfile, isdir
from zipfile import ZipFile

####################################################################################

MENU_XML = 		open('menu.xml','r').read()

####################################################################################

def loaddata():
  BASMM.store.clear()
  with open('data.json', "r+") as json_file:
    i = 		0
    index = 		""
    jsondata = 		json.load(json_file)
    data = 		{}
    keylist = 		list(jsondata.keys())
    for key in keylist:
      index = 		str(i)
      jsonmodname =	jsondata[key]["modname"]
      jsonmodlocation =	jsondata[key]["modlocation"]
      jsondateadded =	jsondata[key]["dateadded"]
      data[index] = 	{
    			 "modname" 	: jsonmodname, 
    			 "modlocation" 	: jsonmodlocation,
    			 "dateadded"	: jsondateadded
    			}
      modname =		data[index]["modname"]
      modlocation =	data[index]["modlocation"]
      dateadded =	data[index]["dateadded"]			 
    
      BASMM.store.append(None,[modname,dateadded,True])
      i += 1
    json_file.seek(0)
    write_json(data)

####################################################################################

def unzipfile(filepath, modfolderpath):
  with ZipFile(filepath,'r') as modzip:
    modzip.extractall(modfolderpath)

####################################################################################

def write_json(data, filename='data.json'):
  with open(filename,'w') as f:
      json.dump(data, f, indent=3)

####################################################################################

def winsteam():
  location =    'C:/Program Files (x86)/Steam/steamapps/'
  library = 		'libraryfolders.vdf'
  manifest = 		'appmanifest_629730.acf'
  
  librarypath = 	(location + library)
  manifestpath = 	(location + manifest)
  
  
  if (isfile(manifestpath)):
    with open(manifestpath, 'r') as f:
      acfdata = 	dict(vdf.VDFDict(vdf.load(f))["AppState"])
      path = (location + "common" + "/" + acfdata["installdir"])
      print (path)
       
  else:
    with open(librarypath, 'r') as f:
      vdfdata = 	dict(vdf.VDFDict(vdf.load(f))["LibraryFolders"])
      del 		vdfdata['TimeNextStatsReport']
      del 		vdfdata['ContentStatsID']
      keylist = 	list(vdfdata.keys())
      for key in keylist:
        liblocation = vdfdata[key] + "/" + "steamapps" + "/"
        
        manifestpath = (liblocation + manifest)
        with open(manifestpath, 'r') as f:
          acfdata = 	dict(vdf.VDFDict(vdf.load(f))["AppState"])
          path = (liblocation + "common" + "/" + acfdata["installdir"])
          if(isdir(path)):
            print (path)
####################################################################################

def linuxsteam():
  location = 		expanduser('~/.steam/steam/steamapps/')
  library = 		'libraryfolders.vdf'
  manifest = 		'appmanifest_629730.acf'
  
  librarypath = 	(location + library)
  manifestpath = 	(location + manifest)
  
  
  if (isfile(manifestpath)):
    with open(manifestpath, 'r') as f:
      acfdata = 	dict(vdf.VDFDict(vdf.load(f))["AppState"])
      path = (location + "common" + "/" + acfdata["installdir"])
      print (path)
       
  else:
    with open(librarypath, 'r') as f:
      vdfdata = 	dict(vdf.VDFDict(vdf.load(f))["LibraryFolders"])
      del 		vdfdata['TimeNextStatsReport']
      del 		vdfdata['ContentStatsID']
      keylist = 	list(vdfdata.keys())
      for key in keylist:
        liblocation = vdfdata[key] + "/" + "steamapps" + "/"
        
        manifestpath = (liblocation + manifest)
        with open(manifestpath, 'r') as f:
          acfdata = 	dict(vdf.VDFDict(vdf.load(f))["AppState"])
          path = (liblocation + "common" + "/" + acfdata["installdir"])
          if(isdir(path)):
            print (path)
      
####################################################################################

def macsteam():
  print("STUB")

####################################################################################

class Handler:

####################################################################################

    def onDestroy(self, *args):
      Gtk.main_quit()
      Files.destroy()

####################################################################################

    def DeleteClicked(self, *args):
      selection = 	List.get_selection()
      model, paths = 	selection.get_selected_rows()
      for path in paths:
        iter =  	model.get_iter(path)
        model.remove(iter)
        with open('data.json', "r+") as json_file:
          target = 	json.load(json_file)
          del 		target[str(path)]
          
          json_file.seek(0)
          write_json(target)
        loaddata()

####################################################################################

    def SaveClicked(self, *args):
      print("SaveClicked")

####################################################################################

    def ApplyClicked(self, *args):
      print("ApplyClicked")

####################################################################################      

    def AddClicked(self, *args):
      filelocation = 	Import.get_filename()
      filename = 	ntpath.basename(filelocation)
      urilocation = 	Import.get_uri()
      today = 		str(date.today())
      

      with open('data.json', "r+") as json_file:
        data = 		json.load(json_file) 
        key =		str(len(data))
        addition = 	{
                         key: {
                               "modname":	filename,
                               "modlocation":	filelocation,
                               "dateadded": 	today
                              }
                        }
        data.update(addition)
        json_file.seek(0)
        write_json(data)


      if(not filelocation == None and not urilocation == "None"):
        Import.set_uri("None")
        BASMM.store.append(None, [filelocation, today, True])

####################################################################################

# GTK Setup
builder = 		Gtk.Builder()
builder.add_from_string(MENU_XML)
builder.connect_signals(Handler())
BASMM =			builder.get_object("BASMM")
Box =	  		builder.get_object("Box")
Name =			builder.get_object("Top_Button")
Import =		builder.get_object("Import")
Delete =		builder.get_object("Delete")
List =			builder.get_object("List")
Bottom_Button = 	builder.get_object("Bottom_Button")
Save =			builder.get_object("Save")
Apply =			builder.get_object("Apply")
Files =			builder.get_object("Files")
row = 			builder.get_object("row")
Add = 			builder.get_object("Add")

#Creates Columns for TreeView
BASMM.store = 		Gtk.TreeStore(str,str,bool)
List.set_model(BASMM.store)
renderer_text = 	Gtk.CellRendererText()
Gtk.Window.set_default_size(BASMM, 640, 480)

column_mods=Gtk.TreeViewColumn("ModName",renderer_text,text=0)
List.append_column(column_mods)

column_date=Gtk.TreeViewColumn("Date",renderer_text, text=1)
List.append_column(column_date)

#Responds to toggle signal for Enabled
def on_toggle(cell, path, model, *ignore):
    if path is not None:
        it = BASMM.store.get_iter(path)
        model[it][2] = not model[it][2]


renderer_enable=Gtk.CellRendererToggle()
renderer_enable.connect("toggled", on_toggle, BASMM.store)
column_enable=Gtk.TreeViewColumn("Enabled",renderer_enable, active=2)
List.append_column(column_enable)


####################################################################################
####################################################################################
####################################################################################
  
loaddata()

if platform == "linux":
    linuxsteam()
elif platform == "darwin":
    macsteam()
elif platform == "win32" or platform == "cygwin":
    winsteam()

####################################################################################

BASMM.show_all()
BASMM.connect("destroy", Gtk.main_quit)
Gtk.main()
