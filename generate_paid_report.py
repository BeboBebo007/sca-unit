import json
from pathlib import Path

def main():
    raw = json.loads(Path('sample_sca_report.json').read_text(encoding='utf-8'))
    a = raw['assessment']
    e = raw['engine']
    lines = [
        '# SCA-Unit Generated Structural Report',
        '',
        '## Report type',
        'Generated Paid Structural Compatibility Report',
        '',
        '## Input summary',
        f"- Source A: {a['first_identity']}",
        f"- Source B: {a['second_identity']}",
        '',
        '## Executive verdict',
        a['verdict'].capitalize(),
        '',
        '## Compatibility score',
        str(a['compatibility']),
        '',
        '## Structural metrics',
        f"- Node similarity: {a['node_similarity']}",
        f"- Edge similarity: {a['edge_similarity']}",
        f"- Conflict: {a['conflict']}",
        f"- Engine version: {e['version']}",
        '',
        '## Risk interpretation',
        'The compared structures are compatible, but the score indicates that structural differences exist and should be reviewed before integration or migration.',
        '',
        '## Practical recommendation',
        'Proceed only after confirming that the structural additions are intentional and supported by the target environment.',
        '',
        '## Service boundary',
        'This report is generated from public SCA-Unit functionality and does not expose protected internal architecture.',
    ]
    Path('GENERATED_PAID_REPORT.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
