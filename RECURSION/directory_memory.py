import os
import argparse


def memory_use(path):
    # if file return size and sum, if folder keep recursion

    if os.path.isfile(path):
        print("file: ", path, "visited")
        return os.path.getsize(path)
    
    if os.path.isdir(path):
        print("dir: ", path, "visited")
        return memory_use(path)
    
    memory = 0
    memory += memory_use(path)

    return memory
    

def main(args):
    assert os.path.isdir(args.fpath), "Path Format Is Not Dir"
    assert os.path.exists(args.fpath), "Path Does Not Exist"

    print(f"\n{args.fpath}\n\nMemory: {memory_use(args.fpath)} bytes\n")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Given a folder computes the memory used by it."
    )

    parser.add_argument("-f", "--fpath", type=str, help="Folder Path.")

    args = parser.parse_args()

    main(args)