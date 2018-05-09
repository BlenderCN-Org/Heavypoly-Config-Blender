bl_info = {
    "name": "Heavypoly Operators",
    "description": "Operators that make for smooth blending",
    "author": "Vaughan Ling",
    "version": (0, 1, 0),
    "blender": (2, 78, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Operators"
    }

import bpy
from bpy.types import Menu
from bpy.types import Operator
from bpy.props import BoolProperty


class PushAndSlide(bpy.types.Operator):
    bl_idname = "mesh.push_and_slide"        # unique identifier for buttons and menu items to reference.
    bl_label = "Push And Slide"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (True, False, False):
            bpy.ops.transform.vert_slide('INVOKE_DEFAULT', mirror=False, correct_uv=True)
        elif tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True):
            bpy.ops.transform.shrink_fatten('INVOKE_DEFAULT', use_even_offset=True, mirror=False)
        else:
            bpy.ops.transform.edge_slide('INVOKE_DEFAULT', mirror=False, correct_uv=True)
        return {'FINISHED'}


class VIEW3D_OT_edit_mesh_extrude_move(Operator):
    """Extrude and move along normals"""
    bl_label = "Extrude and Move on Normals"
    bl_idname = "view3d.extrude_normal"

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.mode == 'EDIT')

    @staticmethod
    def extrude_region(context, use_vert_normals):
        mesh = context.object.data

        totface = mesh.total_face_sel
        totedge = mesh.total_edge_sel
        #~ totvert = mesh.total_vert_sel

        if totface >= 1:
            bpy.ops.mesh.extrude_region_shrink_fatten('INVOKE_REGION_WIN',
                        TRANSFORM_OT_shrink_fatten={"use_even_offset":True})

        else:
            bpy.ops.mesh.extrude_region_move('INVOKE_REGION_WIN',
                    TRANSFORM_OT_translate={
                        "constraint_orientation": 'NORMAL',
                        # not a popular choice, too restrictive for retopo.
                        #~ "constraint_axis": (True, True, False)})
                        "constraint_axis": (False, False, False)})

        # ignore return from operators above because they are 'RUNNING_MODAL',
        # and cause this one not to be freed. [#24671]
        return {'FINISHED'}

    def execute(self, context):
        return VIEW3D_OT_edit_mesh_extrude_move.extrude_region(context, False)

    def invoke(self, context, event):
        return self.execute(context)
        
class SmartBevel(bpy.types.Operator):
    bl_idname = "mesh.smart_bevel"        # unique identifier for buttons and menu items to reference.
    bl_label = "Smart Bevel"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (True, False, False):
            bpy.ops.mesh.bevel('INVOKE_DEFAULT',vertex_only=True)
        elif tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True):
            bpy.ops.mesh.region_to_loop()
            bpy.ops.mesh.bevel('INVOKE_DEFAULT',vertex_only=False)
        else:
            bpy.ops.mesh.bevel('INVOKE_DEFAULT',vertex_only=False)
        return {'FINISHED'}


class SeparateAndSelect(bpy.types.Operator):
    bl_idname = "mesh.separate_and_select"        # unique identifier for buttons and menu items to reference.
    bl_label = "Separate and Select"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
    def execute(self, context):

        base = bpy.context.active_object
        bpy.ops.mesh.separate(type='SELECTED')
        bpy.ops.object.editmode_toggle()
        base.select = False
        selected = bpy.context.selected_objects
        for sel in selected:
            bpy.context.scene.objects.active = sel
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        return {'FINISHED'}

class SmartShadeSmooth(bpy.types.Operator):
    bl_idname = "view3d.smart_shade_smooth_toggle"        # unique identifier for buttons and menu items to reference.
    bl_label = "Smart Shade Smooth"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        if context.active_object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            bpy.ops.object.shade_smooth()
            bpy.context.object.data.use_auto_smooth = True
            bpy.context.object.data.auto_smooth_angle = 0.436332
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        else:
            bpy.ops.object.shade_smooth()
            bpy.context.object.data.use_auto_smooth = True
            bpy.context.object.data.auto_smooth_angle = 0.436332
        return {'FINISHED'}

class toggle_render_material(bpy.types.Operator):
    bl_idname = "view3d.toggle_render_material"        # unique identifier for buttons and menu items to reference.
    bl_label = ""         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        if bpy.context.space_data.viewport_shade != 'MATERIAL':
            bpy.context.space_data.viewport_shade = 'MATERIAL'
        elif bpy.context.space_data.viewport_shade == 'MATERIAL':
            bpy.context.space_data.viewport_shade = 'RENDERED'
        return {'FINISHED'}


class Smart_Delete(bpy.types.Operator):
    bl_idname = "view3d.smart_delete"        # unique identifier for buttons and menu items to reference.
    bl_label = ""         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        obj = context.object
        objType = getattr(obj, 'type', '')
        act = bpy.context.active_object
        if not act:
            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o
                act = bpy.context.active_object
        actname = act.name
        if objType == 'CURVE':
            if context.active_object.mode == 'OBJECT':
                bpy.ops.object.delete(use_global=False)
            else:
                bpy.ops.curve.delete(type='VERT')
        elif 'Bool_Cutter' in act.name and context.active_object.mode == 'OBJECT':
            bpy.ops.object.delete(use_global=False)
            bpy.ops.object.select_all(action='SELECT')
            for o in bpy.context.selected_objects:
                bpy.context.scene.objects.active = o
                bpy.ops.object.modifier_remove(modifier=actname)
            bpy.ops.object.select_all(action='DESELECT')
        else:
            if context.active_object.mode == 'OBJECT':
                bpy.ops.object.delete(use_global=False)
            elif tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True):
                bpy.ops.mesh.delete(type='FACE')
            else:
                bpy.ops.mesh.delete(type='VERT')
        return {'FINISHED'}

class Subdivision_Toggle(bpy.types.Operator):
    bl_idname = "view3d.subdivision_toggle"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):

        for o in bpy.context.selected_objects:
            bpy.context.scene.objects.active = o
            if 0 < len([m for m in bpy.context.object.modifiers if m.type == "SUBSURF"]):
                if bpy.context.object.modifiers["Subsurf_Base"].levels == 0:
                    bpy.context.object.modifiers["Subsurf_Base"].render_levels = 3
                    bpy.context.object.modifiers["Subsurf_Base"].levels = 3
                else:
                    bpy.context.object.modifiers["Subsurf_Base"].render_levels = 0
                    bpy.context.object.modifiers["Subsurf_Base"].levels = 0

            else:
                o.modifiers.new("Subsurf_Base", "SUBSURF")
                bpy.context.object.modifiers["Subsurf_Base"].name = "Subsurf_Base"
                bpy.context.object.modifiers["Subsurf_Base"].render_levels = 3
                bpy.context.object.modifiers["Subsurf_Base"].levels = 3
                bpy.context.object.modifiers["Subsurf_Base"].show_only_control_edges = True
                bpy.context.object.modifiers["Subsurf_Base"].show_on_cage = True
                bpy.context.object.modifiers["Subsurf_Base"].use_opensubdiv = True

        return {'FINISHED'}

class SaveWithoutPrompt(bpy.types.Operator):
    bl_idname = "wm.save_without_prompt"
    bl_label = "Save without prompt"

    def execute(self, context):
        bpy.ops.wm.save_mainfile()
        return {'FINISHED'}
class RevertWithoutPrompt(bpy.types.Operator):
    bl_idname = "wm.revert_without_prompt"
    bl_label = "Revert without prompt"

    def execute(self, context):
        bpy.ops.wm.revert_mainfile()
        return {'FINISHED'}
class DeleteWithoutPrompt(bpy.types.Operator):
    bl_idname = "wm.delete_without_prompt"
    bl_label = "Delete without prompt"

    def execute(self, context):
        bpy.ops.object.delete()
        return {'FINISHED'}

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
