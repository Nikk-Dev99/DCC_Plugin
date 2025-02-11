bl_info = {
    "name": "Flask Connector",
    "blender": (3, 0, 0),
    "category": "Object",
}

import bpy
import requests

SERVER_URL = "http://127.0.0.1:5000"

# Send Transform Data
def send_transform_data():
    obj = bpy.context.object
    if obj is None:
        return
    
    data = {
        "position": list(obj.location),
        "rotation": list(obj.rotation_euler),
        "scale": list(obj.scale),
    }
    
    response = requests.post(f"{SERVER_URL}/transform", json=data)
    print("Response:", response.json())

# Blender Operator (Button Click)
class SendTransformOperator(bpy.types.Operator):
    bl_idname = "object.send_transform"
    bl_label = "Send Transform"

    def execute(self, context):
        send_transform_data()
        return {'FINISHED'}

# UI Panel
class TransformPanel(bpy.types.Panel):
    bl_label = "Flask Connector"
    bl_idname = "OBJECT_PT_transform_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Flask"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.send_transform")

# Register Plugin
def register():
    bpy.utils.register_class(SendTransformOperator)
    bpy.utils.register_class(TransformPanel)

def unregister():
    bpy.utils.unregister_class(SendTransformOperator)
    bpy.utils.unregister_class(TransformPanel)

if __name__ == "__main__":
    register()
