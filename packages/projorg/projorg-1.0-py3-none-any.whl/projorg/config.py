import argparse
import hashlib
import json


def shorten_filename(filename, max_length=255):
    """Shorten the filename using a hash if it exceeds max_length."""
    if len(filename) > max_length:
        hash_object = hashlib.sha1(filename.encode())
        hash_filename = hash_object.hexdigest()
        extension = filename.split(".")[-1] if "." in filename else ""
        short_filename = (
            f"{filename[: max_length - len(hash_filename) - 1]}.{hash_filename}"
            if extension
            else hash_filename
        )
        return short_filename
    return filename


def read_config(filename):
    """Read input variables and values from a json file."""
    with open(filename) as f:
        configs = json.load(f)
    return configs


def write_config(args, filename):
    "Write command line arguments into a json file."
    with open(filename, "w") as f:
        json.dump(args, f)


def parse_input_args(args):
    "Use variables in args to create command line input parser."
    parser = argparse.ArgumentParser(description="")
    for key, value in args.items():
        parser.add_argument("--" + key, default=value, type=type(value))
    return parser.parse_args()


def make_experiment_name(args, ignore_arg_list=["experiment_name"]):
    """Make experiment name based on input arguments"""
    experiment_name = args.experiment_name + "_"
    for key, value in vars(args).items():
        if key not in ignore_arg_list:
            experiment_name += key + "-{}_".format(value)
    experiment_name = experiment_name[:-1].replace(" ", "").replace(",", "-")
    return shorten_filename(experiment_name)


def process_sequence_arguments(args, sequence_args_and_types):
    """Process sequence arguments to remove spaces and split by
    comma."""

    for seq_args, arg_type in sequence_args_and_types:
        if hasattr(args, seq_args):
            setattr(
                args,
                seq_args,
                [
                    arg_type(_)
                    for _ in getattr(args, seq_args).replace(" ", "").split(",")
                ],
            )
    return args
