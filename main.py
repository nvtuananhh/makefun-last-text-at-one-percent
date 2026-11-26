# Last Text at One Percent — final version
# Writes a single final text message to entry.txt.
# The dying phone speaks in its own voice, with one twist
# in the final words: it was testing how long you'd ignore it.
import os

ENTRY = "I've been at 1% for 41 hours. I just wanted to see how long you'd ignore me."

# The joke: a phone at 1% for 41 hours is absurd on its face, and the
# punchline is the confession — it was never dying, it was testing you.
# One sentence, one twist at the end, no low-battery pun in sight.
assert 1 <= len(ENTRY) <= 200

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
