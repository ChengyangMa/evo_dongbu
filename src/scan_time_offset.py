import subprocess
import numpy as np
import re

REF = "data/mocap_marker_1173.tum"
EST = "data/slam_clean.tum"

offsets = np.arange(-3.0, 3.001, 0.005)

best_rmse = float("inf")
best_offset = None

pattern = re.compile(r"rmse\s+([0-9.eE+-]+)")

for off in offsets:
    cmd = [
        "evo_ape", "tum", REF, EST,
        "--align",
        "--pose_relation", "trans_part",
        "--t_max_diff", "0.005",
        "--t_offset", f"{off}",
        "-va"
    ]

    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        m = pattern.search(out)
        if m:
            rmse = float(m.group(1))
            if rmse < best_rmse:
                best_rmse = rmse
                best_offset = off
                print(f"[BEST] offset={off:.3f}s  rmse={rmse:.4f}")
    except subprocess.CalledProcessError:
        continue

print("\n=== 最优结果 ===")
print(f"t_offset = {best_offset:.3f} s")
print(f"RMSE     = {best_rmse:.4f} m")
