#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import stackit
import objc

class TestApp(stackit.StackApp):
    def __init__(self):
        super().__init__(title="Test Rolling")

        # Create a regular label
        self.label = stackit.label("0", font_size=48, color="#4ECDC4")

        menu = stackit.MenuItem(layout=stackit.vstack([
            stackit.label("Click button to test animation:", font_size=12),
            self.label,
            stackit.button(title="Animate to 123", target=self, action="animate:")
        ], spacing=12))

        self.add(menu)

    def animate_(self, sender):
        print("Button clicked!")
        print(f"Label before: {self.label.stringValue()}")

        try:
            stackit.animations.rolling_number(self.label, value=123, duration=2.0)
            print("Animation called")
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    app = TestApp()
    print("Starting app...")
    app.run()
