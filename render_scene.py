
import os
import numpy as np
from xvfbwrapper import Xvfb

# 使用Xvfb创建虚拟显示
vdisplay = Xvfb()
vdisplay.start()

import pyrender
import trimesh

# 示例顶点数据和面数据
vertices = np.array([
    [-0.5, -0.5, 0.0],
    [0.5, -0.5, 0.0],
    [0.5, 0.5, 0.0],
    [-0.5, 0.5, 0.0]
])

faces = np.array([
    [0, 1, 2],
    [0, 2, 3]
])

# 示例关节数据
joints = np.array([
    [0.0, 0.0, 0.1],
    [0.0, 0.0, -0.1]
])

plotting_module = 'pyrender'
plot_joints = True

if plotting_module == 'pyrender':
    # 创建顶点颜色
    vertex_colors = np.ones([vertices.shape[0], 4]) * [0.3, 0.3, 0.3, 0.8]
    # 创建三角网格
    tri_mesh = trimesh.Trimesh(vertices, faces, vertex_colors=vertex_colors)
    mesh = pyrender.Mesh.from_trimesh(tri_mesh)

    # 创建场景并添加网格
    scene = pyrender.Scene()
    scene.add(mesh)

    if plot_joints:
        # 创建关节球体
        sm = trimesh.creation.uv_sphere(radius=0.005)
        sm.visual.vertex_colors = [0.9, 0.1, 0.1, 1.0]
        tfs = np.tile(np.eye(4), (len(joints), 1, 1))
        tfs[:, :3, 3] = joints
        joints_pcl = pyrender.Mesh.from_trimesh(sm, poses=tfs)
        scene.add(joints_pcl)

    # 使用pyrender进行渲染
    pyrender.Viewer(scene, use_raymond_lighting=True)

# 停止虚拟显示
vdisplay.stop()
