bl_info = {
    "name": "Pie Rotate_90",
    "description": "Rotate 90",
    "author": "Vaughan Ling",
    "version": (0, 1, 0),
    "blender": (2, 78, 0),
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

class VIEW3D_PIE_Rotate_90(Menu):
    bl_idname = "pie.rotate90"
    bl_label = "Rotate_90"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        #4 - LEFT
        # left
        prop = pie.operator("transform.rotate", text="Z", icon="FILE_REFRESH")
        prop.constraint_axis = (False, False, True)
        prop.value = -1.5708
        prop.constraint_orientation = 'GLOBAL'
        # right
        prop = pie.operator("transform.rotate", text="Z", icon="FILE_REFRESH")
        prop.constraint_axis = (False, False, True)
        prop.value = 1.5708
        prop.constraint_orientation = 'GLOBAL'
        # bottom
        prop = pie.operator("transform.rotate", text="X", icon="FILE_REFRESH")
        prop.constraint_axis = (True, False, False)
        prop.value = -1.5708
        prop.constraint_orientation = 'GLOBAL'
        # top
        prop = pie.operator("transform.rotate", text="X", icon="FILE_REFRESH")
        prop.constraint_axis = (True, False, False)
        prop.value = 1.5708
        prop.constraint_orientation = 'GLOBAL'  
        # topleft
        prop = pie.operator("transform.rotate", text="Y", icon="FILE_REFRESH")
        prop.constraint_axis = (False, True, False)
        prop.value = 1.5708
        prop.constraint_orientation = 'GLOBAL'
        # topright
        prop = pie.operator("transform.rotate", text="Y", icon="FILE_REFRESH")
        prop.constraint_axis = (False, True, False)
        prop.value = -1.5708
        prop.constraint_orientation = 'GLOBAL'

        
        
        split = pie.split()
        split = pie.split()
        col = split.column(align=True)
		
        row = col.row(align=True)
        row.scale_y=1.5
        row.operator("transform.resize", text="Flatten X", icon="ALIGN").value = (0, 1, 1)
        row = col.row(align=True)
        row.scale_y=1.5
        row.operator("transform.resize", text="Flatten Y", icon="ALIGN").value = (1, 0, 1)
        row = col.row(align=True)
        row.scale_y=1.5
        row.operator("transform.resize", text="Flatten Z", icon="ALIGN").value = (1, 1, 0)


def register():
    bpy.utils.register_class(VIEW3D_PIE_Rotate_90)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PIE_Rotate_90)

if __name__ == "__main__":
    register()
