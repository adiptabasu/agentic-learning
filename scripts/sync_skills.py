import argparse
import filecmp
import shutil
import sys
from pathlib import Path

HOSTS = {
    "abacus": ".abacusai/skills",
    "codex": ".agents/skills",
    "claude": ".claude/skills",
}

parser = argparse.ArgumentParser(description="Copy canonical skills to host discovery folders.")
parser.add_argument("--host", choices=(*HOSTS.keys(), "all"), required=True)
parser.add_argument("--write", action="store_true", help="Copy missing skill files.")
parser.add_argument("--force", action="store_true", help="Replace differing copies when used with --write.")
args = parser.parse_args()
if args.force and not args.write:
    parser.error("--force requires --write")

root = Path(__file__).resolve().parent.parent
skills = sorted(p for p in (root / "skills").iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
hosts = HOSTS if args.host == "all" else {args.host: HOSTS[args.host]}
issues = []
for host, folder in hosts.items():
    for skill in skills:
        source = skill / "SKILL.md"
        target = root / folder / skill.name / "SKILL.md"
        label = host + ":" + skill.name
        if not target.exists():
            if args.write:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
                print("copied " + label)
            else:
                print("missing " + label)
                issues.append(label)
        elif filecmp.cmp(source, target, shallow=False):
            print("current " + label)
        elif args.write and args.force:
            shutil.copy2(source, target)
            print("updated " + label)
        else:
            print("conflict " + label + " (review or use --write --force)")
            issues.append(label)
if issues:
    sys.exit(1)
print("Selected host copies match canonical skills.")
