bl_info = {
    "name": "Pie Selection",
    "description": "Select Modes",
    "author": ("Chebhou", "Vladislav Kindushov", "Vaughan Ling"),
    "version": (0, 1, 0),
    "blender": (2, 78, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
    }
    
    
import bpy
import bgl
from mathutils import Vector
from bpy.props import IntProperty, BoolProperty

def draw_callback_px_blue(self, context):

    bgl.glEnable(bgl.GL_BLEND)


    if self.selecting:
        # when selecting draw dashed line box
        bgl.glColor4f(0.7, 0.7, 1.0, 0.9)
        bgl.glLineWidth(2)
        bgl.glEnable(bgl.GL_LINE_STIPPLE)
        bgl.glLineStipple(1, 0x3333)
        bgl.glBegin(bgl.GL_LINE_LOOP)
        bgl.glVertex2i(self.min_x, self.min_y)
        bgl.glVertex2i(self.min_x, self.max_y)
        bgl.glVertex2i(self.max_x, self.max_y)
        bgl.glVertex2i(self.max_x, self.min_y)
        bgl.glEnd()
        bgl.glDisable(bgl.GL_LINE_STIPPLE)
        
    # restore opengl defaults
    bgl.glLineWidth(2)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)

def draw_callback_px_red(self, context):

    bgl.glEnable(bgl.GL_BLEND)


    if self.selecting:
        # when selecting draw dashed line box
        bgl.glColor4f(1.0, 0.5, 0.5, .9)
        bgl.glLineWidth(2)
        bgl.glEnable(bgl.GL_LINE_STIPPLE)
        bgl.glLineStipple(1, 0x3333)
        bgl.glBegin(bgl.GL_LINE_LOOP)
        bgl.glVertex2i(self.min_x, self.min_y)
        bgl.glVertex2i(self.min_x, self.max_y)
        bgl.glVertex2i(self.max_x, self.max_y)
        bgl.glVertex2i(self.max_x, self.min_y)
        bgl.glEnd()
        bgl.glDisable(bgl.GL_LINE_STIPPLE)
        
    # restore opengl defaults
    bgl.glLineWidth(2)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
def draw_callback_px(self, context):

    bgl.glEnable(bgl.GL_BLEND)


    if self.selecting:
        # when selecting draw dashed line box
        bgl.glColor4f(1.0, 1.0, 1.0, .9)
        bgl.glLineWidth(2)
        bgl.glEnable(bgl.GL_LINE_STIPPLE)
        bgl.glLineStipple(1, 0x3333)
        bgl.glBegin(bgl.GL_LINE_LOOP)
        bgl.glVertex2i(self.min_x, self.min_y)
        bgl.glVertex2i(self.min_x, self.max_y)
        bgl.glVertex2i(self.max_x, self.max_y)
        bgl.glVertex2i(self.max_x, self.min_y)
        bgl.glEnd()
        bgl.glDisable(bgl.GL_LINE_STIPPLE)
        
    # restore opengl defaults
    bgl.glLineWidth(2)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)


class Select_Through_Border(bpy.types.Operator):
    bl_idname = "view3d.select_through_border"
    bl_label = "Select Through Border"

    min_x = IntProperty(default = 0)
    min_y = IntProperty(default = 0)
    max_x = IntProperty()
    max_y = IntProperty()

    selecting = BoolProperty(default = True) # just for drawing in bgl

    def modal(self, context, event):
        bpy.context.space_data.use_occlude_geometry = False
        context.area.tag_redraw()
        if event.type == 'MOUSEMOVE': # just for drawing the box
            self.max_x = event.mouse_region_x
            self.max_y = event.mouse_region_y

        elif event.type == 'LEFTMOUSE':
            if event.value == 'PRESS': # start selection
                self.selecting = True
                self.min_x = event.mouse_region_x
                self.min_y = event.mouse_region_y
            if event.value == 'RELEASE': # end of selection
                #we have to sort the coordinates before passing them to select_border()
                self.max_x = max(event.mouse_region_x, self.min_x)
                self.max_y = max(event.mouse_region_y, self.min_y)
                self.min_x = min(event.mouse_region_x, self.min_x)
                self.min_y = min(event.mouse_region_y, self.min_y)

                bpy.ops.view3d.select_border(xmin=self.min_x, xmax=self.max_x, ymin=self.min_y, ymax=self.max_y, extend=False)
                bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')    
                bpy.context.space_data.use_occlude_geometry = True
                return {'FINISHED'}         

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):

        if context.space_data.type == 'VIEW_3D':
            args = (self, context)
            self.min_x = event.mouse_region_x
            self.min_y = event.mouse_region_y
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Active space must be a View3d")
            return {'CANCELLED'}
class Select_Through_Border_Subtract(bpy.types.Operator):
    bl_idname = "view3d.select_through_border_subtract"
    bl_label = "DeSelect Through Border"

    min_x = IntProperty(default = 0)
    min_y = IntProperty(default = 0)
    max_x = IntProperty()
    max_y = IntProperty()

    selecting = BoolProperty(default = True) # just for drawing in bgl

    def modal(self, context, event):
        bpy.context.space_data.use_occlude_geometry = False
        context.area.tag_redraw()
        if event.type == 'MOUSEMOVE': # just for drawing the box
            self.max_x = event.mouse_region_x
            self.max_y = event.mouse_region_y

        elif event.type == 'LEFTMOUSE':
            if event.value == 'PRESS': # start selection
                self.selecting = True
                self.min_x = event.mouse_region_x
                self.min_y = event.mouse_region_y
            if event.value == 'RELEASE': # end of selection
                #we have to sort the coordinates before passing them to select_border()
                self.max_x = max(event.mouse_region_x, self.min_x)
                self.max_y = max(event.mouse_region_y, self.min_y)
                self.min_x = min(event.mouse_region_x, self.min_x)
                self.min_y = min(event.mouse_region_y, self.min_y)

                bpy.ops.view3d.select_border(xmin=self.min_x, xmax=self.max_x, ymin=self.min_y, ymax=self.max_y, extend=False, deselect=True)
                bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')    
                bpy.context.space_data.use_occlude_geometry = True
                return {'FINISHED'}         

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):

        if context.space_data.type == 'VIEW_3D':
            args = (self, context)
            self.min_x = event.mouse_region_x
            self.min_y = event.mouse_region_y
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px_red, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Active space must be a View3d")
            return {'CANCELLED'}
            

class Select_Through_Border_Add(bpy.types.Operator):
    bl_idname = "view3d.select_through_border_add"
    bl_label = "Select Through Border"

    min_x = IntProperty(default = 0)
    min_y = IntProperty(default = 0)
    max_x = IntProperty()
    max_y = IntProperty()

    selecting = BoolProperty(default = True) # just for drawing in bgl

    def modal(self, context, event):
        bpy.context.space_data.use_occlude_geometry = False
        context.area.tag_redraw()
        if event.type == 'MOUSEMOVE': # just for drawing the box
            self.max_x = event.mouse_region_x
            self.max_y = event.mouse_region_y

        elif event.type == 'LEFTMOUSE':
            if event.value == 'PRESS': # start selection
                self.selecting = True
                self.min_x = event.mouse_region_x
                self.min_y = event.mouse_region_y
            if event.value == 'RELEASE': # end of selection
                #we have to sort the coordinates before passing them to select_border()
                self.max_x = max(event.mouse_region_x, self.min_x)
                self.max_y = max(event.mouse_region_y, self.min_y)
                self.min_x = min(event.mouse_region_x, self.min_x)
                self.min_y = min(event.mouse_region_y, self.min_y)

                bpy.ops.view3d.select_border(xmin=self.min_x, xmax=self.max_x, ymin=self.min_y, ymax=self.max_y, extend=True)
                bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')    
                bpy.context.space_data.use_occlude_geometry = True
                return {'FINISHED'}         

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}
        
    def invoke(self, context, event):

        if context.space_data.type == 'VIEW_3D':
            args = (self, context)
            self.min_x = event.mouse_region_x
            self.min_y = event.mouse_region_y
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px_blue, args, 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Active space must be a View3d")
            return {'CANCELLED'}
            
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
