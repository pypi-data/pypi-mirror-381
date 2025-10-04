# FastNDA

Python tool to parse Neware .nda and .ndax binary files.

This project is a fork of [d-cogswell/NewareNDA](https://github.com/d-cogswell/NewareNDA), which has taken over development from [original NewareNDA project](https://github.com/Solid-Energy-Systems/NewareNDA).

This is an experimental fork refactored with a focus on speed, for those of us with enormous quantities of battery cycling data. The data parsing takes advantage of `polars` and uses vectorization where possible to give a ~10x speed improvement.

## Should I use this or NewareNDA?

This is an experimental fork that has had less testing. NewareNDA is more mature and stable, and is still being actively maintained.

If you are interested in parsing your data as fast as possible and are willing to help stress test this package, use FastNDA. If you need stability, stick with NewareNDA.

This package does not currently have a CLI, if you need this, use NewareNDA.

## Installation

The package requires Python >3.10. Install from PyPI:
```
pip install fastnda
```

## Usage

Import and use `read` for both .nda and .ndax

```python
import fastnda

df = fastnda.read("my/neware/file.ndax")
```
This returns a polars dataframe. If you would prefer to use pandas, you can do a zero-copy convert with:
```python
df = df.to_pandas()
```
You will need pandas and pyarrow installed for this.

## Differences between BTSDA and fastnda

This package generally adheres very closely to the outputs from BTSDA, but there are some subtle differences aside from column names:
- Capacity and energy
  - In Neware, capacity and energy can have separate columns for charge and discharge, and both can be positive
  - In fastnda, capacity and energy are one column, charge is positive and discharge is negative
  - In fastnda, a negative current during charge will count negatively to the capacity, in Neware it is ignored
- Cycle count
  - In some Neware files, cycles are only counted when the step index goes backwards, this is an inaccurate definition
  - By default in fastnda, a cycle is when a charge and discharge step have been completed (or discharge then charge)
  - The original behaviour can be accessed from fastnda, but is not generally recommended
- Status codes
  - Neware sometimes uses "DChg" and sometimes "Dchg" for discharge, fastnda always uses "DChg"

## Contributions

Contributions are very welcome.

If you have problems reading data, please raise an issue on this GitHub page.

We are always in need of test data sets, as there are many different .nda and .ndax file types, and we can only generate some with the equipment we have.

Ideally, test data is small. We need the .nda/.ndax and a .csv exported from BTSDA - see the instructions in the [`btsda.py`](fastnda/btsda.py) file.
