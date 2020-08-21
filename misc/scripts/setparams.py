# ref.: https://docs.python.org/3.8/library/xml.etree.elementtree.html#element-objects

import os
import argparse
import logging as log

from xml.etree import ElementTree


def to_str(value):
    return str(value) if not isinstance(value, bool) else str(value).lower()


def set_params(filepath, new_stage_params, output_folder=None, separator="__"):
    assert os.path.isfile(filepath), f"Invalid {filepath=}"
    tree = ElementTree.parse(filepath)

    vprint("stages:")
    for stage in tree.getroot().iter(tag="post_processing_stage"):
        stage_name = stage.get("name")
        vprint(f"- {stage_name}")
        if stage_name in new_stage_params.keys():
            for param in stage:
                if (param_name := param.get("name")) in (new_params := new_stage_params[stage_name]):
                    if (old_value := param.get("value")) != (new_value := to_str(new_params[param_name])):
                        vprint(f"  ..replacing {param_name}={old_value} with {param_name}={new_value}")
                        param.set("value", new_value)

    filename, _ = os.path.splitext(os.path.basename(filepath))
    output_filepath = (
        filename
        + separator
        + separator.join(
            [
                f"{name}-{to_str(value).replace('.', '_')}"
                for params in new_stage_params.values()
                for name, value in params.items()
            ]
        )
        + ".appleseed"
    )

    if output_folder is not None:
        output_filepath = os.path.join(output_folder, output_filepath)
    tree.write(output_filepath, encoding="UTF-8", xml_declaration=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=str, help="Path to .appleseed project file")
    parser.add_argument("outputdir", type=str, help="Path to folder where the modified file will be save")
    parser.add_argument("--verbose", "-v", action="store_true")

    args = parser.parse_args()

    global vprint
    vprint = print if args.verbose else lambda *a, **k: None

    from newparams import NEW_STAGE_PARAMS_LIST

    for stage_name, new_stage_params_list in NEW_STAGE_PARAMS_LIST.items():
        for new_stage_params in new_stage_params_list:
            set_params(args.filepath, {stage_name: new_stage_params}, args.outputdir, separator="__")
