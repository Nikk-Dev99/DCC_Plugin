import bpy

def get_selected_object():
    return bpy.context.object if bpy.context.object else None
