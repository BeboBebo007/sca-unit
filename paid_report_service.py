import argparse
import subprocess
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Run SCA-Unit and generate a paid structural report.')
    parser.add_argument('first_json', help='First structural JSON input')
    parser.add_argument('second_json', help='Second structural JSON input')
    parser.add_argument('-r','--raw-output', default='paid_raw_sca_report.json', help='Raw SCA-Unit JSON output path')
    parser.add_argument('-o','--output', default='paid_structural_report.md', help='Generated paid Markdown report path')
    args = parser.parse_args()

    sca_cmd = [sys.executable, '-m', 'sca_unit.cli', args.first_json, args.second_json, '--output', args.raw_output]
    subprocess.run(sca_cmd, check=True)

    gen_cmd = [sys.executable, 'generate_paid_report.py', args.raw_output, '--output', args.output]
    subprocess.run(gen_cmd, check=True)

    print(f'Paid report workflow completed: {args.output}')

if __name__ == '__main__':
    main()
