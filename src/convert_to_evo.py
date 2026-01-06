import csv
import re

# ========== 输入文件 ==========
MOCAP_CSV = "data/Take 2026-01-05 06.23.38 PM.csv"
SLAM_RAW  = "data/slam_raw.txt"
#data/slam_raw.txt

# ========== 输出文件 ==========
MOCAP_TUM = "data/mocap_clean2.tum"
SLAM_TUM  = "data/slam_clean2.tum"


# ---------------------------------------------------------
# 1. 处理 SLAM 轨迹
# ---------------------------------------------------------
slam_data = []

with open(SLAM_RAW, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        # 删除非法省略号
        line = line.replace("...", "")

        parts = line.split()
        if len(parts) != 8:
            continue

        try:
            row = [float(p) for p in parts]
        except ValueError:
            continue

        slam_data.append(row)

if not slam_data:
    raise RuntimeError("SLAM 文件解析失败")

# 时间戳归零
slam_t0 = slam_data[0][0]

with open(SLAM_TUM, "w") as f:
    for t, tx, ty, tz, qx, qy, qz, qw in slam_data:
        t -= slam_t0
        f.write(
            f"{t:.6f} {tx:.9f} {ty:.9f} {tz:.9f} "
            f"{qx:.9f} {qy:.9f} {qz:.9f} {qw:.9f}\n"
        )

print(f"[OK] SLAM -> {SLAM_TUM}")


# ---------------------------------------------------------
# 2. 处理动作捕捉 CSV
# ---------------------------------------------------------
mocap_rows = []

with open(MOCAP_CSV, "r", encoding="utf-8", errors="ignore") as f:
    reader = csv.reader(f)

    # 跳到真正数据头
    for row in reader:
        if len(row) >= 5 and row[0] == "Frame" and "Time" in row[1]:
            break

    # 读取数据
    for row in reader:
        if len(row) < 5:
            continue
        try:
            t = float(row[1])
            x = float(row[2]) / 1000.0  # mm -> m
            y = float(row[3]) / 1000.0
            z = float(row[4]) / 1000.0
        except ValueError:
            continue

        mocap_rows.append((t, x, y, z))

if not mocap_rows:
    raise RuntimeError("动作捕捉 CSV 解析失败")

# 时间戳是否归零：建议是
t0 = mocap_rows[0][0]

with open(MOCAP_TUM, "w") as f:
    for t, x, y, z in mocap_rows:
        t -= t0
        f.write(
            f"{t:.6f} {x:.9f} {y:.9f} {z:.9f} 0 0 0 1\n"
        )

print(f"[OK] Mocap -> {MOCAP_TUM}")


# ---------------------------------------------------------
# 3. 完成
# ---------------------------------------------------------
print("\n转换完成，可直接用于 evo：")
print(f"  - {MOCAP_TUM}")
print(f"  - {SLAM_TUM}")
