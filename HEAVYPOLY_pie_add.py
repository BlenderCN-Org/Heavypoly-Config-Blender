bl_info = {
    "name": "Pie Add",
    "description": "",
    "author": "Vaughan Ling",
    "version": (0, 1, 0),
    "blender": (2, 79, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
    }

import bpy
from bpy.types import Menu
from bpy.types import Operator
from bpy.props import BoolProperty
from mathutils import Matrix

class VIEW3D_PIE_Add(Menu):
    bl_idname = "pie.add"
    bl_label = "Add"
    def draw(self, context):
        layout = self.layout
        view = context.space_data
        obj = context.active_object
        pie = layout.menu_pie()
        # Left
        split = pie.split()
        col = split.column()
        col.scale_y=1.5
        col.scale_x=1
        col.operator("view3d.hp_add_primitive", icon='MESH_PLANE', text="Plane").type = 'Plane'
        col.operator("view3d.hp_add_primitive", icon='MESH_PLANE', text="Plane Small").type = 'Plane_Small'
        col = split.column()
        col.scale_y=1.5
        col.scale_x=2
        col.operator("view3d.hp_add_primitive", icon='MESH_CIRCLE', text="6").type = 'Circle_6'
        col.operator("view3d.hp_add_primitive", icon='MESH_CIRCLE', text="8").type = 'Circle_8'
        col.operator("view3d.hp_add_primitive", icon='MESH_CIRCLE', text="12").type = 'Circle_12'
        col.operator("view3d.hp_add_primitive", icon='MESH_CIRCLE', text="24").type = 'Circle_24'
        col.operator("view3d.hp_add_primitive", icon='MESH_CIRCLE', text="32").type = 'Circle_32'
        # Right
        split = pie.split()
        col = split.column()
        col.scale_y=1.5
        col.scale_x=2
        col.operator("view3d.hp_add_primitive", icon='MESH_UVSPHERE', text="12").type = 'Sphere_12'
        col.operator("view3d.hp_add_primitive", icon='MESH_UVSPHERE', text="24").type = 'Sphere_24'
        col.operator("view3d.hp_add_primitive", icon='MESH_UVSPHERE', text="32").type = 'Sphere_32'
        # Bottom
        split = pie.split()
        col = split.column()
        col.scale_y=1.5
        col.scale_x=1
        col.operator("view3d.hp_add_primitive", icon='MESH_CUBE', text="Cube").type = 'Cube'
        col.operator("view3d.hp_add_primitive", icon='MESH_CUBE', text="Cube Small").type = 'Cube_Small'        

        split = pie.split()
        col = split.column()
        col.scale_y=1.5
        col.scale_x=2
        col.operator("view3d.hp_add_primitive", icon='MESH_CYLINDER', text="6").type = 'Cylinder_6'
        col.operator("view3d.hp_add_primitive", icon='MESH_CYLINDER', text="8").type = 'Cylinder_8'
        col.operator("view3d.hp_add_primitive", icon='MESH_CYLINDER', text="12").type = 'Cylinder_12'
        col.operator("view3d.hp_add_primitive", icon='MESH_CYLINDER', text="24").type = 'Cylinder_24'

        col = split.column()
        col.scale_y=1.5
        col.scale_x=2
        col.operator("view3d.hp_add_primitive", icon='MESH_CYLINDER', text="32").type = 'Cylinder_32'
        col.operator("view3d.hp_add_primitive", icon='MESH_CYLINDER', text="64").type = 'Cylinder_64'
        col.operator("view3d.hp_add_primitive", icon='MESH_CYLINDER', text="128").type = 'Cylinder_128'

class HPAddPrimitive(bpy.types.Operator):
    bl_idname = "view3d.hp_add_primitive"        # unique identifier for buttons and menu items to reference.
    bl_label = "HP Add Primitive"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO',}  # enable undo for the operator.
    type = bpy.props.StringProperty(name="Type")
    def invoke(self, context, event):
        cur = bpy.context.scene.cursor_location
        cur = list(cur)
        def prim(self, type):
            if self.type == 'Cube':
                bpy.ops.mesh.primitive_cube_add(radius=.5)
            if self.type == 'Cube_Small':           
                bpy.ops.mesh.primitive_cube_add(radius=.05)
            if self.type == 'Plane':
                bpy.ops.mesh.primitive_plane_add()
            if self.type == 'Plane_Small':
                bpy.ops.mesh.primitive_plane_add(radius=.1)
            if self.type == 'Circle_6':
                bpy.ops.mesh.primitive_circle_add(vertices=6, radius=0.08, fill_type='NGON')
            if self.type == 'Circle_8':
                bpy.ops.mesh.primitive_circle_add(fill_type='NGON', radius=.25, vertices=8)
            if self.type == 'Circle_12':
                bpy.ops.mesh.primitive_circle_add(fill_type='NGON', radius=.25, vertices=12)
            if self.type == 'Circle_24':
                bpy.ops.mesh.primitive_circle_add(fill_type='NGON', radius=.25, vertices=24)
            if self.type == 'Circle_32':
                bpy.ops.mesh.primitive_circle_add(fill_type='NGON', vertices=32)

                


                
                
            if self.type == 'Cylinder_6':
                bpy.ops.mesh.primitive_cylinder_add(radius=.08,depth=.1, vertices=6)
            if self.type == 'Cylinder_8':
                bpy.ops.mesh.primitive_cylinder_add(radius=.25,depth=.5, vertices=8)
            if self.type == 'Cylinder_12':
                bpy.ops.mesh.primitive_cylinder_add(radius=.25,depth=.5, vertices=12)
            if self.type == 'Cylinder_24':
                bpy.ops.mesh.primitive_cylinder_add(radius=.25,depth=.5, vertices=24)
            if self.type == 'Cylinder_32':
                bpy.ops.mesh.primitive_cylinder_add(vertices=32)
            if self.type == 'Cylinder_64':
                bpy.ops.mesh.primitive_cylinder_add(vertices=64)            
            if self.type == 'Cylinder_128':
                bpy.ops.mesh.primitive_cylinder_add(vertices=128)
            if self.type == 'Sphere_12':           
                bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=6, size=0.1)
            if self.type == 'Sphere_24':           
                bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12)
            if self.type == 'Sphere_32':           
                bpy.ops.mesh.primitive_uv_sphere_add()
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, False):
            prim(self, type)
        elif tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True) and context.object.data.total_vert_sel != 0:
            o = bpy.context.scene.objects.active
            bpy.ops.view3d.snap_cursor_to_selected()
            bpy.ops.transform.create_orientation(name="AddAxis", use=True, overwrite=True)
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()
            prim(self, type)
            bpy.ops.transform.transform(mode='ALIGN', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='AddAxis', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=5.81828)
            o.select = True
            bpy.context.scene.objects.active = o
            bpy.ops.object.join()
            bpy.ops.object.editmode_toggle()
        else:
            bpy.ops.view3d.snap_cursor_to_selected()
            prim(self, type)
        bpy.context.scene.cursor_location = cur
        bpy.context.space_data.transform_orientation = 'NORMAL'
        return {'FINISHED'}
def register():
    bpy.utils.register_module(__name__)
def unregister():
    bpy.utils.unregister_module(__name__)
if __name__ == "__main__":
    register()
