from pathlib import Path
import json, re
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
def main():
    papers=json.loads((ROOT/'data/papers.json').read_text(encoding='utf-8'))
    synthesis=json.loads((ROOT/'data/research-synthesis.json').read_text(encoding='utf-8'))
    html=(ROOT/'INDEX.html').read_text(encoding='utf-8')
    assert (ROOT/'index.html').read_text(encoding='utf-8') == html
    required={'id','title','authors','year','venue','url','category','type','tags','core_contribution','technical_contribution','relevance_to_project','agent_framework','models','experimental_data','metrics','code_available','explored_dimensions','verification_status','limitations','checked_at','local_result'}
    assert papers and len({p['id'] for p in papers})==len(papers)
    assert any(p['category'].startswith('E · 时序/外观规避') for p in papers)
    assert (ROOT/'literature/survey.md').read_text(encoding='utf-8') == (ROOT/'literature/refocused-survey.md').read_text(encoding='utf-8')
    for p in papers:
        assert required <= p.keys(), p['id']
        assert 2020<=p['year']<=2026
        assert p['local_result'].startswith('TBD')
        for key in ['url','code_url','project_url']:
            if p.get(key):
                u=urlparse(p[key]);assert u.scheme=='https' and u.netloc,(p['id'],key)
        if p['code_available'] in ['repo_inspected','author_linked']:
            assert p['code_url'],p['id']
        assert (ROOT/'literature/refocused'/f"{p['id']}.md").exists()
    ids={p['id'] for p in papers}
    for s in synthesis['sections']+synthesis['deep']:
        assert set(s['refs'])<=ids
    for v in ['literature','synthesis','methods','resources','graph','analysis','experiments','notes']:
        assert f'id="{v}"' in html,v
    for bad in ['innerHTML','eval(','new Function','<script src=','__PAPERS__','__SYNTHESIS__']:
        assert bad not in html,bad
    assert 'Content-Security-Policy' in html
    embedded=re.search(r'const PAPERS=(.*?);\nconst SYNTHESIS=',html,re.S).group(1)
    assert json.loads(embedded)==papers
    js=re.search(r'<script>(.*?)</script>',html,re.S).group(1)
    (ROOT/'to_human').mkdir(exist_ok=True)
    (ROOT/'to_human/desk-script-check.js').write_text(js,encoding='utf-8')
    stats={'entries':len(papers),'recent_papers':sum(p['type']=='论文' and p['year']>=2025 for p in papers),'repo_links':sum(bool(p['code_url']) for p in papers),'methods_checked':sum(p['verification_status']=='methods_and_protocol_checked' for p in papers),'status':'passed'}
    (ROOT/'to_human/data-validation.json').write_text(json.dumps(stats,indent=2),encoding='utf-8')
    print(json.dumps(stats))
if __name__=='__main__': main()
