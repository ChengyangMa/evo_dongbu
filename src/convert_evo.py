import numpy as np

# 读取文件并调整时间
def adjust_time_to_zero(input_file, output_file):
    # 读取文件数据
    data = np.loadtxt(input_file)
    
    # 获取文件的第一行时间戳
    first_time = data[0, 0]
    
    # 调整时间为从零开始
    data[:, 0] -= first_time
    
    # 保存调整后的数据到输出文件
    np.savetxt(output_file, data, fmt='%f', delimiter=' ')

# 设置文件路径
slam_file = "data/slam_raw.txt"
motion_capture_file = "data/motive_raw.txt"

# 设置输出文件路径
slam_output_file = "slam_adjusted.txt"
motion_capture_output_file = "motion_capture_adjusted.txt"

# 调整SLAM轨迹时间
adjust_time_to_zero(slam_file, slam_output_file)
print(f"SLAM轨迹时间已调整为从零开始，保存到 {slam_output_file}")

# 调整动作捕捉轨迹时间
adjust_time_to_zero(motion_capture_file, motion_capture_output_file)
print(f"动作捕捉轨迹时间已调整为从零开始，保存到 {motion_capture_output_file}")
