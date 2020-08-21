# ref.: https://docs.python.org/3/library/subprocess.html#subprocess.run

import os
import sys
import argparse
import subprocess

from os.path import join


_compiler = "vc141"
_config = "Release"  # Debug, Release, Profile or Ship

_path_to_appleseed_sandbox = join(f"D:{os.sep}", "dev", "Appleseed", "appleseed", "sandbox")
_path_to_appleseed_cli_exe = join(_path_to_appleseed_sandbox, "bin", _compiler, _config, "appleseed.cli.exe")

_path_to_test_scenes = join(_path_to_appleseed_sandbox, "tests", "test scenes")
_test_scene_folders = ["", "bloom", "vignette"]

LOG_FILE = "rendertimes.txt"


def render_scene(filepath, threads, resolution, output, verbose):
    cli_args = []
    if threads is not None:
        cli_args.extend(["--threads", str(threads)])
    if resolution is not None:
        width, height = resolution
        cli_args.extend(["--resolution", str(width), str(height)])
    if output is not None:
        cli_args.extend(["--output", str(output)])

    cmd_list = [_path_to_appleseed_cli_exe, f"\"{filepath}\"", *cli_args]

    if verbose:
        print(' '.join(cmd_list))
    else:
        result = subprocess.run(
            ' '.join(cmd_list),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode != 0:
            FAIL, ENDC = '\033[91m', '\033[0m'
            for line in result.stderr.split(b"\n"):
                print(FAIL + line.replace(b".\r", b"").decode("ascii") + ENDC)
        else:
            for line in result.stderr.split(b"\n"):
                if b"post-processing finished in " in line:
                    _, time = line.split(b"post-processing finished in ", 1)
                    time = time.replace(b".\r", b"").decode("ascii")
                    print(time)  # TODO capture time
                    with open(LOG_FILE, "a" if os.path.exists(LOG_FILE) else "w") as log_file:
                        print(time + "\t" + filepath, file=log_file)


def main(filename, threads, resolution, output, verbose):
    if os.path.isfile(filename):
        filepath = filename
    else:
        for folder in _test_scene_folders:
            if os.path.isfile(fpath := join(_path_to_test_scenes, folder, filename)):
                filepath = fpath
                break
        assert os.path.isfile(filepath), f"Invalid {filepath=}"

    render_scene(filepath, threads, resolution, output, verbose)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="Name of the .appleseed project file")
    parser.add_argument("--threads", "-t", type=int, default=4, help="Set the number of rendering threads")
    parser.add_argument("--resolution", "-r", nargs=2, help="Set the resolution of the rendered image")
    parser.add_argument("--output", "-o", type=str, help="Set the name of the output file")
    parser.add_argument("--verbose", "-v", action="store_true")

    args = parser.parse_args()

    if not args.filename.endswith(".appleseed"):
        args.filename += ".appleseed"

    if args.output is None:
        args.output = os.path.splitext(args.filename)[0] + ".png"

    main(args.filename, args.threads, args.resolution, args.output, args.verbose)
