# Nanobot gateway Dockerfile - multi-stage build with uv
# Build context: ./nanobot
# Additional contexts: workspace: .

# ---
# Stage 1: build the application in the `/app` directory.
# ---

ARG REGISTRY_PREFIX_DOCKER_HUB
FROM ${REGISTRY_PREFIX_DOCKER_HUB}astral/uv:python3.14-bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Disable Python downloads
ENV UV_PYTHON_DOWNLOADS=0

WORKDIR /app
COPY --from=workspace pyproject.toml uv.lock /app/

# Copy mcp and nanobot-websocket-channel from workspace
COPY --from=workspace mcp /app/mcp
COPY --from=workspace nanobot-websocket-channel /app/nanobot-websocket-channel

# Copy nanobot pyproject.toml
COPY pyproject.toml /app/nanobot/pyproject.toml

# Copy the rest of nanobot source (from build context)
COPY . /app/nanobot

# Sync nanobot project (installs nanobot-ai and dependencies)
RUN cd /app/nanobot && uv sync --no-dev

# Install workspace dependencies explicitly using uv pip
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --python /app/.venv/bin/python -e /app/mcp

RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --python /app/.venv/bin/python -e /app/nanobot-websocket-channel/nanobot-channel-protocol

RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --python /app/.venv/bin/python -e /app/nanobot-websocket-channel/nanobot-webchat

# ---
# Stage 2: use a final image without uv
# ---

ARG REGISTRY_PREFIX_DOCKER_HUB
FROM ${REGISTRY_PREFIX_DOCKER_HUB}python:3.14.2-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8

# Setup a non-root user
RUN groupadd --system --gid 999 nonroot \
    && useradd --system --gid 999 --uid 999 --create-home nonroot

# Copy the application from the builder
COPY --from=builder --chown=nonroot:nonroot /app /app

# Install CA certificates for HTTPS
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Use the non-root user
USER nonroot

WORKDIR /app/nanobot

# Run the nanobot gateway via entrypoint
CMD ["python", "/app/nanobot/entrypoint.py"]
