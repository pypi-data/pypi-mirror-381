# RunRL Python SDK (v0.2.0)

The RunRL Python SDK provides a friendly, fully typed interface to the RunRL REST API. It supports
both synchronous and asynchronous workflows and introduces a principled futures system inspired by
distributed ML orchestration platforms. Use the SDK to automate training runs, monitor progress,
manipulate files, deploy checkpoints, and integrate RunRL into your ML pipelines.

## Installation

```bash
pip install runrl
```

## Quick Start

```python
from runrl import RunRLClient

client = RunRLClient(api_key="rl_your_api_key")

# Upload a reward function
reward = client.files.create_from_content(
    name="latency_reward",
    content="""def reward_fn(prompt, response):\n    return 1 - response['latency']""",
    file_type="reward_function",
)

# Launch a training run (returns a Future immediately)
future = client.runs.create(
    model="Qwen/Qwen3-8B",
    prompt_file_id="PROMPT_UUID",
    reward_file_id=reward.id,
    completion_length=1024,
)

# Wait for completion (polls RunRL behind the scenes)
run = future.result()
print(run.status)
print(run.metrics_url)
```

## Features

- **Unified Client** – simple configuration, automatic retries, pagination helpers.
- **Futures System** – wait for long-running operations with rich status metadata.
- **Sync & Async** – mirrored APIs for both paradigms (`RunRLClient` / `AsyncRunRLClient`).
- **Typed Models** – Pydantic models to validate API responses and guide development.
- **Extensive Docs** – tutorials, futures guide, and endpoint-level reference in `docs/`.

See [`docs/index.md`](docs/index.md) for the full documentation set.
