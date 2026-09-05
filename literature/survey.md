# 风控前沿文献追踪系统 · 文献调研报告

更新：2026-09-05。范围：2025 至今为主，保留必要历史基础；三个近期主线加长期行为图专题。

## 范围与证据

本轮为定向广度检索与关键方法深挖，并非穷尽式系统综述。所有条目有一手来源；摘要核验、定向方法核验与本地复现严格区分。当前没有训练或复现实验。

## A｜底层表示 → 少样本识别 → 异常定位

先拆分四个层次：①图像／视频 Transformer 编码器；②时序聚合与匹配；③正常性或异常类别的判别；④未裁剪视频中的区间定位。V-JEPA 2/2.1、PE 提供骨干，TEAM/TAMT 提供少样本迁移思路，UniVAD 解决正常参考图，Flashback/SphereVAD 面向视频异常。不同层次的论文不能互相替代。

- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/)
- [V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482)
- [Perception Encoder: The best visual embeddings are not at the output of the network](https://ai.meta.com/research/publications/perception-encoder-the-best-visual-embeddings-are-not-at-the-output-of-the-network/)
- [Temporal Alignment-Free Video Matching for Few-shot Action Recognition](https://arxiv.org/abs/2504.05956)
- [TAMT: Temporal-Aware Model Tuning for Cross-Domain Few-Shot Action Recognition](https://arxiv.org/abs/2411.19041)
- [UniVAD: A Training-free Unified Model for Few-shot Visual Anomaly Detection](https://openaccess.thecvf.com/content/CVPR2025/html/Gu_UniVAD_A_Training-free_Unified_Model_for_Few-shot_Visual_Anomaly_Detection_CVPR_2025_paper.html)
- [Flashback: Memory-Driven Zero-shot, Real-time Video Anomaly Detection](https://arxiv.org/abs/2505.15205)
- [SphereVAD: Training-Free Video Anomaly Detection via Geodesic Inference on the Unit Hypersphere](https://arxiv.org/abs/2605.08003)

## B｜把 evasion 定义为漏检，而不是泛化成所有越狱

核心目标应定义为：保持人类可辨的异常事件与业务标签不变，使原本能检出的异常被判为正常。分开记录白盒／迁移／查询受限；像素扰动／外观滤镜／贴纸与 OCR／图文冲突／时间变换。OOD 是未知类别或场景变化，未必带有攻击意图；先单独测 OOD，再测 OOD×evasion。

- [FrameShield: Adversarially Robust Video Anomaly Detection](https://arxiv.org/abs/2510.21532)
- [PatchGuard: Adversarially Robust Anomaly Detection and Localization through Vision Transformers and Pseudo Anomalies](https://arxiv.org/abs/2506.09237)
- [SCAM: A Real-World Typographic Robustness Evaluation for Multimodal Foundation Models](https://arxiv.org/abs/2504.04893)
- [Web Artifact Attacks Disrupt Vision Language Models](https://arxiv.org/abs/2503.13652)
- [Auxiliary Prompt Tuning of Vision-Language Models for Few-Shot Out-of-Distribution Detection](https://openaccess.thecvf.com/content/ICCV2025/html/Miao_Auxiliary_Prompt_Tuning_of_Vision-Language_Models_for_Few-Shot_Out-of-Distribution_Detection_ICCV_2025_paper.html)
- [Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation](https://arxiv.org/abs/2604.06950)

## C｜8B 以内必须同时控制参数、视觉 token 与输出长度

优先比较冻结编码器＋小头、Qwen3-VL 2B/4B、SmolVLM2，以及 8B 边界候选。LoRA、量化、视频压缩是不同维度：少训练参数不意味着推理一定快，4-bit 不意味着 KV cache 免费，MCQA 不掉分也不代表短异常不漏检。端到端包括解码、抽帧、视觉编码、prefill、decode 和后处理。

- [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631)
- [SmolVLM2: Bringing Video Understanding to Every Device](https://huggingface.co/blog/smolvlm2)
- [NVILA: Efficient Frontier Visual Language Models](https://research.nvidia.com/labs/eai/publication/nvila/)
- [PruneVid: Visual Token Pruning for Efficient Video Large Language Models](https://aclanthology.org/2025.findings-acl.1024/)
- [Efficient Video Sampling: Pruning Temporally Redundant Tokens for Faster VLM Inference](https://arxiv.org/abs/2510.14624)
- [Sink-Token-Aware Pruning for Fine-Grained Video Understanding in Efficient Video LLMs](https://arxiv.org/abs/2604.20937)
- [Gemma 4 model card and launch](https://ai.google.dev/gemma/docs/core/model_card_4)
- [Few-Shot Adversarial Low-Rank Fine-Tuning of Vision-Language Models](https://arxiv.org/abs/2505.15130)

## D｜长期行为图：先验证结构贡献，再做 GraphLLM

建立用户—内容—设备／会话的带时间交互图（节点种类由实际数据决定）。冻结多模态内容特征作为节点属性，与行为结构表示做 late fusion、对比对齐、graph-token 三组比较。Graph-MLLM 的节点划分实验不等于长期预测；EGRA/RecGOAT 的推荐提升不等于风控召回；GraphRAG 更适合作解释和证据检索层。

- [Graph-MLLM: Harnessing Multimodal Large Language Models for Multimodal Graph Learning](https://arxiv.org/abs/2506.10282)
- [EGRA: Toward Enhanced Behavior Graphs and Representation Alignment for Multimodal Recommendation](https://arxiv.org/abs/2508.16170)
- [RecGOAT: Graph Optimal Adaptive Transport for LLM-Enhanced Multimodal Recommendation with Dual Semantic Alignment](https://arxiv.org/abs/2602.00682)
- [Let Relations Speak: An End-to-End LLM-GNN Soft Prompt Framework for Fraud Detection](https://arxiv.org/abs/2605.28524)
- [L2IR: Revealing Latent Intent in Graph Fraud Detection](https://arxiv.org/abs/2605.26040)
- [TGB-Seq Benchmark: Challenging Temporal GNNs with Complex Sequential Dynamics](https://arxiv.org/abs/2502.02975)
- [Combat financial fraud with GraphRAG on Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/combat-financial-fraud-with-graphrag-on-amazon-bedrock-knowledge-bases/)

## 最有价值的研究交叉｜少样本异常 × 规避鲁棒 × 压缩

本轮检索中，各方向已有直接论文，但未找到能覆盖目标业务全部组合的统一证据。值得先验证：语义保持滤镜和文字干扰在 1/4/16-shot 下是否放大漏检；token 剪枝是否选择性删除稀疏异常；鲁棒 LoRA 能否在相同标注与延迟预算下改善事件 Recall。这里是待检验假设，不是声称文献中不存在相关工作。

- [FrameShield: Adversarially Robust Video Anomaly Detection](https://arxiv.org/abs/2510.21532)
- [Auxiliary Prompt Tuning of Vision-Language Models for Few-Shot Out-of-Distribution Detection](https://openaccess.thecvf.com/content/ICCV2025/html/Miao_Auxiliary_Prompt_Tuning_of_Vision-Language_Models_for_Few-Shot_Out-of-Distribution_Detection_ICCV_2025_paper.html)
- [PruneVid: Visual Token Pruning for Efficient Video Large Language Models](https://aclanthology.org/2025.findings-acl.1024/)
- [Sink-Token-Aware Pruning for Fine-Grained Video Understanding in Efficient Video LLMs](https://arxiv.org/abs/2604.20937)
- [Few-Shot Adversarial Low-Rank Fine-Tuning of Vision-Language Models](https://arxiv.org/abs/2505.15130)

## 黑产滤镜证据缺口

本轮发现文字干扰、网页 artifacts、内容语义 smuggling 和传统对抗扰动的公开证据，但没有取得经过归因、去重和授权的真实黑产滤镜数据集。平台中的滤镜、压缩、贴纸和变速是拟议测试维度，不能标记为已证明的真实黑产手法分布。后续应按实际样本建立标签保持与可见性审核。

- [SCAM: A Real-World Typographic Robustness Evaluation for Multimodal Foundation Models](https://arxiv.org/abs/2504.04893)
- [Web Artifact Attacks Disrupt Vision Language Models](https://arxiv.org/abs/2503.13652)
- [Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation](https://arxiv.org/abs/2604.06950)

## Flashback｜在线便宜，但骨干和平滑协议不能忽略

原文 v1 §4.1 使用 GPT-4o 离线语义记忆、ImageBind 或 PE、每段 1 秒采 16 帧；§4.1/Table 1 报告 PE 的 UCF AUROC 87.29、XD AP 75.13。必须区分离线生成费用与在线延迟，并核对高斯平滑的未来帧依赖。复现前固定模型、记忆库与平滑配置；不能把后续版本数字拼接到 v1。

- [Flashback: Memory-Driven Zero-shot, Real-time Video Anomaly Detection](https://arxiv.org/abs/2505.15205)

## FrameShield｜最贴近视频 evasion，但不是 few-shot 成果

§4 先用 PromptMIL 获得伪标签，再用 SRD 补充时序一致的伪异常以支持帧级对抗训练。§5/Appendix P 使用 16 帧块、40 epochs、AdamW；默认扰动预算 0.5/255。Appendix E 显示更大预算会使训练不稳定。与 PatchGuard 的 8/255 不是同一强度；少样本迁移必须重做协议。

- [FrameShield: Adversarially Robust Video Anomaly Detection](https://arxiv.org/abs/2510.21532)
- [PatchGuard: Adversarially Robust Anomaly Detection and Localization through Vision Transformers and Pseudo Anomalies](https://arxiv.org/abs/2506.09237)

## PatchGuard｜局部图像异常的 robust 基线

§6–7 的核心不是简单叠加数据增强，而是用带位置标签的前景伪异常训练 ViT。训练与评测攻击步数不同；Table 20 在 MVTec 给出 clean／adversarial AUROC。其证据主要是工业和医学图像，不能推断滤镜、图中文字与用户行为异常已被解决。

- [PatchGuard: Adversarially Robust Anomaly Detection and Localization through Vision Transformers and Pseudo Anomalies](https://arxiv.org/abs/2506.09237)

## AdvCLIP-LoRA｜三条主线的直接桥梁

实验在 CLIP 的视觉和文本编码器上同时加 LoRA，rank 2、dropout 0.25；覆盖 ImageNet、Caltech101、DTD、OxfordPets、Flowers102、Food101、SUN397、UCF101。正文图表包含 4-shot 和 16-shot。其 FGSM／PGD 预算数值和单位需对照实现，不能直接与 8/255 比较；UCF101 也不是异常视频基准。

- [Few-Shot Adversarial Low-Rank Fine-Tuning of Vision-Language Models](https://arxiv.org/abs/2505.15130)

## 文字机制防御｜只保护 CLS 可能不够

论文 limitations 明确指出，防御约束文字注意力头向 CLS 写入，但 LLaVA 等下游还使用空间 token。故不能把 CLIP 分类上的改善直接当作完整 VLM 抗文字干扰。应同时测 CLS 分类、patch-token 下游、正常 OCR 和异常文字证据。

- [Towards Mechanistic Defenses Against Typographic Attacks in CLIP](https://arxiv.org/abs/2508.20570)
- [SCAM: A Real-World Typographic Robustness Evaluation for Multimodal Foundation Models](https://arxiv.org/abs/2504.04893)

## 压缩方法｜需要更换评价终点

PruneVid 合并时空冗余与查询相关剪枝；EVS 处理时间静态 patch；SToP 指出只看多选 QA 会忽略细粒度证据损失。建议统一画事件 Recall@固定 FPR 对 P95 延迟曲线，按事件长度和目标面积分层。异常短帧被删除是待测假设，不能由 QA 论文直接证实。

- [PruneVid: Visual Token Pruning for Efficient Video Large Language Models](https://aclanthology.org/2025.findings-acl.1024/)
- [Efficient Video Sampling: Pruning Temporally Redundant Tokens for Faster VLM Inference](https://arxiv.org/abs/2510.14624)
- [Sink-Token-Aware Pruning for Fine-Grained Video Understanding in Efficient Video LLMs](https://arxiv.org/abs/2604.20937)

## Graph-MLLM｜先看无图对照

§4.1 使用 Amazon/Reddit 六个图数据集、60/20/20 节点划分，研究节点分类。§4.2 显示多模态表示的收益与模型／数据集有关，结构感知增强并不稳定占优。业务必须加入无边 MLP、打乱边、冻结内容特征和时序 GNN，对 graph-token 的收益做归因。

- [Graph-MLLM: Harnessing Multimodal Large Language Models for Multimodal Graph Learning](https://arxiv.org/abs/2506.10282)
- [TGB-Seq Benchmark: Challenging Temporal GNNs with Complex Sequential Dynamics](https://arxiv.org/abs/2502.02975)

## 8B 边界｜effective 与 total 不是同一个数

Qwen3-VL 官方提供 2B/4B/8B dense 变体；Gemma 4 模型卡把 E2B 写为 2.3B effective、含 embeddings 5.1B，E4B 为 4.5B effective、含 embeddings 8B。对于严格全模型 8B 上限，还须检查视觉／音频组件计数。26B-A4B 与 30B-A3B 不按激活参数冒充 8B 内模型。

- [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631)
- [Gemma 4 model card and launch](https://ai.google.dev/gemma/docs/core/model_card_4)

## 评测协议

|设置|允许数据|指标|参考|关键限制|
|---|---|---|---|---|
|正常参考 few-shot|仅少量正常样本；明确是否允许外域训练|图像：图／像素 AUROC、AUPRO；视频：帧 AUROC、事件召回|UniVAD；历史 self-context|参考集与测试集去重，禁止把测试异常用于调阈值|
|异常类别 few-shot|N-way K-shot，support 含异常；另保留正常背景|类均衡 accuracy、事件 Recall、跨 episode 置信区间|TEAM、TAMT、Anomaly Crossing|同用户／同原视频片段不跨 support 和 query|
|开放词汇／零样本|目标标签视频不可用于梯度训练，记录合成校准|frame AUROC/AP + Recall@预先固定 FPR|Flashback、SphereVAD|区分无训练、无标注、无目标数据；检查跨视频传导|
|主动 evasion|限定扰动面、知识、查询预算与标签保持|ASR 条件于 clean 原本检出的异常；同时报告总体召回|FrameShield、PatchGuard、SCAM|不把普通失误计入攻击成功；报告 clean utility|
|OOD／漂移|按场景、设备、类别、时间留出；外部 outlier 单列|AUROC、AUPR、FPR95；拒识后剩余异常召回|APT|未知不总是有害；FPR95 与业务固定 FPR 不同|
|高效推理|相同硬件、batch、帧数、分辨率、输出长度|解码到决策 P50/P95、TTFT、显存、事件 Recall|PruneVid、EVS、SToP、vLLM|warm/cold 分开；运行时和 checkpoint 锁版本|
|长期行为图|严格时间切分，所有特征仅使用预测时刻之前的数据|AUPRC、Recall@FPR、时间外推与冷启动|TGB-Seq、Graph-MLLM、RecGOAT|不能随机分边造成未来泄漏；异常标签与推荐点击分开|

## 文献与资源索引

|ID|年份|类别|标题|来源类型|
|---|---|---|---|---|
|r001|2025|A · 视频识别与少样本|[Flashback: Memory-Driven Zero-shot, Real-time Video Anomaly Detection](https://arxiv.org/abs/2505.15205)|论文|
|r002|2025|A · 视频识别与少样本|[VERA: Explainable Video Anomaly Detection via Verbalized Learning of Vision-Language Models](https://arxiv.org/abs/2412.01095)|论文|
|r003|2025|A · 视频识别与少样本|[Ex-VAD: Explainable Fine-grained Video Anomaly Detection Based on Visual-Language Models](https://proceedings.mlr.press/v267/huang25ad.html)|论文|
|r004|2025|A · 视频识别与少样本|[UniVAD: A Training-free Unified Model for Few-shot Visual Anomaly Detection](https://openaccess.thecvf.com/content/CVPR2025/html/Gu_UniVAD_A_Training-free_Unified_Model_for_Few-shot_Visual_Anomaly_Detection_CVPR_2025_paper.html)|论文|
|r005|2026|A · 视频识别与少样本|[SphereVAD: Training-Free Video Anomaly Detection via Geodesic Inference on the Unit Hypersphere](https://arxiv.org/abs/2605.08003)|论文|
|r006|2025|A · 视频识别与少样本|[Temporal Alignment-Free Video Matching for Few-shot Action Recognition](https://arxiv.org/abs/2504.05956)|论文|
|r007|2025|A · 视频识别与少样本|[TAMT: Temporal-Aware Model Tuning for Cross-Domain Few-Shot Action Recognition](https://arxiv.org/abs/2411.19041)|论文|
|r008|2026|A · 视频识别与少样本|[MPL: Match-guided Prototype Learning for Few-shot Action Recognition](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_MPL_Match-guided_Prototype_Learning_for_Few-shot_Action_Recognition_CVPR_2026_paper.html)|论文|
|r009|2026|A · 视频识别与少样本|[No Need For Real Anomaly: MLLM Empowered Zero-Shot Video Anomaly Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Dai_No_Need_For_Real_Anomaly_MLLM_Empowered_Zero-Shot_Video_Anomaly_CVPR_2026_paper.html)|论文|
|r010|2025|A · 视频识别与少样本|[V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/)|论文|
|r011|2026|A · 视频识别与少样本|[V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482)|论文|
|r012|2025|A · 视频识别与少样本|[Perception Encoder: The best visual embeddings are not at the output of the network](https://ai.meta.com/research/publications/perception-encoder-the-best-visual-embeddings-are-not-at-the-output-of-the-network/)|论文|
|r013|2025|A · 视频识别与少样本|[SigLIP 2: A better multilingual vision language encoder](https://huggingface.co/blog/siglip2)|官方博客|
|r014|2022|A · 视频识别与少样本|[Transformer Based Self-Context Aware Prediction for Few-Shot Anomaly Detection in Videos](https://arxiv.org/abs/2503.00670)|论文|
|r015|2021|A · 视频识别与少样本|[Anomaly Crossing: New Horizons for Video Anomaly Detection as Cross-domain Few-shot Learning](https://arxiv.org/abs/2112.06320)|论文|
|r016|2025|A · 视频识别与少样本|[OpenTAD: A Unified Framework and Comprehensive Study of Temporal Action Detection](https://openaccess.thecvf.com/content/CVPR2025W/PVUW/html/Liu_OpenTAD_A_Unified_Framework_and_Comprehensive_Study_of_Temporal_Action_CVPRW_2025_paper.html)|论文|
|r017|2025|B · Evasion 与 OOD|[FrameShield: Adversarially Robust Video Anomaly Detection](https://arxiv.org/abs/2510.21532)|论文|
|r018|2025|B · Evasion 与 OOD|[PatchGuard: Adversarially Robust Anomaly Detection and Localization through Vision Transformers and Pseudo Anomalies](https://arxiv.org/abs/2506.09237)|论文|
|r019|2025|B · Evasion 与 OOD|[SCAM: A Real-World Typographic Robustness Evaluation for Multimodal Foundation Models](https://arxiv.org/abs/2504.04893)|论文|
|r020|2025|B · Evasion 与 OOD|[Web Artifact Attacks Disrupt Vision Language Models](https://arxiv.org/abs/2503.13652)|论文|
|r021|2025|B · Evasion 与 OOD|[Towards Mechanistic Defenses Against Typographic Attacks in CLIP](https://arxiv.org/abs/2508.20570)|论文|
|r022|2025|B · Evasion 与 OOD|[Auxiliary Prompt Tuning of Vision-Language Models for Few-Shot Out-of-Distribution Detection](https://openaccess.thecvf.com/content/ICCV2025/html/Miao_Auxiliary_Prompt_Tuning_of_Vision-Language_Models_for_Few-Shot_Out-of-Distribution_Detection_ICCV_2025_paper.html)|论文|
|r023|2026|B · Evasion 与 OOD|[Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation](https://arxiv.org/abs/2604.06950)|论文|
|r024|2026|B · Evasion 与 OOD|[Laundering AI Authority with Adversarial Examples](https://arxiv.org/abs/2605.04261)|论文|
|r025|2025|B · Evasion 与 OOD|[Robustness in Both Domains: CLIP Needs a Robust Text Encoder](https://arxiv.org/abs/2506.03355)|论文|
|r026|2022|B · Evasion 与 OOD|[Adversarial Machine Learning Attacks Against Video Anomaly Detection Systems](https://openaccess.thecvf.com/content/CVPR2022W/ArtOfRobust/papers/Mumcu_Adversarial_Machine_Learning_Attacks_Against_Video_Anomaly_Detection_Systems_CVPRW_2022_paper.pdf)|论文|
|r027|2025|C · 小模型微调与推理|[Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631)|论文|
|r028|2025|C · 小模型微调与推理|[SmolVLM2: Bringing Video Understanding to Every Device](https://huggingface.co/blog/smolvlm2)|官方博客|
|r029|2025|C · 小模型微调与推理|[NVILA: Efficient Frontier Visual Language Models](https://research.nvidia.com/labs/eai/publication/nvila/)|论文|
|r030|2025|C · 小模型微调与推理|[PruneVid: Visual Token Pruning for Efficient Video Large Language Models](https://aclanthology.org/2025.findings-acl.1024/)|论文|
|r031|2025|C · 小模型微调与推理|[FastVID: Dynamic Density Pruning for Fast Video Large Language Models](https://arxiv.org/abs/2503.11187)|论文|
|r032|2025|C · 小模型微调与推理|[Efficient Video Sampling: Pruning Temporally Redundant Tokens for Faster VLM Inference](https://arxiv.org/abs/2510.14624)|论文|
|r033|2026|C · 小模型微调与推理|[Sink-Token-Aware Pruning for Fine-Grained Video Understanding in Efficient Video LLMs](https://arxiv.org/abs/2604.20937)|论文|
|r034|2026|C · 小模型微调与推理|[Gemma 4 model card and launch](https://ai.google.dev/gemma/docs/core/model_card_4)|模型卡|
|r035|2025|C · 小模型微调与推理|[Few-Shot Adversarial Low-Rank Fine-Tuning of Vision-Language Models](https://arxiv.org/abs/2505.15130)|论文|
|r036|2025|C · 小模型微调与推理|[Rethinking Fine-Tuning: Unlocking Hidden Capabilities in Vision-Language Models](https://arxiv.org/abs/2512.23073)|论文|
|r037|2026|C · 小模型微调与推理|[TRL SFT Trainer — vision-language model training](https://huggingface.co/docs/trl/sft_trainer)|官方文档|
|r038|2026|C · 小模型微调与推理|[vLLM — Multimodal Inputs](https://docs.vllm.ai/en/latest/features/multimodal_inputs/)|官方文档|
|r039|2025|C · 小模型微调与推理|[Vision Language Model Prompt Engineering Guide for Image and Video Understanding](https://developer.nvidia.com/blog/vision-language-model-prompt-engineering-guide-for-image-and-video-understanding/)|官方博客|
|r040|2025|D · 长线行为图|[Graph-MLLM: Harnessing Multimodal Large Language Models for Multimodal Graph Learning](https://arxiv.org/abs/2506.10282)|论文|
|r041|2025|D · 长线行为图|[EGRA: Toward Enhanced Behavior Graphs and Representation Alignment for Multimodal Recommendation](https://arxiv.org/abs/2508.16170)|论文|
|r042|2025|D · 长线行为图|[Training Large Recommendation Models via Graph-Language Token Alignment](https://arxiv.org/abs/2502.18757)|论文|
|r043|2026|D · 长线行为图|[RecGOAT: Graph Optimal Adaptive Transport for LLM-Enhanced Multimodal Recommendation with Dual Semantic Alignment](https://arxiv.org/abs/2602.00682)|论文|
|r044|2026|D · 长线行为图|[Let Relations Speak: An End-to-End LLM-GNN Soft Prompt Framework for Fraud Detection](https://arxiv.org/abs/2605.28524)|论文|
|r045|2026|D · 长线行为图|[L2IR: Revealing Latent Intent in Graph Fraud Detection](https://arxiv.org/abs/2605.26040)|论文|
|r046|2025|D · 长线行为图|[TGB-Seq Benchmark: Challenging Temporal GNNs with Complex Sequential Dynamics](https://arxiv.org/abs/2502.02975)|论文|
|r047|2025|D · 长线行为图|[Use Graph Machine Learning to detect fraud with Amazon Neptune Analytics and GraphStorm](https://aws.amazon.com/blogs/database/use-graph-machine-learning-to-detect-fraud-with-amazon-neptune-analytics-and-graphstorm/)|官方博客|
|r048|2025|D · 长线行为图|[Combat financial fraud with GraphRAG on Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/combat-financial-fraud-with-graphrag-on-amazon-bedrock-knowledge-bases/)|官方博客|
|r049|2025|C · 小模型微调与推理|[VideoLLaMA 3: Frontier Multimodal Foundation Models for Image and Video Understanding](https://arxiv.org/abs/2501.13106)|论文|
|r050|2025|C · 小模型微调与推理|[Qwen2.5-VL Technical Report](https://arxiv.org/abs/2502.13923)|论文|
