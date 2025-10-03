(installing)=
# Installing

To use the VCP CLI tool, you will need:

* Python version 3.10 or greater
* On MacOS or [Windows WSL](https://learn.microsoft.com/en-us/windows/wsl/), you will need a terminal app.
* For the `benchmarks` commands, you will need to be running on an Intel/AMD64 architecture CPU with NVIDIA GPU, running Linux with NVIDIA drivers.
* For other commands (e.g. `data`) you will need a Virtual Cell Platform account ([register here](https://virtualcellmodels.cziscience.com/?register=true))

## From PyPi

The Virtual Cells Platform (VCP) CLI is published to [PyPi](https://pypi.org/project/vcp-cli/).

It can be installed with:

```bash
pip install vcp-cli
```

```{note}
It is recommended to install the VCP CLI tool in a virtual environment such as `venv` to avoid conflicts with other Python packages in your system.
```
