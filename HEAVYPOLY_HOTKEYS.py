bl_info = {
    "name": "Heavypoly Hotkeys",
    "description": "Hotkeys",
    "author": "Vaughan Ling",
    "version": (0, 1, 0),
    "blender": (2, 78, 0),
    "location": "DooDooButter",
    "warning": "",
    "wiki_url": "",
    "category": "Hotkeys"
    }

import bpy
import os

def kmi_props_setattr(kmi_props, attr, value):
    try:
        setattr(kmi_props, attr, value)
    except AttributeError:
        print("Warning: property '%s' not found in keymap item '%s'" %
              (attr, kmi_props.__class__.__name__))
    except Exception as e:
        print("Warning: %r" % e)

def Keymap_Heavypoly():

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    k_viewfit = 'MIDDLEMOUSE'
    k_manip = 'LEFTMOUSE'
    k_cursor = 'RIGHTMOUSE'
    k_nav = 'MIDDLEMOUSE'
    k_menu = 'SPACE'
     
    # kmi = km.keymap_items.new('gpencil.blank_frame_add', 'B', 'PRESS', key_modifier='FOUR')
# "ACCENT_GRAVE"
#Window
    km = kc.keymaps.new('Window', space_type='EMPTY', region_type='WINDOW', modal=False)
    kmi = km.keymap_items.new('screen.animation_play', 'SIX', 'PRESS')
    # kmi = km.keymap_items.new('transform.translate', 'EVT_TWEAK_L', 'NORTH', alt=True).properties.constraint_axis=(False, False, True)
    # kmi = km.keymap_items.new('transform.translate', 'EVT_TWEAK_L', 'SOUTH', alt=True).properties.constraint_axis=(False, False, True)
    # kmi = km.keymap_items.new('transform.translate', 'EVT_TWEAK_L', 'WEST', alt=True).properties.constraint_axis=(True, False, False)
    # kmi = km.keymap_items.new('transform.translate', 'EVT_TWEAK_L', 'EAST', alt=True).properties.constraint_axis=(True, False, False)
    # kmi = km.keymap_items.new('transform.translate', 'EVT_TWEAK_L', 'NORTH_EAST', alt=True).properties.constraint_axis=(False, True, False)
    # kmi = km.keymap_items.new('transform.translate', 'EVT_TWEAK_L', 'NORTH_WEST', alt=True).properties.constraint_axis=(False, True, False)
    # kmi = km.keymap_items.new('transform.translate', 'EVT_TWEAK_L', 'SOUTH_EAST', alt=True).properties.constraint_axis=(False, True, False)
    # kmi = km.keymap_items.new('transform.translate', 'EVT_TWEAK_L', 'SOUTH_WEST', alt=True).properties.constraint_axis=(False, True, False)    
    kmi = km.keymap_items.new('view3d.extrude_normal', 'EVT_TWEAK_L', 'SOUTH', alt=True)       
    kmi = km.keymap_items.new('view3d.extrude_normal', 'EVT_TWEAK_L', 'NORTH', alt=True)
    kmi = km.keymap_items.new('mesh.push_and_slide', 'EVT_TWEAK_L', 'NORTH', ctrl=True, alt=True)
    kmi = km.keymap_items.new('mesh.push_and_slide', 'EVT_TWEAK_L', 'SOUTH', ctrl=True, alt=True)
    kmi = km.keymap_items.new('mesh.inset', 'EVT_TWEAK_L', 'WEST', alt=True)
    kmi = km.keymap_items.new('mesh.inset', 'EVT_TWEAK_L', 'EAST', alt=True)    
    kmi = km.keymap_items.new('transform.resize', k_menu,"PRESS",alt=True)    
#    kmi = km.keymap_items.new("transform.edge_slide", 'EVT_TWEAK_L', 'WEST', alt=True)
    #kmi = km.keymap_items.new("mesh.push_and_slide",'EVT_TWEAK_L', 'SOUTH_WEST', alt=True)
    #kmi_props_setattr(kmi.properties, 'use_even_offset', True)
    kmi = km.keymap_items.new('transform.translate', 'SPACE', 'PRESS')
#kmi = km.keymap_items.new('transform.resize', 'SPACE', 'PRESS', alt=True)
    kmi = km.keymap_items.new('transform.rotate', 'C', 'PRESS')
    kmi = km.keymap_items.new("wm.window_fullscreen_toggle","F11","PRESS")
    kmi = km.keymap_items.new("wm.call_menu_pie", k_menu,"PRESS",ctrl=True ,shift=True, alt=True).properties.name="pie.areas"
    kmi = km.keymap_items.new("wm.revert_without_prompt","N","PRESS", alt=True)
    kmi = km.keymap_items.new("screen.redo_last","D","PRESS")
    kmi = km.keymap_items.new("screen.userpref_show","TAB","PRESS", ctrl=True)
    kmi = km.keymap_items.new("wm.call_menu_pie","S","PRESS", ctrl=True).properties.name="pie.save"
    kmi = km.keymap_items.new("wm.call_menu_pie","S","PRESS", ctrl=True, shift=True).properties.name="pie.importexport"
    kmi = km.keymap_items.new('script.reload', 'U', 'PRESS', shift=True)
    kmi = km.keymap_items.new("screen.repeat_last","THREE","PRESS", ctrl=True, shift=True)
    kmi = km.keymap_items.new("ed.undo","TWO","PRESS", ctrl=True, shift=True)
    kmi = km.keymap_items.new('popup.hp_materials', 'V', 'PRESS', shift=True)
    
# Map Image
    km = kc.keymaps.new('Image', space_type='IMAGE_EDITOR', region_type='WINDOW', modal=False)
    kmi = km.keymap_items.new('image.view_all', k_viewfit, 'PRESS', ctrl=True, shift=True)
    kmi_props_setattr(kmi.properties, 'fit_view', True)
    kmi = km.keymap_items.new('image.view_pan', k_nav, 'PRESS', shift=True)
    kmi = km.keymap_items.new('image.view_zoom', k_nav, 'PRESS', ctrl=True)

# Map Node Editor
    km = kc.keymaps.new('Node Editor', space_type='NODE_EDITOR', region_type='WINDOW', modal=False)
    kmi = km.keymap_items.new('node.view_selected', k_viewfit, 'PRESS', ctrl=True, shift=True)
# Map View2D
    km = kc.keymaps.new('View2D', space_type='EMPTY', region_type='WINDOW', modal=False)
# Map Animation
    km = kc.keymaps.new('Animation', space_type='EMPTY', region_type='WINDOW', modal=False)

    kmi = km.keymap_items.new('anim.change_frame', 'SELECTMOUSE', 'PRESS')

# Map Graph Editor
# km = kc.keymaps.new('Graph Editor', space_type='GRAPH_EDITOR', region_type='WINDOW', modal=False)

    km = kc.keymaps.new('Graph Editor', space_type='GRAPH_EDITOR', region_type='WINDOW', modal=False)
    kmi = km.keymap_items.new('graph.view_selected', k_viewfit, 'PRESS', ctrl=True, shift=True)
    kmi = km.keymap_items.new('graph.select_lasso', 'EVT_TWEAK_L', 'ANY', shift=True, ctrl=True)
    kmi_props_setattr(kmi.properties, 'extend', True)
    kmi = km.keymap_items.new('graph.select_lasso', 'EVT_TWEAK_L', 'ANY', ctrl=True)
    kmi_props_setattr(kmi.properties, 'deselect', True)
    kmi = km.keymap_items.new('graph.select_border', 'EVT_TWEAK_L', 'ANY', shift=True)
    kmi_props_setattr(kmi.properties, 'extend', True)
    kmi = km.keymap_items.new('graph.select_border', 'EVT_TWEAK_L', 'ANY')
    kmi_props_setattr(kmi.properties, 'extend', False)
# Map UV Editor
    km = kc.keymaps.new('UV Editor', space_type='EMPTY', region_type='WINDOW', modal=False)
    kmi = km.keymap_items.new("wm.call_menu_pie", k_menu,"PRESS",ctrl=True, alt=True).properties.name="pie.rotate90"
    kmi = km.keymap_items.new('uv.select_lasso', 'EVT_TWEAK_L', 'ANY', shift=True, ctrl=True)
    kmi_props_setattr(kmi.properties, 'extend', True)
    kmi = km.keymap_items.new('uv.select_lasso', 'EVT_TWEAK_L', 'ANY', ctrl=True)
    kmi_props_setattr(kmi.properties, 'deselect', True)
    kmi = km.keymap_items.new('uv.select_border', 'EVT_TWEAK_L', 'ANY', shift=True)
    kmi_props_setattr(kmi.properties, 'extend', True)
    kmi = km.keymap_items.new('uv.select_border', 'EVT_TWEAK_L', 'ANY')
    kmi_props_setattr(kmi.properties, 'extend', False)


# Map Mask Editing
#    km = kc.keymaps.new('Mask Editing', space_type='EMPTY', region_type='WINDOW', modal=False)
#3D View
    km = kc.keymaps.new('3D View', space_type='VIEW_3D', region_type='WINDOW', modal=False)
    kmi = km.keymap_items.new('view3d.render_border', 'B', 'PRESS',shift=True, ctrl=True)
    kmi = km.keymap_items.new("wm.call_menu_pie", k_menu,"PRESS",ctrl=True ,shift=True, alt=True).properties.name="pie.areas"
#    kmi = km.keymap_items.new('view3d.select_lasso', 'EVT_TWEAK_L', 'ANY', alt=True)
    kmi = km.keymap_items.new('view3d.view_selected', k_viewfit, 'PRESS', ctrl=True, shift=True)
    kmi = km.keymap_items.new('view3d.move', k_nav, 'PRESS', shift=True)
    kmi = km.keymap_items.new('view3d.zoom', k_nav, 'PRESS', ctrl=True)
    kmi = km.keymap_items.new('view3d.rotate', k_nav, 'PRESS')
    kmi = km.keymap_items.new('view3d.manipulator', k_manip, 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'release_confirm', True)
    kmi_props_setattr(kmi.properties, 'use_accurate', False)
    kmi_props_setattr(kmi.properties, 'use_planar_constraint', True)
    kmi = km.keymap_items.new('view3d.manipulator', k_manip, 'PRESS')
    kmi_props_setattr(kmi.properties, 'release_confirm', True)
    kmi_props_setattr(kmi.properties, 'use_accurate', False)
    kmi_props_setattr(kmi.properties, 'use_planar_constraint', False)
    kmi = km.keymap_items.new("wm.call_menu_pie", k_menu,"PRESS",ctrl=True).properties.name="pie.select"
    kmi = km.keymap_items.new("wm.call_menu_pie", k_menu, 'PRESS',ctrl=True, alt=True).properties.name="pie.rotate90"
    kmi = km.keymap_items.new("wm.call_menu_pie", k_menu,"PRESS",ctrl=True ,shift=True).properties.name="pie.view"
    kmi = km.keymap_items.new('wm.call_menu_pie', k_menu,'PRESS',shift=True).properties.name="pie.transforms"
    kmi = km.keymap_items.new("wm.call_menu_pie","Z","PRESS").properties.name="pie.shading"
    kmi = km.keymap_items.new("wm.call_menu_pie","D","PRESS",ctrl=True, shift=True).properties.name="pie.specials"
    kmi = km.keymap_items.new("wm.call_menu_pie","ONE","PRESS").properties.name="pie.modifiers"
    kmi = km.keymap_items.new("wm.call_menu_pie","X","PRESS",shift=True).properties.name="pie.symmetry"
    kmi = km.keymap_items.new('wm.call_menu_pie', 'B', 'PRESS',ctrl=True).properties.name="pie.hp_boolean"
    kmi = km.keymap_items.new("screen.repeat_last","Z","PRESS",ctrl=True, alt=True)
    kmi = km.keymap_items.new("screen.repeat_last","WHEELINMOUSE","PRESS",ctrl=True, shift=True, alt=True)
    kmi = km.keymap_items.new("ed.undo","WHEELOUTMOUSE","PRESS",ctrl=True, shift=True, alt=True)
    kmi = km.keymap_items.new("view3d.screencast_keys","U","PRESS",alt=True)
    kmi = km.keymap_items.new("paint.sample_color","V","PRESS",ctrl=True, shift=True)
    kmi = km.keymap_items.new('view3d.select_lasso', 'EVT_TWEAK_L', 'ANY', shift=True, ctrl=True)
    kmi_props_setattr(kmi.properties, 'extend', True)
    kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY', ctrl=True)
    kmi_props_setattr(kmi.properties, 'deselect', True)
    kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY', shift=True)
    kmi_props_setattr(kmi.properties, 'extend', True)
    kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY')
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi = km.keymap_items.new('view3d.smart_delete', 'X', 'PRESS')
    kmi = km.keymap_items.new("wm.search_menu","FIVE","PRESS")
    kmi = km.keymap_items.new("view3d.subdivision_toggle","TAB","PRESS")
    kmi = km.keymap_items.new("view3d.smart_snap_cursor","RIGHTMOUSE","PRESS",ctrl=True)
    kmi = km.keymap_items.new("view3d.smart_snap_origin","RIGHTMOUSE","PRESS",ctrl=True, shift=True)
    # Map Vertex Paint
    km = kc.keymaps.new('Vertex Paint', space_type='EMPTY', region_type='WINDOW', modal=False)
    kmi = km.keymap_items.new('wm.call_menu_pie', 'LEFTMOUSE', 'PRESS', alt=True).properties.name="pie.vertex_paint"
    kmi = km.keymap_items.new('view3d.select_lasso', 'EVT_TWEAK_L', 'ANY', alt=True)
    kmi = km.keymap_items.new('view3d.select_lasso', 'EVT_TWEAK_L', 'ANY', shift=True, ctrl=True)
    kmi_props_setattr(kmi.properties, 'extend', True)
    kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY', ctrl=True)
    kmi_props_setattr(kmi.properties, 'deselect', True)
    kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY', shift=True)
    kmi_props_setattr(kmi.properties, 'extend', True)
    kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_L', 'ANY')
    kmi_props_setattr(kmi.properties, 'extend', False)
    kmi = km.keymap_items.new('paint.vertex_paint', 'LEFTMOUSE', 'PRESS')
    kmi = km.keymap_items.new('paint.brush_colors_flip', 'C', 'PRESS')
    kmi = km.keymap_items.new('paint.sample_color', 'S', 'PRESS')
    kmi = km.keymap_items.new('paint.vertex_color_set', 'G', 'PRESS')
    kmi = km.keymap_items.new('paint.vertex_color_hsv', 'U', 'PRESS', ctrl=True)
    kmi = km.keymap_items.new('paint.vertex_color_levels', 'L', 'PRESS', ctrl=True)
    kmi = km.keymap_items.new('paint.vertex_color_invert', 'I', 'PRESS', ctrl=True)
    kmi = km.keymap_items.new('brush.scale_size', 'LEFT_BRACKET', 'PRESS')
    kmi_props_setattr(kmi.properties, 'scalar', 0.8999999761581421)
    kmi = km.keymap_items.new('brush.scale_size', 'RIGHT_BRACKET', 'PRESS')
    kmi_props_setattr(kmi.properties, 'scalar', 1.1111111640930176)
    kmi = km.keymap_items.new('brush.scale_size', 'A', 'PRESS')
    kmi_props_setattr(kmi.properties, 'scalar', 0.8999999761581421)
    kmi = km.keymap_items.new('brush.scale_size', 'D', 'PRESS')
    kmi_props_setattr(kmi.properties, 'scalar', 1.1111111640930176)
    kmi = km.keymap_items.new('brush.active_index_set', 'ONE', 'PRESS')
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 0)
    kmi = km.keymap_items.new('brush.active_index_set', 'TWO', 'PRESS')
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 1)
    kmi = km.keymap_items.new('brush.active_index_set', 'THREE', 'PRESS')
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 2)
    kmi = km.keymap_items.new('brush.active_index_set', 'FOUR', 'PRESS')
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 3)
    kmi = km.keymap_items.new('brush.active_index_set', 'FIVE', 'PRESS')
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 4)
    kmi = km.keymap_items.new('brush.active_index_set', 'SIX', 'PRESS')
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 5)
    kmi = km.keymap_items.new('brush.active_index_set', 'SEVEN', 'PRESS')
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 6)
    kmi = km.keymap_items.new('brush.active_index_set', 'EIGHT', 'PRESS')
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 7)
    kmi = km.keymap_items.new('brush.active_index_set', 'NINE', 'PRESS')
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 8)
    kmi = km.keymap_items.new('brush.active_index_set', 'ZERO', 'PRESS')
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 9)
    kmi = km.keymap_items.new('brush.active_index_set', 'ONE', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 10)
    kmi = km.keymap_items.new('brush.active_index_set', 'TWO', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 11)
    kmi = km.keymap_items.new('brush.active_index_set', 'THREE', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 12)
    kmi = km.keymap_items.new('brush.active_index_set', 'FOUR', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 13)
    kmi = km.keymap_items.new('brush.active_index_set', 'FIVE', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 14)
    kmi = km.keymap_items.new('brush.active_index_set', 'SIX', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 15)
    kmi = km.keymap_items.new('brush.active_index_set', 'SEVEN', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 16)
    kmi = km.keymap_items.new('brush.active_index_set', 'EIGHT', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 17)
    kmi = km.keymap_items.new('brush.active_index_set', 'NINE', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 18)
    kmi = km.keymap_items.new('brush.active_index_set', 'ZERO', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'mode', 'vertex_paint')
    kmi_props_setattr(kmi.properties, 'index', 19)
    kmi = km.keymap_items.new('wm.radial_control', 'F', 'PRESS')
    kmi_props_setattr(kmi.properties, 'data_path_primary', 'tool_settings.vertex_paint.brush.size')
    kmi_props_setattr(kmi.properties, 'data_path_secondary', 'tool_settings.unified_paint_settings.size')
    kmi_props_setattr(kmi.properties, 'use_secondary', 'tool_settings.unified_paint_settings.use_unified_size')
    kmi_props_setattr(kmi.properties, 'rotation_path', 'tool_settings.vertex_paint.brush.texture_slot.angle')
    kmi_props_setattr(kmi.properties, 'color_path', 'tool_settings.vertex_paint.brush.cursor_color_add')
    kmi_props_setattr(kmi.properties, 'fill_color_path', 'tool_settings.vertex_paint.brush.color')
    kmi_props_setattr(kmi.properties, 'fill_color_override_path', 'tool_settings.unified_paint_settings.color')
    kmi_props_setattr(kmi.properties, 'fill_color_override_test_path', 'tool_settings.unified_paint_settings.use_unified_color')
    kmi_props_setattr(kmi.properties, 'zoom_path', '')
    kmi_props_setattr(kmi.properties, 'image_id', 'tool_settings.vertex_paint.brush')
    kmi_props_setattr(kmi.properties, 'secondary_tex', False)
    kmi = km.keymap_items.new('wm.radial_control', 'F', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'data_path_primary', 'tool_settings.vertex_paint.brush.strength')
    kmi_props_setattr(kmi.properties, 'data_path_secondary', 'tool_settings.unified_paint_settings.strength')
    kmi_props_setattr(kmi.properties, 'use_secondary', 'tool_settings.unified_paint_settings.use_unified_strength')
    kmi_props_setattr(kmi.properties, 'rotation_path', 'tool_settings.vertex_paint.brush.texture_slot.angle')
    kmi_props_setattr(kmi.properties, 'color_path', 'tool_settings.vertex_paint.brush.cursor_color_add')
    kmi_props_setattr(kmi.properties, 'fill_color_path', 'tool_settings.vertex_paint.brush.color')
    kmi_props_setattr(kmi.properties, 'fill_color_override_path', 'tool_settings.unified_paint_settings.color')
    kmi_props_setattr(kmi.properties, 'fill_color_override_test_path', 'tool_settings.unified_paint_settings.use_unified_color')
    kmi_props_setattr(kmi.properties, 'zoom_path', '')
    kmi_props_setattr(kmi.properties, 'image_id', 'tool_settings.vertex_paint.brush')
    kmi_props_setattr(kmi.properties, 'secondary_tex', False)
    kmi = km.keymap_items.new('wm.radial_control', 'F', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'data_path_primary', 'tool_settings.vertex_paint.brush.texture_slot.angle')
    kmi_props_setattr(kmi.properties, 'data_path_secondary', '')
    kmi_props_setattr(kmi.properties, 'use_secondary', '')
    kmi_props_setattr(kmi.properties, 'rotation_path', 'tool_settings.vertex_paint.brush.texture_slot.angle')
    kmi_props_setattr(kmi.properties, 'color_path', 'tool_settings.vertex_paint.brush.cursor_color_add')
    kmi_props_setattr(kmi.properties, 'fill_color_path', 'tool_settings.vertex_paint.brush.color')
    kmi_props_setattr(kmi.properties, 'fill_color_override_path', 'tool_settings.unified_paint_settings.color')
    kmi_props_setattr(kmi.properties, 'fill_color_override_test_path', 'tool_settings.unified_paint_settings.use_unified_color')
    kmi_props_setattr(kmi.properties, 'zoom_path', '')
    kmi_props_setattr(kmi.properties, 'image_id', 'tool_settings.vertex_paint.brush')
    kmi_props_setattr(kmi.properties, 'secondary_tex', False)
    kmi = km.keymap_items.new('brush.stencil_control', 'RIGHTMOUSE', 'PRESS')
    kmi_props_setattr(kmi.properties, 'mode', 'TRANSLATION')
    kmi = km.keymap_items.new('brush.stencil_control', 'RIGHTMOUSE', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'mode', 'SCALE')
    kmi = km.keymap_items.new('brush.stencil_control', 'RIGHTMOUSE', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'mode', 'ROTATION')
    kmi = km.keymap_items.new('brush.stencil_control', 'RIGHTMOUSE', 'PRESS', alt=True)
    kmi_props_setattr(kmi.properties, 'mode', 'TRANSLATION')
    kmi_props_setattr(kmi.properties, 'texmode', 'SECONDARY')
    kmi = km.keymap_items.new('brush.stencil_control', 'RIGHTMOUSE', 'PRESS', shift=True, alt=True)
    kmi_props_setattr(kmi.properties, 'mode', 'SCALE')
    kmi_props_setattr(kmi.properties, 'texmode', 'SECONDARY')
    kmi = km.keymap_items.new('brush.stencil_control', 'RIGHTMOUSE', 'PRESS', ctrl=True, alt=True)
    kmi_props_setattr(kmi.properties, 'mode', 'ROTATION')
    kmi_props_setattr(kmi.properties, 'texmode', 'SECONDARY')
    kmi = km.keymap_items.new('wm.context_toggle', 'M', 'PRESS')
    kmi_props_setattr(kmi.properties, 'data_path', 'vertex_paint_object.data.use_paint_mask')
    kmi = km.keymap_items.new('wm.context_toggle', 'S', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'data_path', 'tool_settings.vertex_paint.brush.use_smooth_stroke')
    kmi = km.keymap_items.new('wm.call_menu', 'R', 'PRESS')
    kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_angle_control')
    kmi = km.keymap_items.new('wm.context_menu_enum', 'E', 'PRESS')
    kmi_props_setattr(kmi.properties, 'data_path', 'tool_settings.vertex_paint.brush.stroke_method')

#Mesh
    km = kc.keymaps.new(name='Mesh')
#    kmi = km.keymap_items.new('view3d.extrude_normal', 'EVT_TWEAK_L', 'ANY', alt=True, shift=True)
    kmi = km.keymap_items.new("mesh.dupli_extrude_cursor", 'V', 'PRESS')
    kmi = km.keymap_items.new('view3d.select_through_border', 'EVT_TWEAK_L', 'ANY')
    kmi = km.keymap_items.new('view3d.select_through_border_subtract', 'EVT_TWEAK_L', 'ANY', ctrl=True)
    kmi = km.keymap_items.new('view3d.select_through_border_add', 'EVT_TWEAK_L', 'ANY', shift=True)
    kmi = km.keymap_items.new("wm.call_menu_pie","A","PRESS", shift=True).properties.name="pie.add"
    kmi = km.keymap_items.new("screen.userpref_show","TAB","PRESS", ctrl=True)
    kmi = km.keymap_items.new("view3d.subdivision_toggle","TAB","PRESS")
    kmi = km.keymap_items.new('mesh.select_all', 'SELECTMOUSE', 'CLICK', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'INVERT')
    kmi = km.keymap_items.new('mesh.shortest_path_pick', 'LEFTMOUSE', 'CLICK',ctrl=True, shift=True).properties.use_fill=True
    kmi = km.keymap_items.new('mesh.select_linked', 'SELECTMOUSE', 'DOUBLE_CLICK')
    kmi = km.keymap_items.new('mesh.select_linked', 'SELECTMOUSE', 'DOUBLE_CLICK', shift=True)
    kmi = km.keymap_items.new('mesh.select_more', 'WHEELINMOUSE', 'PRESS',ctrl=True, shift=True)    
    kmi = km.keymap_items.new('mesh.select_less', 'WHEELOUTMOUSE', 'PRESS',ctrl=True, shift=True)
    kmi = km.keymap_items.new('mesh.select_more', 'Z', 'PRESS',alt=True)    
    kmi = km.keymap_items.new('mesh.select_next_item', 'WHEELINMOUSE', 'PRESS', shift=True)
    kmi = km.keymap_items.new('mesh.select_next_item', 'Z', 'PRESS', shift=True)
    kmi = km.keymap_items.new('mesh.select_prev_item', 'WHEELOUTMOUSE', 'PRESS', shift=True)
    kmi = km.keymap_items.new('mesh.edgering_select', 'SELECTMOUSE', 'DOUBLE_CLICK', alt=True).properties.extend = False
    kmi = km.keymap_items.new('mesh.loop_multi_select', 'SELECTMOUSE', 'DOUBLE_CLICK', alt=True, shift=True)
    kmi = km.keymap_items.new('mesh.loop_select', 'SELECTMOUSE', 'CLICK', alt=True, shift=True).properties.extend = True

    kmi = km.keymap_items.new('view3d.manipulator', k_manip, 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'release_confirm', True)
    kmi_props_setattr(kmi.properties, 'use_accurate', False)
    kmi_props_setattr(kmi.properties, 'use_planar_constraint', True)
    kmi = km.keymap_items.new('view3d.manipulator', k_manip, 'PRESS')
    kmi_props_setattr(kmi.properties, 'release_confirm', True)
    kmi_props_setattr(kmi.properties, 'use_accurate', False)
    kmi_props_setattr(kmi.properties, 'use_planar_constraint', False)

    kmi = km.keymap_items.new("wm.call_menu_pie","FOUR","PRESS").properties.name="GPENCIL_PIE_tool_palette"
    kmi = km.keymap_items.new("mesh.select_prev_item","TWO","PRESS")
    kmi = km.keymap_items.new("mesh.select_next_item","THREE","PRESS")
    kmi = km.keymap_items.new("mesh.select_less","TWO","PRESS", ctrl=True)
    kmi = km.keymap_items.new("mesh.select_more","THREE","PRESS", ctrl=True)
    kmi = km.keymap_items.new("transform.edge_slide", "SPACE", "DOUBLE_CLICK")
    kmi = km.keymap_items.new("mesh.push_and_slide","G","PRESS", shift=True)
    kmi_props_setattr(kmi.properties, 'use_even_offset', True)
    kmi = km.keymap_items.new('mesh.separate_and_select', 'P', 'PRESS')
    kmi = km.keymap_items.new('view3d.extrude_normal', 'E', 'PRESS')
    kmi = km.keymap_items.new('mesh.bridge_edge_loops', 'B', 'PRESS', shift=True)
    kmi = km.keymap_items.new('mesh.smart_bevel','B', 'PRESS')
    kmi = km.keymap_items.new('mesh.merge', 'J', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'type', 'LAST')
    kmi = km.keymap_items.new('mesh.reveal', 'H', 'PRESS', ctrl=True, shift=True)
#Object Mode
    km = kc.keymaps.new(name='Object Mode')
    kmi = km.keymap_items.new('view3d.smart_delete', 'X', 'PRESS')
    kmi = km.keymap_items.new("wm.call_menu_pie","FOUR","PRESS").properties.name="GPENCIL_PIE_tool_palette"
    kmi = km.keymap_items.new('object.hide_view_clear', 'H', 'PRESS', ctrl=True, shift=True)
    kmi = km.keymap_items.new('object.select_all', 'SELECTMOUSE', 'CLICK', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'INVERT')
    kmi = km.keymap_items.new('view3d.manipulator', k_manip, 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'release_confirm', True)
    kmi_props_setattr(kmi.properties, 'use_accurate', False)
    kmi_props_setattr(kmi.properties, 'use_planar_constraint', True)
    kmi = km.keymap_items.new('view3d.manipulator', k_manip, 'PRESS')
    kmi_props_setattr(kmi.properties, 'release_confirm', True)
    kmi_props_setattr(kmi.properties, 'use_accurate', False)
    kmi_props_setattr(kmi.properties, 'use_planar_constraint', False)
# Map Curve
    km = kc.keymaps.new('Curve', space_type='EMPTY', region_type='WINDOW', modal=False)
    kmi = km.keymap_items.new('curve.select_linked', 'SELECTMOUSE', 'DOUBLE_CLICK', shift=True)
    kmi = km.keymap_items.new('curve.select_linked_pick', 'SELECTMOUSE', 'DOUBLE_CLICK')
    kmi = km.keymap_items.new('curve.reveal', 'H', 'PRESS', ctrl=True, shift=True)
    kmi = km.keymap_items.new('curve.draw', 'LEFTMOUSE', 'PRESS', alt=True)
    kmi_props_setattr(kmi.properties, 'wait_for_input', False)
    kmi = km.keymap_items.new('view3d.manipulator', k_manip, 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'release_confirm', True)
    kmi_props_setattr(kmi.properties, 'use_accurate', False)
    kmi_props_setattr(kmi.properties, 'use_planar_constraint', True)
    kmi = km.keymap_items.new('view3d.manipulator', k_manip, 'PRESS')
    kmi_props_setattr(kmi.properties, 'release_confirm', True)
    kmi_props_setattr(kmi.properties, 'use_accurate', False)
    kmi_props_setattr(kmi.properties, 'use_planar_constraint', False)
# Outliner
    km = kc.keymaps.new('Outliner', space_type='OUTLINER', region_type='WINDOW', modal=False)
    kmi = km.keymap_items.new('outliner.select_border', 'EVT_TWEAK_L', 'ANY')
    kmi = km.keymap_items.new('outliner.show_active', k_nav, 'PRESS', ctrl=True, shift=True)
    kmi = km.keymap_items.new('wm.delete_without_prompt', 'X', 'PRESS')
# Map Timeline
    km = kc.keymaps.new('Timeline', space_type='TIMELINE', region_type='WINDOW', modal=False)

    kmi = km.keymap_items.new('time.start_frame_set', 'S', 'PRESS')
    kmi = km.keymap_items.new('time.end_frame_set', 'E', 'PRESS')
    kmi = km.keymap_items.new('time.view_all', 'HOME', 'PRESS')
    kmi = km.keymap_items.new('time.view_all', k_viewfit, 'PRESS', ctrl=True, shift=True)
    kmi = km.keymap_items.new('time.view_all', 'NDOF_BUTTON_FIT', 'PRESS')
    kmi = km.keymap_items.new('time.view_frame', 'NUMPAD_0', 'PRESS')
    kmi = km.keymap_items.new('screen.animation_play', k_menu, 'PRESS')



def register():
    Keymap_Heavypoly()

def unregister():
    Keymap_Heavypoly()

if __name__ == "__main__":
    register()
