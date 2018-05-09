import bpy
import random
from bpy.props import *

class PopupVMaterial(bpy.types.Operator):
    bl_idname = "popup.hp_materials"
    bl_label = "Heavypoly Material Popup"

    def execute(self, context):
        return {'FINISHED'}
 
    def invoke(self, context, event):
        ob = context.object
        wm = context.window_manager
        return wm.invoke_popup(self, width=400, height=500)
    def check(self, context):
        return True
    @classmethod
    def poll(cls, context):
        return (context.material or context.object) and CyclesButtonsPanel.poll(context)
    def find_node_input(node, name):
        for input in node.inputs:
            if input.name == name:
                return input
        return None
    def draw(self, context):
        layout = self.layout
        split = layout.split()
        col = split.column()
         #Vertex Color
        ts = context.tool_settings
        ups = ts.unified_paint_settings
        ptr = ups if ups.use_unified_color else ts.vertex_paint.brush
        col.template_color_picker(ptr, 'color', value_slider=True)
        col.operator("mesh.fill_color", text='Fill Color (Only for V Materials)')
        col.prop(ptr, 'color', text='Vertex Color')
        me = bpy.context.active_object.data
        col.template_list("MESH_UL_uvmaps_vcols", "vcols", me, "vertex_colors", me.vertex_colors, "active_index", rows=1)
#        col.operator("mesh.vertex_color_add", icon='ZOOMIN', text="")
#        col.operator("mesh.vertex_color_remove", icon='ZOOMOUT', text="")

        #Material Slots
        rows=10
        ob = context.object
        actob = context.active_object
        row = col.row()
        sub = row.column()
        sub.template_list("MATERIAL_UL_matslots", "", ob, "material_slots", ob, "active_material_index", rows=rows)
        sub = row.column()
        sub.operator("3dview.material_slot_add", icon='ZOOMIN', text="")      
        sub.operator("3dview.material_slot_remove", icon='ZOOMOUT', text="")
        sub.operator("object.material_slot_move", icon='TRIA_UP', text="").direction='UP'
        sub.operator("object.material_slot_move", icon='TRIA_DOWN', text="").direction='DOWN'
        col.separator()         
        col.separator()        
        col.template_ID(ob, "active_material")
        col.separator()         
        col.separator()
        row = col.row()
        sub = row.column()
        sub.operator('3dview.material_copy', icon='MATERIAL', text='Copy Material')
        sub.operator('3dview.material_new', icon='MATERIAL', text='New Material')
        sub.operator('3dview.material_delete', icon='MATERIAL', text='Delete Material')
        sub.operator("object.material_slot_assign", text="Assign to Slot")
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True):
            sub.operator("mesh.select_similar").type = 'MATERIAL'

        #Nodes 
        col = split.column() 
        actnode = bpy.context.active_object.active_material.node_tree.nodes.active
        col.prop(actnode, 'type', text='Shader')
        for x in bpy.context.active_object.active_material.node_tree.nodes.active.inputs:
            if x.name != 'Normal' and x.name != 'Clearcoat Normal' and x.name != 'Tangent':
                col.prop(x,'default_value', text = x.name)

class MaterialDelete(bpy.types.Operator):
    bl_idname = '3dview.material_delete'
    bl_label = 'Delete Material'
    def execute(self, context):
        bpy.data.materials.remove(bpy.context.object.active_material)
        if context.active_object.mode != 'OBJECT':
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.material_slot_remove()
            bpy.ops.object.editmode_toggle()
        else:
            bpy.ops.object.material_slot_remove()
        return {'FINISHED'}
class MaterialCopy(bpy.types.Operator):
    bl_idname = '3dview.material_copy'
    bl_label = 'Copy Material'
    def execute(self, context):
        i = bpy.context.object.active_material_index
        newmat = bpy.context.active_object.active_material.copy()
        bpy.context.object.data.materials.append(newmat)
        bpy.context.object.active_material_index=len(bpy.context.object.data.materials)-1
        move = len(bpy.context.object.data.materials)-i-2
        for m in range(move):
            bpy.ops.object.material_slot_move(direction='UP')
        bpy.ops.object.material_slot_assign()
        return {'FINISHED'}
    
class MaterialSlotAdd(bpy.types.Operator):
    bl_idname = '3dview.material_slot_add'
    bl_label = 'Add Material Slot'
    def execute(self, context):
        i = bpy.context.object.active_material_index
        bpy.ops.object.material_slot_add()           
        bpy.context.object.active_material_index=len(bpy.context.object.data.materials)-1
        move = len(bpy.context.object.data.materials)-i-2
        for m in range(move):
            bpy.ops.object.material_slot_move(direction='UP')
        bpy.ops.object.material_slot_assign()
        return {'FINISHED'} 
class MaterialSlotRemove(bpy.types.Operator):
    bl_idname = '3dview.material_slot_remove'
    bl_label = 'Remove Material Slot'
    def execute(self, context):
        if context.active_object.mode != 'OBJECT':
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.material_slot_remove()
            bpy.ops.object.editmode_toggle()
        else:
            bpy.ops.object.material_slot_remove()
        return {'FINISHED'}
class MaterialNew(bpy.types.Operator):
    bl_idname = '3dview.material_new'
    bl_label = 'Add New Material'
    def execute(self, context):
        newmat = bpy.data.materials.new('Material')
        bpy.context.active_object.data.materials.append(newmat)
        bpy.context.object.active_material_index=len(bpy.context.object.data.materials)-1
        bpy.context.active_object.active_material.use_nodes=True
        bpy.ops.object.material_slot_assign()
        return {'FINISHED'}
class FillColor(bpy.types.Operator):
    bl_idname = "mesh.fill_color"        # unique identifier for buttons and menu items to reference.
    bl_label = "Fill Color"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
    def execute(self, context):
        obj = bpy.context.object
        mesh = obj.data
        if tuple(bpy.context.scene.tool_settings.mesh_select_mode) == (False, False, True):
            bpy.ops.object.editmode_toggle()
            bpy.ops.paint.vertex_paint_toggle()
            bpy.context.object.data.use_paint_mask = True
            bpy.ops.paint.vertex_color_set()
            bpy.ops.object.editmode_toggle()
        else:
            bpy.ops.object.editmode_toggle()
            bpy.ops.paint.vertex_paint_toggle()
            bpy.context.object.data.use_paint_mask_vertex = True
            bpy.ops.paint.vertex_color_set()
            bpy.ops.object.editmode_toggle()
        bpy.ops.object.material_slot_assign()
        return {'FINISHED'}

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()