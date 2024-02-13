import os
import argparse


def memory_use(path):
    # if file return size and sum, if folder keep recursion

    if os.path.isfile(path):
        return os.path.getsize(path)

    memory = 0

    if os.path.isdir(path):
        for child in os.listdir(path):
            memory += memory_use(os.path.join(path, child))

    return memory


def main(args):
    assert os.path.isdir(args.fpath), "Path Format Is Not Dir"
    assert os.path.exists(args.fpath), "Path Does Not Exist"

    print(f"\n{args.fpath}\tMemory: {memory_use(args.fpath)/1e6 : .2f} Mb\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Given a folder computes the memory used by it."
    )

    parser.add_argument("-f", "--fpath", type=str, help="Folder Path.")

    args = parser.parse_args()

    main(args)
