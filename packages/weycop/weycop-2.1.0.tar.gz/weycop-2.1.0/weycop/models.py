"""
Data models for WeyCP Client
"""

from typing import List, Optional, Literal, Dict, Any
from dataclasses import dataclass


@dataclass
class Message:
    """Chat message"""
    role: Literal["system", "user", "assistant"]
    content: str
    
    def to_dict(self) -> Dict[str, str]:
        return {"role": self.role, "content": self.content}


@dataclass
class Usage:
    """Token usage information"""
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


@dataclass
class Choice:
    """Chat completion choice"""
    index: int
    message: Message
    finish_reason: Optional[str] = None


@dataclass
class ChatCompletion:
    """Chat completion response"""
    id: str
    object: str
    created: int
    model: str
    usage: Usage
    choices: List[Choice]


@dataclass 
class ProviderConfig:
    """Configuration for a specific AI provider"""
    name: Literal["local", "openai", "anthropic"]
    models: List[str]
    description: str
    requires_api_key: bool
    

@dataclass
class ModelInfo:
    """Detailed information about a specific model"""
    name: str
    provider: Literal["local", "openai", "anthropic"]
    description: str
    context_length: int
    cost_per_1k_input_tokens: float
    cost_per_1k_output_tokens: float
    best_for: List[str]


@dataclass
class ChatCompletionChunk:
    """Streaming chat completion chunk"""
    id: str
    object: str
    created: int
    model: str
    choices: List[Dict[str, Any]]


@dataclass
class HealthStatus:
    """Health check response"""
    status: str
    ollama_models: List[Dict[str, Any]]
    timestamp: str