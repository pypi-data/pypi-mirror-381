import os
import sys
import subprocess


def restart_cli():
    # Clean up prompt_toolkit session if active
    try:
        from janito.cli.chat_mode import chat_mode as main

        session = getattr(main, "active_prompt_session", None)
        if session is not None and hasattr(session, "app"):
            session.app.exit()
    except Exception:
        pass  # Ignore cleanup errors

    if os.name == "nt":
        if (
            "powershell" in os.environ.get("SHELL", "").lower()
            or "pwsh" in sys.executable.lower()
        ):
            args = [
                "powershell",
                "-Command",
                "Start-Process",
                sys.executable,
                "-ArgumentList",
                "'-m','janito"
                + ("','" + "','".join(sys.argv[1:]) if sys.argv[1:] else "")
                + "'",
            ]
            subprocess.Popen(args)
        else:
            subprocess.Popen([sys.executable, "-m", "janito"] + sys.argv[1:])
        sys.exit(0)
    else:
        os.execv(sys.executable, [sys.executable, "-m", "janito"] + sys.argv[1:])


def handle_exit(**kwargs):
    console.print("[bold red]Exiting chat mode.[/bold red]")
    sys.exit(0)


handle_exit.help_text = "Exit chat mode"
