# 贡献指南

感谢为风控前沿文献追踪系统补充资料。请优先提交一手来源，并明确区分论文事实、作者报告和个人判断。

## 推荐论文或报告问题

可以创建 Issue，至少包含：

- 标题与一手来源链接；
- 出版或首次公开年份；
- 所属方向及与视频风控的关系；
- 是否找到作者代码或项目页；
- 希望补充或纠正的具体内容。

## 修改文献数据库

1. 编辑 `data/papers.json`。不要直接修改生成的 `index.html`、`INDEX.html` 或 `literature/refocused/r*.md`。
2. 每条资料必须包含 HTTPS 主来源。未知字段使用 `needs extraction`、`unknown` 或 `TBD`，不要推测作者、venue、数据集或结果。
3. `reported_result` 只记录来源明确的作者报告；本地运行结果写入 `local_result`，并补充环境、命令、配置、随机种子、数据版本和 checkpoint revision。
4. 如果只是确认仓库存在，使用 `author_linked`；只有检查过仓库内容后才使用 `repo_inspected`。两者都不表示代码已成功运行。
5. 运行：

```bash
python scripts/build_desk.py
python scripts/validate_desk.py
```

6. 提交生成后的 `index.html`、`INDEX.html`、报告和单篇笔记。Pull Request 中说明新增资料、证据层级和仍未核验的内容。

## 内容边界

- 仅提交合法、公开、可引用的研究资料；
- 不上传私人数据、真实用户数据、访问凭据或未经授权的攻击样本；
- 面向攻击的内容应服务于评测和防御，并清楚记录威胁模型与限制。
