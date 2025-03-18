import bpy
import os
import sys

scene = bpy.context.scene
mainScreen = bpy.context.window


mainScreen.scene = bpy.data.scenes["PreComp"]



# -- output
bpy.data.scenes["PreComp"].node_tree.nodes["File Output"].mute = True #AO
bpy.data.scenes["PreComp"].node_tree.nodes["File Output.003"].mute = True #Z
bpy.data.scenes["PreComp"].node_tree.nodes["File Output.002"].mute = False #Beauty
bpy.data.scenes["PreComp"].node_tree.nodes["BG_EXR"].mute = False
bpy.data.scenes["PreComp"].node_tree.nodes["File Output.008"].mute = True #BG
bpy.data.scenes["PreComp"].node_tree.nodes["CH_EXR"].mute = False
bpy.data.scenes["PreComp"].node_tree.nodes["FG_EXR"].mute = True
bpy.data.scenes["PreComp"].node_tree.nodes["File Output.005"].mute = True #CH
bpy.data.scenes["PreComp"].node_tree.nodes["File Output.007"].mute = True #Normal
bpy.data.scenes["PreComp"].node_tree.nodes["File Output.010"].mute = True #VolLGT

# -- layer
bpy.data.scenes["MAIN"].view_layers["_out"].use = False
bpy.data.scenes["MAIN"].view_layers["_CH"].use = True
bpy.data.scenes["MAIN"].view_layers["_BG"].use = True
bpy.data.scenes["MAIN"].view_layers["_FG"].use = False
bpy.data.scenes["AO"].view_layers["_out"].use = False
bpy.data.scenes["NOR"].view_layers["_out"].use = False
bpy.data.scenes["PreComp"].view_layers["_Crypto"].use = True

bpy.ops.tk_render.apply_settings()
bpy.data.scenes["PreComp"].render.fps = 25
bpy.data.scenes["PreComp"].render.resolution_x = 1920
bpy.data.scenes["PreComp"].render.resolution_y = 1080


# bpy.context.scene.cgru.pause = False
bpy.ops.wm.save_mainfile(compress=True, relative_remap=True)

# bpy.ops.cgru.submit()
