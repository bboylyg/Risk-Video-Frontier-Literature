# Research Log

| # | Date | Type | Summary |
|---|---|---|---|
| 1 | 2026-08-25 | bootstrap | 定义五条检索主线：基础模型、视频/长视频、MLLM 安全、风控鉴伪/KYC/内容审核、Agentic 多模态 pipeline。证据优先使用 arXiv/会议原文、官方项目页和官方仓库。 |
| 2 | 2026-08-25 | bootstrap | 核验 2023–2026 的 41 个核心条目；2026 条目明确按预印本/代码状态标注。 |
| 3 | 2026-08-25 | outer-loop | 形成三代 Agentic 演进：LLM 编排视觉专家 → 记忆/RAG 驱动的迭代取证 → 经 SFT/RL 训练的原生主动感知。方向：DEEPEN。 |
| 4 | 2026-08-25 | report | 生成 BackdoorClaw 风格 standalone 研究桌面、结构化文献库、pipeline 建议和四周学习路线。 |
| 5 | 2026-08-25 | conclude | 完成 5 个视图、桌面/移动渲染、筛选、41 行实验矩阵、JS 语法、链接/CSP/安全 DOM 模式验证；本轮文献研究交付完成。 |
| 6 | 2026-08-25 | verification | 逐项核验用户补充的 SingGuard、Shieldstral、SmuggleBench、KuaiMod、Filter-And-Refine、ZwZ 与 LoMC；纠正系列规格、venue、数据来源和安全含义。 |
| 7 | 2026-08-25 | expand | 补入独立的 SingGuard-NSFA，以及 2026 工业视频审核 UNIVID、IPS；文献库从 41 条扩展到 51 条。 |
| 8 | 2026-08-25 | synthesize | 将新增资料映射到 Guard、Agent 操作安全、对抗 OCR、感知层、工业级联、RAG/趋势治理和模型编辑红队七个系统位置。 |
| 9 | 2026-08-25 | expand | 追加 HiddenDetect、JailNeurons、Cross-Modal Safety Mechanism Transfer、CARE、IAR、图像/生成 latent 安全等工作，检索库从 51 条扩展到 61 条。 |
| 10 | 2026-08-25 | qwen-vl | 核验 FalconEye、ARGUS、QwenSafe、L2S、VLMGuard-R1 与 Qwen-VL-Series-Finetune；区分安全检测器、内容分类器、视频取证 Agent、steering/rewriter 与训练工具。 |
| 11 | 2026-08-25 | synthesize | 明确视频安全的五类独立信号：时间顺序、状态变化、运动/物理一致性、跨模态冲突和事件片段定位；新增视频信号消融与 Qwen PEFT 实验建议。 |
| 12 | 2026-08-25 | report | 将 17 条资料和两条业务方法论写入 Research Desk；总库达到 68 条，待重新构建与验证。 |
| 13 | 2026-08-29 | expand | 去重并新增 20 条 Agent Harness、视觉工具 RL、长视频 Agent、视觉 Agent 评测与视频安全资料；LongVideoAgent 更新为 ACL 2026 与官方代码已发布。 |
| 14 | 2026-08-29 | synthesize | 把 Harness 明确定义为上下文、记忆、工具、权限、轨迹、恢复与验证组成的运行层，并形成模型—Harness 共评原则。 |
| 15 | 2026-08-29 | business | 新增“可探索业务”独立页：八类业务机会、统一 Evidence-first Risk Harness、选择矩阵、输出 schema、实施节奏与论文切入点。 |
| 16 | 2026-09-02 | verification | 核验截图简称与正式来源：USB 为 ACL 2026 Main，MMSafeAware 为 ACL 2025，Video-SafetyBench 为 NeurIPS 2025 Datasets & Benchmarks，ASTRA 为 CVPR 2025，MARS 为 2026 预印本。 |
| 17 | 2026-09-02 | classify | 将截图资料分成业务评测主线、表示/激活干预、机制与红队背景三层；Abliteration/Blackfrost 明确标为非业务主线，Blackfrost 仅按社区项目和作者自报证据记录。 |
| 18 | 2026-09-02 | report | 新增 7 条资料、给 4 条既有资料补“截图重点”标签，并加入一键筛选；文献库由 88 条扩展到 95 条。 |

## Reproducibility record

- 检索更新至：2026-09-02（Asia/Singapore）
- 主要来源：arXiv、会议论文页面、官方 GitHub、官方 Hugging Face 模型卡/项目页
- 检索词组：multimodal agent, agent harness, harness benchmark, visual tool use RL, video agent, long video understanding, active video perception, multimodal safety, hidden-state safety probe, Qwen-VL fine-tuning, video safety, content moderation, USB safety benchmark, MMSafeAware, Video-SafetyBench, activation steering, MARS refusal direction, abliteration, Blackfrost
- 证据规则：不使用搜索摘要中的动态 star 数作为项目质量指标；未读全文或未确认代码的字段标为 `unknown`、`announced` 或 `needs full read`。
- 本轮未运行模型实验；所有性能描述均来自论文/官方项目的报告，不视为本地复现结果。

## 2026-09-05 — Scope correction

依据用户最新需求重构为三个近期方向与一个长期行为图专题。保存旧版、建立 50 条定向资料、定向核验关键方法／协议，重建离线 Research Desk。完整来源和检索路径见 literature/search-provenance-2026-09-05.md；未运行模型实验。
