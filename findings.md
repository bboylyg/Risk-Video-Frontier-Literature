# Current research findings — 2026-09-05

主线已根据用户反馈重新聚焦，旧 Agentic / harness 结论不再作为本轮默认路线。

阅读完整报告： [refocused-survey.md](literature/refocused-survey.md)。

- 视频识别：分开底层编码器、少样本动作头、正常记忆与异常事件定位。
- 鲁棒性：以 FrameShield、PatchGuard、AdvCLIP-LoRA 为核心，区分主动 evasion、图中文字干扰和 OOD。
- 效率：对比小型 VLM、LoRA 与视觉 token 压缩，同时测事件召回和端到端延迟。
- 长线图：先检验结构贡献；多模态节点分类／推荐结果不能直接外推到长期风险。
- 核验发现：FrameShield 的默认扰动预算与 PatchGuard 不同；CLS 防御不能自动保护空间 token；有效参数不等于总参数。
- 以上包含综合研究判断，未执行本地模型实验。
