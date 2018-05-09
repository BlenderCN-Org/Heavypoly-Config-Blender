bl_info = {
    "name": "Pie Save",
    "description": "Save import export Pie",
    "author": "Vaughan Ling",
    "version": (0, 1, 0),
    "blender": (2, 79, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
    }

import bpy
from bpy.types import (
        Menu,
        Operator,
        )
import os

# save import export

class VIEW3D_PIE_SAVE(Menu):
    bl_idname = "pie.save"
    bl_label = "Save"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("wm.link", text = "Link/Reference")
        pie.operator("wm.save_without_prompt", text="Save", icon='FILE_TICK')
        pie.operator("wm.save_as_mainfile", text="Save As...", icon='SAVE_AS')
        pie.operator("wm.open_mainfile", text="Open file", icon='FILE_FOLDER')
        pie.menu("INFO_MT_file_import", icon='IMPORT')
        pie.menu("INFO_MT_file_export", icon='EXPORT')
        pie.operator("wm.read_homefile", text="New", icon='NEW')



#import_mesh.stl

        # box = pie.split().column()
        # row = box.row(align=True)

        # #9 - TOP - RIGHT
        # box = pie.split().column()
        # row = box.row(align=True)

def register():
    bpy.utils.register_class(VIEW3D_PIE_SAVE)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PIE_SAVE)

if __name__ == "__main__":
    register()
