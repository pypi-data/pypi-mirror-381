
#include "../machete_mm_launcher.cuh"

namespace machete {
    

struct sch_128x64_2x1x1_TmaMI__TmaCoop_streamK {
  using TileShapeNM = Shape<_128, _64>;
  using ClusterShape = Shape<_2, _1, _1>;
  // TODO: Reimplement
  // using KernelSchedule   = cutlass::gemm::KernelTmaWarpSpecializedCooperative;
  using EpilogueSchedule = cutlass::epilogue::TmaWarpSpecializedCooperative;
  using TileScheduler    = cutlass::gemm::StreamKScheduler;
  using EpilogueTileType = cutlass::epilogue::collective::EpilogueTileAuto;
};

struct sch_128x16_1x1x1_TmaMI__TmaCoop_streamK {
  using TileShapeNM = Shape<_128, _16>;
  using ClusterShape = Shape<_1, _1, _1>;
  // TODO: Reimplement
  // using KernelSchedule   = cutlass::gemm::KernelTmaWarpSpecializedCooperative;
  using EpilogueSchedule = cutlass::epilogue::TmaWarpSpecializedCooperative;
  using TileScheduler    = cutlass::gemm::StreamKScheduler;
  using EpilogueTileType = cutlass::epilogue::collective::EpilogueTileAuto;
};

struct sch_256x16_1x1x1_TmaMI__TmaCoop_streamK {
  using TileShapeNM = Shape<_256, _16>;
  using ClusterShape = Shape<_1, _1, _1>;
  // TODO: Reimplement
  // using KernelSchedule   = cutlass::gemm::KernelTmaWarpSpecializedCooperative;
  using EpilogueSchedule = cutlass::epilogue::TmaWarpSpecializedCooperative;
  using TileScheduler    = cutlass::gemm::StreamKScheduler;
  using EpilogueTileType = cutlass::epilogue::collective::EpilogueTileAuto;
};

struct sch_256x128_2x1x1_TmaMI__TmaCoop_streamK {
  using TileShapeNM = Shape<_256, _128>;
  using ClusterShape = Shape<_2, _1, _1>;
  // TODO: Reimplement
  // using KernelSchedule   = cutlass::gemm::KernelTmaWarpSpecializedCooperative;
  using EpilogueSchedule = cutlass::epilogue::TmaWarpSpecializedCooperative;
  using TileScheduler    = cutlass::gemm::StreamKScheduler;
  using EpilogueTileType = cutlass::epilogue::collective::EpilogueTileAuto;
};

struct sch_128x32_2x1x1_TmaMI__TmaCoop_streamK {
  using TileShapeNM = Shape<_128, _32>;
  using ClusterShape = Shape<_2, _1, _1>;
  // TODO: Reimplement
  // using KernelSchedule   = cutlass::gemm::KernelTmaWarpSpecializedCooperative;
  using EpilogueSchedule = cutlass::epilogue::TmaWarpSpecializedCooperative;
  using TileScheduler    = cutlass::gemm::StreamKScheduler;
  using EpilogueTileType = cutlass::epilogue::collective::EpilogueTileAuto;
};

struct sch_256x32_2x1x1_TmaMI__TmaCoop_streamK {
  using TileShapeNM = Shape<_256, _32>;
  using ClusterShape = Shape<_2, _1, _1>;
  // TODO: Reimplement
  // using KernelSchedule   = cutlass::gemm::KernelTmaWarpSpecializedCooperative;
  using EpilogueSchedule = cutlass::epilogue::TmaWarpSpecializedCooperative;
  using TileScheduler    = cutlass::gemm::StreamKScheduler;
  using EpilogueTileType = cutlass::epilogue::collective::EpilogueTileAuto;
};

struct sch_128x128_2x1x1_TmaMI__TmaCoop_streamK {
  using TileShapeNM = Shape<_128, _128>;
  using ClusterShape = Shape<_2, _1, _1>;
  // TODO: Reimplement
  // using KernelSchedule   = cutlass::gemm::KernelTmaWarpSpecializedCooperative;
  using EpilogueSchedule = cutlass::epilogue::TmaWarpSpecializedCooperative;
  using TileScheduler    = cutlass::gemm::StreamKScheduler;
  using EpilogueTileType = cutlass::epilogue::collective::EpilogueTileAuto;
};

    

template<typename Sch>
using Kernel_s8u4b8f16voidf32f32f16s32 = MacheteKernelTemplate<
  int8_t,  // ElementA
  cutlass::vllm_uint4b8_t,  // ElementB
  cutlass::half_t,  // ElementD
  int32_t, // Accumulator
  cutlass::half_t, // GroupScaleT
  void, // GroupZeroT
  float, // ChannelScaleT
  float, // TokenScaleT
  cutlass::gemm::KernelTmaWarpSpecializedCooperative,
  Sch>;


torch::Tensor 
impl_s8u4b8f16voidf32f32f16s32_sch_256x16_1x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_s8u4b8f16voidf32f32f16s32<sch_256x16_1x1x1_TmaMI__TmaCoop_streamK>>(args);
}
template<typename Sch>
using Kernel_s8u4b8voidvoidf32f32f16s32 = MacheteKernelTemplate<
  int8_t,  // ElementA
  cutlass::vllm_uint4b8_t,  // ElementB
  cutlass::half_t,  // ElementD
  int32_t, // Accumulator
  void, // GroupScaleT
  void, // GroupZeroT
  float, // ChannelScaleT
  float, // TokenScaleT
  cutlass::gemm::KernelTmaWarpSpecializedCooperative,
  Sch>;


torch::Tensor 
impl_s8u4b8voidvoidf32f32f16s32_sch_128x128_2x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_s8u4b8voidvoidf32f32f16s32<sch_128x128_2x1x1_TmaMI__TmaCoop_streamK>>(args);
}
torch::Tensor 
impl_s8u4b8voidvoidf32f32f16s32_sch_128x64_2x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_s8u4b8voidvoidf32f32f16s32<sch_128x64_2x1x1_TmaMI__TmaCoop_streamK>>(args);
}
torch::Tensor 
impl_s8u4b8voidvoidf32f32f16s32_sch_128x32_2x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_s8u4b8voidvoidf32f32f16s32<sch_128x32_2x1x1_TmaMI__TmaCoop_streamK>>(args);
}
torch::Tensor 
impl_s8u4b8voidvoidf32f32f16s32_sch_256x128_2x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_s8u4b8voidvoidf32f32f16s32<sch_256x128_2x1x1_TmaMI__TmaCoop_streamK>>(args);
}
torch::Tensor 
impl_s8u4b8voidvoidf32f32f16s32_sch_128x16_1x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_s8u4b8voidvoidf32f32f16s32<sch_128x16_1x1x1_TmaMI__TmaCoop_streamK>>(args);
}
torch::Tensor 
impl_s8u4b8voidvoidf32f32f16s32_sch_256x32_2x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_s8u4b8voidvoidf32f32f16s32<sch_256x32_2x1x1_TmaMI__TmaCoop_streamK>>(args);
}
torch::Tensor 
impl_s8u4b8voidvoidf32f32f16s32_sch_256x16_1x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_s8u4b8voidvoidf32f32f16s32<sch_256x16_1x1x1_TmaMI__TmaCoop_streamK>>(args);
}
template<typename Sch>
using Kernel_e4m3u4b8f16voidf32f32f16f32 = MacheteKernelTemplate<
  cutlass::float_e4m3_t,  // ElementA
  cutlass::vllm_uint4b8_t,  // ElementB
  cutlass::half_t,  // ElementD
  float, // Accumulator
  cutlass::half_t, // GroupScaleT
  void, // GroupZeroT
  float, // ChannelScaleT
  float, // TokenScaleT
  cutlass::gemm::KernelTmaWarpSpecializedCooperative,
  Sch>;


torch::Tensor 
impl_e4m3u4b8f16voidf32f32f16f32_sch_128x128_2x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_e4m3u4b8f16voidf32f32f16f32<sch_128x128_2x1x1_TmaMI__TmaCoop_streamK>>(args);
}
torch::Tensor 
impl_e4m3u4b8f16voidf32f32f16f32_sch_128x64_2x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_e4m3u4b8f16voidf32f32f16f32<sch_128x64_2x1x1_TmaMI__TmaCoop_streamK>>(args);
}
torch::Tensor 
impl_e4m3u4b8f16voidf32f32f16f32_sch_128x32_2x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_e4m3u4b8f16voidf32f32f16f32<sch_128x32_2x1x1_TmaMI__TmaCoop_streamK>>(args);
}
torch::Tensor 
impl_e4m3u4b8f16voidf32f32f16f32_sch_256x128_2x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_e4m3u4b8f16voidf32f32f16f32<sch_256x128_2x1x1_TmaMI__TmaCoop_streamK>>(args);
}
torch::Tensor 
impl_e4m3u4b8f16voidf32f32f16f32_sch_128x16_1x1x1_TmaMI__TmaCoop_streamK(MMArgs args) {
  return run_impl<Kernel_e4m3u4b8f16voidf32f32f16f32<sch_128x16_1x1x1_TmaMI__TmaCoop_streamK>>(args);
}

}; // namespace machete