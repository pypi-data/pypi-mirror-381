# PromptFlow SDK

**Version control and analytics for voice AI prompts**

PromptFlow is like Git for AI prompts. Version control, instant rollbacks, A/B testing, and metrics tracking for voice AI agents built on Vapi, Retell, Bland AI, and custom voice stacks.

## Installation

```bash
pip install promptflow-sdk
```

## Quick Start

```python
from promptflow import PromptFlowClient

# Initialize client
client = PromptFlowClient(base_url="http://localhost:8000")

# Get production prompt
prompt_content = client.get_production_prompt("customer-support")

# Use with your voice AI platform
# Example with Vapi:
from vapi import Vapi
vapi = Vapi(token='your-token')
assistant = vapi.assistants.create(
    model={
        'provider': 'openai',
        'model': 'gpt-4',
        'messages': [{'role': 'system', 'content': prompt_content}]
    }
)

# Track conversation metrics
client.track_conversation(
    name="customer-support",
    success=True,
    turns=12,
    duration_seconds=180
)
```

## Features

- **Version Control**: Every prompt change creates an immutable version
- **Instant Rollback**: Revert to any previous version in seconds
- **Analytics**: Track success rates, turns, and duration per version
- **Platform Integrations**: Built-in helpers for Vapi, Retell, and Bland AI
- **Simple API**: Clean, intuitive Python interface

## Core Methods

### Prompt Management

```python
# List all prompts
prompts = client.list_prompts()

# Get prompt details
prompt = client.get_prompt("customer-support")

# Create new prompt
client.create_prompt(
    name="sales-agent",
    content="You are a helpful sales agent",
    message="Initial version"
)

# Update prompt (creates new version)
client.update_prompt(
    name="sales-agent",
    content="You are an EXCELLENT sales agent",
    message="Made greeting more enthusiastic"
)
```

### Version Control

```python
# Deploy specific version to production
client.deploy_version("sales-agent", version_number=2)

# Rollback to previous version
client.deploy_version("sales-agent", version_number=1)

# Get specific version
version = client.get_version("sales-agent", 2)
```

### Analytics

```python
# Track conversation
client.track_conversation(
    name="sales-agent",
    success=True,
    turns=8,
    duration_seconds=145,
    metadata={"user_id": "user_123"}
)

# Get metrics
metrics = client.get_metrics("sales-agent")
print(f"Success rate: {metrics['success_rate']}%")
print(f"Avg turns: {metrics['avg_turns']}")
print(f"Avg duration: {metrics['avg_duration_seconds']}s")

# Get metrics for specific version
metrics_v2 = client.get_metrics("sales-agent", version_number=2)
```

## Platform Integrations

### Vapi

```python
config = client.get_vapi_config("sales-agent")
assistant = vapi.assistants.create(
    model={
        'messages': [{'role': 'system', 'content': config['content']}]
    }
)
```

### Retell AI

```python
config = client.get_retell_config("sales-agent")
agent = retell.agent.create(
    agent_name="Sales Agent",
    initial_prompt=config['initial_prompt']
)
```

### Bland AI

```python
prompt_content = client.get_production_prompt("sales-agent")
call = bland.calls.create(
    prompt=prompt_content,
    phone_number="+1234567890"
)
```

## Documentation

Visit [http://localhost:3000/docs](http://localhost:3000/docs) for complete documentation.

## Requirements

- Python 3.8+
- PromptFlow backend instance running

## License

MIT License
