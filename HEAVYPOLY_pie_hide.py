bl_info = {
    "name": "Pie hide",
    "description": "hide Modes",
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
import bmesh


class VIEW3D_PIE_hide(Menu):
    bl_idname = "pie.hide"
    bl_label = "hide"

    def draw(self, context):

        layout = self.layout
        view = context.space_data
        obj = context.active_object
        pie = layout.menu_pie()

        # Object Hide
        # Left
        pie.operator("view3d.smart_unhide", text="UnHide")
        # Right
        pie.operator("view3d.smart_hide", text="Hide")
        # Bottom
        pie.operator("view3d.smart_hideunselected", text="Hide Unselected")
        # Top
        pie.operator("view3d.localview", text="Isolate")
        # Top Left
        pie.operator("view3d.toggle_background_wire", text="Toggle Background Wire")
        # Top Right
        pie.operator("view3d.toggle_background_hide", text="Toggle Background Hide")
        # Bottom Left
        pie.operator("view3d.boolean_toggle_cutters", text="Toggle Cutters")
        # Bottom Right
        pie.split


class Smart_Hide(bpy.types.Operator):
    bl_idname = "view3d.smart_hide"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.mode == 'EDIT_MESH':
            bpy.ops.mesh.hide(unselected=False)
        else:
            bpy.ops.object.hide_view_set(unselected=False)
        return {'FINISHED'}

class Smart_HideUnselected(bpy.types.Operator):
    bl_idname = "view3d.smart_hideunselected"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.mode == 'EDIT_MESH':
            bpy.ops.mesh.hide(unselected=True)
        else:
            bpy.ops.object.hide_view_set(unselected=True)
        return {'FINISHED'}

class Smart_UnHide(bpy.types.Operator):
    bl_idname = "view3d.smart_unhide"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.mode == 'EDIT_MESH':
            obj = bpy.context.object
            mesh = obj.data
            obj.update_from_editmode()

            selected_polygons = [p for p in mesh.polygons if p.select]
            selected_edges = [e for e in mesh.vertices if e.select]
            selected_vertices = [v for v in mesh.vertices if v.select]
            if len(selected_vertices) == 0:
                bpy.ops.mesh.reveal()
            else:
                bpy.ops.mesh.select_all(action='INVERT')
                bpy.ops.mesh.reveal()
                bpy.ops.mesh.select_all(action='INVERT')
        else:
            bg = bpy.context.selected_objects
            if len(bg) != 0: #If an object is selected
                base = bpy.context.selected_objects
                bpy.ops.object.hide_view_clear()
                sel = bpy.context.selected_objects
                list = set(sel) - set(base)
                for unhidden in list:
                    unhidden.select = False

            else:
                bpy.ops.object.hide_view_clear()
        return {'FINISHED'}
class Toggle_Background_Hide(bpy.types.Operator):
    bl_idname = "view3d.toggle_background_hide"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}
        # for ob in bpy.context.scene.objects:
            # if ob.type == 'MESH' and ob.name.startswith("Bool_Cutter"):
            #     if ob.hide == False:
            #         ob.hide = True
            #     elif ob.hide == True:
            #         ob.hide = False
    def execute(self, context):
        if bpy.context.mode == 'EDIT_MESH' and bpy.context.object.type == "MESH":
            bpy.ops.object.editmode_toggle()
            active = bpy.context.active_object
            selected = bpy.context.selected_objects
            bpy.ops.object.select_all(action='INVERT')
            # if selected.type == 'MESH' and selected.name.startswith("Bool_Cutter"):
            #     selected.select = False
            bg = bpy.context.selected_objects
            if len(bg) != 0: #If BG is visible
                for o in bg:  #Hide BG
                    o.hide = True
                for o in selected:
                    o.select = True

            else:     #Else BG is hidden so unhide it
                bpy.ops.object.hide_view_clear()
                selectednew = bpy.context.selected_objects
                for o in selectednew:
                    o.select = False
                for o in selected:
                    o.select = True
                active.select=True
            bpy.ops.object.editmode_toggle()
        else: #Object Mode
            active = bpy.context.active_object
            selected = bpy.context.selected_objects
            bpy.ops.object.select_all(action='INVERT')

            bg = bpy.context.selected_objects
            if len(bg) != 0: #If BG is visible
                for o in bg:  #Hide BG
                    o.hide = True
                for o in selected:
                    o.select = True

            else:     #Else BG is hidden so unhide it
                bpy.ops.object.hide_view_clear()
                selectednew = bpy.context.selected_objects
                for o in selectednew:
                    if o.name.startswith("Bool_Cutter"): #Hide Cutters
                        o.hide = True
                        o.select = False
                    o.select = False
                for o in selected: #Select Originals
                    o.select = True
                active.select=True
        return {'FINISHED'}

class Toggle_Background_Wire(bpy.types.Operator):
    bl_idname = "view3d.toggle_background_wire"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.mode == 'EDIT_MESH' and bpy.context.object.type == "MESH":
            bpy.ops.object.editmode_toggle()
            active = bpy.context.active_object
            if active.draw_type == 'WIRE':
                bpy.ops.object.select_all(action='INVERT')
                selected = bpy.context.selected_objects
                for o in selected:
                    if o.draw_type == 'TEXTURED':
                        o.draw_type = 'WIRE'
                bpy.ops.object.select_all(action='INVERT')
                active.draw_type = 'TEXTURED'
                bpy.ops.object.editmode_toggle()
                return {'FINISHED'}

            bpy.ops.object.select_all(action='INVERT')
            selected = bpy.context.selected_objects
            if True in (o.draw_type == 'WIRE' for o in selected):
                for o in selected:
                    if o.draw_type == 'WIRE':
                        o.draw_type = 'TEXTURED'
            else:
                for o in selected:
                    if o.draw_type == 'TEXTURED':
                        o.draw_type = 'WIRE'
            bpy.ops.object.select_all(action='INVERT')
            bpy.ops.object.editmode_toggle()
        else:
            active = bpy.context.active_object
            if active.draw_type == 'WIRE':
                bpy.ops.object.select_all(action='INVERT')
                selected = bpy.context.selected_objects
                for o in selected:
                    if o.draw_type == 'TEXTURED':
                        o.draw_type = 'WIRE'
                bpy.ops.object.select_all(action='INVERT')
                active.draw_type = 'TEXTURED'
                return {'FINISHED'}

            bpy.ops.object.select_all(action='INVERT')
            selected = bpy.context.selected_objects
            if True in (o.draw_type == 'WIRE' for o in selected):
                for o in selected:
                    if o.draw_type == 'WIRE':
                        o.draw_type = 'TEXTURED'
            else:
                for o in selected:
                    if o.draw_type == 'TEXTURED':
                        o.draw_type = 'WIRE'
            bpy.ops.object.select_all(action='INVERT')

        return {'FINISHED'}

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()


        # split = pie.split()
        # col = split.column()
        # col.scale_y=1.5
        # col.scale_x=2
        # col.operator("mesh.hide", text="Hide")
        # col.operator("mesh.hide", text="Hide Unselected").unselected = True
        # col.operator("mesh.reveal", text="Unhide")
        # col = split.column()
        # col.scale_y=1.5
        # col.scale_x=2
        # col.operator("view3d.hide_object", text="Hide Object")
        # col.operator("view3d.hide_unselected_object", text="Hide Unselected Objects")
        # col.operator("view3d.unhide_object", text="Unhide Objects")


#
# class Unhide_Object(bpy.types.Operator):
#     bl_idname = "view3d.unhide_object"        # unique identifier for buttons and menu items to reference.
#     bl_label = ""         # display name in the interface.
#     bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
#
#     def execute(self, context):
#         selected = bpy.context.selected_objects
#         base = bpy.context.active_object
#         bpy.ops.object.hide_view_clear()
#         selectednew = bpy.context.selected_objects
#         if len(selected) > 0:
#             for x in selectednew:
#                 x.select = False
#             base.select = True
#
#         return {'FINISHED'}
#
#
# class Hide_Object(bpy.types.Operator):
#     bl_idname = "view3d.hide_object"        # unique identifier for buttons and menu items to reference.
#     bl_label = ""         # display name in the interface.
#     bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
#
#     def execute(self, context):
#         if bpy.context.mode == 'OBJECT':
#             bpy.ops.object.hide_view_set(unselected=False)
#         else:
#             bpy.ops.object.editmode_toggle()
#             bpy.ops.object.hide_view_set(unselected=False)
#             # bpy.ops.object.mode_set(mode='EDIT')
#         return {'FINISHED'}
#
# class Hide_Unselected_Object(bpy.types.Operator):
#     bl_idname = "view3d.hide_unselected_object"        # unique identifier for buttons and menu items to reference.
#     bl_label = ""         # display name in the interface.
#     bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
#
#     def execute(self, context):
#         if bpy.context.mode == 'OBJECT':
#             bpy.ops.object.hide_view_set(unselected=True)
#         else:
#             bpy.ops.object.editmode_toggle()
#             bpy.ops.object.hide_view_set(unselected=True)
#             bpy.ops.object.mode_set(mode='EDIT')
#         return {'FINISHED'}
