#!/bin/bash

# 读取文件并调整时间
adjust_time_to_zero() {
    input_file=$1
    output_file=$2

    # 获取文件的第一行时间戳
    first_time=$(awk 'NR==1 {print $1}' $input_file)

    # 创建输出文件并写入调整后的数据
    awk -v first_time=$first_time '{ $1 = $1 - first_time; print $0 }' $input_file > $output_file
}

# 设置文件路径
slam_file="data/slam_raw.txt"
motion_capture_file="data/motive_raw.txt"

# 设置输出文件路径
slam_output_file="slam_adjusted.txt"
motion_capture_output_file="motion_capture_adjusted.txt"

# 调整SLAM轨迹时间
adjust_time_to_zero $slam_file $slam_output_file
echo "SLAM轨迹时间已调整为从零开始，保存到 $slam_output_file"

# 调整动作捕捉轨迹时间
adjust_time_to_zero $motion_capture_file $motion_capture_output_file
echo "动作捕捉轨迹时间已调整为从零开始，保存到 $motion_capture_output_file"
