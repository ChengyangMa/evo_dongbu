import os

REF = "data/mocap_marker_1173.tum"
EST = "data/slam_clean.tum"
# 检查文件是否存在
print("检查参考轨迹文件:", REF, "存在:", os.path.exists(REF))
print("检查估计轨迹文件:", EST, "存在:", os.path.exists(EST))

# 查看文件头几行
if os.path.exists(REF):
    with open(REF, 'r') as f:
        print("参考文件前5行:")
        for i in range(5):
            print(f.readline().strip())

if os.path.exists(EST):
    with open(EST, 'r') as f:
        print("\n估计文件前5行:")
        for i in range(5):
            print(f.readline().strip())