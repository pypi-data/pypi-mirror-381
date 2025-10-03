# snakebar

A tqdm-like progress bar that fills your terminal with a one-character-thick snake along a random space-filling curve. Based on https://observablehq.com/@esperanc/random-space-filling-curves

## Installation
```bash
pip install snakebar
```

### Installation with uv
If you are using `uv` as your Python environment manager, you can install snakebar with:
```bash
uv pip install snakebar
```

## Usage

### Basic Python usage

Using `snake_tqdm` as a drop-in replacement for tqdm:
```python
from snakebar import snake_tqdm
for i in snake_tqdm(range(100)):
    # your code here
    pass
```

Using `SnakeTQDM` for manual progress bar updates:
```python
from snakebar import SnakeTQDM
with SnakeTQDM(total=100) as pbar:
    for i in range(100):
        # your code here
        pbar.update(1)
```

### CLI usage

You can also use the `snakebar` command line interface:

```bash
snakebar -n 100 --desc "Processing" --sleep 0.05
```

Options:
- `-n`, `--total`: Total number of steps (default 100)
- `--desc`: Description text to show alongside the progress bar
- `--sleep`: Time in seconds to sleep between steps (simulates work)

## Development

To install snakebar in editable mode for development, run:
```bash
uv pip install -e .
```

To run the CLI demo during development:
```bash
snakebar -n 100 --desc "Demo" --sleep 0.05
```