# Coding with AI Demo

This file provides a demonstration of how to use AI-assisted coding tools (like GitHub Copilot, OpenAI Codex, Claude Code, or Gemini) to work with code in this repository. It includes examples of how to ask for code generation, debugging help, and explanations of code snippets.

## Examples

### Example 1

Write a GRASS Python *function* to generate a synthetic raster elevation surface using the sum of sines.

```python

```

### Example 2

Asking for help debugging a GRASS Python script that is not producing the expected output.

```python
import subprocess
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import ipywidgets as widgets
from IPython.display import display

# Ensure GRASS Python packages are importable (for local builds)
try:
    import grass.script as gs
except ImportError:
    sys.path.insert(
        0,
        subprocess.check_output(
            ["grass", "--config", "python_path"], text=True
        ).strip(),
    )
    import grass.script as gs

import grass.jupyter as gj
from grass.tools import Tools

# Start GRASS session
project = "temp_workshop"  # Use the temporary workshop location

# Start GRASS Session
session = gj.init(grassdata / project / mapset)
print("GRASS session started.")

gs.run_command("r.mapcalc", expression="streams_der_30m = if(abs(accum_10K) > 10000000, 1, null())")
gs.run_command("r.to.vect", input="basin_10", output="basin_10K", type="area", flags="s")
gs.run_command("r.thin", input="streams_der_30m", output="streams_der_30m_t")
gs.run_command("r.to.vect", input="streams_der_30m_t", output="streams_der_30m", type="line", flags="sj")
```

### Example 3

Requesting an explanation of a complex code snippet that uses GRASS Python APIs.

```python

```

### Example 4

Using AI to refactor a piece of code for better readability and performance.

```python

```

### Example 5

Getting suggestions for additional features or improvements to a GRASS Python script.

```python

```

### Example 6

Write a GRASS tool using C that calculates the slope of a raster elevation surface.

```c

```

## Advanced Prompts (Multi-step code generation)

### Example 7

Creating a complete Jupyter Notebook for a specific task.

#### Original Prompt

```markdown
# Exploring r.sim.water Diffusion Parameters on a Ditch-Berm Landform

This notebook creates a synthetic north-facing slope with a contour-parallel
ditch and berm, then runs *r.sim.water* across a grid of parameter values
to explore how the internal diffusion mechanism handles overflowing ditches.

**Parameters explored:**

- **hmax**: Threshold water depth (m) above which diffusion activates.
  Lower values trigger diffusion sooner.
- **hbeta**: Weighting factor for the "prevailing" flow direction.
  Controls how many previous cells are used to average flow direction
  when depth exceeds **hmax**.
- **halpha**: Diffusion increase constant. Controls how much diffusion
  amplifies when depth exceeds **hmax** (diffusion multiplied by halpha + 1).
- **diffusion_coeff**: Base water diffusion constant. Helps overcome
  small shallow pits and smooth flow over slope discontinuities.
```

#### Improved Prompt with Planning

```markdown
Create a Jupyter notebook that explores how the r.sim.water internal diffusion
mechanism handles overflowing ditches on a synthetic landform. Use `grass.script`
for all GRASS module calls and document design choices in markdown cells.

## 1. Initialize GRASS Session
Start a GRASS GIS session using `grass.jupyter.init` with a new temporary mapset.

## 2. Create the Synthetic Surface
The domain is 50 rows (north-south) by 20 columns (east-west) at 1 m resolution.
The base surface is a uniform north-facing slope where elevation = row() (high in
the south, low in the north), so water flows south to north.

A ditch (3 m deep) and berm (3 m high) run east-west along contours. Going
downslope (south to north), water first encounters the ditch, then the berm.

Build the surface with `r.mapcalc`:
- Base slope: elevation = row() (south=50, north=1)
- Ditch at rows 26-28: subtract 3 m (depression)
- Berm at rows 23-25: add 3 m (raised barrier)
- Downslope order: slope -> ditch (rows 28-26) -> berm (rows 25-23) -> slope

## 3. Run Simulations Across Parameter Grid
Run `r.sim.water` for each combination of:
- `hmax` (threshold depth for diffusion activation): [0.01, 0.05, 0.1] m
- `hbeta` (prevailing flow direction weight): [1, 5, 10]
- `halpha` (diffusion increase constant): [1, 5, 10]
- `diffusion_coeff` (base water diffusion constant): [0.1, 0.5, 1.0]

Run simulations in parallel using all available CPU cores (each simulation uses
a single thread internally). Store results as named rasters and extract
north-south profiles through the center of the domain.

## 4. Interactive Visualization
Create an interactive widget with two panels:
- **Left panel**: 2D water depth map
- **Right panel**: North-south cross-section profile through the domain center
  (south = high elevation/upslope to north = low elevation/downslope)

Include controls for:
- **Add depth to elevation**: toggle to overlay the water surface on the terrain
  profile (both in meters)
- **Depth multiplier**: slider to exaggerate water depth for visibility against
  the terrain
```
