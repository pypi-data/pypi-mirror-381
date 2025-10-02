#        _       __        __    __________    _____     __   __     __
#   	/ \	    |  |	  |__|  |__________|  |  _  \   |__|  \ \   / /
#      / _ \	|  |	   __       |  |      | |_)  |   __    \ \_/ /   Alitrix - Modern NLP
#     / /_\ \	|  |	  |  |      |  |      |  _  /   |  |    } _ {    Languages: Python, C#
#    / _____ \	|  |____  |  |      |  |      | | \ \   |  |   / / \ \   http://github.com/Alitrix
#   /_/     \_\	|_______| |__|	    |__|      |_|  \_\  |__|  /_/   \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Alitrix Authors <http://github.com/Alitrix>

#------INTERFACES-----------------------------------------------------------
from ..Infrastructure.MCP.Middleware.logging_middleware import LoggingMiddleware
from ..Application.Abstractions.External.base_mcp_client import BaseMCPClient
from ..Infrastructure.MCP.mcp_client import MCPClient
from ..Infrastructure.Rest.hash_token_config import HashTokenConfig
from ..Application.Abstractions.Core.base_jwt_service import BaseAuthServiceFWDI
from .AuthService.auth_service_static import AuthServiceFWDI
from ..Application.Abstractions.Core.base_jwt_service_instance import BaseAuthServiceV2FWDI
from ..Infrastructure.AuthService.auth_service_inst import AuthServiceV2FWDI
from ..Application.Abstractions.External.base_service_collection import BaseServiceCollectionFWDI
from ..Application.Abstractions.External.base_rest_client import BaseRestClientFWDI
from ..Application.Abstractions.Core.base_hash_token_config import BaseHashTokenConfig
#------/INTERFACES----------------------------------------------------------

#-----INSTANCE--------------------------------------------------------------
from ..Infrastructure.Rest.rest_client import RestClientFWDI
#-----/INSTANCE-------------------------------------------------------------

class DependencyInjection():
    @staticmethod
    def AddInfrastructure(services:BaseServiceCollectionFWDI):
        services.AddSingleton(BaseHashTokenConfig, HashTokenConfig)
        services.AddTransient(BaseRestClientFWDI, RestClientFWDI)
        services.AddSingleton(BaseAuthServiceFWDI, AuthServiceFWDI)
        services.AddTransient(BaseAuthServiceV2FWDI, AuthServiceV2FWDI)
        services.AddTransient(BaseMCPClient, MCPClient)
    
    @staticmethod
    def AdLog(services: BaseServiceCollectionFWDI):
        services.AddLog(LoggingMiddleware)