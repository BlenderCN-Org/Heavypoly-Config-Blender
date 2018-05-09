bl_info = {
    "name": "Pie Selection",
    "description": "Select Modes",
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

# Select Pie
class VIEW3D_PIE_SELECT(Menu):
    bl_idname = "pie.select"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        # left
        pie.operator("mesh.loop_to_region", text="Fill Border")
        # right
        # if context.mode == 'OBJECT':
        #     pie.operator("object.mode_set", text="Vertex Paint", icon='OBJECT_DATAMODE').mode='VERTEX_PAINT'

        pie.operator("mesh.region_to_loop", text="Border", icon='LOOPSEL')
        # bottom
        pie.operator("object.mode_set", text="Object", icon='OBJECT_DATAMODE').mode='OBJECT'
        # top
        pie.operator("object.selectsmartedge", text="Edge", icon='EDGESEL')
        # topleft
        pie.operator("object.selectsmartvert", text="Vert", icon='VERTEXSEL')
        # topright
        pie.operator("object.selectsmartface", text="Face", icon='FACESEL')
        # bottomleft
        if context.mode == 'OBJECT':
            pie.operator("object.select_grouped", text="Similar")
        else:
            pie.operator("mesh.select_similar", text="Similar")
        # bottomright
        pie.operator("mesh.faces_select_linked_flat", text="Select Flat Linked").sharpness=0.436332






class SelectSmartSimilar(bpy.types.Operator):
    """SelectSmartVert"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "view3d.selectsmartsimilar"        # unique identifier for buttons and menu items to reference.
    bl_label = "Select Smart Similar"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        if bpy.context.mode=='OBJECT':
            bpy.ops.object.select_grouped()
        else:
            bpy.ops.mesh.select_similar()



class SelectSmartAll(bpy.types.Operator):
    """SelectSmartVert"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.selectsmartall"        # unique identifier for buttons and menu items to reference.
    bl_label = "Select Smart All"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        if bpy.context.mode=='OBJECT':
            bpy.ops.object.select_all(action='TOGGLE')
        else:
            bpy.ops.mesh.select_all(action='TOGGLE')
        return {'FINISHED'}

class SelectSmartLinkedAndLoop(bpy.types.Operator):
    """SelectSmartVert"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "mesh.selectsmartlinkedandloop"        # unique identifier for buttons and menu items to reference.
    bl_label = "Select Smart Linked And Loop"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, True, False):
            bpy.ops.mesh.loop_multi_select()
        else:
            bpy.ops.mesh.select_linked(delimit={'SEAM'})
        return {'FINISHED'}

class SelectSmartVert(bpy.types.Operator):
    """SelectSmartVert"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.selectsmartvert"        # unique identifier for buttons and menu items to reference.
    bl_label = "Select Smart Vert"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        if bpy.context.mode == 'OBJECT' and bpy.context.object.type == "MESH":
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        elif bpy.context.mode == 'EDIT_MESH':
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        else:
            bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}


class SelectSmartEdge(bpy.types.Operator):
    """SelectSmartEdge"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.selectsmartedge"        # unique identifier for buttons and menu items to reference.
    bl_label = "Select Smart Edge"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        if bpy.context.mode == 'OBJECT' and bpy.context.object.type == "MESH":
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        elif bpy.context.mode == 'EDIT_MESH':
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        else:
            bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

class SelectSmartFace(bpy.types.Operator):
    """SelectSmartFace"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.selectsmartface"        # unique identifier for buttons and menu items to reference.
    bl_label = "Select Smart Face"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        if bpy.context.mode == 'OBJECT' and bpy.context.object.type == "MESH":
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        elif bpy.context.mode == 'EDIT_MESH':
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        else:
            bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

class BorderSelectThrough(bpy.types.Operator):
    """BorderSelectThrough"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "mesh.borderselectthrough"        # unique identifier for buttons and menu items to reference.
    bl_label = "Border Select Through"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        #
        # bpy.context.space_data.use_occlude_geometry = True
        # VIEW3D_OT_select_lasso
        bpy.ops.view3d.select_border
        # bpy.context.space_data.use_occlude_geometry = False
        return {'FINISHED'}



def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
