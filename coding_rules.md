# Coding rules

## General

* Only add comments when a line does not speak for itself or contains something that might be confusing or seem wrong.
* Clarity > Length, so rather `file_modification_time` than `f_mod_time`. Of course sometimes (common) abbreviations can be done e.g. "temperature" to "temp" or "image" to "img".
* Write dates in format of YYYY/MM/DD e.g. 2022/01/24 for 24st January 2022.

## Python

* For strings always use '' instead of "".
* For file paths, always use absolute file paths, easy way: `WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))`
* Add type hints and defaults for functions e.g. `def set_time_resolution_of_df(df: pd.DataFrame, time_resolution: str) -> pd.DataFrame:`
* Follow _autopep8_ formatting, except line length rule.
* Generic functions that are useful for multiple files can be put in `utils.py`.
* Instead of print use the logging functions with the appropriate loggin level (DEBUG, INFO, WARNING, ERROR).
* We use pytest for testing, when you create a function try to create a unit test for it ASAP, add it in the test folder.

From <https://kobzol.github.io/rust/python/2023/05/20/writing-python-like-its-rust.html>:

* Use type hints.
* Use dataclasses insetad of tuples or dictionaries.
* Use Union types for grouping dataclasses.
* Use `NewType`.
* Instead of adding multiple ways to create an object in the `__init__.py`, use construction functions.

## Library specific

### Pandas

* Abbreviate dataframe to df.
* The column with the date in it should always be called `ds`.
* Use the `df['column_name']` notation instead of `df.column_name`.

## Naming

* file names use underscores.
* function names should start with a verb and use underscores (`def get_creation_time()`)
* class names use camel case (`FileHandlerObject`)
