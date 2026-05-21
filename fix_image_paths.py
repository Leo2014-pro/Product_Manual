import os, re

base = '.'
fixed_count = 0

for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.md'):
            continue
        full_path = os.path.join(root, f)
        rel = os.path.relpath(full_path, base)
        # Only fix files in subdirectories (not root)
        if os.sep in rel and rel.count(os.sep) >= 1:
            with open(full_path, 'r', encoding='utf-8') as fp:
                content = fp.read()
            # Replace images/xxx.png with ../images/xxx.png
            new_content = re.sub(r'\]\((images/)', r']($1../', content) if content.startswith('..') else content
            # Actually, let's do it more carefully
            new_content = content
            # Check if there are references that need fixing
            if re.search(r'\]\(images/(?!../)', new_content):
                new_content = re.sub(r'\]\(images/(image\d+\.png)\)', r'](../images/\1)', new_content)
                if new_content != content:
                    with open(full_path, 'w', encoding='utf-8') as fp:
                        fp.write(new_content)
                    print(f'Fixed: {rel}')
                    fixed_count += 1

print(f'\nTotal fixed: {fixed_count}')
