#!/usr/bin/env python3
"""从 doc-itasca 的 out_commands.txt / out_fish.txt 生成 docs/reference 速查页。

用法: python scripts/generate_reference.py
"""
import html
import os
import re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'doc-itasca')
OUT = os.path.join(ROOT, 'docs', 'reference')


def clean(s: str) -> str:
    """去除 HTML 标签、解码实体、合并空白。"""
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = s.replace('`', "'")
    s = s.replace('|', r'\|')
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def cmd_category(path: str):
    if path.startswith('pfc/pfcmodule/doc/manual/ball_manual'):
        return 'ball', 'Ball 命令'
    if path.startswith('pfc/pfcmodule/doc/manual/wall_manual'):
        return 'wall', 'Wall 命令'
    if path.startswith('pfc/pfcmodule/doc/manual/clump_manual'):
        return 'clump', 'Clump 命令'
    if path.startswith('pfc/rblock'):
        return 'rblock', 'RBlock 命令'
    if path.startswith('common/contactmodel'):
        return 'contact-models', '接触模型命令'
    if path.startswith('common/contact'):
        return 'contact', 'Contact 命令'
    if path.startswith('common/geometry'):
        return 'geometry', 'Geometry 命令'
    if path.startswith('common/kernel'):
        return 'kernel', 'Model / Program 命令'
    if path.startswith('common/module'):
        return 'range', 'Range 命令'
    if path.startswith('common/dfn'):
        return 'dfn', 'DFN 命令'
    if path.startswith('common/guimodule'):
        return 'plot', 'Plot / GUI 命令'
    if path.startswith('pfc/pfcthermalmodule') or path.startswith('pfc/rblockthermal'):
        return 'thermal', 'Thermal 命令'
    if path.startswith('pfc/ccfd'):
        return 'ccfd', 'CCFD 命令'
    return 'other', '其他命令'


def fish_category(name: str):
    p = name.split('.')[0]
    m = {
        'ball': ('fish-ball', 'Ball FISH 函数'),
        'wall': ('fish-wall', 'Wall FISH 函数'),
        'clump': ('fish-clump', 'Clump FISH 函数'),
        'contact': ('fish-contact', 'Contact FISH 函数'),
        'rblock': ('fish-rblock', 'RBlock FISH 函数'),
    }
    if p in m:
        return m[p]
    if p in ('geom', 'dfn', 'fracture', 'fragment'):
        return 'fish-geometry', '几何 / DFN FISH 函数'
    return 'fish-utility', '工具 / 系统 FISH 函数'


def is_pfc_relevant(path: str) -> bool:
    if path.startswith('flac3d/'):
        return False
    if path.startswith('common/models/'):
        return False
    return path.startswith('pfc/') or path.startswith('common/')


def parse(path_txt: str, get_key):
    """返回 {key: (label, [(name, syntax), ...])}"""
    groups = defaultdict(lambda: ('', []))
    with open(path_txt, encoding='utf-8') as f:
        for line in f:
            parts = line.split(None, 2)
            if len(parts) < 2:
                continue
            name, path = parts[0], parts[1]
            syntax = parts[2] if len(parts) > 2 else ''
            if not is_pfc_relevant(path):
                continue
            key, label = get_key(name, path)
            groups[key] = (label, groups[key][1] + [(name, clean(syntax))])
    return groups


def dedupe_sort(items):
    seen = set()
    out = []
    for name, syntax in items:
        k = (name.lower(), syntax)
        if k not in seen:
            seen.add(k)
            out.append((name, syntax))
    out.sort(key=lambda x: x[0].lower())
    return out


def write_pages(groups, kind, header):
    rows = []
    for key, (label, items) in sorted(groups.items(), key=lambda x: x[0]):
        items = dedupe_sort(items)
        fname = os.path.join(OUT, f'{key}.md')
        col = header[0]
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(f'# {label}\n\n')
            f.write(f'> 共 {len(items)} 条。\n\n')
            f.write(f'| {header[0]} | {header[1]} |\n|------|------|\n')
            for name, syntax in items:
                f.write(f'| `{name}` | `{syntax}` |\n')
        rows.append((key, label, len(items)))
    return rows


def main():
    os.makedirs(OUT, exist_ok=True)

    cmd_groups = parse(os.path.join(SRC, 'out_commands.txt'), lambda n, p: cmd_category(p))
    fish_groups = parse(os.path.join(SRC, 'out_fish.txt'), lambda n, p: fish_category(n))

    cmd_rows = write_pages(cmd_groups, '命令', ('命令', '语法'))
    fish_rows = write_pages(fish_groups, 'FISH', ('函数', '签名'))

    total_cmd = sum(r[2] for r in cmd_rows)
    total_fish = sum(r[2] for r in fish_rows)

    with open(os.path.join(OUT, 'index.md'), 'w', encoding='utf-8') as f:
        f.write('# 官方文档速查\n\n')
        f.write('由 Itasca 官方文档（doc-itasca，2020 版）自动生成的命令与 FISH 函数速查表，'
                f'仅保留 PFC 相关内容。\n\n')
        f.write(f'**命令共 {total_cmd} 条，FISH 函数共 {total_fish} 条。**\n\n')
        f.write('## 命令速查\n\n')
        for key, label, n in cmd_rows:
            f.write(f'- [{label}](./{key})（{n}）\n')
        f.write('\n## FISH 速查\n\n')
        for key, label, n in fish_rows:
            f.write(f'- [{label}](./{key})（{n}）\n')

    print(f'命令页 {len(cmd_rows)} 个，共 {total_cmd} 条')
    print(f'FISH 页 {len(fish_rows)} 个，共 {total_fish} 条')
    for key, label, n in cmd_rows + fish_rows:
        print(f'  {key:20s} {label:24s} {n}')


if __name__ == '__main__':
    main()
