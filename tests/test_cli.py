import sys
from mouse_recorder import cli


def test_cli_help(capsys):
    # Ensure the CLI parses --help (will raise SystemExit)
    sys_argv = sys.argv
    try:
        sys.argv = ["mouse-recorder", "--help"]
        try:
            cli.main()
        except SystemExit:
            pass
    finally:
        sys.argv = sys_argv
