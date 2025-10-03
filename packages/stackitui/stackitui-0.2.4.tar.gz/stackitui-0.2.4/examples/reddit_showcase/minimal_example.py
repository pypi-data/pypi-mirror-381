#!/usr/bin/env python3
"""
Minimal Example - Show how easy it is to create a menu bar app
Perfect for Reddit: "5 lines to create a macOS menu bar app"
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import stackit

# That's it - a working menu bar app in 5 lines!
app = stackit.StackApp(title="Hello", icon="star.fill")
item = stackit.MenuItem(title="Click me!", callback=lambda s: print("Clicked!"))
app.add(item)
app.run()
