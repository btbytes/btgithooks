import argparse
import os
import subprocess


def check_for_untitled_file(filenames, root="", filename="content/Untitled"):
    target_file = os.path.join(root, filename)
    return os.path.exists(target_file)


def get_git_root():
    return (
        subprocess.check_output(["git", "rev-parse", "--show-toplevel"])
        .decode()
        .strip()
    )


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames", nargs="*", help="Filenames pre-commit believes are changed."
    )
    args = parser.parse_args(argv)

    root = get_git_root()
    if check_for_untitled_file(args.filenames, root):
        print("Error: 'content/Untitled' file found.")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
