#!/usr/bin/env python3

# Copyright (c) 2000-2025, Board of Trustees of Leland Stanford Jr. University
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""
Representations of plugin sets.
"""

# Remove in Python 3.14
# See https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class/33533514#33533514
from __future__ import annotations

from abc import ABC, abstractmethod
import os
from pathlib import Path
import shlex
import subprocess
import sys
from typing import Annotated, Any, ClassVar, Literal, Optional, Union

from pydantic import BaseModel, Field

from .plugin import Plugin, PluginIdentifier
from .util import BaseModelWithRoot

#: A type alias for the plugin set catalog kind.
PluginSetCatalogKind = Literal['PluginSetCatalog']


class PluginSetCatalog(BaseModelWithRoot):
    """
    A Pydantic model (``lockss.turtles.util.BaseModelWithRoot``) to represent a
    plugin set catalog.
    """
    #: This object's kind.
    kind: PluginSetCatalogKind = Field(title='Kind', description="This object's kind")
    #: A non-empty list of plugin set files.
    plugin_set_files: list[str] = Field(alias='plugin-set-files', min_length=1, title='Plugin Set Files', description="A non-empty list of plugin set files")

    def get_plugin_set_files(self) -> list[Path]:
        """
        Return this plugin set catalog's list of plugin set definition file
        paths (relative to the root if not absolute).

        :return: A list of plugin set definition file paths.
        :rtype: list[Path]
        """
        return [self.get_root().joinpath(p) for p in self.plugin_set_files]


#: A type alias for the plugin set builder type.
PluginSetBuilderType = Literal['ant', 'maven']


class BasePluginSetBuilder(BaseModelWithRoot, ABC):
    """
    An abstract Pydantic model (``lockss.turtles.util.BaseModelWithRoot``) to
    represent a plugin set builder, with concrete implementations
    ``AntPluginSetBuilder`` and ``MavenPluginSetBuilder``.
    """

    #: Pydantic definition of the ``type`` field.
    TYPE_FIELD: ClassVar[dict[str, str]] = dict(title='Plugin Builder Type', description='A plugin builder type')
    #: Pydantic definition of the ``main`` field.
    MAIN_FIELD: ClassVar[dict[str, str]] = dict(title='Main Code Path', description="The path to the plugins' source code, relative to the root of the project")
    #: Pydantic definition of the ``test`` field.
    TEST_FIELD: ClassVar[dict[str, str]] = dict(title='Test Code Path', description="The path to the plugins' unit tests, relative to the root of the project")

    @abstractmethod
    def build_plugin(self, plugin_id: PluginIdentifier, keystore_path: Path, keystore_alias: str, keystore_password=None) -> tuple[Path, Plugin]:
        """
        Builds the given plugin, using the given plugin signing credentials.

        :param plugin_id: A plugin identifier.
        :type plugin_id: PluginIdentifier
        :param keystore_path: The path to the plugin signing keystore.
        :type keystore_path: Path
        :param keystore_alias: The signing alias to use from the plugin signing
                               keystore.
        :type keystore_alias: str
        :param keystore_password: The signing password.
        :type keystore_password: Any
        :return: A tuple of the plugin JAR path and the corresponding ``Plugin``
                 object.
        :rtype: tuple[Path, Plugin]
        """
        pass # FIXME: typing of keystore_password

    def get_main(self) -> Path:
        """
        Returns this plugin set builder's main code path (relative to the root
        if not absolute).

        :return: This plugin set's main code path.
        :rtype: Path
        :raises ValueError: If this object is not properly initialized.
        """
        return self.get_root().joinpath(self._get_main())

    def get_test(self) -> Path:
        """
        Returns this plugin set builder's unit test path (relative to the root
        if not absolute).

        :return: This plugin set's unit test path.
        :rtype: Path
        :raises ValueError: If this object is not properly initialized.
        """
        return self.get_root().joinpath(self._get_test())

    def get_type(self) -> PluginSetBuilderType:
        """
        Returns this plugin set builder's type.

        :return: This plugin set builder's type.
        :rtype: PluginSetBuilderType
        """
        return getattr(self, 'type')

    def has_plugin(self, plugin_id: PluginIdentifier) -> bool:
        """
        Determines if the given plugin identifier represents a plugin that is
        present in the plugin set.

        :param plugin_id: A plugin identifier.
        :type plugin_id: PluginIdentifier
        :return: Whether the plugin is present in the plugin set.
        :rtype: bool
        """
        return self._plugin_path(plugin_id).is_file()

    def make_plugin(self, plugin_id: PluginIdentifier) -> Plugin:
        """
        Makes a ``Plugin`` object from the given plugin identifier.

        :param plugin_id: A plugin identifier.
        :type plugin_id: PluginIdentifier
        :return: The corresponding ``Plugin`` object.
        :rtype: Plugin
        """
        return Plugin.from_path(self._plugin_path(plugin_id))

    def _get_main(self) -> str:
        """
        Returns the concrete implementation's ``main`` field.

        :return: The ``main`` field.
        :rtype: str
        """
        return getattr(self, 'main')

    def _get_test(self) -> str:
        """
        Returns the concrete implementation's ``test`` field.

        :return: The ``test`` field.
        :rtype: str
        """
        return getattr(self, 'test')

    def _plugin_path(self, plugin_id: PluginIdentifier) -> Path:
        """
        Returns the path of the plugin file for the given plugin identifier
        relative to the plugin set's main code path.

        :param plugin_id: A plugin identifier.
        :type plugin_id: PluginIdentifier
        :return: The plugin file.
        :rtype: Path
        """
        return self.get_main().joinpath(Plugin.id_to_file(plugin_id))


class AntPluginSetBuilder(BasePluginSetBuilder):
    #: Default value for the ``main`` field.
    DEFAULT_MAIN: ClassVar[str] = 'plugins/src'
    #: Default value for the ``test`` field.
    DEFAULT_TEST: ClassVar[str] = 'plugins/test/src'

    #: This plugin set builder's type.
    type: Literal['ant'] = Field(**BasePluginSetBuilder.TYPE_FIELD)
    #: This plugin set builder's main code path.
    main: Optional[str] = Field(DEFAULT_MAIN, **BasePluginSetBuilder.MAIN_FIELD)
    #: This plugin set builder's unit test path.
    test: Optional[str] = Field(DEFAULT_TEST, **BasePluginSetBuilder.TEST_FIELD)

    #: An internal flag to remember if a build has occurred.
    _built: bool

    def build_plugin(self, plugin_id: PluginIdentifier, keystore_path: Path, keystore_alias: str, keystore_password=None) -> tuple[Path, Plugin]:
        # Prerequisites
        if 'JAVA_HOME' not in os.environ:
            raise Exception('error: JAVA_HOME must be set in your environment')
        # Big build (maybe)
        self._big_build()
        # Little build
        return self._little_build(plugin_id, keystore_path, keystore_alias, keystore_password=keystore_password)

    def model_post_init(self, context: Any) -> None:
        super().model_post_init(context)
        self._built = False

    def _big_build(self) -> None:
        """
        Optionally performs the "big build".
        """
        if not self._built:
            # Do build
            subprocess.run('ant load-plugins',
                           shell=True, cwd=self.get_root(), check=True, stdout=sys.stdout, stderr=sys.stderr)
            self._built = True

    def _little_build(self, plugin_id: PluginIdentifier, keystore_path: Path, keystore_alias: str, keystore_password: str=None) -> tuple[Path, Plugin]:
        """
        Performs the "little build" of the given plugin.

        :param plugin_id: A plugin identifier.
        :type plugin_id: PluginIdentifier
        :param keystore_path: The path to the plugin signing keystore.
        :type keystore_path: Path
        :param keystore_alias: The signing alias to use from the plugin signing
                               keystore.
        :type keystore_alias: str
        :param keystore_password: The signing password.
        :type keystore_password: str
        :return: A tuple of the plugin JAR path and the corresponding ``Plugin``
                 object.
        :rtype: tuple[Path, Plugin]
        """
        orig_plugin = None
        cur_id = plugin_id
        # Get all directories for jarplugin -d
        dirs = []
        while cur_id is not None:
            cur_plugin = self.make_plugin(cur_id)
            orig_plugin = orig_plugin or cur_plugin
            cur_dir = Plugin.id_to_dir(cur_id)
            if cur_dir not in dirs:
                dirs.append(cur_dir)
            for aux_package in cur_plugin.get_aux_packages():
                aux_dir = Plugin.id_to_dir(f'{aux_package}.FAKEPlugin')
                if aux_dir not in dirs:
                    dirs.append(aux_dir)
            cur_id = cur_plugin.get_parent_identifier()
        # Invoke jarplugin
        jar_fstr = Plugin.id_to_file(plugin_id)
        jar_path = self.get_root().joinpath('plugins/jars', f'{plugin_id}.jar')
        jar_path.parent.mkdir(parents=True, exist_ok=True)
        cmd = ['test/scripts/jarplugin',
               '-j', str(jar_path),
               '-p', str(jar_fstr)]
        for d in dirs:
            cmd.extend(['-d', d])
        subprocess.run(cmd, cwd=self.get_root(), check=True, stdout=sys.stdout, stderr=sys.stderr)
        # Invoke signplugin
        cmd = ['test/scripts/signplugin',
               '--jar', str(jar_path),
               '--alias', keystore_alias,
               '--keystore', str(keystore_path)]
        if keystore_password is not None:
            cmd.extend(['--password', keystore_password])
        try:
            subprocess.run(cmd, cwd=self.get_root(), check=True, stdout=sys.stdout, stderr=sys.stderr)
        except subprocess.CalledProcessError as cpe:
            raise self._sanitize(cpe)
        if not jar_path.is_file():
            raise FileNotFoundError(str(jar_path))
        return jar_path, orig_plugin

    # def _plugin_path(self, plugin_id: PluginIdentifier) -> Path:
    #     return self.get_main().joinpath(Plugin.id_to_file(plugin_id))

    def _sanitize(self, called_process_error: subprocess.CalledProcessError) -> subprocess.CalledProcessError:
        cmd = called_process_error.cmd[:]
        for i in range(1, len(cmd)):
            if cmd[i - 1] == '--password':
                cmd[i] = '<password>'
        called_process_error.cmd = ' '.join([shlex.quote(c) for c in cmd])
        return called_process_error


class MavenPluginSetBuilder(BasePluginSetBuilder):
    DEFAULT_MAIN: ClassVar[str] = 'src/main/java'
    DEFAULT_TEST: ClassVar[str] = 'src/test/java'

    type: Literal['maven'] = Field(**BasePluginSetBuilder.TYPE_FIELD)
    main: Optional[str] = Field(DEFAULT_MAIN, **BasePluginSetBuilder.MAIN_FIELD)
    test: Optional[str] = Field(DEFAULT_TEST, **BasePluginSetBuilder.TEST_FIELD)

    _built: bool

    def build_plugin(self, plugin_id: PluginIdentifier, keystore_path: Path, keystore_alias: str, keystore_password=None) -> tuple[Path, Plugin]:
        self._big_build(keystore_path, keystore_alias, keystore_password=keystore_password)
        return self._little_build(plugin_id)

    def model_post_init(self, context: Any) -> None:
        super().model_post_init(context)
        self._built = False

    def _big_build(self, keystore_path: Path, keystore_alias: str, keystore_password: str=None) -> None:
        if not self._built:
            # Do build
            cmd = ['mvn', 'package',
                   f'-Dkeystore.file={keystore_path!s}',
                   f'-Dkeystore.alias={keystore_alias}',
                   f'-Dkeystore.password={keystore_password}']
            try:
                subprocess.run(cmd, cwd=self.get_root(), check=True, stdout=sys.stdout, stderr=sys.stderr)
            except subprocess.CalledProcessError as cpe:
                raise self._sanitize(cpe)
            self._built = True

    def _little_build(self, plugin_id: PluginIdentifier) -> tuple[Path, Plugin]:
        jar_path = self.get_root().joinpath('target', 'pluginjars', f'{plugin_id}.jar')
        if not jar_path.is_file():
            raise FileNotFoundError(str(jar_path))
        return jar_path, Plugin.from_jar(jar_path)

    def _sanitize(self, called_process_error: subprocess.CalledProcessError) -> subprocess.CalledProcessError:
        cmd = called_process_error.cmd[:]
        for i in range(len(cmd)):
            if cmd[i].startswith('-Dkeystore.password='):
                cmd[i] = '-Dkeystore.password=<password>'
        called_process_error.cmd = ' '.join([shlex.quote(c) for c in cmd])
        return called_process_error


PluginSetBuilder = Annotated[Union[AntPluginSetBuilder, MavenPluginSetBuilder], Field(discriminator='type')]


PluginSetKind = Literal['PluginSet']


PluginSetIdentifier = str


class PluginSet(BaseModel):
    kind: PluginSetKind = Field(title='Kind', description="This object's kind")
    id: PluginSetIdentifier = Field(title='Plugin Set Identifier', description='An identifier for the plugin set')
    name: str = Field(title='Plugin Set Name', description='A name for the plugin set')
    builder: PluginSetBuilder = Field(title='Plugin Set Builder', description='A builder for the plugin set')

    def build_plugin(self, plugin_id: PluginIdentifier, keystore_path: Path, keystore_alias: str, keystore_password=None) -> tuple[Path, Plugin]:
        return self.builder.build_plugin(plugin_id, keystore_path, keystore_alias, keystore_password)

    def get_builder(self) -> PluginSetBuilder:
        return self.builder

    def get_id(self) -> PluginSetIdentifier:
        return self.id

    def get_name(self) -> str:
        return self.name

    def has_plugin(self, plugin_id: PluginIdentifier) -> bool:
        return self.get_builder().has_plugin(plugin_id)

    def initialize(self, root: Path) -> PluginSet:
        self.get_builder().initialize(root)
        return self

    def make_plugin(self, plugin_id: PluginIdentifier) -> Plugin:
        return self.get_builder().make_plugin(plugin_id)
