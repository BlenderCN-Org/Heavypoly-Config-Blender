bl_info = {
    "name": "Pie View",
    "description": "View Modes",
#    "author": "Vaughan Ling",
#    "version": (0, 1, 0),
    "blender": (2, 78, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
    }


import bpy
from bpy.types import Menu

# View Pie with left meaning left of model vs Blender defaults

class VIEW3D_PIE_View(Menu):
    bl_idname = "pie.view"
    bl_label = "View"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        # left
        pie.operator("VIEW3D_OT_viewnumpad", text="Left").type = "LEFT"
        # right
        pie.operator("VIEW3D_OT_viewnumpad", text="Right").type = "RIGHT"
        # bottom
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.scale_y=1.5
        row.operator("VIEW3D_OT_viewnumpad", text="Camera").type = "CAMERA"
        col.separator()
        row = col.row(align=True)
        row.scale_y=1.5
        row.operator("view3d.create_camera_at_view", text="Create Camera At View")
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("wm.context_toggle", text="Lock Camera To View")
        prop.data_path = "space_data.lock_camera"
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("view3d.object_as_camera", text="Set as Render Camera")

        # top
        pie.operator("VIEW3D_OT_viewnumpad", text="Top").type = "TOP"
        # topleft
        pie.operator("VIEW3D_OT_viewnumpad", text="Back").type = "BACK"
        # topright
        pie.operator("VIEW3D_OT_viewnumpad", text="Front").type = "FRONT"
        # bottomleft

        # bottomright
        pie.operator("VIEW3D_OT_viewnumpad", text="Bottom").type = "BOTTOM"

        #pie.operator("view3d.localview", text="Isolate")

        props = pie.operator("view3d.viewnumpad", text="Align Active")
        props.align_active = True
        props.type = 'TOP'




class Create_Camera_At_View(bpy.types.Operator):
    bl_idname = "view3d.create_camera_at_view"        # unique identifier for buttons and menu items to reference.
    bl_label = ""         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        if context.active_object.mode == 'EDIT':
            active_object = bpy.context.active_object
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.camera_add()
            bpy.context.object.data.passepartout_alpha = 1
            active_cam = bpy.context.active_object
            bpy.context.scene.camera = active_cam 
            bpy.ops.view3d.camera_to_view()
            bpy.context.scene.objects.active = active_object
            bpy.ops.object.editmode_toggle()
        else:
            bpy.ops.object.camera_add()
            bpy.context.object.data.passepartout_alpha = 1
            active_cam = bpy.context.active_object
            bpy.context.scene.camera = active_cam 
            bpy.ops.view3d.camera_to_view()



        return {'FINISHED'}

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
