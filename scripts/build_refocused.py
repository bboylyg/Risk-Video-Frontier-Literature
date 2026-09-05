from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = (ROOT / 'INDEX.html', ROOT / 'index.html')
SURVEY_OUTPUTS = (ROOT / 'literature/refocused-survey.md', ROOT / 'literature/survey.md')

def main():
    papers = json.loads((ROOT / 'data/papers.json').read_text(encoding='utf-8'))
    synthesis = json.loads((ROOT / 'data/research-synthesis.json').read_text(encoding='utf-8'))
    template = (ROOT / 'src/research-desk.html').read_text(encoding='utf-8')
    for key, data in [('__PAPERS__', papers), ('__SYNTHESIS__', synthesis)]:
        template = template.replace(key, json.dumps(data, ensure_ascii=False).replace('<', '\\u003c'))
    for output in OUTPUTS:
        output.write_text(template, encoding='utf-8')
    folder = ROOT / 'literature/refocused'
    folder.mkdir(exist_ok=True)
    for p in papers:
        lines = [f"# {p['title']}", '']
        for key, val in p.items():
            lines.extend([f'## {key}', '', ', '.join(map(str,val)) if isinstance(val,list) else str(val), ''])
        (folder / (p['id']+'.md')).write_text('\n'.join(lines), encoding='utf-8')
    report = ['# 风控前沿文献追踪系统 · 文献调研报告', '', '更新：2026-09-05。范围：2025 至今为主，保留必要历史基础；四个近期主线加长期行为图专题。', '', '## 范围与证据', '', '本轮为定向广度检索与关键方法深挖，并非穷尽式系统综述。所有条目有一手来源；摘要核验、定向方法核验与本地复现严格区分。当前没有训练或复现实验。', '']
    for section in synthesis['sections'] + synthesis['deep']:
        report.extend(['## '+section['title'], '', section['body'], ''])
        for rid in section['refs']:
            p = next(x for x in papers if x['id']==rid)
            report.append(f"- [{p['title']}]({p['url']})")
        report.append('')
    report.extend(['## 评测协议', '', '|设置|允许数据|指标|参考|关键限制|', '|---|---|---|---|---|'])
    report += ['|'+'|'.join(row)+'|' for row in synthesis['protocols']]
    report.extend(['', '## 文献与资源索引', '', '|ID|年份|类别|标题|来源类型|', '|---|---|---|---|---|'])
    report += [f"|{p['id']}|{p['year']}|{p['category']}|[{p['title']}]({p['url']})|{p['type']}|" for p in papers]
    for output in SURVEY_OUTPUTS:
        output.write_text('\n'.join(report)+'\n', encoding='utf-8')
    print(f'Built INDEX.html and index.html: {len(papers)} entries; notes and survey generated.')

if __name__ == '__main__':
    main()
