#! usr/bin/env python3

import open3d as o3d
import numpy as np
from data_classes import RadarPointCloud


pcd_name='/home/utk/Perception/data/sets/nuscenes/samples/RADAR_FRONT/n008-2018-08-01-15-16-36-0400__RADAR_FRONT__1533151603555991.pcd'
scan=RadarPointCloud.from_file(pcd_name)
# points = scan.reshape((-1, 5))[:, :4]
radar_points = scan.points.T
#print(radar_points)

vel_x = radar_points[:,8] #compensated x component of velocity of the ego vehicle
vel_y = radar_points[:,9] #compensated y component of velocity of the ego vehicle
velocity = np.sqrt((vel_x+vel_y)*(vel_x+vel_y))
print(velocity)

color = np.zeros([len(velocity), 3])
for i in range(len(velocity)):
    if velocity[i] < 0.05:
        color[i, 0] = velocity[i]
        color[i, 1] = velocity[i]*0
        color[i, 2] = velocity[i]*0
    elif velocity[i] < 0.2:
        color[i, 0] = velocity[i]*0
        color[i, 1] = velocity[i]
        color[i, 2] = velocity[i]*0
    else:
        color[i, 0] = velocity[i]*0
        color[i, 1] = velocity[i]*0
        color[i, 2] = velocity[i]

# velocity_x = points

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(radar_points[:, :3])
pcd.colors = o3d.utility.Vector3dVector(color)

o3d.visualization.draw_geometries([pcd])