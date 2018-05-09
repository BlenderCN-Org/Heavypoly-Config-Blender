bl_info = {
    "name": "HP Boolean Pie",
    "description": "",
    "author": "Vaughan Ling",
    "version": (0, 1, ),
    "blender": (2, 79, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
    }
import bpy
from bpy.types import Menu

# Boolean Pie
class VIEW3D_PIE_HP_Boolean(Menu):
    bl_idname = "pie.hp_boolean"
    bl_label = "HP Boolean"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        split = pie.split()
        col = split.column(align=True)
		#Plain ol Booleans
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("view3d.hp_boolean_live", text="Add")
        prop.bool_operation = 'UNION'
        prop.cutline = 'NO'
        prop.insetted = 'NO'
        prop.live = 'NO'
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("view3d.hp_boolean_live", text="Intersect")
        prop.bool_operation = 'INTERSECT'
        prop.cutline = 'NO'
        prop.insetted = 'NO'
        prop.live = 'NO'		
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("view3d.hp_boolean_live", text="Subtract")
        prop.bool_operation = 'DIFFERENCE'
        prop.cutline = 'NO'
        prop.insetted = 'NO'
        prop.live = 'NO'
        row = col.row(align=True)
        row.scale_y=1.5
        row.operator("view3d.hp_boolean_slice", text="Slice")
		#Live Booleans
        split = pie.split()
        col = split.column(align=True)
		
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("view3d.hp_boolean_live", text="Live Add")
        prop.bool_operation = 'UNION'
        prop.live = 'YES'
        prop.cutline = 'NO'
        prop.insetted = 'NO'
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("view3d.hp_boolean_live", text="Live Intersect")
        prop.bool_operation = 'INTERSECT'
        prop.cutline = 'NO'
        prop.insetted = 'NO'
        prop.live = 'YES'		
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("view3d.hp_boolean_live", text="Live Subtract")
        prop.bool_operation = 'DIFFERENCE'
        prop.live = 'YES'
        prop.cutline = 'NO'
        prop.insetted = 'NO'
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("view3d.hp_boolean_live", text="Live Subtract Inset")
        prop.bool_operation = 'DIFFERENCE'
        prop.live = 'YES'
        prop.cutline = 'NO'
        prop.insetted = 'YES'
        row = col.row(align=True)
        row.scale_y=1.5
        prop = row.operator("view3d.hp_boolean_live", text="Live Cutline")
        prop.bool_operation = 'DIFFERENCE'
        prop.live = 'YES'
        prop.cutline = 'YES'
        prop.insetted = 'NO'        
		
        split = pie.split()
        col = split.column(align=True)
		
        row = col.row(align=True)
        row.scale_y=1.5  
        row.operator("view3d.hp_boolean_apply", text="Apply and Copy").dup = 'YES'
        row = col.row(align=True)
        row.scale_y=1.5
        row.operator("view3d.hp_boolean_apply", text="Apply").dup = 'NO'
        row = col.row(align=True)
        row.scale_y=1.5
        #row.operator("view3d.hp_boolean_toggle_bool_solver", text="Toggle Solver")
        pie.operator("view3d.hp_boolean_toggle_cutters", text="Toggle Cutters")

        
        
class HP_Boolean_Toggle_Cutters(bpy.types.Operator):
    bl_idname = "view3d.hp_boolean_toggle_cutters"
    bl_label = "hp_boolean_toggle_cutters"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        for ob in bpy.context.scene.objects:
            if ob.type == 'MESH' and ob.name.startswith("Bool_Cutter"):
                if ob.hide == False:
                    ob.hide = True
                elif ob.hide == True:
                    ob.hide = False
        return {'FINISHED'}
#class HP_Boolean_Toggle_Solver(bpy.types.Operator):
#    bl_idname = "view3d.hp_boolean_toggle_bool_solver"
#    bl_label = "hp_boolean_toggle_cutters"
#    bl_options = {'REGISTER', 'UNDO'}
#    def execute(self, context):
#        sel = bpy.context.selected_objects
#        scene = bpy.context.scene
#        bases = [base for base in scene.objects if not base.name.startswith("Bool_Cutter") and base.type == 'MESH']
#        for ob in sel: 
#            #Get Cutters in Sel
#            if ob.name.startswith('Bool_Cutter'):
#                cutter = ob
#                for base in bases:
#                    for mod in base.modifiers: 
#                        if mod.name == cutter.name:
#                            if mod.solver == 'BMESH':
#                                mod.solver = 'CARVE'
#                            else:
#                                mod.solver = 'BMESH'
#            else:               
#                base = ob
#                for mod in base.modifiers: 
#                    if mod.name.startswith ('Bool_Cutter'):
#                        if mod.solver == 'BMESH':
#                            mod.solver = 'CARVE'
#                        else:
#                            mod.solver = 'BMESH'
#        return {'FINISHED'}
class HP_Boolean_Live(bpy.types.Operator):
    bl_idname = "view3d.hp_boolean_live"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}
    cutline = bpy.props.StringProperty(name='Cutline',default='NO')   
    live = bpy.props.StringProperty(name='Live',default='NO')   
    insetted = bpy.props.StringProperty(name='Insetted',default='NO')   
    drawtype = bpy.props.StringProperty(name="Draw Type",default='BOUNDS')
    bool_operation = bpy.props.StringProperty(name="Boolean Operation")
    bool_solver = bpy.props.StringProperty(name="Boolean Solver",default='BMESH')
    def execute(self, context):
        sel = bpy.context.selected_objects
        base = bpy.context.active_object
        scene = bpy.context.scene
        isedit = False
        if context.active_object.mode != 'OBJECT' and self.live == 'NO':
            bpy.ops.mesh.select_linked(delimit={'NORMAL'})
            bpy.ops.mesh.intersect_boolean(operation=self.bool_operation)
            return {'FINISHED'}
        def create_cutter(drawtype, insetted):
            bpy.context.scene.objects.active = cutter
            cutter.name = "Bool_Cutter"
            scene_cutters = [obj for obj in scene.objects if obj.name.startswith("Bool_Cutter")]
            for x in scene_cutters:
                if x != cutter:
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=x.name)
            cutter.name = "Bool_Cutter_" + str(len(scene_cutters))
            if self.cutline == 'YES':
                cutter.modifiers.new('Cutline', "SOLIDIFY")
                bpy.context.object.modifiers['Cutline'].thickness = 0.02     
            if self.insetted == 'YES':
                base.select = False
                cutter.select = True
                for x in scene_cutters:
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier = x.name)
                bpy.ops.object.duplicate()
                bpy.context.scene.objects.active.name = "Bool_Inset"
                inset = bpy.context.active_object
                bpy.ops.object.editmode_toggle()
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'
                bpy.ops.transform.resize(value=(0.92, 0.92, 0.92), constraint_axis=(False, False, False), mirror=False, proportional='DISABLED')
                bpy.context.space_data.pivot_point = 'MEDIAN_POINT'
                bpy.ops.object.editmode_toggle()      
                bpy.context.scene.objects.active = cutter
                bpy.ops.object.constraint_add(type='COPY_TRANSFORMS')
                bpy.context.object.constraints["Copy Transforms"].target = inset
                inset.select = True
                bpy.context.scene.objects.active = inset
            cutter.draw_type = drawtype
            cutter.hide_render = True
            cutter.cycles_visibility.camera = False
            cutter.cycles_visibility.diffuse = False
            cutter.cycles_visibility.glossy = False
            cutter.cycles_visibility.shadow = False
            cutter.cycles_visibility.scatter = False
            cutter.cycles_visibility.transmission = False
            cutter.select = False
        def create_bool(bool_operation, live):
            Bool = base.modifiers.new(cutter.name, "BOOLEAN")
            Bool.object = cutter
            Bool.operation = bool_operation
            #Bool.solver = bool_solver
            base.select = True
            bpy.context.scene.objects.active = base
            bpy.ops.object.modifier_move_down(modifier="Mirror Base")
            if self.live == 'NO':
                if context.active_object.mode != 'OBJECT':
                    bpy.ops.object.editmode_toggle()
                bpy.ops.object.modifier_apply(apply_as='DATA', modifier=cutter.name)
                base.select = False
                cutter.select = True
                bpy.ops.object.delete(use_global=False)
                base.select = True
                i = base.data.vertex_colors.active_index
                base.data.vertex_colors.active_index = i + 1
                bpy.ops.mesh.vertex_color_remove()

        if context.active_object.mode != 'OBJECT':
            isedit = True
            bpy.ops.mesh.select_linked()
            bpy.ops.mesh.normals_make_consistent(inside=False)
            bpy.ops.mesh.separate(type='SELECTED')
            bpy.ops.object.editmode_toggle()
            sel = bpy.context.selected_objects                
        for cutter in sel:
            if cutter != base:
                create_cutter(self.drawtype, self.insetted)
                create_bool(self.bool_operation, self.live)
        if isedit == True and self.live == 'NO':
            bpy.ops.object.editmode_toggle()
        if self.insetted == 'YES':
            base.select = False	
            for x in bpy.context.selected_objects:
                bpy.context.scene.objects.active = x
        return {'FINISHED'}
class HP_Boolean_Slice(bpy.types.Operator):
    """slice"""
    bl_idname = "view3d.hp_boolean_slice"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}
    def invoke(self, context, event):
        if bpy.context.mode=='OBJECT':
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.object.vertex_group_add()
            bpy.ops.object.vertex_group_assign()                 
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.join()
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.vertex_group_select() 
            bpy.ops.mesh.select_all(action='INVERT')      
            bpy.ops.object.vertex_group_remove()
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        bpy.ops.mesh.select_linked(delimit=set())
        bpy.ops.mesh.normals_make_consistent(inside=False)
        bpy.ops.object.vertex_group_add()
        bpy.ops.object.vertex_group_assign()
        bpy.ops.mesh.intersect()
        bpy.ops.object.vertex_group_add()
        bpy.ops.object.vertex_group_assign() 
        i = bpy.context.active_object.vertex_groups.active_index
        i = i-1
        bpy.context.active_object.vertex_groups.active_index = i
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()        
        bpy.ops.mesh.select_linked(delimit=set())
        bpy.ops.mesh.delete(type='VERT')
        bpy.ops.object.vertex_group_remove()
        bpy.ops.object.vertex_group_select()       
        bpy.ops.object.vertex_group_remove()
        return {'FINISHED'}

class HP_Boolean_Apply(bpy.types.Operator):
    bl_idname = "view3d.hp_boolean_apply" 
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}
    dup = bpy.props.StringProperty(name='Duplicate')
    def execute(self, context):
        def apply(dup):
            sel = bpy.context.selected_objects
            scene = bpy.context.scene
            scene_cutters = [obj for obj in scene.objects if obj.name.startswith("Bool_Cutter")]
            for ob in sel:
                if ob.name.startswith('Bool_Cutter'):
                    iscutter = True
                    cutter = ob
                    for base in scene.objects:
                        for mod in base.modifiers:
                            bpy.context.scene.objects.active = base
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier=cutter.name)
                    cutter.select = True
                else:
                    base = ob
                    if self.dup == 'YES':
                        bpy.ops.object.duplicate()
                        clone = bpy.context.active_object
                        base.hide = True
                    for mod in base.modifiers:
                        cutter = bpy.context.scene.objects[mod.name]
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=cutter.name)
                        if self.dup == 'YES':
                            cutter.hide = True
                            continue
                        cutter.select = True
                        base.select = False
                        bpy.ops.object.delete()
                        base.select = True
            try:
                if iscutter == True:
                    bpy.ops.object.delete() 
                    bpy.context.active_object.select = True
                    sel = bpy.context.selected_objects  
            except:
                pass  
        apply(self.dup)
        return {'FINISHED'}  
def register():
    bpy.utils.register_module(__name__)
def unregister():
    bpy.utils.unregister_module(__name__)
if __name__ == "__main__":
    register()
