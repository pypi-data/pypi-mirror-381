# Data

## What is the data CLI Tool?

A command-line interface for searching, exploring metadata, and downloading data registered in the Virtual Cell Platform ("VCP"). This tool allows you to search for data across multiple scientific domains, without needing to write code or scripts.

### Metadata Schemas

Registered data comes with rich metadata to streamline search. Learn about our data schemas including the cross modality schema that specifies the key metadata available for all registered datasets.

```{toctree}
:maxdepth: 1

data_schemas/cross_modality_schema
data_schemas/imaging_metadata_schema
data_schemas/sequencing_schema
data_schemas/mass_spectrometry_schema
```

## Getting Started

### Prerequisites

* Your Virtual Cell Platform account credentials ([register here](https://virtualcellmodels.cziscience.com/?register=true))
* Python version 3.10 or greater
* The [VCP CLI tool](https://pypi.org/project/vcp-cli/). See [Installation](installing) for instructions.

### Authentication

Some CLI commands will require that you have a user account on the Virtual
Cell Models (Virtual Cell Platform) website and that you login to your account using the CLI. If needed, you
can create a new account [in the Virtual Cells Platform website](https://virtualcellmodels.cziscience.com/).

#### Login via Web Browser

To log in to your Virtual Cell Platform account using your browser:

```bash
vcp login
```

Once you log in, you can go back to the command line and continue.

#### Login via the Command Line

To log in to your Virtual Cell Platform account from your terminal, specify the `--username` option:

```bash
vcp login --username your.name@example.org
```

You will be prompted for a password. Use the same one you use on [the
Virtual Cell Models web page](https://virtualcellmodels.cziscience.com).

### Get Help Using the CLI

The `--help` flag provides additional documentation and tips. You can add it to the end of any of the available commands for more information.

For example, to learn what commands are available for this tool, run:

```bash
vcp --help
```

You can also get help with learning how to use individual commands by adding it to a command, for example:

```bash
vcp data describe --help
```

## Overview of Data Commands

The CLI has 4 core data commands:

| Command | Description |
| ----- | ----- |
| `vcp data search "<TERM>"` | Search for datasets using keywords or fields [Lucene style queries](https://lucene.apache.org/core/10_3_0/queryparser/org/apache/lucene/queryparser/classic/package-summary.html#package.description) are supported. |
| `vcp data describe <DATASET_ID>` | View a summary of dataset metadata, including domain, species, tissues, and assets. |
| `vcp data download <DATASET_ID>` | Download a dataset by ID to a local directory. |
| `vcp data credentials <DATASET_ID>` | Show download credentials for a dataset. Use this to retrieve download credentials if you're accessing a dataset through other tools or workflows. |

The CLI also has the following flags that can be used to adjust commands:

| Flag | Purpose |
| ----- | ----- |
| `--download` | Download all datasets returned by the search. |
| `--full` | Show detailed metadata for each dataset in the search results as a pretty-printed JSON  |
| `--raw` | Show the raw returned record |
| `-o`, `--outdir` | Specify a directory for downloads (used with `--download` or `vcp data download`). |
| `--help` | Show help message and usage information for the command. |

### Simple Command Examples

#### Search for Datasets

```bash
vcp data search "cryoet"
```

This will return an overall count of the datasets with “cryoet” in the dataset name or metadata and a paginated table of those datasets with their associated metadata. To automatically download the datasets returned by search add the flag `--download` to the end of your query.

The CLI supports Lucene-style search, so you can use:

* AND, OR, NOT to combine terms
* Quotation marks `" "` to group multi-word terms
* Field-specific search, like `”species:mouse AND tissue:brain”`
* Wildcard terms with `*` and `?`
* Fuzzy search with `~`

Examples using each type of Lucene query are below.

#### Combine Terms with Boolean Operators

The following returns to imaging datasets that specifically involve human data.

```bash
vcp data search "domain:imaging AND species:human"
```

The following returns neuron datasets that **do not** include mouse data.

```bash
vcp data search "cell_type:neuron NOT species:mouse"
```

#### Multiword Terms

```bash
vcp data search "cryoet data portal"
```

#### Field-specific Terms

```bash
vcp data search "species:mouse"
```

#### Wildcard Terms

The `*` symbol can be used as a multicharacter wildcard and the `?` as a single character wildcard. For example, to search for data from any cryogenic technique, use:

```bash
vcp data search "cryo*"
```
To search for cryoET or cryoEM data, you could use:

```bash
vcp data search "cryoe?"
```

#### Fuzzy Search

To do a fuzzy search, use a `~` symbol at the end of a single word term. This type of search accounts for simple typos and formatting differences.

```bash
vcp data search “Hpylori~”
```

#### View Dataset Metadata

```bash
vcp data describe 688ab21b2f6b6186d8332644
```
This returns a table with additional metadata beyond what is displayed with the `search` command.

To show comprehensive metadata for a dataset add the flag `--full` to the end of your query, for example:

```bash
vcp data describe 688ab21b2f6b6186d8332644 --full
```

All of the metadata displayed can be used for field specific search, for example:

```bash
vcp data search namespace:cellxgene
```

#### Download a Dataset

```bash
vcp data download 688ab21b2f6b6186d8332644
```

This will initiate a download in the current working directory. During the download, a progress bar is displayed along with the full file size in bytes.

You can use the following flags `-o` or `--outdir` followed by a path to a folder to specify the output directory for download. For example, to download a file to your Documents folder, run:

```bash
vcp data download -o ~/Documents 688ab21b2f6b6186d8332644
```
Or

```bash
vcp data download --outdir ~/Documents 688ab21b2f6b6186d8332644
```

## Tips

* Put multi-word terms in quotes: `"stem cell"` not `stem cell`.
* Start simple: Try `vcp data search "cellxgene"` to get a feel for results.
* Use `--help` often: Every command supports it!

For more information on the available commands and flags, see {ref}`cli-reference`.
