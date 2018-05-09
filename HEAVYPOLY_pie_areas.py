bl_info = {
    "name": "Pie Areas",
    "description": "Area Types",
    "author": "Vaughan Ling",
    "version": (0, 1, 0),
    "blender": (2, 78, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
    }

import bpy
from bpy.types import (
        Menu,
        Operator,
        )
import os

# save import export

class VIEW3D_PIE_Areas(Menu):
    bl_idname = "pie.areas"
    bl_label = "Areas"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()     
        # left
        pie.operator("wm.preview_render", text="Preview Render")

        # right
        pie.operator("wm.3dview", text="3D View")
        # bottom
        #block
        split = pie.split()
        col = split.column(align=True)
        
        row = col.row(align=True)
        row.scale_y=1.5       
        prop = row.operator("wm.context_set_enum", text="Properties")
        prop.data_path = "area.type"
        prop.value = 'PROPERTIES'
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("wm.context_set_enum", text="Timeline")
        prop.data_path = "area.type"
        prop.value = 'TIMELINE'
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("wm.context_set_enum", text="Text Editor")
        prop.data_path = "area.type"
        prop.value = 'TEXT_EDITOR'
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("wm.context_set_enum", text="Python Console")
        prop.data_path = "area.type"
        prop.value = 'CONSOLE'  
        row = col.row(align=True)
        row.scale_y=1.5        
        row.operator('wm.window_fullscreen_toggle', text='Fullscreen')
        # top
        pie.operator("screen.screen_full_area", text="Maximize")


        prop = pie.operator("wm.context_set_enum", text="Image Editor")
        prop.data_path = "area.type"
        prop.value = 'IMAGE_EDITOR'
        prop = pie.operator("wm.context_set_enum", text="Graph Editor")
        prop.data_path = "area.type"
        prop.value = 'GRAPH_EDITOR'
        prop = pie.operator("wm.context_set_enum", text="Node Editor")
        prop.data_path = "area.type"
        prop.value = 'NODE_EDITOR'        
        prop = pie.operator("wm.context_set_enum", text="Outliner")
        prop.data_path = "area.type"
        prop.value = 'OUTLINER'
        
        


class AreasPreviewRender(bpy.types.Operator):
    bl_idname = 'wm.preview_render'
    bl_label = 'Preview Render'
    def execute(self, context):
        bpy.ops.wm.context_set_enum(data_path='area.type', value='VIEW_3D')
        if bpy.ops.view3d.viewnumpad != 'CAMERA':
            bpy.ops.view3d.viewnumpad(type='CAMERA')
        bpy.ops.wm.context_set_enum(data_path='space_data.viewport_shade', value='RENDERED')
        bpy.context.space_data.show_only_render = True

        return {'FINISHED'}

class Areas3DView(bpy.types.Operator):
    bl_idname = 'wm.3dview'
    bl_label = '3D View, material'
    def execute(self, context):
        bpy.ops.wm.context_set_enum(data_path='area.type', value='VIEW_3D')
        bpy.ops.wm.context_set_enum(data_path='space_data.viewport_shade', value='MATERIAL')
        bpy.context.space_data.show_only_render = False
        return {'FINISHED'}


class TexturePaintToggle(bpy.types.Operator):
    bl_idname = 'wm.texture_paint_toggle'
    bl_label = 'Texture Paint Toggle'
    def execute(self, context):
        bpy.ops.object.mode_set(mode='TEXTURE_PAINT', toggle=False)  
        return {'FINISHED'}

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()