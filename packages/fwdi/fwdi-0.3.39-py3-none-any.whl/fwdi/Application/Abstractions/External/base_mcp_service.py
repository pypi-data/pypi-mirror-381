from abc import ABC, abstractmethod
from collections.abc import Awaitable
from typing import Any, Callable

from fastmcp.server.server import Transport
from fastmcp.prompts.prompt import PromptResult
from fastmcp.server.http import StarletteWithLifespan

class BaseMCPService(ABC):

    @abstractmethod
    def add_tool(self, 
                 fn_tool:Callable[..., Any], 
                 description:str, 
                 tags:set[str], 
                 name:str=str(), 
                 title:str=str()):
        ...
    
    @abstractmethod
    def add_resource(self, 
                     fn_tool:Callable[..., Any], 
                     uri:str, 
                     description:str, 
                     tags:set[str], 
                     name:str=str(), 
                     title:str=str()):
        ...
    
    @abstractmethod
    def add_prompt(self, 
                   fn_tool:Callable[..., PromptResult | Awaitable[PromptResult]], 
                   description:str, 
                   tags:set[str], 
                   name:str=str(), 
                   title:str=str()):
        ...
    
    @abstractmethod
    def run(self, transport:Transport='streamable-http'):
        ...
    
    @abstractmethod
    def get_http_app(self, path:str='/mcp')->StarletteWithLifespan:
        ...
    
    @abstractmethod
    def create_proxy_from_config(self, 
                                 name:str, 
                                 config_file:str,
                                 path:str='/mcp_proxy')->bool:
        ...
    
    @abstractmethod
    def create_proxy_from_client(self, 
                                 url:str,
                                 api_key:str)->bool:
        ...