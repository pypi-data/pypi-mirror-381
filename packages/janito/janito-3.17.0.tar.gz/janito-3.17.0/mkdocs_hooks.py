"""
MkDocs hooks for dynamic content generation.
This module provides hooks to automatically inject build-time information.
"""

import subprocess
import os


def get_git_commit_hash():
    """Get the current git commit hash (short form)."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "unknown"


def on_config(config):
    """
    MkDocs hook called when the config is loaded.
    This allows us to dynamically set values in the config.
    """
    commit_hash = get_git_commit_hash()

    # Update the extra section with dynamic values
    if "extra" not in config:
        config["extra"] = {}

    config["extra"]["commit_hash"] = commit_hash
    config["extra"]["copyright"] = (
        f"Made with Material for MkDocs • "
        
        f"Commit: {commit_hash}"
    )

    return config


def on_page_context(context, page, config, nav):
    """
    MkDocs hook called for each page context.
    This allows us to add the commit hash to page-specific contexts if needed.
    """
    context["commit_hash"] = config["extra"].get("commit_hash", "unknown")
    return context
