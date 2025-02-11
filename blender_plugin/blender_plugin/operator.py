import bpy
import requests
import json

class SendTransformOperator(bpy.types.Operator):
    """Send Transform Data to Flask Server"""
    bl_idname = "object.send_transform"
    bl_label = "Send Transform"

    def execute(self, context):
        obj = context.object
        if not obj:
            self.report({'ERROR'}, "No object selected!")
            return {'CANCELLED'}

        transform_data = {
            "name": obj.name,
            "position": list(obj.location),
            "rotation": list(obj.rotation_euler),
            "scale": list(obj.scale),
        }

        endpoint = context.scene.endpoint
        url = f"http://127.0.0.1:5000/{endpoint}"  # Flask server URL

        try:
            response = requests.post(url, json=transform_data)
            if response.status_code == 200:
                self.report({'INFO'}, "Data sent successfully!")
            else:
                self.report({'ERROR'}, f"Server error: {response.status_code}")
        except Exception as e:
            self.report({'ERROR'}, f"Failed to send data: {str(e)}")

        return {'FINISHED'}

def register():
    bpy.utils.register_class(SendTransformOperator)

def unregister():
    bpy.utils.unregister_class(SendTransformOperator)
