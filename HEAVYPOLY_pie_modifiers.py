bl_info = {
    "name": "Pie Modifiers",
    "description": "Modifiers",
#    "author": "Vaughan Ling",
#    "version": (0, 1, 0),
    "blender": (2, 79, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
    }

import bpy
from bpy.types import Menu

class Bevel_Angle(bpy.types.Operator):
    bl_idname = "view3d.bevel_angle"        # unique identifier for buttons and menu items to reference.
    bl_label = ""         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):
        sel = bpy.context.selected_objects
        base = bpy.context.active_object

        for ob in sel:
            Bev = ob.modifiers.new("BevelAngle_" + ob.name, "BEVEL")
            Bev.angle_limit = 0.872665
            Bev.use_clamp_overlap = False
            Bev.limit_method = 'ANGLE'
            Bev.width = 0.005
        return {'FINISHED'}


class VIEW3D_PIE_MODIFIERS(Menu):
    bl_idname = "pie.modifiers"
    bl_label = "Modifiers"

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()
        # left
        # right
        pie.operator("object.modifier_add", text="Solidify").type = 'SOLIDIFY'
        # bottom
        pie.operator("object.modifier_add", text="Shrinkwrap").type = 'SHRINKWRAP'
        # top
        # topleft
        pie.operator("view3d.bevel_angle", text="Bevel")
        # topright
        pie.operator("object.modifier_add", text="Array").type = 'ARRAY'
        # bottomleft
        # bottomright


def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
