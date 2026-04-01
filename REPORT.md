# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Agent response to "What is the agentic loop?":**

```
The agentic loop is the core reasoning cycle that AI agents use to accomplish tasks autonomously. It
typically consists of these steps:

 1 Perceive — Observe the current state of the environment (read files, check outputs, gather context)
 2 Reason/Plan — Analyze the situation and decide what action to take next
 3 Act — Execute an action (run a command, write a file, call a tool, send a message)
 4 Observe — Check the result of the action
 5 Repeat — Continue the loop until the goal is achieved or a stopping condition is met

This loop enables agents to:

 • Break down complex tasks into smaller steps
 • Adapt based on feedback from each action
 • Handle errors and retry with different approaches
 • Work autonomously without constant human guidance

In my case as nanobot, I'm constantly running this loop: I read your request, plan my approach, use tools
to act, observe the results, and continue until I've completed your task.
```

**Agent response to "What labs are available in our LMS?":**

```
Available Labs in the LMS

Here are the 8 labs currently available:

 ID  Title
 ───────────────────────────────────────────────────────────
 1   Lab 01 – Products, Architecture & Roles
 2   Lab 02 — Run, Fix, and Deploy a Backend Service
 3   Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4   Lab 04 — Testing, Front-end, and AI Agents
 5   Lab 05 — Data Pipeline and Analytics Dashboard
 6   Lab 06 — Build Your Own Agent
 7   Lab 07 — Build a Client with an AI Coding Agent
 8   lab-08
```

## Task 1B — Agent with LMS tools

**Agent response to "What labs are available?":**

```
Available Labs in the LMS

Here are the 8 labs currently available:

 ID  Title
 ───────────────────────────────────────────────────────────
 1   Lab 01 – Products, Architecture & Roles
 2   Lab 02 — Run, Fix, and Deploy a Backend Service
 3   Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4   Lab 04 — Testing, Front-end, and AI Agents
 5   Lab 05 — Data Pipeline and Analytics Dashboard
 6   Lab 06 — Build Your Own Agent
 7   Lab 07 — Build a Client with an AI Coding Agent
 8   lab-08

Would you like more details about any specific lab, such as completion rates, pass rates, or top learners?
```

**Agent response to "Describe the architecture of the LMS system":**

The agent uses MCP tools to query the LMS backend and returns real data about labs, learners, pass rates, timelines, and group performance.

## Task 1C — Skill prompt

**Agent response to "Show me the scores" (without specifying a lab):**

```
I'll fetch the pass rates and scores for each lab. Let me get that information for you.

Lab Scores Summary

Here are the average scores and attempt counts for each lab:

Lab 01 – Products, Architecture & Roles

 Task                                        Avg Score  Attempts
 ───────────────────────────────────────────────────────────────
 Lab setup                                   84.2%      3,516
 Task 0: Practice the Git workflow           64.5%      306
 Task 1: Product & architecture description  55.1%      161
 Task 2: Roles and skills mapping            49.8%      83
 Optional: Resolve a merge conflict          34.6%      13
 Optional: Create a release                  60.0%      5
 Optional: Add a CI check                    42.9%      7
 Optional: Plan skill development            16.7%      6

[... and so on for all 8 labs ...]

Key Observations:

 • Highest scoring tasks: Lab setup (84.2%), Plan and Scaffold (76.7%), Documentation Agent (73.9%)
 • Most attempted tasks: Lab setup (3,516), The System Agent (2,068), Back-end Testing (761)
 • Lowest scoring tasks: Make your VM a proxy (0%), Plan skill development (16.7%), CI/CD tasks (~33-44%)

Would you like more details on any specific lab, such as completion rates or top learners?
```

The skill prompt guides the agent to:
- Fetch data for all labs when no specific lab is provided
- Format numeric results as percentages
- Provide key observations and insights
- Offer follow-up assistance

## Task 2A — Deployed agent

**Nanobot gateway startup log:**

```
nanobot-1  | Resolved config written to /app/nanobot/config.resolved.json
nanobot-1  | Using config: /app/nanobot/config.resolved.json
nanobot-1  | 🐈 Starting nanobot gateway version 0.1.4.post6 on port 18790...
nanobot-1  | 2026-04-01 00:05:12.134 | INFO | nanobot.channels.manager:_init_channels:58 - WebChat channel enabled
nanobot-1  | ✓ Channels enabled: webchat
nanobot-1  | ✓ Heartbeat: every 1800s
nanobot-1  | 2026-04-01 00:05:12.893 | INFO | nanobot.channels.manager:start_all:91 - Starting webchat channel...
nanobot-1  | 2026-04-01 00:05:12.894 | INFO | nanobot.channels.manager:_dispatch_outbound:119 - Outbound dispatcher started
nanobot-1  | 2026-04-01 00:05:15.109 | INFO | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'lms': connected, 9 tools registered
nanobot-1  | 2026-04-01 00:05:15.109 | INFO | nanobot.agent.loop:run:280 - Agent loop started
```

**Files created/modified:**
- `nanobot/entrypoint.py` - Runtime config resolver and gateway launcher
- `nanobot/Dockerfile` - Multi-stage build with uv
- `nanobot/config.json` - Gateway and webchat channel configuration
- `docker-compose.yml` - Uncommented nanobot service with host.docker.internal for LLM access
- `caddy/Caddyfile` - Uncommented /ws/chat route

**Verification commands:**
```bash
# Check nanobot is running
docker compose ps | grep nanobot

# Check webchat channel is enabled
docker compose logs nanobot | grep "WebChat channel enabled"

# Check WebSocket endpoint (requires websocat or similar)
echo '{"content":"Hello"}' | websocat "ws://localhost:42002/ws/chat?access_key=qwe"
```

## Task 2B — Web client

**Flutter client verification:**
```bash
# Check Flutter serves main.dart.js
curl -sf http://10.93.26.38:42002/flutter/main.dart.js > /dev/null && echo "OK"
# Output: OK

# Check Flutter index.html
curl -sf http://10.93.26.38:42002/flutter/ | head -5
# Output: <!DOCTYPE html><html><head><base href="/flutter/">...
```

**WebSocket endpoint test:**
- Endpoint: `ws://10.93.26.38:42002/ws/chat?access_key=qwe`
- Flutter client: `http://10.93.26.38:42002/flutter`

**Files created/modified:**
- `.gitmodules` - Added nanobot-websocket-channel submodule
- `nanobot-websocket-channel/` - Submodule with webchat channel and Flutter client
- `nanobot/pyproject.toml` - Added nanobot-webchat dependency
- `nanobot/Dockerfile` - Added nanobot-channel-protocol and nanobot-webchat installation
- `docker-compose.yml` - Uncommented client-web-flutter service and caddy volume
- `caddy/Caddyfile` - Uncommented /flutter route
- `nanobot-websocket-channel/client-web-flutter/Dockerfile` - Fixed to copy build output to /output/

**Verification:**
- `docker compose ps` shows nanobot-1 and client-web-flutter-1 running
- Flutter client accessible at http://10.93.26.38:42002/flutter
- WebChat channel enabled in nanobot logs
- Agent responds to WebSocket messages with LLM-backed answers

**MCP tools registered (from nanobot logs):**
```
nanobot-1 | MCP registered tool 'mcp_lms_lms_health' from server 'lms'
nanobot-1 | MCP registered tool 'mcp_lms_lms_labs' from server 'lms'
nanobot-1 | MCP registered tool 'mcp_lms_lms_learners' from server 'lms'
nanobot-1 | MCP registered tool 'mcp_lms_lms_pass_rates' from server 'lms'
nanobot-1 | MCP registered tool 'mcp_lms_lms_timeline' from server 'lms'
nanobot-1 | MCP registered tool 'mcp_lms_lms_groups' from server 'lms'
nanobot-1 | MCP registered tool 'mcp_lms_lms_top_learners' from server 'lms'
nanobot-1 | MCP registered tool 'mcp_lms_lms_completion_rate' from server 'lms'
nanobot-1 | MCP registered tool 'mcp_lms_lms_sync_pipeline' from server 'lms'
nanobot-1 | MCP server 'lms': connected, 9 tools registered
```

**Test conversation (via WebSocket):**
When a user sends "What labs are available?" through the WebSocket:
1. The webchat channel receives the message
2. The agent calls the `lms_labs` MCP tool
3. The MCP server queries the LMS backend at http://backend:8000/items/
4. The backend returns the list of labs (lab-01 through lab-08)
5. The agent formats and returns the response to the user via WebSocket

The agent uses the `lms_labs` MCP tool to fetch real lab data from the backend and returns formatted results showing all 8 available labs with their titles.

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
