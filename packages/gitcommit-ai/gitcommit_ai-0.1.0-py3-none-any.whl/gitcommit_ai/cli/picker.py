"""Interactive picker for selecting commit messages."""
from typing import Optional

from gitcommit_ai.generator.message import CommitMessage


class InteractivePicker:
    """Simple numbered picker for commit message selection."""

    def pick(self, suggestions: list[CommitMessage]) -> Optional[CommitMessage]:
        """Display suggestions and let user pick one.

        Args:
            suggestions: List of CommitMessage options.

        Returns:
            Selected CommitMessage, or None if cancelled.
        """
        if not suggestions:
            return None

        print("\nSelect a commit message:")
        print()

        # Display numbered options
        for i, msg in enumerate(suggestions, 1):
            formatted = msg.format()
            print(f"{i}. {formatted}")

        print()

        # Get user selection
        while True:
            try:
                choice = input("Enter number (1-{}) or Ctrl+C to cancel: ".format(len(suggestions)))

                # Validate input
                try:
                    num = int(choice)
                    if 1 <= num <= len(suggestions):
                        return suggestions[num - 1]
                    else:
                        print(f"Invalid choice. Please enter 1-{len(suggestions)}")
                except ValueError:
                    print("Please enter a number")

            except KeyboardInterrupt:
                print("\nCancelled.")
                return None
