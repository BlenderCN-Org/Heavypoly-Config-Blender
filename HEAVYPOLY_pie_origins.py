bl_info = {
    "name": "Pie Origins",
    "description": "Origins Modes",
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

# Origins Pie
# class VIEW3D_PIE_Origins(Menu):
#     bl_idname = "pie.origins"
#     bl_label = "Origins"
#
#     def draw(self, context):
#         layout = self.layout
#
#         pie = layout.menu_pie()
#
#
#
#         pie.operator("view3d.smart_origin_to_000", text="Origin Reset")
#
#         pie.operator("view3d.smart_origin_to_selected", text="Origin to Selected")
#
#         pie.operator("view3d.smart_move_to_000", text="Move to 0,0,0")
#
#         pie.operator("view3d.snap_selected_to_cursor", text="Move to Cursor").use_offset=True

class SmartSnapCursor(bpy.types.Operator):
    bl_idname = "view3d.smart_snap_cursor"        # unique identifier for buttons and menu items to reference.
    bl_label = ""         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
    def invoke(self, context, event):

        if context.active_object.mode == 'EDIT':
            if  context.object.data.total_vert_sel > 0:
                bpy.ops.view3d.snap_cursor_to_selected()
                bpy.context.space_data.pivot_point = 'CURSOR'
            else:
                bpy.ops.view3d.snap_cursor_to_center()
                bpy.context.space_data.pivot_point = 'CURSOR'

        elif len(bpy.context.selected_objects) > 0:
            bpy.ops.view3d.snap_cursor_to_selected()
            bpy.context.space_data.pivot_point = 'CURSOR'
        else:
            bpy.ops.view3d.snap_cursor_to_center()
            bpy.context.space_data.pivot_point = 'CURSOR'

        return {'FINISHED'}

class SmartSnapOrigin(bpy.types.Operator):
    bl_idname = "view3d.smart_snap_origin"        # unique identifier for buttons and menu items to reference.
    bl_label = ""         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
    def invoke(self, context, event):
        if context.active_object.mode == 'EDIT':
            if context.object.data.total_vert_sel > 0:
                bpy.ops.view3d.snap_cursor_to_selected()
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.origin_set(type = 'ORIGIN_CURSOR')
                bpy.ops.object.mode_set(mode='EDIT')
            else:
                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        elif len(bpy.context.selected_objects) > 0:
            bpy.ops.object.origin_set(type = 'ORIGIN_GEOMETRY')
        else:
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'


        return {'FINISHED'}

#
# class SmartSnapCursorToSelected(bpy.types.Operator):
#     bl_idname = "view3d.smart_snap_cursor_to_selected"        # unique identifier for buttons and menu items to reference.
#     bl_label = ""         # display name in the interface.
#     bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
#
#     def invoke(self, context, event):
#         bpy.ops.view3d.snap_cursor_to_selected()
#         bpy.context.space_data.pivot_point = 'CURSOR'
#         return {'FINISHED'}
#
# class SmartSnapCursorTo000(bpy.types.Operator):
#     bl_idname = "view3d.smart_snap_cursor_to_000"        # unique identifier for buttons and menu items to reference.
#     bl_label = ""         # display name in the interface.
#     bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
#
#     def invoke(self, context, event):
#         bpy.ops.view3d.snap_cursor_to_center()
#         bpy.context.space_data.pivot_point = 'CURSOR'
#         return {'FINISHED'}
#
#
# class SmartMoveTo000(bpy.types.Operator):
#     bl_idname = "view3d.smart_move_to_000"        # unique identifier for buttons and menu items to reference.
#     bl_label = ""         # display name in the interface.
#     bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
#
#     def invoke(self, context, event):
#         bpy.ops.view3d.snap_cursor_to_center()
#         bpy.ops.view3d.snap_selected_to_cursor()
#         return {'FINISHED'}
#
# class SmartOriginTo000(bpy.types.Operator):
#     bl_idname = "view3d.smart_origin_to_000"        # unique identifier for buttons and menu items to reference.
#     bl_label = "Smart Origin to 000"         # display name in the interface.
#     bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
#
#     def invoke(self, context, event):
#         if context.active_object.mode == 'EDIT':
#             bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
#             bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
#             bpy.ops.object.mode_set(mode='EDIT', toggle=False)
#         else:
#             bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
#         return {'FINISHED'}
#
#
# class SmartOriginToCursor(bpy.types.Operator):
#     bl_idname = "view3d.smart_origin_to_cursor"        # unique identifier for buttons and menu items to reference.
#     bl_label = "Smart Origin to Cursor"         # display name in the interface.
#     bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
#
#     def invoke(self, context, event):
#         if context.active_object.mode == 'EDIT':
#             bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
#             bpy.ops.object.origin_set(type = 'ORIGIN_CURSOR')
#             bpy.ops.object.mode_set(mode='EDIT', toggle=False)
#         else:
#             bpy.ops.object.origin_set(type = 'ORIGIN_CURSOR')
#         return {'FINISHED'}
#
# class SmartOriginToSelected(bpy.types.Operator):
#     bl_idname = "view3d.smart_origin_to_selected"        # unique identifier for buttons and menu items to reference.
#     bl_label = "Smart Origin to selected"         # display name in the interface.
#     bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
#
#     def invoke(self, context, event):
#         if context.active_object.mode == 'EDIT':
#             bpy.ops.view3d.snap_cursor_to_selected()
#             bpy.ops.object.mode_set(mode='OBJECT')
#             bpy.ops.object.origin_set(type = 'ORIGIN_CURSOR')
#             bpy.ops.object.mode_set(mode='EDIT')
#         else:
#             bpy.ops.object.origin_set(type = 'ORIGIN_GEOMETRY')
#         return {'FINISHED'}



def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
