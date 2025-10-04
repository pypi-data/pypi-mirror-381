"""Base agent class for multi-agent architecture"""

import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional, Dict, Any
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock, ResultMessage


class BaseAgent(ABC):
    """Base class for all VulnGuard agents"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-3-5-sonnet-20241022",
        debug: bool = False
    ):
        """
        Initialize base agent
        
        Args:
            api_key: Claude API key (reads from CLAUDE_API_KEY if not provided)
            model: Claude model to use
            debug: Enable debug output
        """
        if api_key:
            os.environ["CLAUDE_API_KEY"] = api_key
        
        self.model = model
        self.debug = debug
        self.total_cost = 0.0
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Agent name for logging"""
        pass
    
    @property
    @abstractmethod
    def allowed_tools(self) -> list[str]:
        """List of tools this agent can use"""
        pass
    
    @abstractmethod
    def build_system_prompt(self) -> str:
        """Build the system prompt for this agent"""
        pass
    
    @abstractmethod
    def build_user_prompt(self, **kwargs) -> str:
        """Build the user prompt for this agent"""
        pass
    
    async def run(self, repo_path: str, **kwargs) -> Dict[str, Any]:
        """
        Run the agent
        
        Args:
            repo_path: Path to repository
            **kwargs: Agent-specific parameters
            
        Returns:
            Agent result dictionary
        """
        repo = Path(repo_path).resolve()
        if not repo.exists():
            raise ValueError(f"Repository path does not exist: {repo_path}")
        
        print(f"🤖 [{self.name}] Starting analysis...")
        
        # Configure Claude Agent SDK
        options = ClaudeAgentOptions(
            allowed_tools=self.allowed_tools,
            cwd=str(repo),
            system_prompt=self.build_system_prompt(),
            max_turns=30,
            permission_mode='default',
        )
        
        # Build user prompt
        user_prompt = self.build_user_prompt(**kwargs)
        
        # Execute query
        response_text = []
        
        try:
            async for message in query(prompt=user_prompt, options=options):
                # Debug output
                if self.debug and isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(f"📝 [{self.name}]: {block.text[:150]}...")
                
                # Collect text responses
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            response_text.append(block.text)
                
                # Track usage
                if isinstance(message, ResultMessage):
                    usage_data = message.usage
                    if usage_data and hasattr(usage_data, 'total_cost_usd'):
                        self.total_cost = usage_data.total_cost_usd or 0.0
            
            # Display cost
            if self.total_cost > 0:
                print(f"💰 [{self.name}] Cost: ${self.total_cost:.4f}")
            
            # Process results
            full_response = "\n".join(response_text)
            result = self.process_results(full_response, str(repo), **kwargs)
            
            print(f"✅ [{self.name}] Complete")
            
            return result
            
        except Exception as e:
            print(f"❌ [{self.name}] Error: {e}")
            raise
    
    @abstractmethod
    def process_results(self, response: str, repo_path: str, **kwargs) -> Dict[str, Any]:
        """
        Process the agent's response into structured results
        
        Args:
            response: Full text response from Claude
            repo_path: Repository path
            **kwargs: Agent-specific parameters
            
        Returns:
            Structured result dictionary
        """
        pass
    
    def get_vulnguard_dir(self, repo_path: str) -> Path:
        """Get or create .vulnguard directory"""
        vulnguard_dir = Path(repo_path) / ".vulnguard"
        vulnguard_dir.mkdir(exist_ok=True)
        return vulnguard_dir
