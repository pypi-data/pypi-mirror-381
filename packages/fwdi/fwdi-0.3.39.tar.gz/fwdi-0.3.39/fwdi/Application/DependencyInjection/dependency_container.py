#        _       __        __    __________    _____     __   __     __
#   	/ \	    |  |	  |__|  |__________|  |  _  \   |__|  \ \   / /
#      / _ \	|  |	   __       |  |      | |_)  |   __    \ \_/ /   Alitrix - Modern NLP
#     / /_\ \	|  |	  |  |      |  |      |  _  /   |  |    } _ {    Languages: Python, C#
#    / _____ \	|  |____  |  |      |  |      | | \ \   |  |   / / \ \   http://github.com/Alitrix
#   /_/     \_\	|_______| |__|	    |__|      |_|  \_\  |__|  /_/   \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Alitrix Authors <http://github.com/Alitrix>

import inspect
import logging
from types import UnionType
from typing import Type, TypeVar, get_args

from ...Domain.Configure.global_setting_service import GlobalSettingService
from ...Domain.Enums.service_life import ServiceLifetime

from ...Application.Logging.manager_logging import ManagerLogging
from ...Application.Abstractions.Core.service_descriptor import ServiceDescriptorFWDI
from ...Application.Abstractions.Core.base_di_container import BaseDIConteinerFWDI
from ...Application.Abstractions.Core.base_logging import BaseSysLogging

TService = TypeVar('TService')

class DependencyContainerFWDI(BaseDIConteinerFWDI):
    def __init__(self, serviceDescriptors:dict) -> None:
        self.__serviceDescriptors:dict[type, ServiceDescriptorFWDI] = serviceDescriptors
        self.__log__:BaseSysLogging = ManagerLogging.get_logging(f"{__name__}")
    
    def contains(self, base_type:type)->bool:
        #=========DEBUG============================================
        
        if GlobalSettingService.log_lvl == logging.DEBUG:
            self.__log__(f"__GetService (serviceType={base_type})")

            for item in self.__serviceDescriptors:
                compare_test = item == base_type.__name__
                self.__log__(f"{compare_test} compared Item: {item}")

        #=========DEBUG============================================

        return True if base_type.__name__ in self.__serviceDescriptors else False

    def __GetService(self, base_type:type)->tuple[TService|None, ServiceLifetime|None]:
        from ...Utilites.ext_reflection import ExtReflection

        #=========DEBUG============================================

        if GlobalSettingService.log_lvl == logging.DEBUG:
            self.__log__(f"__GetService (serviceType={base_type})")

            for item in self.__serviceDescriptors:
                compare_test = item == base_type.__name__
                self.__log__(f"{compare_test} compared Item: {item}")

        #=========DEBUG============================================
        try:
            descriptor:ServiceDescriptorFWDI = self.__serviceDescriptors.get(base_type.__name__, None)
        except Exception as ex:
            if isinstance(base_type, UnionType):
                type_args = get_args(base_type)
                class_args = [item for item in type_args if item is not type(None)]
                if class_args:
                    if hasattr(class_args[0], '__name__'):
                        name_class = class_args[0].__name__
                        descriptor:ServiceDescriptorFWDI = self.__serviceDescriptors.get(name_class, None)
                    else:
                        raise Exception("Error wrong UnionType!")
                else:
                    raise Exception("Error wrong UnionType!")
            else:
                raise Exception("Error wrong Type!")

        if not descriptor:
            raise Exception("Error Type or BaseType not exists ")

        if descriptor.Implementation:
            return descriptor.Implementation, descriptor.Lifetime

        if descriptor.ImplementationType:
            actualType = descriptor.ImplementationType
        else:
            actualType = descriptor.ServiceType

        if inspect.isabstract(actualType):
            raise Exception(f"Cannot instantiate abstract classes. : {actualType.__name__}")

        sig = inspect.signature(actualType)
        lst_args_obj:dict = {}

        if sig.parameters:
            for item in sig.parameters:
                annotation = sig.parameters[item].annotation
                implement, _ = self.__GetService(annotation)
                lst_args_obj[item] = implement
        else:
            if self.contains(actualType):
                if ExtReflection.is_injectable_init(actualType):
                    implementation = actualType(**{'is_inject': True})
                else:
                    implementation = actualType()
            else:
                implementation = actualType()

            if descriptor.Lifetime == ServiceLifetime.Singleton:
                descriptor.Implementation = implementation
                
            return implementation, descriptor.Lifetime

        if self.contains(actualType):
            if ExtReflection.is_injectable_init(actualType):
                lst_args_obj.update({'is_inject': True})

        implementation = actualType(**lst_args_obj)

        if descriptor.Lifetime == ServiceLifetime.Singleton:
            descriptor.Implementation = implementation

        return implementation, descriptor.Lifetime

    def GetService(self, cls:Type[TService])->tuple[TService|None, ServiceLifetime|None]:
        return self.__GetService(cls)