---
title: "Specification: plamGFP"
site:
    hide-toc: true
    numbered_references: false
---

## Overview

Mitochondria consectetur adipiscing phylum, sed do ribosomes tempor incididunt ut chlorophyll et dolore magna cytoplasm. Ut enim ad minim chromosome, quis nostrud photosynthesis ullamco laboris nisi ut enzyme aliquip ex ea commodo peptide. Duis aute nucleotide in reprehenderit in voluptate vesicle esse cillum genome fugiat nulla pariatur.

### Schematic

::::{aside}
:::{dropdown} TODO

What are good guidelines for a schematic representations of different modules? For a protein output I think it might be useful to include a table of properties, there properties might correspond to parameters that we would put into the CDK can start with molecular weight and isoelectric point for proteins, small molecules might include MW, membrane permeability? Although some of this might be split into a particular instance as well - particularly if it involves interaction with membrane...
:::
::::

:::{figure} gfp-schematic.png
:width: 50%

This is a schematic of the module.
:::

### Designs

::::{aside}
:::{dropdown} TODO

What should belong in this table? It feels like this should actually just be one thing...
:::
::::

| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pOpen-pT7-plamGFP-PURE` | 2946 | [design](https://github.com/bnext-bio/nucleus/blob/main/dna-distribution/v0.1.0-001/plamGFP-PURE.gb) |
| `pOpen-??-plamGFP-TXTL` | 2958 | [design](https://github.com/bnext-bio/nucleus/blob/main/dna-distribution/v0.1.0-001/plamGFP-TXTL.gb) |
| `pOpen-??-plamGFP-Chimeric` | 2958 | [design](https://github.com/bnext-bio/nucleus/blob/main/dna-distribution/v0.1.0-001/plamGFP-Chimeric.gb) |

### Compatible processes

::::{aside}
:::{dropdown} TODO

For GFP the distinction between process and instances feels overwrought or at least hard to distinguish
:::
::::

- [b.next PURE](./docs/02-collections/cytosols.md)
- [OnePot PURE]()

::::{dropdown} [36Pot PURE]()

**Formulation**. This module can be implemented in [my-process] by implementing the following formulation in the base process. TODO: can I reference a table from another page? 


(this-tbl-36pot-formulation)=:::{table}
:name: spec00:tbl-36pot-formulation

| Component | Experiment (uL) |
| --- | --- |
| NEB Sol B -Ribos |  |
| Workshop Protein Mix( ___ ug/uL) | 3 |
| NEB Ribosomes | 4.5 |
| NEB Sol A | 10 |
| NEB Sol B |  |
| RNse Inhibitor | 1.25 |
| pT7-plamGFP plasmid (120 ng/uL) | 1.25 |
| Ultrapure water | 5 |
| **Total** | **25** |
:::

**Process** The following steps should be REMOVED, ADDED, or MODIFIED to implement the Module in the Process. 

- ADD. Preparation of PPK stock solution [Reference-instance??]

::::



- [Simple Cell]()

### Usage

**Collections**

::::{aside}
:::{dropdown} TODO

At least for GFP this approach seems like it will blow up fairly quickly...
Also in this category I think we would treat b.next PURE and 36Pot PURE as interchangeable
We should also have a **Articles** that explain some of our reasoning behind certain design choices, for example why we regard 36Pot and OnePot as being _distinguishable_. 
:::
::::

- Instance of plamGFP in b.next PURE
- Instance of plamGFP in OnePot PURE
- Instance of plamGFP in 36Pot PURE
- Instance of plamGFP in b.next PURE + PPK
- Instance of plamGFP in OnePot PURE + PPK
- Instance of plamGFP in 36Pot PURE + PPK
- Instance of plamGFP in Simple Cell
- Instance of plamGFP in Simple Cell + PPK Cell

**DevNotes**

- [DevNote-3](https://doi.org/10.63765/djnv7772)

**Literature**

- [Wang *et al.* 2019](https://doi.org/10.1021/acssynbio.9b00456)

::::{aside}
:::{dropdown} TODO

I want to figure out how to hide the list of references from being auto generated at the bottom.
:::
::::
