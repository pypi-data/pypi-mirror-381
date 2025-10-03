#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import stackit

# Simple test
app = stackit.StackApp(title="Test")

label = stackit.label("0", font_size=48)

def test_click(sender):
    print("Clicking...")
    stackit.animations.rolling_number(label, value=123)
    print("Animation called")

menu = stackit.MenuItem(layout=stackit.vstack([
    label,
    stackit.button(title="Test", target=app, action="testAction:")
]))

app.testAction_ = test_click
app.add(menu)
app.run()
