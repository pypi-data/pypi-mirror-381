# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**StacKit** (stylized as "StacKit", not "StackIt") is a Python framework for creating native macOS menu bar (status bar) applications with rich custom layouts. It's built directly on PyObjC/AppKit with zero external dependencies (except PyObjC), providing SwiftUI-inspired layout patterns (hstack/vstack) and extensive UI controls.

**Key Design Principle**: StacKit is NOT based on rumps—it's a completely standalone framework with its own implementation. The codebase emphasizes native macOS integration, declarative layouts, and a clean Pythonic API.

## Architecture

### Core Components

1. **core.py** - Central application architecture
   - `StackApp`: Main application class managing the status bar presence
   - `MenuItem`: Individual menu items with custom layout support
   - `StackView`: Custom NSStackView with list-like manipulation methods
   - `hstack()` / `vstack()`: Standalone functions for creating layouts
   - Uses PyObjC's `objc.super()` pattern for Objective-C interop
   - Global state tracked via `_STACK_APP_INSTANCE`

2. **delegate.py** - Application lifecycle and callback management
   - `StackAppDelegate`: NSApplication delegate handling app lifecycle
   - Centralized callback registry (`_callback_registry`) for all UI controls
   - Workspace notifications for system sleep/wake events
   - Status bar appearance management with SF Symbol rendering mode awareness

3. **controls.py** - UI control creation functions
   - Standalone factory functions for creating NSView controls
   - All controls return properly configured NSView subclasses
   - Custom classes: `WrappingLabel`, `LinkLabel`, `ComboBox`, `Editing`, `SecureEditing`, `SearchFieldEditing`
   - Control callbacks registered via `StackAppDelegate.register_callback()`

4. **sfsymbol.py** - SF Symbol integration
   - `SFSymbol` class wrapping NSImage symbol creation
   - Rendering modes: automatic, monochrome, hierarchical, palette, multicolor
   - Weight, scale, point_size, color customization
   - Supports `palette_colors` for multi-color palette mode
   - Creates NSImage via `imageWithSystemSymbolName_accessibilityDescription_`
   - Parameters: `name`, `rendering`, `color`, `palette_colors`, `point_size`, `weight`, `scale`, `text_style`

5. **utils.py** - Helper utilities
   - Alerts, notifications, timers (using NSTimer)
   - File dialogs, preferences storage
   - Application control (quit, open URL)

### Layout System

StackIt uses a SwiftUI-inspired layout paradigm:
- `stackit.hstack(controls, spacing=8.0)`: Horizontal layout (NSUserInterfaceLayoutOrientationHorizontal)
- `stackit.vstack(controls, spacing=8.0)`: Vertical layout (NSUserInterfaceLayoutOrientationVertical)
- Layouts are StackView instances - controls can be added via `.append()`, `.extend()`, `.insert()`
- Layouts can be passed directly to `MenuItem(layout=...)` or applied later via `.set_layout()`

### Callback System

All callbacks are managed centrally through `StackAppDelegate`:
1. Controls register callbacks: `StackAppDelegate.register_callback(obj, stack_item, callback)`
2. Delegate provides specific callback methods: `sliderCallback_`, `checkboxCallback_`, etc.
3. Callbacks can be Python functions or method name strings
4. For target/action pattern: action names must end with `:`, methods must end with `_`

## Development Commands

### Running Examples
```bash
# Run the main controls demo
python3 examples/controls_demo.py

# Run other examples
python3 examples/blocks_demo.py
python3 examples/timer.py
python3 examples/sfsymbol_rendering_modes.py
python3 examples/badge_demo.py
python3 examples/screentime.py  # Screen time tracker with charts
python3 examples/yt.py
```

### Testing
No formal test suite currently exists. Test by running example applications.

### Installation
```bash
# From PyPI
pip install stackitui

# Development installation from source
git clone https://github.com/bbalduzz/stackit.git
cd stackit
pip install -e .
```

### Building Distribution
```bash
# Build package for PyPI
python3 -m build

# Upload to PyPI
python3 -m twine upload dist/*
```

### Building Documentation
```bash
# Build Sphinx docs locally
cd docs
pip install -r requirements.txt
sphinx-build -b html . _build/html
open _build/html/index.html
```

## Important Implementation Details

### PyObjC Patterns
- Use `objc.super(ClassName, self).method()` for calling super methods
- Mark Python methods with `@objc.python_method` when they shouldn't be exposed to Objective-C
- Use `objc.python_method` decorator for Python-only logic in NSObject subclasses

### Status Bar Display
- Status bar supports both icon and title simultaneously
- SF Symbols with multicolor/hierarchical/palette rendering should NOT have template mode enabled
- Template mode forces monochrome, overriding special rendering modes
- Icon and title can be updated at runtime using `app.set_icon()` and `app.set_title()`
- Icon handling in `delegate.py:_update_status_bar_appearance()`

### Control Constraints
- All controls must call `.setTranslatesAutoresizingMaskIntoConstraints_(False)`
- Width/height constraints set via `.widthAnchor().constraintEqualToConstant_().setActive_(True)`
- Spacer controls use low hugging priority for expansion

### Menu Item Padding
- Default padding: `(6.0, 12.0, 6.0, 12.0)` (top, leading, bottom, trailing)
- Applied in `MenuItem.set_layout()` via constraints

### Color Parsing
- Supports hex strings: `"#FFFFFF"`, `"#FFFFFFFF"` (with alpha)
- Supports RGB/RGBA tuples: `(255, 0, 0)` or `(1.0, 0.0, 0.0)`
- Auto-normalizes 0-255 range to 0-1.0 for NSColor

### Timer Management
- Timers created via `timer()`, `after()`, `every()`
- Uses `TimerTarget` wrapper class to handle Python callbacks
- Timers run in `NSRunLoopCommonModes` so they continue firing even when menus are open
- Call `.invalidate()` on timer to stop repeating timers

## Common Patterns

### Creating a Basic App
```python
app = stackit.StackApp(title="My App", icon="gear")

# Custom layout menu item
item = stackit.MenuItem(layout=stackit.hstack([
    stackit.label("Hello", bold=True),
    stackit.spacer(),
    stackit.label("World")
]))

app.add(item)  # No key needed
app.run()  # Automatically adds Quit button
```

### Simple Text Menu Items
```python
app = stackit.StackApp(title="My App")

# Simple menu items (like Preferences, About, etc.)
prefs = stackit.MenuItem(
    title="Preferences...",
    callback=open_prefs,
    key_equivalent=","  # ⌘,
)
app.add(prefs)

about = stackit.MenuItem(title="About", callback=show_about)
app.add(about)
```

### Building Complex Layouts
```python
# Build layout, then pass to MenuItem
layout = stackit.vstack([
    stackit.hstack([
        stackit.label("Status:", bold=True),
        stackit.spacer(),
        stackit.label("Online", color="green")
    ]),
    stackit.progress_bar(value=0.75),
    stackit.button("Refresh", callback=refresh_handler)
], spacing=12.0)

item = stackit.MenuItem(layout=layout)
app.add(item)
```

### Dynamic Layout Updates
```python
# Create MenuItem without layout first
item = stackit.MenuItem()
app.add(item, key="status")

# Update layout dynamically
def update(timer):
    new_layout = stackit.vstack([
        stackit.label(f"Time: {current_time}"),
        stackit.progress_bar(value=progress)
    ])
    item.set_layout(new_layout)

    # Force menu to redraw (needed for updates while menu is open)
    app.update()

stackit.every(1.0, update)
```

### Adding Controls with Callbacks
```python
def slider_changed(sender):
    print(f"Value: {sender.doubleValue()}")

slider = stackit.slider(value=50, callback=slider_changed)
```

### Working with SF Symbols
```python
icon = stackit.SFSymbol("heart.fill", rendering="hierarchical", color="#FF0000")
image_view = stackit.image(icon, width=24, height=24)
```

### Dynamic Status Bar Updates
```python
# Create app with both icon and title
app = stackit.StackApp(
    title="Idle",
    icon=stackit.SFSymbol("circle", color="gray")
)

# Update icon and title at runtime
def update_status():
    app.set_icon(stackit.SFSymbol("checkmark.circle.fill", color="green"))
    app.set_title("Active")

# Both icon and title are displayed simultaneously
```

### Menu Item Badges (macOS 14.0+)
```python
# Add badge to menu item
item = stackit.MenuItem(
    title="Updates Available",
    callback=check_updates,
    badge="updates"  # Shows update indicator
)

# Set badge with count
item.set_badge("new-items", count=5)  # Shows "5" on badge
item.set_badge("alerts", count=12)    # Shows "12" on badge

# Available badge types: "updates", "new-items", "alerts"

# Remove badge
item.set_badge(None)

# Badge types map to NSMenuItemBadgeType constants:
# - "updates" → NSMenuItemBadgeTypeUpdates
# - "new-items" → NSMenuItemBadgeTypeNewItems
# - "alerts" → NSMenuItemBadgeTypeAlerts
```

## File Organization

```
stackit/
├── __init__.py          # Public API exports
├── core.py              # StackApp, MenuItem, StackView, hstack, vstack
├── controls.py          # UI control factory functions
├── sfsymbol.py          # SF Symbol wrapper
├── utils.py             # Utilities (alerts, timers, preferences)
├── delegate.py          # NSApplication delegate & callbacks
├── examples/            # Demo applications
│   ├── controls_demo.py       # Comprehensive showcase of all features
│   ├── blocks_demo.py
│   ├── timer.py
│   ├── sfsymbol_rendering_modes.py
│   ├── badge_demo.py
│   ├── screentime.py          # macOS screen time tracker with charts
│   └── yt.py
├── docs/                # Sphinx documentation
│   ├── conf.py
│   ├── index.rst
│   ├── installation.rst
│   ├── quickstart.rst
│   ├── examples.rst
│   └── api/
├── pyproject.toml       # Package metadata
├── LICENSE              # MIT License
└── README.md            # GitHub README
```

## Dependencies

### Runtime Dependencies
- **pyobjc-framework-Cocoa>=9.0**: Core macOS integration (Foundation, AppKit)
- **httpx>=0.23.0**: Used in `controls.py` for loading images from URLs

### Development Dependencies
- **sphinx>=7.0.0**: Documentation generation
- **autodocsumm**: Sphinx extension for auto-summaries
- **revitron-sphinx-theme**: Documentation theme

### System Requirements
- **Python 3.7+**
- **macOS 11.0+** (for SF Symbols support)

### PyPI Package
- Package name: `stackitui`
- Import name: `stackit`

## Notes for Code Modifications

- When adding new controls, follow the pattern in `controls.py`: standalone factory functions returning configured NSView subclasses
- Register any new control callbacks in `delegate.py` with a corresponding `*Callback_` class method
- SF Symbol features require macOS version checks (use `hasattr()` for API availability)
- The framework maintains strict isolation from rumps—do not introduce rumps dependencies
- Menu items automatically get a Quit button via `_ensure_default_items()` unless manually disabled

## API Design Principles

The StackIt API follows these principles:
1. **No unused parameters**: All parameters should have a clear purpose
2. **Optional keys**: Keys are optional in `app.add()` and auto-generated when not provided
3. **Direct layout passing**: Layouts can be passed directly to `MenuItem(layout=...)` for cleaner code
4. **Consistent naming**: Use `add()`, `remove()`, `get()` instead of `add_item()`, `remove_item()`, `get_item()`
5. **Standalone functions**: `hstack()` and `vstack()` are standalone functions, not methods on MenuItem
6. **Fluent updates**: Use `set_layout()` for dynamic updates, then call `app.update()` to force redraw
7. **Menu-aware timers**: All timers use `NSRunLoopCommonModes` to continue running when menus are open
8. **Python callbacks**: Controls use Python function callbacks, not target/action strings
9. **Direct instantiation**: `SFSymbol()` is directly instantiated, not via `.create()` method

## Breaking Changes from Previous Versions

If upgrading from earlier versions, note these API changes:
- `StackMenuItem` → `MenuItem`
- `add_item()` → `add()`
- `get_item()` → `get()`
- `remove_item()` → `remove()`
- `set_root_stack()` → `set_layout()`
- `SFSymbol.create()` → `SFSymbol()` (direct instantiation)
- `size` parameter → `point_size` (in SFSymbol)
- `rendering_mode` → `rendering` (in SFSymbol)
- `secondary_color`/`tertiary_color` → `palette_colors` list (in SFSymbol)
