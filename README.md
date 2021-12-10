## pyjsta

Some helper functions. Mostly clones of rstats functions.

### Installation

`pip install --upgrade -e .`

### Usage

```python
import pyjsta
pyjsta.rrep(["1", "2"], 3)
```

```python
import pyjsta
import pandas as pd
df = pd.DataFrame(zip(["a"], ["d"]), columns = ["b", "c"])
pyjsta.pdf_table(df, "df.pdf")
print(pyjsta.pdf_table(df))
```
