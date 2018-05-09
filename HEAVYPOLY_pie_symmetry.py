bl_info = {
    "name": "Pie Symmetry",
    "description": "Symmetry and Mirroring",
    "author": "Vaughan Ling",
    "blender": (2, 78, 0),
    "category": "Pie Menu"
    }

import bpy
from bpy.types import Menu

# symmetrize, mirror and mirror modifier

class VIEW3D_PIE_SYMMETRY(Menu):
    bl_idname = "pie.symmetry"
    bl_label = "Symmetry"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        # left
        pie.operator("mesh.symmetrize", text="X").direction = 'POSITIVE_X'
        # right
        pie.operator("mesh.symmetrize", text="X").direction = 'NEGATIVE_X'
        # bottom
        pie.operator("mesh.symmetrize", text="Z").direction = 'POSITIVE_Z'
        # top
        pie.operator("mesh.symmetrize", text="Z").direction = 'NEGATIVE_Z'
        # topleft
        pie.operator("mesh.symmetrize", text="Y").direction = 'NEGATIVE_Y'
        # topright
        pie.operator("view3d.mirror_toggle", text="Live Mirror")
        #pie.operator("object.modifier_add", text="Mirror Modifier").type = 'MIRROR'
        # bottomleft
        pie.operator("view3d.mirror_clip_toggle", text="Toggle Center Clip")
        # bottomright
        pie.operator("mesh.symmetrize", text="Y").direction = 'POSITIVE_Y'

class MIRROR_CLIP_Toggle(bpy.types.Operator):
    bl_idname = "view3d.mirror_clip_toggle"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):

        if bpy.context.object.modifiers["Mirror Base"].use_clip == False:
            bpy.context.object.modifiers["Mirror Base"].use_clip = True
        else:
            bpy.context.object.modifiers["Mirror Base"].use_clip = False
        return {'FINISHED'}

class MIRROR_TOGGLE(bpy.types.Operator):
    bl_idname = "view3d.mirror_toggle"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):

        for o in bpy.context.selected_objects:
            bpy.context.scene.objects.active = o
            if 0 < len([m for m in bpy.context.object.modifiers if m.type == "MIRROR"]):
                bpy.ops.object.modifier_remove(modifier="Mirror Base")


            else:
                o.modifiers.new("Mirror Base", "MIRROR")
                #bpy.context.object.modifiers["Subsurf_Base"].name = "Subsurf_Base"
            return {'FINISHED'}

def register():
    bpy.utils.register_module(__name__)
def unregister():
    bpy.utils.unregister_module(__name__)
if __name__ == "__main__":
    register()
