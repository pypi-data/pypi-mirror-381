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
git clone https://github.com/markovanderpuil/retro-dos-border-ui.git
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

## Colors and Highlighting

The library supports colored tables with row-specific colors and highlighting.

### Color Classes

Available colors via `RetroUI.Colors`:

- `SUCCESS` (Green)
- `ERROR` (Red)
- `WARNING` (Yellow)
- `INFO` (Blue)
- `SECONDARY` (Magenta)
- `ACCENT` (Cyan)
- `DEFAULT` (White)
- `GREY` (Alias for DEFAULT)

### Table with Colors and Highlighting

```python
import curses
import time
from retro_dos_border_ui import RetroUI

def main(stdscr):
    ui = RetroUI(stdscr)
    ui.scr.nodelay(True)  # non-blocking getch

    columns = [("Color", 12), ("Example", 12)]
    data_rows = [
        ["Success", "Green text"],
        ["Error", "Red text"],
        ["Warning", "Yellow text"],
        ["Info", "Blue text"],
        ["Secondary", "Magenta text"],
        ["Accent", "Cyan text"],
        ["Default", "White text"]
    ]
    row_colors = {
        0: RetroUI.Colors.SUCCESS,
        1: RetroUI.Colors.ERROR,
        2: RetroUI.Colors.WARNING,
        3: RetroUI.Colors.INFO,
        4: RetroUI.Colors.SECONDARY,
        5: RetroUI.Colors.ACCENT,
        6: RetroUI.Colors.DEFAULT
    }

    highlight_row = 0
    last_update = time.time()

    while True:
        current_time = time.time()
        if current_time - last_update >= 1.0:
            highlight_row = (highlight_row + 1) % len(data_rows)
            last_update = current_time

            ui.scr.clear()
            ui.current_y_pos = 0

            ui.draw_border_top()
            ui.draw_vertical_borders()
            ui.draw_border_bottom()

            ui.add_title("My App")
            ui.add_table(
                columns=columns,
                data_rows=data_rows,
                row_colors=row_colors,
                highlight_row=highlight_row
            )
            ui.add_status_bar("Status line 1", f"Highlighting row {highlight_row}")

            ui.refresh()

        key = ui.scr.getch()
        if key != -1:
            break
        time.sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(main)
```

This creates a table where each row has a different color, and the highlighted row cycles every second (inverted colors).

## Available Characters

You can also use the drawing characters directly:
```python
from retro_dos_border_ui import ULCORNER, HLINE, VLINE, etc.
```

## Running the Example

Run the included `example.py` for a demonstration:

```bash
python example.py
```

## Requirements

- Python 3.6+
- curses (built-in on Mac/Linux, Windows users may need Windows Curses)

## Author

Marko van der Puil

## License

MIT License - see LICENSE file for details
