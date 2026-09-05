# Refocused research provenance — 2026-09-05

Scope: 2025-01-01 to 2026-09-05; a few explicitly labelled historical foundations. This is a targeted breadth survey and selected method/protocol review, not an exhaustive systematic review.

The user's four numbered requirements are represented as three near-term tracks (A/B/C) plus a retained long-term graph track (D). No separate agent delegation, model training, attacks on live systems, dataset collection, or model inference was performed.

## Sources and query families

Queries were run with the web search tool and followed to primary sources. Search engine crawl/publication estimates were not used as paper publication dates.

- 2025 / 2026 few shot video anomaly detection; zero shot video anomaly; VERA; Ex-VAD; Flashback; SphereVAD.
- 2025 few shot action recognition temporal matching; TAMT; Temporal Alignment-Free Video Matching; MPL.
- 2025 / 2026 adversarial video anomaly detection; PatchGuard; FrameShield; image filters evasion.
- typographic attacks CLIP; SCAM; Web Artifact Attacks; SmuggleBench; few shot OOD Auxiliary Prompt Tuning.
- Few-Shot Adversarial Low-Rank Fine-Tuning; small VLM; NVILA; SmolVLM2; Qwen3-VL; Gemma 4 total parameters.
- PruneVid; FastVID; Efficient Video Sampling; Sink-Token-Aware Pruning.
- Graph-MLLM; user behavior graph multimodal alignment; EGRA; RecGOAT; graph fraud LLM; TGB-Seq.
- Official company sources: Meta video representation papers and blog; Google model card / encoder release; NVIDIA efficiency / prompting; AWS graph fraud engineering; Hugging Face VLM / TRL.

Exact accepted source URLs are stored per entry in data/papers.json. Anonymous review copies and secondary summaries were not used to upgrade publication status. A CVF fetch failure was handled with the indexed official page/abstract or the authors' primary arXiv version; such entries remain abstract-level.

## Versioned primary text inspected beyond abstracts

- Flashback: https://arxiv.org/html/2505.15205v1 — §3, §4.1, Table 1.
- PatchGuard: https://arxiv.org/html/2506.09237v1 — §6–7, Table 20, limitations.
- FrameShield: https://arxiv.org/html/2510.21532v1 — §4–5, Appendices E/P.
- AdvCLIP-LoRA: https://arxiv.org/html/2505.15130v1 — experiments and implementation.
- Typographic mechanism defense: https://arxiv.org/html/2508.20570v1 — method and limitations.
- Graph-MLLM: https://arxiv.org/html/2506.10282v1 — §4.1–4.2.
- Qwen3-VL official README — architecture, model sizes, fine-tuning path.
- Gemma 4 official model card — effective vs total parameter definitions.

These are selective reviews, not claims of full-paper or appendix completion.

## Reproducibility and status

- Windows PowerShell; bundled Python and Node.
- Build: python scripts/build_desk.py
- Data validation: python scripts/validate_desk.py
- JavaScript syntax: node --check to_human/desk-script-check.js
- Headless browser verification: node scripts/check_desk_ui.cjs (Edge executable; isolated new browser context).
- No training seeds, trained checkpoints or local benchmark results exist. Future experiment plan recommends recording support/query seeds, exact manifests, hashes, checkpoint revisions, runtime versions and target hardware.
- All proposed experiment outcomes remain TBD.
- data/refocused-papers.json is the 2026-09-05 research snapshot; data/papers.json is the editable canonical current database.
- Old platform and build scripts preserved in archive/2026-09-05-before-refocus; old p001–p095 notes remain as historical material and are not counted in the new UI.

