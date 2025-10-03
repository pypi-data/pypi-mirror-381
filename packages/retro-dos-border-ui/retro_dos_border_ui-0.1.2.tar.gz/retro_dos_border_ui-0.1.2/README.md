# Retro DOS Border UI

A retro DOS-style console UI library using Python's curses module to create terminal interfaces with classic box-drawing characters and table displays.

## Features

- Retro DOS-style borders using Unicode box-drawing characters
- Table rendering with borders and separators
- Status bars and title display
- Simple API for terminal UI creation
- Cross-platform (works on Mac, Linux, etc. - anywhere curses is supported)

## Installation

### From PyPI
```bash
pip install retro-dos-border-ui
```

### From Source
```bash
git clone https://github.com/yourusername/retro-dos-border-ui.git
cd retro-dos-border-ui
pip install .
```

## Usage

```python
import curses
from retro_dos_border_ui import RetroUI

def main(stdscr):
    ui = RetroUI(stdscr)

    # Draw borders
    ui.draw_border_top()
    ui.draw_vertical_borders()
    ui.draw_border_bottom()

    # Add content
    ui.add_title("My App")
    ui.add_table([("Column1", 10), ("Column2", 10)], [["data1", "data2"]])
    ui.add_status_bar("Status line 1", "Status line 2")

    ui.refresh()
    ui.get_key()

if __name__ == "__main__":
    curses.wrapper(main)
```

Would give a design like this:
```
┌───────────────────────────────────────────────────────────────────────────────┐
│                                Retro Interface                                │
├───────────┬───────────────────────────────────────────────────────────────────┤
│ Column1   │Column2                                                            │
├───────────┼───────────────────────────────────────────────────────────────────┤
│ data1     │data2                                                              │
├───────────┴───────────────────────────────────────────────────────────────────┤
│                                                                               │
│                                                                               │
│                                                                               │
│                                                                               │
│                                                                               │
│                                                                               │
│                                                                               │
│                                                                               │
│ System Status: All servers operational. Collection completed successfully.    │
│ F1=Help  F2=Refresh  F3=Sort  ESC=Exit                                        │
│                                                                               │
└───────────────────────────────────────────────────────────────────────────────┘
```

## Available Characters

You can also use the drawing characters directly:
```python
from retro_dos_border_ui import ULCORNER, HLINE, VLCONE, etc.
```

## Requirements

- Python 3.6+
- curses (built-in on Mac/Linux, Windows users may need Windows Curses)

## Author

Marko van der Puil

## License

MIT License - see LICENSE file for details
