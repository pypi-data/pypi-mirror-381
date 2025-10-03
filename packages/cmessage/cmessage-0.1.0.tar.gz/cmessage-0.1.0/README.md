# cmessage

Simple ctypes-based MessageBox wrapper for Windows.

## Usage

```python
from cmessage import CMessage

cm = CMessage()
cm.Message().Show("Info", "Hello world!")
