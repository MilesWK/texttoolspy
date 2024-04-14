# texttoolspy 0.0.7

[![PyPI](https://img.shields.io/pypi/v/texttoolspy)](https://pypi.org/project/texttoolspy/)
[![PyPI - License](https://img.shields.io/pypi/l/texttoolspy)](https://pypi.org/project/texttoolspy/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/texttoolspy)](https://pypi.org/project/texttoolspy/)


Tools to make responsive and simple items in text.

**How to install:**
```bash
pip install texttoolspy
```

Texttools is a module that creates responsive and simple "tools" in your python code. THESE ONLY WORK WHEN RUNNING IN THE TERMINAL. 

Example usage of the `menu()` function:
```python
import texttoolspy as ttp

MenuItems = ["Item1","Item2","Item3"]

ttp.menu(MenuItems, 1)
```
Save and run this code in the command prompt/terminal. 

This allows the user to use arrow keys to choose an item, and then click enter to select the item. When the user selects an item, the selected item will be returned

To see the rest of the features, check out the [wiki](https://github.com/MilesWK/texttoolspy/wiki).
