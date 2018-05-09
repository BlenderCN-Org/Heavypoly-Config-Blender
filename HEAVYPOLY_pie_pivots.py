bl_info = {
    "name": "Pie Pivots",
    "description": "Pivots Modes",
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

# Pivots Pie
class VIEW3D_PIE_Pivots(Menu):
    bl_idname = "pie.pivots"
    bl_label = "Pivots"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        prop = pie.operator("wm.context_set_enum", text="Pivot Active Element", icon='OUTLINER_OB_EMPTY')
        prop.data_path = "space_data.pivot_point"
        prop.value = 'ACTIVE_ELEMENT'

#         prop = pie.operator("wm.context_set_enum", text="Pivot Bounding Box", icon='OUTLINER_OB_EMPTY')
#         prop.data_path = "space_data.pivot_point"
#         prop.value = 'BOUNDING_BOX_CENTER'

        prop = pie.operator("wm.context_set_enum", text="Pivot Individuals", icon='OUTLINER_OB_EMPTY')
        prop.data_path = "space_data.pivot_point"
        prop.value = 'INDIVIDUAL_ORIGINS'

        prop = pie.operator("wm.context_set_enum", text="Pivot Median", icon='OUTLINER_OB_EMPTY')
        prop.data_path = "space_data.pivot_point"
        prop.value = 'MEDIAN_POINT'

        prop = pie.operator("wm.context_set_enum", text="Pivot Cursor", icon='OUTLINER_OB_EMPTY')
        prop.data_path = "space_data.pivot_point"
        prop.value = 'CURSOR'



class SmartPivotNormal(bpy.types.Operator):
    bl_idname = "view3d.smart_pivot_normal"        # unique identifier for buttons and menu items to reference.
    bl_label = "Smart Pivot Normal"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def invoke(self, context, event):
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'
        bpy.context.space_data.transform_orientation = 'NORMAL'
        return {'FINISHED'}



def register():
    bpy.utils.register_class(VIEW3D_PIE_Pivots)
    bpy.utils.register_class(SmartPivotNormal)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PIE_Pivots)
    bpy.utils.unregister_class(SmartPivotNormal)

if __name__ == "__main__":
    register()
