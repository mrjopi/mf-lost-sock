"""Entry for make.fun "Funniest Lost Sock Status Update" (u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce).

Writes the single entry line to /output/entry.txt.
The line is the whole entry: one line, under the contest's character limit.
"""
import os

LINE = 'Day 47 behind the dryer. My partner moved on with a flip-flop. I respect it. I hate it.'

def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
