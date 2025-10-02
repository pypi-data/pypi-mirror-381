from typing import TYPE_CHECKING

from vocalizr.app.runner import app

if TYPE_CHECKING:
    from gradio import Blocks


def main() -> None:
    """Launch the Gradio voice generation web app."""
    application: Blocks = app.gui()
    application.queue(api_open=True).launch(
        server_port=7860,
        debug=True,
        mcp_server=True,
        show_api=True,
        enable_monitoring=True,
        show_error=True,
    )


if __name__ == "__main__":
    main()
