# 3-5
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
for i in range(0,20):
    mc.setBlock(x,y,z+i,41)
    