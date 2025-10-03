#!/usr/bin/env python3
"""
Pomodoro Timer - Productivity timer in your menu bar
Shows: Timers, state management, notifications, dynamic icons
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import stackit
from datetime import datetime, timedelta
import objc

class PomodoroTimer(stackit.StackApp):
    def __init__(self):
        super().__init__(
            title="25:00",
            icon=stackit.SFSymbol("timer", rendering="hierarchical")
        )

        self.work_duration = 25 * 60  # 25 minutes
        self.break_duration = 5 * 60  # 5 minutes
        self.time_remaining = self.work_duration
        self.is_running = False
        self.is_work_session = True
        self.timer = None

        self.menu_item = stackit.MenuItem()
        self.update_ui()
        self.add(self.menu_item)

        # Update every second
        stackit.every(1.0, self.tick)

    @objc.python_method
    def update_ui(self):
        """Update the menu UI"""
        # Calculate minutes and seconds
        mins = self.time_remaining // 60
        secs = self.time_remaining % 60

        # Session type
        session_type = "Work Session" if self.is_work_session else "Break Time"
        session_color = "#4ECDC4" if self.is_work_session else "#FF6B35"

        # Start/Pause button
        if self.is_running:
            action_button = stackit.button(
                title="Pause",
                target=self,
                action="pauseTimer:",
            )
        else:
            action_button = stackit.button(
                title="Start",
                target=self,
                action="startTimer:",
            )

        self.layout = stackit.vstack([
            # Header
            stackit.hstack([
                stackit.image(
                    stackit.SFSymbol("timer", color=session_color),
                    width=32, height=32
                ),
                stackit.label("Pomodoro Timer", bold=True, font_size=14),
            ]),

            # Session type
            stackit.label(session_type, color=session_color, font_size=12),

            # Big timer display
            stackit.block(
                stackit.hstack([
                    stackit.spacer(),
                    stackit.label(f"{mins:02d}:{secs:02d}", font_size=36, bold=True),
                    stackit.spacer(),
                ]),
                radius=8.0
            ),

            # Controls
            stackit.hstack([
                action_button,
                stackit.button(
                    title="Reset",
                    target=self,
                    action="resetTimer:",
                ),
            ]),

            # Quick actions
            stackit.hstack([
                stackit.label("Quick:", font_size=10, color="gray"),
                stackit.button(title="1 min", target=self, action="set1Min:"),
                stackit.button(title="5 min", target=self, action="set5Min:"),
            ])
        ], spacing=12)

        self.menu_item.set_layout(self.layout)

    @objc.python_method
    def tick(self, timer):
        """Called every second when timer is running"""
        if not self.is_running:
            return

        self.time_remaining -= 1

        # Update status bar title
        mins = self.time_remaining // 60
        secs = self.time_remaining % 60
        self.set_title(f"{mins:02d}:{secs:02d}")

        # Check if timer finished
        if self.time_remaining <= 0:
            self.timer_finished()

        # Rebuild UI
        self.update_ui()

    @objc.python_method
    def timer_finished(self):
        """Called when timer reaches 0"""
        self.is_running = False

        if self.is_work_session:
            # Work session finished, start break
            stackit.notification(
                "Work Complete! 🎉",
                "Time for a break. Great job!"
            )
            self.is_work_session = False
            self.time_remaining = self.break_duration
        else:
            # Break finished, start work
            stackit.notification(
                "Break Over",
                "Ready to get back to work?"
            )
            self.is_work_session = True
            self.time_remaining = self.work_duration

        self.update_ui()

    def startTimer_(self, sender):
        """Start the timer"""
        self.is_running = True
        self.update_ui()

    def pauseTimer_(self, sender):
        """Pause the timer"""
        self.is_running = False
        self.update_ui()

    def resetTimer_(self, sender):
        """Reset the timer"""
        self.is_running = False
        self.is_work_session = True
        self.time_remaining = self.work_duration
        self.set_title("25:00")
        self.update_ui()

    def set1Min_(self, sender):
        """Quick set to 1 minute"""
        self.is_running = False
        self.time_remaining = 60
        self.update_ui()

    def set5Min_(self, sender):
        """Quick set to 5 minutes"""
        self.is_running = False
        self.time_remaining = 300
        self.update_ui()

if __name__ == "__main__":
    app = PomodoroTimer()

    print("Pomodoro Timer running...")
    print("- 25 min work sessions")
    print("- 5 min breaks")
    print("- Notifications when time's up")

    app.run()
