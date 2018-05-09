# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {
    "name": "Transforms Pie",
    "description": "",
    "author": ", Vaughan Ling",
    "version": (0, 1, 0),
    "blender": (2, 79, 0),
    "location": "3D View",
    "warning": "",
    "wiki_url": "",
    "category": "Transforms Pie"
    }

import bpy
from bpy.types import (
        Menu,
        Operator,
        )


class TransformMoveScale(Operator):
    bl_idname = "transform.manip_move_scale"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = " Transform Move And Scale"

    def execute(self, context):
        if context.space_data.show_manipulator == False:
            context.space_data.show_manipulator = True
            context.space_data.transform_manipulators = {'TRANSLATE', 'SCALE'}
        elif context.space_data.show_manipulator == True and context.space_data.transform_manipulators == {'TRANSLATE', 'SCALE'}:
            context.space_data.show_manipulator = False
        elif context.space_data.show_manipulator == True and context.space_data.transform_manipulators == {'ROTATE'}:
            context.space_data.transform_manipulators = {'TRANSLATE', 'SCALE'}
        return {'FINISHED'}

class TransformRotate(Operator):
    bl_idname = "transform.manip_rotate"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = " Transform Rotate"

    def execute(self, context):
        if context.space_data.show_manipulator == False:
            context.space_data.show_manipulator = True
            context.space_data.transform_manipulators = {'ROTATE'}
        elif context.space_data.show_manipulator == True and context.space_data.transform_manipulators == {'ROTATE'}:
            context.space_data.show_manipulator = False
        elif context.space_data.show_manipulator == True and context.space_data.transform_manipulators == {'TRANSLATE', 'SCALE'}:
            context.space_data.transform_manipulators = {'ROTATE'}
        return {'FINISHED'}


class ToggleTransform(Operator):
    bl_idname = "transform.toggle"
    bl_label = "Toggle Transform Type"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = " Toggle Transform Type"

    def execute(self, context):
      if context.space_data.show_manipulator == False:
        context.space_data.show_manipulator = True


      if context.space_data.transform_manipulators != {'TRANSLATE', 'SCALE'}:
        context.space_data.transform_manipulators = {'TRANSLATE', 'SCALE'}
      else:
         context.space_data.transform_manipulators = {'ROTATE'}
      return {'FINISHED'}


# class TogglePivot(Operator):
#     bl_idname = "pivot.toggle"
#     bl_label = "Toggle Pivot Type"
#     bl_options = {'REGISTER', 'UNDO'}
#     bl_description = " Toggle Pivot Type"

#     def execute(self, context):
#       if context.space_data.show_manipulator == False:
#         context.space_data.show_manipulator = True


#       if context.space_data.transform_manipulators != {'TRANSLATE', 'SCALE'}:
#         context.space_data.transform_manipulators = {'TRANSLATE', 'SCALE'}
#       else:
#          context.space_data.transform_manipulators = {'ROTATE'}
#       return {'FINISHED'}

#         prop = pie.operator("wm.context_set_enum", text="Pivot Active Element", icon='OUTLINER_OB_EMPTY')
#         prop.data_path = "space_data.pivot_point"
#         prop.value = 'ACTIVE_ELEMENT'
#         prop = pie.operator("wm.context_set_enum", text="Pivot Median", icon='OUTLINER_OB_EMPTY')
#         prop.data_path = "space_data.pivot_point"
#         prop.value = 'MEDIAN_POINT'

class PieTransforms(Menu):
    bl_idname = "pie.transforms"
    bl_label = "Transforms Pie"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # 4 - LEFT
        prop = pie.operator("wm.context_toggle_enum", text="Direction", icon='OUTLINER_DATA_EMPTY')
        prop.data_path = "space_data.transform_orientation"
        prop.value_1 = "NORMAL"
        prop.value_2 = "GLOBAL"

        # 6 - RIGHT
        pie.operator("transform.toggle", text="Transform Toggle", icon='MANIPUL')


#        pie.operator("translate.scale", text="Move + Scale")
        # 2 - BOTTOM
        split = pie.split()
        col = split.column(align=True)
        row = col.row(align=True)
        row.scale_y=2
        row.scale_x=1.3
        prop = row.operator("wm.context_set_enum", text="Median", icon='OUTLINER_OB_EMPTY')
        prop.data_path = "space_data.pivot_point"
        prop.value = 'MEDIAN_POINT'

        row = col.row(align=True)
        row.scale_y=2
        prop = row.operator("wm.context_set_enum", text="Individuals", icon='OUTLINER_OB_EMPTY')
        prop.data_path = "space_data.pivot_point"
        prop.value = 'INDIVIDUAL_ORIGINS'
        col = split.column(align=True)
        row = col.row(align=True)
        row.scale_y=2
        prop = row.operator("wm.context_set_enum", text="Last Selected", icon='OUTLINER_OB_EMPTY')
        prop.data_path = "space_data.pivot_point"
        prop.value = 'ACTIVE_ELEMENT'
        row = col.row(align=True)
        row.scale_y=2
        prop = row.operator("wm.context_set_enum", text="Cursor", icon='OUTLINER_OB_EMPTY')
        prop.data_path = "space_data.pivot_point"
        prop.value = 'CURSOR'
        # 8 - TOP
        prop = pie.operator("transform.create_orientation", text="Create Axis")
        prop.use = True
        prop.name = "AddAxis"
        prop.overwrite = True
        # 7 - TOP - LEFT
        # prop = pie.operator("transform.manip_rotate", text="Rotate", icon='MANIPUL')
        prop = pie.operator("wm.context_toggle", text="Show Manipulator", icon='MANIPUL')
        prop.data_path = "space_data.show_manipulator"

        # 9 - TOP - RIGHT
        pie.operator("transform.shear", text="Shear")
        # 1 - BOTTOM - LEFT


        # 3 - BOTTOM - RIGHT

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
