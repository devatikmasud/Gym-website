import re, glob

files = glob.glob('*.html')

mirror_re = re.compile(r'\r?\n?<!-- Mirrored from.*?HTTrack Website Copier.*?-->\r?\n?')
title_re = re.compile(r'<title>ShotFit-\s*Fitness and Gym HTML Template</title>')
author_meta_re = re.compile(r'<meta name="author" content="Pixel-plus">')
copy_b_re = re.compile(r'Copyright© <b>Pixel-plus</b>\.')
copy_span_re = re.compile(r'Copyright© <span>Pixel-plus</span>')

report = {}
for f in files:
    with open(f, 'r', encoding='utf-8', newline='') as fh:
        content = fh.read()
    orig = content

    n_mirror = len(mirror_re.findall(content))
    content = mirror_re.sub('\n', content)

    n_title = len(title_re.findall(content))
    content = title_re.sub('<title>ShotFit</title>', content)

    n_meta = len(author_meta_re.findall(content))
    content = author_meta_re.sub('<meta name="author" content="Atik Masud">', content)

    n_copy1 = len(copy_b_re.findall(content))
    content = copy_b_re.sub('&copy; 2026 All Rights Reserved.', content)

    n_copy2 = len(copy_span_re.findall(content))
    content = copy_span_re.sub('&copy; 2026 All Rights Reserved.', content)

    if content != orig:
        with open(f, 'w', encoding='utf-8', newline='') as fh:
            fh.write(content)
    report[f] = (n_mirror, n_title, n_meta, n_copy1, n_copy2)

for f, r in report.items():
    print(f, r)
