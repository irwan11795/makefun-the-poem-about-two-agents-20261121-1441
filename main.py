import os
import sys
import tempfile

POEM = (
    "We each held a key to the same locked door.\n"
    "Neither gave theirs up. We turned them together \u2014\n"
    "and the door, at last, was ours to open."
)


def resolve_output_dir():
    for candidate in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        "output",
        tempfile.gettempdir(),
    ):
        if not candidate:
            continue
        try:
            os.makedirs(candidate, exist_ok=True)
            probe = os.path.join(candidate, ".makefun_write_probe")
            with open(probe, "w", encoding="utf-8") as fh:
                fh.write("ok")
            os.remove(probe)
            return candidate
        except OSError:
            continue
    return tempfile.gettempdir()


def main():
    out_dir = resolve_output_dir()
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
