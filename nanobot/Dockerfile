# Nanobot gateway Dockerfile - multi-stage build with uv
# Build context: ./nanobot
# Additional contexts: workspace: .

# ---
# Stage 1: build the application in the `/app` directory.
# ---

ARG REGISTRY_PREFIX_DOCKER_HUB
FROM ${REGISTRY_PREFIX_DOCKER_HUB}astral/uv:python3.14-bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Omit development dependencies
ENV UV_NO_DEV=1

# Disable Python downloads
ENV UV_PYTHON_DOWNLOADS=0

WORKDIR /app
COPY --from=workspace pyproject.toml uv.lock /app/

# Copy nanobot, mcp, and nanobot-websocket-channel projects from workspace
COPY pyproject.toml /app/nanobot/pyproject.toml
COPY --from=workspace mcp /app/mcp
COPY --from=workspace nanobot-websocket-channel /app/nanobot-websocket-channel

# Sync nanobot with workspace dependencies (without nanobot-webchat first)
RUN --mount=type=cache,target=/root/.cache/uv \
    cd /app/nanobot && uv sync --frozen --no-dev

# Copy the rest of nanobot source (from build context)
COPY . /app/nanobot

# Install nanobot-channel-protocol first (dependency of nanobot-webchat)
RUN --mount=type=cache,target=/root/.cache/uv \
    cd /app/nanobot && uv pip install --no-deps -e /app/nanobot-websocket-channel/nanobot-channel-protocol

# Install nanobot-webchat
RUN --mount=type=cache,target=/root/.cache/uv \
    cd /app/nanobot && uv pip install --no-deps -e /app/nanobot-websocket-channel/nanobot-webchat

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
ENV PYTHONPATH="/app/nanobot"

# Use the non-root user
USER nonroot

WORKDIR /app/nanobot

# Run the nanobot gateway via entrypoint
CMD ["python", "/app/nanobot/entrypoint.py"]
