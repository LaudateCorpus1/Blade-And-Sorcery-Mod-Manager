import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import zipfile
import getpass
from datetime import date
import json
import ntpath
MENU_XML= """
<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.22.2 -->
<interface>
  <requires lib="gtk+" version="3.20"/>
  <object class="GtkApplicationWindow" id="BASMM">
    <property name="name">Blade And Sorcery Mod Manager</property>
    <property name="can_focus">False</property>
    <property name="is_focus">True</property>
    <property name="tooltip_text" translatable="yes">Blade And Sorcery Mod Manager</property>
    <property name="default_width">1920</property>
    <property name="default_height">1080</property>
    <property name="icon_name">Blade And Sorcery Mod Manager</property>
    <child type="titlebar">
      <placeholder/>
    </child>
    <child>
      <object class="GtkBox" id="Box">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="halign">baseline</property>
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkLabel" id="Name">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="label" translatable="yes">Blade and Sorcery Mod Manager</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkActionBar" id="Top_Buttons">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="halign">center</property>
            <child>
              <object class="GtkFileChooserButton" id="Import">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="title" translatable="yes"/>
              </object>
              <packing>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="Add">
                <property name="label" translatable="yes">Add</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <signal name="clicked" handler="AddClicked" swapped="no"/>
              </object>
              <packing>
                <property name="position">2</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkScrolledWindow" id="ListWindow">
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="vexpand">True</property>
            <property name="shadow_type">in</property>
            <child>
              <object class="GtkTreeView" id="List">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="hexpand">True</property>
                <property name="activate_on_single_click">True</property>
                <child internal-child="selection">
                  <object class="GtkTreeSelection" id="List1"/>
                </child>
              </object>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkActionBar" id="Bottom_Buttons">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="double_buffered">False</property>
            <property name="halign">center</property>
            <property name="valign">end</property>
            <child>
              <object class="GtkButton" id="Delete">
                <property name="label" translatable="yes">Delete</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="image_position">right</property>
                <signal name="clicked" handler="DeleteClicked" swapped="no"/>
              </object>
              <packing>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="Apply">
                <property name="label" translatable="yes">Apply</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <signal name="clicked" handler="ApplyClicked" swapped="no"/>
              </object>
              <packing>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="Save">
                <property name="label" translatable="yes">Save</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <signal name="clicked" handler="SaveClicked" swapped="no"/>
              </object>
              <packing>
                <property name="position">0</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">4</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
"""

#data = open('data.txt','r')

class Handler:
    def onDestroy(self, *args):
      Gtk.main_quit()
      Files.destroy()

    

    def DeleteClicked(self, *args):
      selection= List.get_selection()
      model, paths=selection.get_selected_rows()
      for path in paths:
        iter= model.get_iter(path)
        print(path)
        model.remove(iter)
        
        with open('data.json', "r+") as json_file:
          i = 0
          data = json.load(json_file) 
          size = len(data)
          print(data)

          # Remove key from dictionary
          del data[str(path)]
          i = path
          while i < size:
            data[str(i)] = data[str(i + 1)]
            i += 1          
          json_file.seek(0)
          write_json(data)

    def SaveClicked(self, *args):
      print("SaveClicked")



    def ApplyClicked(self, *args):
      print("ApplyClicked")
    def AddClicked(self, *args):
      print(Import.get_filename())
      filelocation=Import.get_filename()
      filename=ntpath.basename(filelocation)
      urilocation=Import.get_uri()
      print(urilocation)
      today=str(date.today())
      

      with open('data.json', "r+") as json_file:
        data = json.load(json_file) 
        print(data)
        key =	str(len(data))

        print(key)
        y = {
            key:{
              "modname":	filename,
              "modlocation":	filelocation,
              "dateadded": 	today
                }
            }
        data.update(y)
        json_file.seek(0)
      write_json(data)


      if(not filelocation==None and not urilocation=="None"):
        Import.set_uri("None")
        BASMM.store.append(None,[filelocation,today,True])



def write_json(data, filename='data.json'):
  with open(filename,'w') as f:
      json.dump(data, f, indent=3)

builder = Gtk.Builder()
builder.add_from_string(MENU_XML)
builder.connect_signals(Handler())
BASMM=builder.get_object("BASMM")
Box=builder.get_object("Box")
Name=builder.get_object("Top_Button")
Import=builder.get_object("Import")
Delete=builder.get_object("Delete")
List=builder.get_object("List")
Bottom_Button=builder.get_object("Bottom_Button")
Save=builder.get_object("Save")
Apply=builder.get_object("Apply")
Files=builder.get_object("Files")
row = builder.get_object("row")
Add = builder.get_object("Add")

#Creates Columns for TreeView
BASMM.store= Gtk.TreeStore(str,str,bool)
List.set_model(BASMM.store)
renderer_text=Gtk.CellRendererText()


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

with open('data.json', "r+") as json_file:
  i = 0
  data = json.load(json_file) 
  count=len(data)
  print(count)
  while i < count:
    key = str(i)
    if key in data:
      print(data[key])
      
      modname =		data[key]["modname"]
      modlocation =	data[key]["modlocation"]
      dateadded =	data[key]["dateadded"]

      BASMM.store.append(None,[modname,dateadded,True])
      i += 1
    else:
      while str(i) not in data:
        i += 1
        data[key] = data[str(i)]
        
      
BASMM.show_all()
BASMM.connect("destroy", Gtk.main_quit)
Gtk.main()
