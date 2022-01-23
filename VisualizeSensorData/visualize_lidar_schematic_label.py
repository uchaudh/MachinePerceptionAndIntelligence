#! usr/bin/env python3

import open3d as o3d
import numpy as np

seg_name='/home/utk/Perception/data/sets/nuscenes/lidarseg/v1.0-mini/4484110755904050a880043268149497_lidarseg.bin'
seg=np.fromfile(seg_name, dtype=np.uint8)
# for x in range(len(seg)):
#     print(seg[x])

color = np.zeros([len(seg), 3])
for i in range(len(seg)):
    if seg[i] == 17:
        color[i, 0] = seg[i]
        color[i, 1] = seg[i]*0
        color[i, 2] = seg[i]*0
    elif seg[i] == 28:
        color[i, 0] = seg[i]*0
        color[i, 1] = seg[i]
        color[i, 2] = seg[i]*0
    else:
        color[i, 0] = seg[i]*0
        color[i, 1] = seg[i]*0
        color[i, 2] = seg[i]

pcd_name='/home/utk/Perception/data/sets/nuscenes/samples/LIDAR_TOP/n008-2018-08-28-16-43-51-0400__LIDAR_TOP__1535489296047917.pcd.bin'
scan=np.fromfile(pcd_name, dtype=np.float32)
points = scan.reshape((-1, 5))[:, :4]

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points[:, :3])
pcd.colors = o3d.utility.Vector3dVector(color)

o3d.visualization.draw_geometries([pcd])