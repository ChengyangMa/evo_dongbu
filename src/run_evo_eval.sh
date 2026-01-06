#!/usr/bin/env bash
set -e

# ===== 默认参数 =====
T_OFFSET=-2.710
T_MAX_DIFF=0.001

# ===== 解析命令行参数 =====
for arg in "$@"; do
  case $arg in
    --t_offset=*)
      T_OFFSET="${arg#*=}"
      shift
      ;;
    --t_max_diff=*)
      T_MAX_DIFF="${arg#*=}"
      shift
      ;;
    *)
      ;;
  esac
done

REF=data/mocap_marker_1173.tum
EST=data/slam_clean.tum
OUTDIR=evo_results

mkdir -p ${OUTDIR}

echo "=== 使用参数 ==="
echo "t_offset    = ${T_OFFSET}"
echo "t_max_diff  = ${T_MAX_DIFF}"

echo "=== 基本检查 ==="
evo_traj tum ${REF} ${EST} --full_check > ${OUTDIR}/check.txt

echo "=== APE（仅平移） ==="
# evo_ape tum ${REF} ${EST} \
#   --t_offset ${T_OFFSET} \
#   --t_max_diff ${T_MAX_DIFF} \
#   --align \
#   --pose_relation trans_part \
#   -va \
#   --save_results ${OUTDIR}/ape_trans.zip \
#   --plot \
#   > ${OUTDIR}/ape_trans.txt

evo_ape tum ${REF} ${EST} \
  --t_max_diff ${T_MAX_DIFF} \
  --align \
  --pose_relation trans_part \
  -va \
  --save_results ${OUTDIR}/ape_trans.zip \
  --plot \
  > ${OUTDIR}/ape_trans.txt

echo "=== 完成 ==="
