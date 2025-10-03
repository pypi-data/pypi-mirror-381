# cmessage

Simple ctypes-based MessageBox wrapper for Windows.

## Usage

```python
import cmessage

cm = cmessage.CMessage()
message = cm.Message()
message.Show("Title", "Message", lambda: print("Clicked!"), cm.ICON_NONE)
