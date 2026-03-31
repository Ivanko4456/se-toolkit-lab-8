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

<!-- Paste a short nanobot startup log excerpt showing the gateway started inside Docker -->

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->

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
