#! usr/bin/env python3

import open3d as o3d
import numpy as np

seg_name='/home/utk/Perception/data/sets/nuscenes/lidarseg/v1.0-mini/4484110755904050a880043268149497_lidarseg.bin'
seg=np.fromfile(seg_name, dtype=np.uint8)

pcd_name='/home/utk/Perception/data/sets/nuscenes/samples/LIDAR_TOP/n008-2018-08-28-16-43-51-0400__LIDAR_TOP__1535489296047917.pcd.bin'
scan=np.fromfile(pcd_name, dtype=np.float32)
points = scan.reshape((-1, 5))[:, :4]
height = points[:,2]
#print(height)

color = np.zeros([len(height), 3])
for i in range(len(height)):
    if height[i] < 0:
        color[i, 0] = abs(height[i])*0.2
        color[i, 1] = abs(height[i])*0.2
        color[i, 2] = 30
    elif height[i] > 0:
        color[i, 0] = 60
        color[i, 1] = height[i]*0.1
        color[i, 2] = height[i]*0.2
    else:
        color[i, 0] = 255
        color[i, 1] = 255
        color[i, 2] = 255     

print(color)
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points[:, :3])
pcd.colors = o3d.utility.Vector3dVector(color)

o3d.visualization.draw_geometries([pcd])