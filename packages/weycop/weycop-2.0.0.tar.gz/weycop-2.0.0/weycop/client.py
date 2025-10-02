"""
WeyCP Client implementation
"""

import json
import time
from typing import List, Optional, Union, Dict, Any, Iterator
import httpx

from .models import Message, ChatCompletion, Usage, Choice, HealthStatus, ProviderConfig, ModelInfo
from .exceptions import (
    WeycopError, 
    AuthenticationError, 
    RateLimitError, 
    APIError, 
    ModelNotFoundError,
    TimeoutError as WeycopTimeoutError
)


class WeycopClient:
    """Synchronous WeyCP API client"""
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.weycop.com",
        timeout: float = 120.0
    ):
        """
        Initialize WeyCP client
        
        Args:
            api_key: Your WeyCP API key
            base_url: API base URL (default: https://api.weycop.com)
            timeout: Request timeout in seconds (default: 120.0)
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        
        self._client = httpx.Client(
            timeout=timeout,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "User-Agent": f"weycop-python/1.0.0"
            }
        )
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def close(self):
        """Close the HTTP client"""
        if self._client:
            self._client.close()
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make HTTP request and handle errors"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = self._client.request(method, url, **kwargs)
            
            if response.status_code == 401:
                raise AuthenticationError("Invalid API key")
            elif response.status_code == 429:
                raise RateLimitError("Rate limit exceeded")
            elif response.status_code >= 400:
                try:
                    error_data = response.json()
                    error_msg = error_data.get("detail", f"HTTP {response.status_code}")
                except json.JSONDecodeError:
                    error_msg = f"HTTP {response.status_code}: {response.text}"
                
                raise APIError(error_msg, status_code=response.status_code, response_data=error_data if 'error_data' in locals() else {})
            
            return response.json()
            
        except httpx.TimeoutException:
            raise WeycopTimeoutError("Request timed out")
        except httpx.RequestError as e:
            raise WeycopError(f"Request failed: {str(e)}")
    
    def chat_completions_create(
        self,
        model: str,
        messages: List[Union[Message, Dict[str, str]]],
        provider: Optional[str] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        stop: Optional[Union[str, List[str]]] = None,
        stream: bool = False
    ) -> ChatCompletion:
        """
        Create a chat completion
        
        Args:
            model: Model name (e.g., "qwen3:4b-instruct", "gpt-4o", "claude-3-5-sonnet-20241022")
            messages: List of messages
            provider: AI provider ("local", "openai", "anthropic"). If not specified, auto-detected from model name
            temperature: Sampling temperature (0-2)
            top_p: Nucleus sampling parameter (0-1)
            max_tokens: Maximum tokens to generate
            stop: Stop sequences
            stream: Whether to stream the response
            
        Returns:
            ChatCompletion object
        """
        # Convert messages to proper format
        formatted_messages = []
        for msg in messages:
            if isinstance(msg, Message):
                formatted_messages.append(msg.to_dict())
            elif isinstance(msg, dict):
                formatted_messages.append(msg)
            else:
                raise ValueError("Messages must be Message objects or dictionaries")
        
        payload = {
            "model": model,
            "messages": formatted_messages,
            "stream": stream
        }
        
        # Add provider if specified
        if provider is not None:
            payload["provider"] = provider
        
        # Add optional parameters
        if temperature is not None:
            payload["temperature"] = temperature
        if top_p is not None:
            payload["top_p"] = top_p
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens
        if stop is not None:
            payload["stop"] = stop
        
        response_data = self._make_request("POST", "/v1/chat/completions", json=payload)
        
        # Parse response
        choices = []
        for choice_data in response_data["choices"]:
            message = Message(
                role=choice_data["message"]["role"],
                content=choice_data["message"]["content"]
            )
            choice = Choice(
                index=choice_data["index"],
                message=message,
                finish_reason=choice_data.get("finish_reason")
            )
            choices.append(choice)
        
        usage = Usage(
            prompt_tokens=response_data["usage"]["prompt_tokens"],
            completion_tokens=response_data["usage"]["completion_tokens"],
            total_tokens=response_data["usage"]["total_tokens"]
        )
        
        return ChatCompletion(
            id=response_data["id"],
            object=response_data["object"],
            created=response_data["created"],
            model=response_data["model"],
            usage=usage,
            choices=choices
        )
    
    def chat_local(
        self,
        model: str,
        messages: List[Union[Message, Dict[str, str]]],
        **kwargs
    ) -> ChatCompletion:
        """
        Create a chat completion using local models (Ollama)
        
        Args:
            model: Local model name (e.g., "qwen3:4b-instruct", "llama3.1:8b-8k")
            messages: List of messages
            **kwargs: Additional parameters (temperature, max_tokens, etc.)
            
        Returns:
            ChatCompletion object
        """
        return self.chat_completions_create(model=model, messages=messages, provider="local", **kwargs)
    
    def chat_openai(
        self,
        model: str,
        messages: List[Union[Message, Dict[str, str]]],
        **kwargs
    ) -> ChatCompletion:
        """
        Create a chat completion using OpenAI models
        
        Args:
            model: OpenAI model name (e.g., "gpt-4o", "gpt-3.5-turbo")
            messages: List of messages
            **kwargs: Additional parameters (temperature, max_tokens, etc.)
            
        Returns:
            ChatCompletion object
        """
        return self.chat_completions_create(model=model, messages=messages, provider="openai", **kwargs)
    
    def chat_anthropic(
        self,
        model: str,
        messages: List[Union[Message, Dict[str, str]]],
        **kwargs
    ) -> ChatCompletion:
        """
        Create a chat completion using Anthropic models
        
        Args:
            model: Anthropic model name (e.g., "claude-3-5-sonnet-20241022")
            messages: List of messages
            **kwargs: Additional parameters (temperature, max_tokens, etc.)
            
        Returns:
            ChatCompletion object
        """
        return self.chat_completions_create(model=model, messages=messages, provider="anthropic", **kwargs)
    
    def get_available_models(self) -> Dict[str, List[str]]:
        """
        Get available models organized by provider
        
        Returns:
            Dictionary with provider names as keys and model lists as values
        """
        try:
            docs_data = self._make_request("GET", "/v1/chat/docs")
            if "models" in docs_data:
                # Group models by provider
                models_by_provider = {"local": [], "openai": [], "anthropic": []}
                for model_name, model_info in docs_data["models"].items():
                    provider = model_info.get("provider", "local")
                    if provider in models_by_provider:
                        models_by_provider[provider].append(model_name)
                return models_by_provider
            return {"local": [], "openai": [], "anthropic": []}
        except Exception:
            return {"local": [], "openai": [], "anthropic": []}
    
    def get_model_info(self, model: str) -> Optional[ModelInfo]:
        """
        Get detailed information about a specific model
        
        Args:
            model: Model name
            
        Returns:
            ModelInfo object or None if model not found
        """
        try:
            docs_data = self._make_request("GET", "/v1/chat/docs")
            if "models" in docs_data and model in docs_data["models"]:
                model_data = docs_data["models"][model]
                return ModelInfo(
                    name=model,
                    provider=model_data.get("provider", "local"),
                    description=model_data.get("description", ""),
                    context_length=model_data.get("context_length", 4096),
                    cost_per_1k_input_tokens=model_data.get("cost_per_1k_input_tokens", 0.0),
                    cost_per_1k_output_tokens=model_data.get("cost_per_1k_output_tokens", 0.0),
                    best_for=model_data.get("best_for", [])
                )
            return None
        except Exception:
            return None
    
    def health_check(self) -> HealthStatus:
        """
        Check API health status
        
        Returns:
            HealthStatus object
        """
        response_data = self._make_request("GET", "/v1/chat/health")
        
        return HealthStatus(
            status=response_data["status"],
            ollama_models=response_data["ollama_models"],
            timestamp=response_data["timestamp"]
        )
    
    def chat(
        self,
        message: str,
        model: str = "qwen3:4b-instruct",
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Simplified chat interface
        
        Args:
            message: User message
            model: Model to use
            system_prompt: Optional system prompt
            **kwargs: Additional parameters for chat_completions_create
            
        Returns:
            Assistant response as string
        """
        messages = []
        
        if system_prompt:
            messages.append(Message("system", system_prompt))
        
        messages.append(Message("user", message))
        
        completion = self.chat_completions_create(
            model=model,
            messages=messages,
            **kwargs
        )
        
        return completion.choices[0].message.content


class AsyncWeycopClient:
    """Asynchronous WeyCP API client"""
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.weycop.com",
        timeout: float = 120.0
    ):
        """
        Initialize async WeyCP client
        
        Args:
            api_key: Your WeyCP API key
            base_url: API base URL (default: https://api.weycop.com)
            timeout: Request timeout in seconds (default: 120.0)
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        
        self._client = httpx.AsyncClient(
            timeout=timeout,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "User-Agent": f"weycop-python/1.0.0"
            }
        )
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
    
    async def close(self):
        """Close the HTTP client"""
        if self._client:
            await self._client.aclose()
    
    async def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make async HTTP request and handle errors"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = await self._client.request(method, url, **kwargs)
            
            if response.status_code == 401:
                raise AuthenticationError("Invalid API key")
            elif response.status_code == 429:
                raise RateLimitError("Rate limit exceeded")
            elif response.status_code >= 400:
                try:
                    error_data = response.json()
                    error_msg = error_data.get("detail", f"HTTP {response.status_code}")
                except json.JSONDecodeError:
                    error_msg = f"HTTP {response.status_code}: {response.text}"
                
                raise APIError(error_msg, status_code=response.status_code, response_data=error_data if 'error_data' in locals() else {})
            
            return response.json()
            
        except httpx.TimeoutException:
            raise WeycopTimeoutError("Request timed out")
        except httpx.RequestError as e:
            raise WeycopError(f"Request failed: {str(e)}")
    
    async def chat_completions_create(
        self,
        model: str,
        messages: List[Union[Message, Dict[str, str]]],
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        max_tokens: Optional[int] = None,
        stop: Optional[Union[str, List[str]]] = None,
        stream: bool = False
    ) -> ChatCompletion:
        """
        Create a chat completion (async)
        
        Args:
            model: Model name
            messages: List of messages
            temperature: Sampling temperature (0-2)
            top_p: Nucleus sampling parameter (0-1)
            max_tokens: Maximum tokens to generate
            stop: Stop sequences
            stream: Whether to stream the response
            
        Returns:
            ChatCompletion object
        """
        # Convert messages to proper format
        formatted_messages = []
        for msg in messages:
            if isinstance(msg, Message):
                formatted_messages.append(msg.to_dict())
            elif isinstance(msg, dict):
                formatted_messages.append(msg)
            else:
                raise ValueError("Messages must be Message objects or dictionaries")
        
        payload = {
            "model": model,
            "messages": formatted_messages,
            "stream": stream
        }
        
        # Add optional parameters
        if temperature is not None:
            payload["temperature"] = temperature
        if top_p is not None:
            payload["top_p"] = top_p
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens
        if stop is not None:
            payload["stop"] = stop
        
        response_data = await self._make_request("POST", "/v1/chat/completions", json=payload)
        
        # Parse response
        choices = []
        for choice_data in response_data["choices"]:
            message = Message(
                role=choice_data["message"]["role"],
                content=choice_data["message"]["content"]
            )
            choice = Choice(
                index=choice_data["index"],
                message=message,
                finish_reason=choice_data.get("finish_reason")
            )
            choices.append(choice)
        
        usage = Usage(
            prompt_tokens=response_data["usage"]["prompt_tokens"],
            completion_tokens=response_data["usage"]["completion_tokens"],
            total_tokens=response_data["usage"]["total_tokens"]
        )
        
        return ChatCompletion(
            id=response_data["id"],
            object=response_data["object"],
            created=response_data["created"],
            model=response_data["model"],
            usage=usage,
            choices=choices
        )
    
    async def health_check(self) -> HealthStatus:
        """
        Check API health status (async)
        
        Returns:
            HealthStatus object
        """
        response_data = await self._make_request("GET", "/v1/chat/health")
        
        return HealthStatus(
            status=response_data["status"],
            ollama_models=response_data["ollama_models"],
            timestamp=response_data["timestamp"]
        )
    
    async def chat(
        self,
        message: str,
        model: str = "qwen3:4b-instruct",
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Simplified chat interface (async)
        
        Args:
            message: User message
            model: Model to use
            system_prompt: Optional system prompt
            **kwargs: Additional parameters for chat_completions_create
            
        Returns:
            Assistant response as string
        """
        messages = []
        
        if system_prompt:
            messages.append(Message("system", system_prompt))
        
        messages.append(Message("user", message))
        
        completion = await self.chat_completions_create(
            model=model,
            messages=messages,
            **kwargs
        )
        
        return completion.choices[0].message.content