# Current research findings — 2026-09-05

主线已根据用户反馈重新聚焦，旧 Agentic / harness 结论不再作为本轮默认路线。

阅读完整报告： [refocused-survey.md](literature/refocused-survey.md)。

- 视频识别：分开底层编码器、少样本动作头、正常记忆与异常事件定位。
- 鲁棒性：以 FrameShield、PatchGuard、AdvCLIP-LoRA 为核心，区分主动 evasion、图中文字干扰和 OOD。
- 效率：对比小型 VLM、LoRA 与视觉 token 压缩，同时测事件召回和端到端延迟。
- 长线图：先检验结构贡献；多模态节点分类／推荐结果不能直接外推到长期风险。
- 时序/外观规避：独立维护篡改与腐化基准，先审核标签保持，再计算 conditional ASR。
- 自适应感知：AKS、KFS-Bench、FOCUS、DIVE 是候选取证组件；尚未证明能抵抗目标规避。
- 测试时防御：R-TPT、TAPT、TAME、ASTRA 需与 RTTDP 式在线投毒风险一起评估。
- 核验发现：FrameShield 的默认扰动预算与 PatchGuard 不同；CLS 防御不能自动保护空间 token；有效参数不等于总参数。
- 以上包含综合研究判断，未执行本地模型实验。
