#!/usr/bin/env python3
"""Entrypoint for nanobot gateway in Docker.

Resolves environment variables into config.json at runtime,
then launches nanobot gateway.
"""

import json
import os
import sys

CONFIG_PATH = "/app/nanobot/config.json"
RESOLVED_PATH = "/app/nanobot/config.resolved.json"
WORKSPACE_PATH = "/app/nanobot/workspace"


def resolve_config():
    """Load config.json and inject environment variable values."""
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

    # Resolve LLM provider API key and base URL from env vars
    if "providers" in config and "custom" in config["providers"]:
        api_key = os.environ.get("LLM_API_KEY", "")
        api_base = os.environ.get("LLM_API_BASE_URL", "")
        if api_key:
            config["providers"]["custom"]["apiKey"] = api_key
        if api_base:
            config["providers"]["custom"]["apiBase"] = api_base

    # Resolve MCP server environment variables
    if "tools" in config and "mcpServers" in config["tools"]:
        if "lms" in config["tools"]["mcpServers"]:
            lms_backend_url = os.environ.get("NANOBOT_LMS_BACKEND_URL", "")
            lms_api_key = os.environ.get("NANOBOT_LMS_API_KEY", "")
            if "env" not in config["tools"]["mcpServers"]["lms"]:
                config["tools"]["mcpServers"]["lms"]["env"] = {}
            if lms_backend_url:
                config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_BACKEND_URL"] = lms_backend_url
            if lms_api_key:
                config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_API_KEY"] = lms_api_key

    # Write resolved config
    with open(RESOLVED_PATH, "w") as f:
        json.dump(config, f, indent=2)

    return RESOLVED_PATH


def main():
    """Resolve config and launch nanobot gateway."""
    resolved_config = resolve_config()
    print(f"Resolved config written to {resolved_config}", file=sys.stderr)

    # Launch nanobot gateway
    os.execvp("nanobot", [
        "nanobot",
        "gateway",
        "--config",
        resolved_config,
        "--workspace",
        WORKSPACE_PATH,
    ])


if __name__ == "__main__":
    main()
