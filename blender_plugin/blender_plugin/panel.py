import bpy

class TransformPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Transform Sender"
    bl_idname = "OBJECT_PT_transform_sender"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Transform Sender"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        if obj:
            row = layout.row()
            row.label(text="Selected Object: " + obj.name)

            row = layout.row()
            row.prop(obj, "location")

            row = layout.row()
            row.prop(obj, "rotation_euler")

            row = layout.row()
            row.prop(obj, "scale")

            row = layout.row()
            layout.prop(context.scene, "endpoint")

            row = layout.row()
            row.operator("object.send_transform", text="Submit")
        else:
            layout.label(text="No object selected")

def register():
    bpy.utils.register_class(TransformPanel)
    bpy.types.Scene.endpoint = bpy.props.EnumProperty(
        name="API Endpoint",
        items=[
            ('transform', "Transform", ""),
            ('translation', "Translation", ""),
            ('rotation', "Rotation", ""),
            ('scale', "Scale", ""),
        ],
        default='transform',
    )

def unregister():
    bpy.utils.unregister_class(TransformPanel)
    del bpy.types.Scene.endpoint
