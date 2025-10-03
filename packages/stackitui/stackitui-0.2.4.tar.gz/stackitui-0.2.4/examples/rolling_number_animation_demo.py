#!/usr/bin/env python3
"""
Rolling Number Animation Demo - Animate existing labels with counting numbers

Shows how to use stackit.animations.rolling_number() to animate label text
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import stackit
from Foundation import NSNumberFormatter
import objc

class RollingNumberDemo(stackit.StackApp):
    def __init__(self):
        super().__init__(
            title="Counter",
            icon=stackit.SFSymbol("number.circle.fill", rendering="hierarchical")
        )

        # Create rolling number views
        self.counter_label = stackit.rolling_number(value=0, font_size=48, color="#4ECDC4")
        self.revenue_label = stackit.rolling_number(value=0, font_size=32, color="#FF6B35")
        self.percent_label = stackit.rolling_number(value=0, font_size=24, color="#95E1D3")

        # State
        self.count = 0
        self.revenue = 0.0

        self.setup_ui()

    @objc.python_method
    def setup_ui(self):
        """Build the menu UI"""
        menu_item = stackit.MenuItem()

        layout = stackit.vstack([
            # Header
            stackit.hstack([
                stackit.image(
                    stackit.SFSymbol("number.circle.fill", color="#4ECDC4"),
                    width=24,
                    height=24
                ),
                stackit.label("Rolling Numbers", bold=True, font_size=14),
            ]),

            # Counter display
            stackit.block(
                stackit.vstack([
                    stackit.label("Counter", color="gray", font_size=11),
                    self.counter_label,
                ], spacing=4),
                radius=8.0
            ),

            # Revenue display
            stackit.block(
                stackit.vstack([
                    stackit.label("Revenue", color="gray", font_size=11),
                    self.revenue_label,
                ], spacing=4),
                radius=8.0
            ),

            # Percentage display
            stackit.block(
                stackit.vstack([
                    stackit.label("Growth", color="gray", font_size=11),
                    self.percent_label,
                ], spacing=4),
                radius=8.0
            ),

            # Controls
            stackit.separator(),

            stackit.hstack([
                stackit.button(
                    title="+1",
                    target=self,
                    action="increment:"
                ),
                stackit.button(
                    title="+10",
                    target=self,
                    action="incrementTen:"
                ),
                stackit.button(
                    title="+100",
                    target=self,
                    action="incrementHundred:"
                ),
            ]),

            stackit.button(
                title="Reset",
                target=self,
                action="reset:"
            ),
        ], spacing=12)

        menu_item.set_layout(layout)
        self.add(menu_item)

    def increment_(self, sender):
        """Increment by 1"""
        self._animate_to(self.count + 1)

    def incrementTen_(self, sender):
        """Increment by 10"""
        self._animate_to(self.count + 10)

    def incrementHundred_(self, sender):
        """Increment by 100"""
        self._animate_to(self.count + 100)

    def reset_(self, sender):
        """Reset to 0"""
        self._animate_to(0)

    @objc.python_method
    def _animate_to(self, new_count):
        """Animate all counters to new value"""
        old_count = self.count
        self.count = new_count

        # Animate counter with rolling numbers
        stackit.animations.rolling_number(
            self.counter_label,
            value=new_count,
            duration=1.0
        )

        # Animate revenue (each count = $50 revenue)
        new_revenue = new_count * 50.0
        self.revenue = new_revenue

        # Create currency formatter
        currency_fmt = NSNumberFormatter.alloc().init()
        currency_fmt.setNumberStyle_(2)  # NSNumberFormatterCurrencyStyle

        stackit.animations.rolling_number(
            self.revenue_label,
            value=new_revenue,
            duration=1.2,
            formatter=currency_fmt
        )

        # Animate percentage (simulated growth)
        new_percent = new_count * 2.5

        stackit.animations.rolling_number(
            self.percent_label,
            value=new_percent,
            duration=0.8
        )

    @objc.python_method
    def _update_percent_display(self, percent):
        """Update percent label with % sign"""
        self.percent_label.setStringValue_(f"{percent:.0f}%")


if __name__ == "__main__":
    app = RollingNumberDemo()

    print("Rolling Number Animation Demo")
    print("- Click buttons to see numbers animate")
    print("- Uses stackit.animations.rolling_number()")
    print("- Works with any label!")

    app.run()
