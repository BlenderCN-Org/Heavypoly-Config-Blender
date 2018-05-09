Hbl_info = {
    "name": "Pie Apply",
    "description": "Apply Modes",
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

# Apply Pie
class VIEW3D_PIE_Apply(Menu):
    bl_idname = "pie.apply"
    bl_label = "Pi Apply"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        # left
        prop = pie.operator("object.transform_apply", text="Reset Location")
        prop.location = True
        prop.rotation = 0
        prop.scale = 0
        # right
        prop = pie.operator("object.transform_apply", text="Reset Rotation")
        prop.location = 0
        prop.rotation = 1
        prop.scale = 0
        # bottom
        # top
        prop = pie.operator("object.transform_apply", text="Reset All")
        prop.location = True
        prop.rotation = True
        prop.scale = True
        #
        prop = pie.operator("object.transform_apply", text="Reset Scale")
        prop.location = 0
        prop.rotation = 0
        prop.scale = 1

        # topleft
        # topright
        # bottomleft

        # bottomright


def register():
    bpy.utils.register_class(VIEW3D_PIE_Apply)
    bpy.utils.register_class(ApplySmartVert)
    bpy.utils.register_class(ApplySmartEdge)
    bpy.utils.register_class(ApplySmartFace)
    bpy.utils.register_class(ApplySmartAll)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PIE_Apply)
    bpy.utils.unregister_class(ApplySmartVert)
    bpy.utils.unregister_class(ApplySmartEdge)
    bpy.utils.unregister_class(ApplySmartFace)
    bpy.utils.unregister_class(ApplySmartAll)

if __name__ == "__main__":
    register()
