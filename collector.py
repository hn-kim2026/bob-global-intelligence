#!/usr/bin/env python3
"""Public RSS headline collection; no external packages or API keys."""
import datetime, email.utils, json, pathlib, urllib.request, xml.etree.ElementTree as ET
FEEDS = [
    ("UN News", "https://news.un.org/feed/subscribe/en/news/all/rss.xml"),
    ("White House briefings", "https://www.whitehouse.gov/briefings-statements/feed/"),
]
OUT=pathlib.Path('docs/index.json')

def value(node, names):
    for name in names:
        el=node.find(name)
        if el is not None and el.text:
            return el.text.strip()
    return ''

def collect(source,url):
    req=urllib.request.Request(url,headers={'User-Agent':'BOB-RSS-Collector/1.0 (+public RSS; no scraping)'})
    with urllib.request.urlopen(req,timeout=20) as r:
        data=r.read(2_000_000)
    root=ET.fromstring(data)
    items=root.findall('.//item')
    atom=False
    if not items:
        items=root.findall('{http://www.w3.org/2005/Atom}entry');atom=True
    result=[]
    for item in items[:80]:
        if atom:
            title=value(item,['{http://www.w3.org/2005/Atom}title'])
            date=value(item,['{http://www.w3.org/2005/Atom}published','{http://www.w3.org/2005/Atom}updated'])
            link=''
            for e in item.findall('{http://www.w3.org/2005/Atom}link'):
                if e.attrib.get('rel','alternate')=='alternate':link=e.attrib.get('href','');break
        else:
            title=value(item,['title']);date=value(item,['pubDate','date']);link=value(item,['link'])
        if title and link.startswith(('http://','https://')):
            result.append({'title':title,'url':link,'date':date,'source':source})
    return result

def main():
    old=[]
    if OUT.exists():
        try:old=json.loads(OUT.read_text(encoding='utf-8')).get('items',[])
        except (ValueError,OSError):pass
    entries=[];errors=[]
    for source,url in FEEDS:
        try:
            found=collect(source,url);entries+=found
            print(source, len(found))
        except Exception as e:
            errors.append(source+': '+str(e));print('ERROR',source,e)
    if not entries and not old:
        raise SystemExit('No feeds available; refusing to publish empty data')
    seen=set();items=[]
    for x in entries+old:
        if x.get('url') and x['url'] not in seen:
            seen.add(x['url']);items.append(x)
        if len(items)>=400:break
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps({'updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'items':items,'feed_errors':errors},ensure_ascii=False,indent=2),encoding='utf-8')
    print('Total',len(items),'Errors',len(errors))
if __name__=='__main__':main()
