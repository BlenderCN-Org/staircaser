import bpy
import json

''' 
You need to paste this script into blender 'Text Editor' window and call it
from there. The script expects to find /tmp/result.json generated by
staircaser.py. It iterates over json's elements and draws them with blender
drawing commands bpy.ops.foo. 

Blender geometries are defined by center + size. For CAD p0 + p1 are probably
better. The json describes the elements in both standards.

You can adapt this script for AutoCad or any other 3D software. 'import bpy' is
blender specific -- you need to remove that line. You can rewrite this script
from python to another language that your software supports. 
'''

f=open("/tmp/result.json", 'r')
g=json.load(f)
f.close()
tx=0
for k,v in g['staircases'].items():
    for i in v:
        bpy.ops.mesh.primitive_cube_add(location=i['center'])
        bpy.ops.transform.resize(value=i['size'])
        bpy.ops.transform.translate(value=(tx,0,0))
    tx+=10

