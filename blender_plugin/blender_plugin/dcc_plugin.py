import bpy

# Yeh function translation apply karega
def apply_translation(obj, x, y, z):
    obj.location = (x, y, z)

# Yeh function rotation apply karega
def apply_rotation(obj, x, y, z):
    obj.rotation_euler = (x, y, z)

# Yeh function scale apply karega
def apply_scale(obj, x, y, z):
    obj.scale = (x, y, z)

# Blender scene mein selected object ko transform karna
selected_object = bpy.context.active_object

apply_translation(selected_object, 1, 2, 3)
apply_rotation(selected_object, 0, 0, 1.57)
apply_scale(selected_object, 2, 2, 2)
