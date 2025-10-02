<h2 align="center">projorg: Python project organization and management</h1>

This repository contains the code for facilitating the project
organization and management.

## Installation

Run the following commands to install the package and its dependencies
to add it to your Python environment:

```bash
pip install projorg
```

To install it within a conda environment, run the following commands:

```bash
# Create a new conda environment.
conda create --name projorg "python<=3.12"
conda activate projorg

# Clone the repository and install the package in editable mode.
git clone https://github.com/alisiahkoohi/projorg
cd projorg/
pip install -e .
```

## Example

A usage example of the subset of utilities provided by the package is
included in the `scripts` directory. Run the following command to see the
usage example:

```bash
python scripts/example_script.py
```

This example uses the default command line arguments stored in the
`configs/example_config_file.json` file. You can provide your own values
as shown below. If you have multiple values, provide as string with comma separation.

```bash
python scripts/example_script.py \
    --experiment_name "some_experiment" \
    --input_size "256,512" \
    --alpha 3.0 \
    --seed 1
```

## Questions

Please contact alisk@rice.edu for questions.

## Author

Ali Siahkoohi




