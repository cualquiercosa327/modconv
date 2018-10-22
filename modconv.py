from pyassimp import *
import datetime
scale = 32 # Integer that scales the model. Default is 32.
fileName = "cube5.fbx"
flag = 0
texture = 0
coord = 0

# Default RGBA values for when the imported model has no RGBA data (0-255)
rgbaR = 0
rgbaG = 0
rgbaB = 0
rgbaA = 255
loopCount = 0
scene = load(fileName
)
assert len(scene.meshes)
mesh = scene.meshes[0]
assert len(mesh.vertices)
vertexCount = len(mesh.vertices)
vertexheader = open("output.h", "w")
currDate = str(datetime.datetime.now())

vertexheader.write("/*\n* VERTICES IN GBI FORMAT\n* GENERATED BY MODCONV ON: " + currDate + "\n*/\n\n")
vertexheader.write("#include <nusys.h> //This is temporary\n")
vertexheader.write("Vtx output__v[] = {\n")

print("Checking for vertex colors...")
try:
    assert len(mesh.colors[0])
    usingvrgba = True
    print("There are vertex colors.")
except:
    print("There are no vertex colors.")
    usingvrgba = False


while (loopCount != vertexCount - 1):
    print("Generating vertex " + str(loopCount))
    vertX = str(int(mesh.vertices[loopCount][0]) * scale)
    vertY = str(int(mesh.vertices[loopCount][1]) * scale)
    vertZ = str(int(mesh.vertices[loopCount][2]) * scale)
    # Vertex RGBA
    if(usingvrgba == True):
        rgbaR = str(int(mesh.colors[0][loopCount][0] * 255))
        rgbaG = str(int(mesh.colors[0][loopCount][1] * 255))
        rgbaB = str(int(mesh.colors[0][loopCount][2] * 255))
        rgbaA = str(int(mesh.colors[0][loopCount][3] * 255))
    else:
        rgbaR = str(int(rgbaR))
        rgbaG = str(int(rgbaG))
        rgbaB = str(int(rgbaB))
        rgbaA = str(int(rgbaA))
    vertexheader.write("{   " + vertX + ",   " + vertY + ",   " + vertZ + ",0,   0,   0," + rgbaR + "," + rgbaG + "," + rgbaB + "," + rgbaA + "},\n")
    loopCount = loopCount + 1

lCPrnt = str(loopCount)
print("Generating vertex " + lCPrnt)
vertX = str(int(mesh.vertices[loopCount][0]) * scale)
vertY = str(int(mesh.vertices[loopCount][1]) * scale)
vertZ = str(int(mesh.vertices[loopCount][2]) * scale)
# Vertex RGBA
if(usingvrgba == True):
    rgbaR = str(int(mesh.colors[0][loopCount][0] * 255))
    rgbaG = str(int(mesh.colors[0][loopCount][1] * 255))
    rgbaB = str(int(mesh.colors[0][loopCount][2] * 255))
    rgbaA = str(int(mesh.colors[0][loopCount][3] * 255))
else:
    rgbaR = str(int(rgbaR))
    rgbaG = str(int(rgbaG))
    rgbaB = str(int(rgbaB))
    rgbaA = str(int(rgbaA))

vertexheader.write("{   " + vertX + ",   " + vertY + ",   " + vertZ + ",0,   0,   0," + rgbaR + "," + rgbaG + "," + rgbaB + "," + rgbaA + "}};\n")

print("Generating displaylist")
outputcfile = open("output.c", "w")
outputcfile.write("/*\n* DISPLAYLIST IN GBI FORMAT\n* GENERATED BY MODCONV ON: " + currDate + "\n*/\n\n//Some decent defaults\n")
# Generate some sane defaults.
outputcfile.write("Gfx output__dl[] = {\ngsDPPipeSync(),\ngsDPSetCycleType(G_CYC_1CYCLE),\ngsDPSetRenderMode(G_RM_AA_ZB_OPA_SURF, G_RM_AA_ZB_OPA_SURF2),\ngsSPClearGeometryMode((G_SHADE|G_SHADING_SMOOTH|G_LIGHTING|G_TEXTURE_GEN|G_TEXTURE_GEN_LINEAR|G_CULL_BOTH|G_FOG)),\ngsSPSetGeometryMode( G_ZBUFFER | G_CULL_BACK | G_SHADE | G_SHADING_SMOOTH | G_LIGHTING ),\ngsDPSetColorDither(G_CD_BAYER),\ngsDPSetCombineMode(G_CC_MULPRIMSHADE,     G_CC_MULPRIMSHADE), /* N64-SHADE-TYPE-G */\n")
loopCount = 0
outputcfile.write("gsSPEndDisplayList(),\n};") # end the displaylist
