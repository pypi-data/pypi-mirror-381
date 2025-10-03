#!/usr/bin/env python3
"""
Clipboard Manager - Keep history of copied items
Shows: Interactive controls, persistence, keyboard shortcuts
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import stackit
from AppKit import NSPasteboard
from collections import deque

class ClipboardManager(stackit.StackApp):
    def __init__(self):
        super().__init__(
            icon=stackit.SFSymbol("doc.on.clipboard", rendering="hierarchical")
        )

        # Load history from preferences
        prefs = stackit.load_preferences("clipboard_manager", defaults={"history": []})
        self.history = deque(prefs.get("history", []), maxlen=10)
        self.last_clipboard = ""
        self.menu_item = stackit.MenuItem()
        self.setup_ui()

    def setup_ui(self):
        """Create the menu UI"""
        items = [
            stackit.hstack([
                stackit.image(stackit.SFSymbol("clock.arrow.circlepath", color="#4ECDC4"), width=20, height=20),
                stackit.label("Clipboard History", bold=True, font_size=13),
                stackit.spacer(),
                stackit.button(
                    image=stackit.SFSymbol("trash", color="#FF6B35"),
                    image_position="only",
                    target=self,
                    action="clearHistory:"
                )
            ])
        ]

        if self.history:
            for i, text in enumerate(self.history):
                # Truncate long text
                display_text = text[:50] + "..." if len(text) > 50 else text

                item_row = stackit.hstack([
                    stackit.label(f"{i+1}.", color="gray", font_size=10),
                    stackit.label(display_text, font_size=11, wraps=True, width=200),
                ])
                items.append(item_row)

                # Add copy button for each item
                copy_item = stackit.MenuItem(
                    title=f"Copy #{i+1}",
                    callback=lambda s, t=text: self.copy_to_clipboard(t),
                    key_equivalent=str((i+1) % 10)  # ⌘1, ⌘2, etc.
                )
                # Store for later use
                items.append(stackit.label(""))  # Placeholder
        else:
            items.append(
                stackit.label("No clipboard history yet", color="gray", font_size=11)
            )

        self.layout = stackit.vstack(items, spacing=8)
        self.menu_item.set_layout(self.layout)
        self.add(self.menu_item)

        # Add separator and actions
        self.add_separator()
        self.add(stackit.MenuItem(
            title="Clear History",
            callback=self.clear_history,
            key_equivalent="k"
        ))

    def check_clipboard(self, timer):
        """Check for new clipboard content"""
        pasteboard = NSPasteboard.generalPasteboard()
        text = pasteboard.stringForType_("public.utf8-plain-text")

        if text and text != self.last_clipboard:
            self.last_clipboard = text

            # Add to history (avoid duplicates)
            if text not in self.history:
                self.history.appendleft(text)

                # Save to preferences
                stackit.save_preferences("clipboard_manager", {
                    "history": list(self.history)
                })

                # Rebuild UI
                self.rebuild_ui()

    def copy_to_clipboard(self, text):
        """Copy text back to clipboard"""
        pasteboard = NSPasteboard.generalPasteboard()
        pasteboard.clearContents()
        pasteboard.setString_forType_(text, "public.utf8-plain-text")
        stackit.notification("Copied", f"Copied to clipboard")

    def clear_history(self, sender):
        """Clear clipboard history"""
        self.history.clear()
        stackit.save_preferences("clipboard_manager", {"history": []})
        self.rebuild_ui()
        stackit.notification("Cleared", "Clipboard history cleared")

    def clearHistory_(self, sender):
        """Objective-C action for clear button"""
        self.clear_history(sender)

    def rebuild_ui(self):
        """Rebuild the menu UI"""
        # Clear current menu
        menu = self._menu
        for item in list(menu.itemArray()):
            menu.removeItem_(item)

        self._menu_items.clear()
        self._default_items_added = False

        # Rebuild
        self.setup_ui()
        self._ensure_default_items()

if __name__ == "__main__":
    app = ClipboardManager()

    # Check clipboard every 2 seconds
    stackit.every(2.0, app.check_clipboard)

    print("Clipboard Manager running...")
    print("- Automatically saves your clipboard history")
    print("- Use ⌘1-9 to quickly paste recent items")
    print("- Use ⌘K to clear history")

    app.run()
