#!/usr/bin/python

#    Copyright 2023 Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Trestle Bot base authored object"""

from abc import ABC, abstractmethod


class AuthoredObjectException(Exception):
    """An error during object authoring"""


class AuthorObjectBase(ABC):
    """
    Abstract base class for OSCAL objects that are authored.
    """

    def __init__(self, trestle_root: str) -> None:
        """Initialize task base and store trestle root path"""
        self._trestle_root = trestle_root

    @abstractmethod
    def assemble(self, model_path: str, version_tag: str = "") -> None:
        """Execute assemble for model path"""
