#!/usr/bin/env python3
"""
System Monitor - Real-time CPU/Memory monitoring in menu bar
Shows: Dynamic updates, charts, SF Symbols, custom layouts
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import stackit
import psutil
from collections import deque

class SystemMonitor(stackit.StackApp):
    def __init__(self):
        super().__init__(
            title="0%",
            icon=stackit.SFSymbol("cpu", rendering="hierarchical")
        )

        # Keep last 20 CPU readings for chart
        self.cpu_history = deque([0] * 20, maxlen=20)
        self.menu_item = stackit.MenuItem()
        self.setup_ui()

    def setup_ui(self):
        """Create the menu UI"""
        self.layout = stackit.vstack([
            # Header
            stackit.hstack([
                stackit.image(stackit.SFSymbol("desktopcomputer", color="#4ECDC4"), width=24, height=24),
                stackit.label("System Monitor", bold=True, font_size=14),
            ]),

            # CPU Chart
            stackit.block(
                stackit.vstack([
                    stackit.label("CPU Usage", color="#4ECDC4", font_size=11),
                    stackit.line_chart(
                        points=list(self.cpu_history),
                        dimensions=(250, 50),
                        max_value=100.0,
                        color="#4ECDC4",
                        fill=True
                    ),
                ], spacing=8),
                radius=8.0
            ),

            # Memory Info
            stackit.block(
                stackit.vstack([
                    stackit.label("Memory", color="#FF6B35", font_size=11),
                    self.create_stat_row("Used:", "0 GB"),
                    self.create_stat_row("Available:", "0 GB"),
                ], spacing=6),
                radius=8.0
            ),
        ], spacing=12)

        self.menu_item.set_layout(self.layout)
        self.add(self.menu_item)

    def create_stat_row(self, label, value):
        """Helper to create a stat row"""
        return stackit.hstack([
            stackit.label(label, font_size=10, color="gray"),
            stackit.spacer(),
            stackit.label(value, font_size=10, bold=True),
        ])

    def update_stats(self, timer):
        """Update system stats (called every second)"""
        # Get CPU and memory stats
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory()

        # Update CPU history
        self.cpu_history.append(cpu)

        # Update status bar title
        self.set_title(f"{cpu:.0f}%")

        # Rebuild the UI with new data
        self.layout = stackit.vstack([
            stackit.hstack([
                stackit.image(stackit.SFSymbol("desktopcomputer", color="#4ECDC4"), width=24, height=24),
                stackit.label("System Monitor", bold=True, font_size=14),
            ]),

            stackit.block(
                stackit.vstack([
                    stackit.label("CPU Usage", color="#4ECDC4", font_size=11),
                    stackit.line_chart(
                        points=list(self.cpu_history),
                        dimensions=(250, 50),
                        max_value=100.0,
                        color="#4ECDC4",
                        fill=True
                    ),
                ], spacing=8),
                radius=8.0
            ),

            stackit.block(
                stackit.vstack([
                    stackit.label("Memory", color="#FF6B35", font_size=11),
                    self.create_stat_row("Used:", f"{mem.used / 1e9:.1f} GB"),
                    self.create_stat_row("Available:", f"{mem.available / 1e9:.1f} GB"),
                ], spacing=6),
                radius=8.0
            ),
        ], spacing=12)

        self.menu_item.set_layout(self.layout)

if __name__ == "__main__":
    app = SystemMonitor()

    # Update every second
    stackit.every(1.0, app.update_stats)

    app.run()
