from collections import namedtuple

TensorOutput = namedtuple('TensorOutput',
                          ['vertices', 'joints', 'betas', 'expression', 'global_orient', 'body_pose', 'left_hand_pose',
                           'right_hand_pose', 'jaw_pose', 'transl', 'full_pose'])

example_output = TensorOutput(
    vertices=[0.0, 1.0, 2.0],  # 假设的顶点坐标数据
    joints=[0.1, 0.2, 0.3],    # 假设的关节位置数据
    betas=[0.01, 0.02, 0.03],  # 形状系数
    expression=[0.1, 0.1, 0.1],  # 表情参数
    global_orient=[0, 0, 0],   # 全局定向
    body_pose=[0.5, 0.5, 0.5],  # 身体姿态
    left_hand_pose=[0, 0, 0],  # 左手姿态
    right_hand_pose=[0, 0, 0],  # 右手姿态
    jaw_pose=[0.05, 0.05, 0.05],  # 下巴姿态
    transl=[5, 5, 5],          # 位移
    full_pose=[1, 1, 1]        # 完整姿态
)

# 访问特定字段
print(example_output.vertices)
