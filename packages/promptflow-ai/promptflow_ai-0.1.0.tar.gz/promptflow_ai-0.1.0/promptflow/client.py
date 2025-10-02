"""
PromptFlow SDK Client
"""

import requests
from typing import Optional, Dict, Any, List
from datetime import datetime


class PromptFlowClient:
    """
    Client for interacting with the PromptFlow API.

    Args:
        base_url: The base URL of your PromptFlow instance (default: http://localhost:8000)
        api_key: Optional API key for authentication (not yet implemented)

    Example:
        >>> client = PromptFlowClient()
        >>> prompt = client.get_prompt("customer-support")
        >>> print(prompt['production_version']['content'])
    """

    def __init__(self, base_url: str = "http://localhost:8000", api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()

        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make HTTP request to API"""
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()

    # Prompt Management

    def list_prompts(self) -> List[Dict[str, Any]]:
        """
        List all prompts.

        Returns:
            List of prompt summaries

        Example:
            >>> prompts = client.list_prompts()
            >>> for p in prompts:
            ...     print(f"{p['name']}: v{p['current_version']}")
        """
        return self._request('GET', '/prompts')

    def get_prompt(self, name: str) -> Dict[str, Any]:
        """
        Get detailed prompt information including all versions.

        Args:
            name: The prompt name

        Returns:
            Complete prompt data with version history

        Example:
            >>> prompt = client.get_prompt("customer-support")
            >>> print(prompt['production_version']['content'])
        """
        return self._request('GET', f'/prompts/{name}')

    def get_production_prompt(self, name: str) -> str:
        """
        Get the production prompt content (convenience method).

        Args:
            name: The prompt name

        Returns:
            The production version content string

        Example:
            >>> content = client.get_production_prompt("customer-support")
            >>> assistant = vapi.create_assistant(prompt=content)
        """
        prompt = self.get_prompt(name)
        return prompt['production_version']['content']

    def create_prompt(self, name: str, content: str, message: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new prompt.

        Args:
            name: Unique prompt name (e.g., "customer-support")
            content: The prompt text/instructions
            message: Optional commit message

        Returns:
            Created prompt and version data

        Example:
            >>> result = client.create_prompt(
            ...     name="sales-agent",
            ...     content="You are a helpful sales agent",
            ...     message="Initial version"
            ... )
        """
        return self._request('POST', '/prompts', json={
            'name': name,
            'content': content,
            'message': message or f'Created prompt {name}'
        })

    def update_prompt(self, name: str, content: str, message: Optional[str] = None) -> Dict[str, Any]:
        """
        Update a prompt (creates new version).

        Args:
            name: The prompt name
            content: New prompt content
            message: Commit message describing the change

        Returns:
            Updated prompt and new version data

        Example:
            >>> result = client.update_prompt(
            ...     name="sales-agent",
            ...     content="You are an EXCELLENT sales agent",
            ...     message="Made greeting more enthusiastic"
            ... )
        """
        return self._request('PUT', f'/prompts/{name}', json={
            'content': content,
            'message': message or f'Updated prompt {name}'
        })

    # Version Management

    def deploy_version(self, name: str, version_number: int) -> Dict[str, Any]:
        """
        Deploy a specific version to production.

        Args:
            name: The prompt name
            version_number: Version number to deploy

        Returns:
            Updated prompt data

        Example:
            >>> # Rollback to v1
            >>> client.deploy_version("sales-agent", 1)
        """
        return self._request('POST', f'/prompts/{name}/deploy/{version_number}')

    def get_version(self, name: str, version_number: int) -> Dict[str, Any]:
        """
        Get a specific version's details.

        Args:
            name: The prompt name
            version_number: Version number

        Returns:
            Version data
        """
        prompt = self.get_prompt(name)
        for version in prompt['versions']:
            if version['version_number'] == version_number:
                return version
        raise ValueError(f"Version {version_number} not found for prompt {name}")

    # Analytics & Tracking

    def track_conversation(
        self,
        name: str,
        success: Optional[bool] = None,
        turns: Optional[int] = None,
        duration_seconds: Optional[int] = None,
        custom_metrics: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Track a conversation with flexible metrics.

        Args:
            name: The prompt name
            success: Whether the conversation was successful (optional)
            turns: Number of conversation turns (optional)
            duration_seconds: Duration in seconds (optional)
            custom_metrics: Custom metrics specific to your use case (optional)
            metadata: Additional context data (optional)

        Returns:
            Confirmation message

        Example:
            >>> # Restaurant booking agent
            >>> client.track_conversation(
            ...     name="restaurant-booking",
            ...     success=True,
            ...     turns=6,
            ...     duration_seconds=95,
            ...     custom_metrics={
            ...         "booking_made": True,
            ...         "party_size": 4,
            ...         "booking_time": "7:00 PM",
            ...         "estimated_revenue": 120.00
            ...     },
            ...     metadata={"user_id": "user_789"}
            ... )

            >>> # E-commerce sales agent
            >>> client.track_conversation(
            ...     name="sales-agent",
            ...     success=True,
            ...     custom_metrics={
            ...         "purchase_made": True,
            ...         "cart_value": 299.99,
            ...         "discount_applied": 15,
            ...         "products_viewed": 3
            ...     }
            ... )
        """
        return self._request('POST', f'/prompts/{name}/conversations', json={
            'success': success,
            'turns': turns,
            'duration_seconds': duration_seconds,
            'custom_metrics': custom_metrics or {},
            'metadata': metadata or {}
        })

    def get_metrics(self, name: str, version_number: Optional[int] = None) -> Dict[str, Any]:
        """
        Get analytics metrics for a prompt.

        Args:
            name: The prompt name
            version_number: Optional specific version (defaults to all versions)

        Returns:
            Metrics data including success rate, avg turns, avg duration

        Example:
            >>> metrics = client.get_metrics("sales-agent")
            >>> print(f"Success rate: {metrics['success_rate']}%")
        """
        endpoint = f'/prompts/{name}/metrics'
        if version_number is not None:
            endpoint += f'?version={version_number}'
        return self._request('GET', endpoint)

    # Integration Helpers

    def get_vapi_config(self, name: str) -> Dict[str, Any]:
        """
        Get prompt configured for Vapi integration.

        Args:
            name: The prompt name

        Returns:
            Dict with content, id, and version

        Example:
            >>> config = client.get_vapi_config("sales-agent")
            >>> assistant = vapi.assistants.create(
            ...     model={'messages': [{'role': 'system', 'content': config['content']}]}
            ... )
        """
        prompt = self.get_prompt(name)
        return {
            'content': prompt['production_version']['content'],
            'id': prompt['id'],
            'version': prompt['production_version']['version_number']
        }

    def get_retell_config(self, name: str) -> Dict[str, str]:
        """
        Get prompt configured for Retell AI integration.

        Args:
            name: The prompt name

        Returns:
            Dict with initial_prompt key

        Example:
            >>> config = client.get_retell_config("sales-agent")
            >>> agent = retell.agent.create(**config)
        """
        prompt = self.get_prompt(name)
        return {
            'initial_prompt': prompt['production_version']['content']
        }
