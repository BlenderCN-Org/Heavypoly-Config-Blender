bl_info = {
    "name": "Pie Shading",
    "description": "Shading Modes",
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

class VIEW3D_PIE_SHADING(Menu):
    bl_idname = "pie.shading"
    bl_label = "Shading"

    def draw(self, context):

        layout = self.layout
        view = context.space_data
        obj = context.active_object
        pie = layout.menu_pie()

        # Left
        prop = pie.operator("wm.context_set_enum", text="Material")
        prop.data_path = "space_data.viewport_shade"
        prop.value = 'MATERIAL'

        prop = pie.operator("wm.context_set_enum", text="Rendered")
        prop.data_path = "space_data.viewport_shade"
        prop.value = 'RENDERED'


        # # Right

        # Bottom
        prop = pie.operator("wm.context_toggle_enum", text="Wireframe", icon='WIRE')
        prop.data_path = "space_data.viewport_shade"
        prop.value_1 = 'SOLID'
        prop.value_2 = 'WIREFRAME'
        # Top
        prop = pie.operator("wm.context_toggle", text="Clean Mode")
        prop.data_path = "space_data.show_only_render"

        # Top Left
        pie.operator("view3d.smart_shade_smooth_toggle", text="Shade Smooth")
        #pie.operator("view3d.boolean_toggle_cutters", text="Toggle Cutters")
        # Top Right
        
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.scale_y=1.5
        row.operator('render.render', text='Render Animation').animation=True
        row = col.row(align=True)
        row.scale_y=1.5
        row.operator('render.render', text='Render Image')

        # Bottom Left


        pie.operator("view3d.toggle_background_wire", text="Toggle BG Wire", icon='WIRE')
        # Bottom Right
        pie.operator("view3d.toggle_background_hide", text="Toggle BG Hide", icon='RESTRICT_VIEW_OFF')
        


def register():
    bpy.utils.register_class(VIEW3D_PIE_SHADING)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PIE_SHADING)


if __name__ == "__main__":
    register()
