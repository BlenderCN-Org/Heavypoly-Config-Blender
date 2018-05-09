import bpy
from bpy.props import IntProperty, FloatProperty

bl_info = {
    "name": "Quick Pipe",
    "author": "floatvoid (Jeremy Mitchell)",
    "version": (1, 0),
    "blender": (2, 72, 0),
    "location": "View3D > Edit Mode",
    "description": "Quickly converts an edge selection to an extruded curve.",
    "warning": "",
    "wiki_url": "",
    "category": "View3D"}


class jmPipeTool(bpy.types.Operator):
    """Create an extruded curve from a selection of edges"""
    bl_idname = "object.quickpipe"
    bl_label = "Quick Pipe"

    first_mouse_x = IntProperty()
    first_value = FloatProperty()

    def modal(self, context, event):
        if event.type == 'MOUSEMOVE':
            delta = self.first_mouse_x - event.mouse_x
            context.object.data.bevel_depth = self.first_value + delta * 0.01
        elif event.type == 'WHEELUPMOUSE':
            bpy.context.object.data.bevel_resolution += 1
        elif event.type == 'WHEELDOWNMOUSE':
            if bpy.context.object.data.bevel_resolution > 0:
                bpy.context.object.data.bevel_resolution -= 1

        elif event.type == 'LEFTMOUSE':
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.object:
            self.first_mouse_x = event.mouse_x
            if( context.object.type == 'MESH' ):         
                bpy.ops.mesh.separate(type='SELECTED')
                bpy.ops.object.editmode_toggle()
                bpy.ops.object.select_all(action='DESELECT')
                
                self.pipe = bpy.context.scene.objects[0]
                self.pipe.select = True
                bpy.context.scene.objects.active = self.pipe
                bpy.ops.object.convert(target='CURVE')
                
                self.pipe.data.fill_mode = 'FULL'
                self.pipe.data.splines[0].use_smooth = True
                self.pipe.data.bevel_resolution = 2
                self.pipe.data.bevel_depth = 0.1
            elif( context.object.type == 'CURVE' ):
                self.pipe = context.object
                        
            self.first_value = self.pipe.data.bevel_depth

            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}


def register():
    bpy.utils.register_class(jmPipeTool)


def unregister():
    bpy.utils.unregister_class(jmPipeTool)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.quickpipe('INVOKE_DEFAULT')
