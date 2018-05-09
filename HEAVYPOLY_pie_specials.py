bl_info = {
    "name": "Pie Specials",
    "description": "Specials Modes",
    "author": "Vaughan Ling",
    "version": (0, 1, 0),
    "blender": (2, 78, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
    }

import bpy
from bpy.types import Menu

# Specials Pie
class VIEW3D_PIE_SPECIALS(Menu):
    bl_idname = "pie.specials"
    bl_label = "Specials"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
#Left
        prop=pie.operator("mesh.spin", text="Duplicate Radial")
        prop.dupli=True
        prop.angle=6.28319

#Right

#Bottom
        pie.operator("transform.tosphere", text="Make Round").value=1
#Top
        pie.operator("object.quickpipe", text="Quick Pipe")
        pie.operator("transform.vertex_random", text="Randomize")

#TopLeft
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.scale_y=1.5
        row.operator("mesh.subdivide", text="Subdivide Smooth").smoothness=1
        row = col.row(align=True)
        row.scale_y=1.5
        row.operator("mesh.subdivide", text="Subdivide Flat").smoothness=0
        
        
        
#TopRight
        pie.operator("mesh.remove_doubles", text="Remove Doubles")
        pie.operator("mesh.bridge_edge_loops", text = "Bridge Smooth").number_cuts=12
#BottomLeft
        split = pie.split()

#BottomRight


def register():
    bpy.utils.register_class(VIEW3D_PIE_SPECIALS)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PIE_SPECIALS)


if __name__ == "__main__":
    register()
