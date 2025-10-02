=======
Turtles
=======

.. |RELEASE| replace:: 0.6.0-dev20
.. |RELEASE_DATE| replace:: ?

.. |HELP| replace:: ``--help/-h``
.. |IDENTIFIER| replace:: ``--identifier/-i``
.. |IDENTIFIERS| replace:: ``--identifiers/-I``
.. |JAR| replace:: ``--jar/-j``
.. |JARS| replace:: ``--jars/-J``
.. |LAYER| replace:: ``--layer/-l``
.. |LAYERS| replace:: ``--layers/-L``
.. |PLUGIN_REGISTRY_CATALOG| replace:: ``--plugin-registry-catalog/-r``
.. |PLUGIN_SET_CATALOG| replace:: ``--plugin-set-catalog/-s``
.. |PLUGIN_SIGNING_CREDENTIALS| replace:: ``--plugin-signing-credentials/-c``
.. |PRODUCTION| replace:: ``--production/-p``
.. |TESTING| replace:: ``--testing/-t``

.. image:: https://assets.lockss.org/images/logos/turtles/turtles_128x128.png
   :alt: Turtles logo
   :align: right

Turtles is a command line tool and Python library to manage LOCKSS plugin sets and LOCKSS plugin registries.

**Latest release:** |RELEASE| (|RELEASE_DATE|)

-----------------
Table of Contents
-----------------

*  `Installation`_

   *  `Prerequisites`_

   *  `pip`_

*  `Overview`_

   *  `Building Plugins`_

   *  `Deploying Plugins`_

* `Configuration Files`_

   *  `Plugin Set Catalog`_

   *  `Plugin Sets`_

   *  `Plugin Set Builders`_

      * `Maven Plugin Set Builder`_

         * `Maven Plugin Set Builder Prerequisites`_

         * `Maven Plugin Set Builder Declaration`_

      * `Ant Plugin Set Builder`_

         * `Ant Plugin Set Builder Prerequisites`_

         * `Ant Plugin Set Builder Declaration`_

   * `Plugin Registry Catalog`_

   * `Plugin Registries`_

   * `Plugin Registry Layouts`_

      * `Directory Plugin Registry Layout`_

         * `Directory Plugin Registry Layout Prerequisites`_

         * `Directory Plugin Registry Layout Declaration`_

      * `RCS Plugin Registry Layout`_

         * `RCS Plugin Registry Layout Prerequisites`_

         * `RCS Plugin Registry Layout Declaration`_

   * `Plugin Registry Layers`_

   * `Plugin Signing Credentials`_

*  `Command Line Tool`_

   * `Synopsis`_

   * `Commands`_

      *  `Top-Level Program`_

      *  `build-plugin`_

      *  `copyright`_

      *  `deploy-plugin`_

      *  `license`_

      *  `release-plugin`_

      *  `usage`_

      *  `version`_

   *  `Options`_

      *  `Plugin Identifier Arguments and Options`_

      *  `Plugin Registry Layer Options`_

      *  `Output Format Control`_

------------
Installation
------------

Turtles is available from the `Python Package Index <https://pypi.org/>`_ (PyPI) as ``lockss-turtles`` (https://pypi.org/project/lockss-turtles), and can be installed with `pip`_.

The installation process adds a ``turtles`` `Command Line Tool`_. You can check at the command line that the installation is functional by running ``turtles version`` or ``turtles --help``.

Prerequisites
=============

*  `Python <https://www.python.org/>`_ 3.7 or greater.

*  Additional prerequisites depending on the types of `Plugin Set Builders`_ or `Plugin Registry Layouts`_ in use (see their respective requirements).

Prerequisites for development work only:

*  `Poetry <https://python-poetry.org/>`_ 1.4 or greater.

.. _pip:

``pip``
=======

You can install Turtles with ``pip``.

To install it in your own non-root, non-virtual environment, use the ``--user`` option::

   pip3 install --user lockss-turtles

To install it in a virtual environment, simply use::

   pip3 install lockss-turtles

.. danger::

   Do not run ``pip3``/``pip`` as ``root``, with ``sudo`` or otherwise.

--------
Overview
--------

Building Plugins
================

You can use Turtles to build (package and sign) LOCKSS plugins from one or more LOCKSS plugin sets (codebases containing plugins).

You will need to define one or more `Plugin Sets`_, list them in a `Plugin Set Catalog`_, and declare your `Plugin Signing Credentials`_.

You then use the `build-plugin`_ command to build plugins, or the `release-plugin`_ command to build and deploy plugins (equivalent of `build-plugin`_ followed by `deploy-plugin`_).

Deploying Plugins
=================

You can use Turtles to deploy LOCKSS plugins to LOCKSS plugin registries.

You will need to define one or more `Plugin Registries`_ and declare them in a `Plugin Registry Catalog`_.

You then use the `deploy-plugin`_ command to deploy plugin JARs, or the `release-plugin`_ command to build and deploy plugins from `Plugin Sets`_ (equivalent of `build-plugin`_ followed by `deploy-plugin`_).

-------------------
Configuration Files
-------------------

All Turtles configuration files are YAML files and have a top-level ``kind`` key that declares what kind of configuration file it is.

Some Turtles commands require a `Plugin Set Catalog`_, `Plugin Registry Catalog`_, or `Plugin Signing Credentials`_. You can specify the configuration file to use via the appropriate command line option (for example |PLUGIN_SET_CATALOG|). Otherwise, Turtles will look for then appropriate configuration file (for example ``plugin-set-catalog.yaml``) in several standard directories, in this order:

*  ``$XDG_CONFIG_HOME/lockss.turtles`` (by default ``$HOME/.config/lockss.turtles``)

*  ``/usr/local/share/lockss.turtles``

*  ``/etc/lockss.turtles``

Plugin Set Catalog
==================

Turtles commands that are `Building Plugins`_ (`build-plugin`_, `release-plugin`_) need a plugin set catalog. It can be specified via the |PLUGIN_SET_CATALOG| option, otherwise Turtles looks through `Configuration Files`_ for a file named ``plugin-set-catalog.yaml``.

A plugin set catalog is defined by a YAML document::

    ---
    kind: PluginSetCatalog
    plugin-set-files:
      - /path/to/some/file1.yaml
      - /path/to/another/file2.yaml
      - ...

The contents are described below:

``kind``
   *Required.* Must be set to ``PluginSetCatalog``.

``plugin-set-files``
   *Required.* A list of one or more paths to `Plugin Sets`_.

Plugin Sets
===========

A plugin set is a project containing the source code of one or more LOCKSS plugins.

A plugin set is defined by a YAML document::

    ---
    kind: PluginSet
    id: mypluginset
    name: My Plugin Set
    builder:
      type: ...
      ...

The contents are described below:

``kind``
   *Required.* Must be set to ``PluginSet``.

``id``
   *Required.* A short identifier for the plugin set, for example ``mypluginset``.

``name``
   *Required.* A display name for the plugin set, for example ``My Plugin Set``.

``builder``
   *Required.* An object defining the plugin set's builder together with its options.

   ``type``
      *Required.* A plugin set builder type. See `Plugin Set Builders`_ below.

   Other
      Additional properties depending on the plugin set builder type. See `Plugin Set Builders`_ below.

Plugin Set Builders
===================

Turtles `Plugin Sets`_ support two types of plugin set builders:

*  `Maven Plugin Set Builder`_

*  `Ant Plugin Set Builder`_

Maven Plugin Set Builder
------------------------

This type of plugin set builder is for a Maven project inheriting from ``org.lockss:lockss-plugins-parent-pom``.

Maven Plugin Set Builder Prerequisites
++++++++++++++++++++++++++++++++++++++

*  Java Development Kit 8 (JDK).

*  `Apache Maven <https://maven.apache.org/>`_.

Maven Plugin Set Builder Declaration
++++++++++++++++++++++++++++++++++++

For this plugin set builder type, the ``builder`` object in the plugin set definition has the following structure::

    ---
    kind: PluginSet
    id: ...
    name: ...
    builder:
      type: mvn
      main: ...
      test: ...

``type``
   *Required.* Must be set to ``mvn``.

``main``
   *Optional.* The path (relative to the root of the project) to the plugins' source code. *Default:* ``src/main/java``.

``test``
   *Optional.* The path (relative to the root of the project) to the plugins' unit tests. *Default:* ``src/test/java``.

Ant Plugin Set Builder
----------------------

This type of plugin set builder is for the LOCKSS 1.x (https://github.com/lockss/lockss-daemon) code tree, based on Ant.

Ant Plugin Set Builder Prerequisites
++++++++++++++++++++++++++++++++++++

*  Java Development Kit 8 (JDK).

*  `Apache Ant <https://ant.apache.org/>`_.

*  ``JAVA_HOME`` must be set appropriately.

Ant Plugin Set Builder Declaration
++++++++++++++++++++++++++++++++++

For this plugin set builder type, the ``builder`` object in the plugin set definition has the following structure::

    ---
    kind: PluginSet
    id: ...
    name: ...
    builder:
      type: ant
      main: ...
      test: ...

``type``
   *Required.* Must be set to ``ant``.

``main``
   *Optional.* The path (relative to the root of the project) to the plugins' source code. *Default:* ``plugins/src``.

``test``
   *Optional.* The path (relative to the root of the project) to the plugins' unit tests. *Default:* ``plugins/test/src``.

Plugin Registry Catalog
=======================

Turtles commands that are `Deploying Plugins`_ (`deploy-plugin`_, `release-plugin`_) need a plugin registry catalog. It can be specified via the |PLUGIN_REGISTRY_CATALOG| option, otherwise Turtles looks through `Configuration Files`_ for a file named ``plugin-registry-catalog.yaml``.

A plugin set catalog is defined by a YAML document::

    ---
    kind: PluginRegistryCatalog
    plugin-registry-files:
      - /path/to/some/file1.yaml
      - /path/to/another/file2.yaml
      - ...

The contents are described below:

``kind``
   *Required.* Must be set to ``PluginRegistryCatalog``.

``plugin-registry-files``
   *Required.* A list of one or more paths to `Plugin Registries`_.

Plugin Registries
=================

A plugin registry is a structure containing LOCKSS plugins packaged as signed JAR files.

Currently the only predefined structures are directory structures local to the file system, which are then typically served by a Web server.

A plugin registry is defined by a YAML document::

    ---
    kind: PluginRegistry
    id: mypluginregistry
    name: My Plugin Registry
    layout:
      type: ...
      ...
    layers:
      - ...
    plugin-identifiers:
      - edu.myuniversity.plugin.publisherx.PublisherXPlugin
      - edu.myuniversity.plugin.publishery.PublisherYPlugin
      - ...
    suppressed-plugin-identifiers:
      - edu.myuniversity.plugin.old.OldPlugin
      - ...

The contents are described below:

``kind``
   *Required.* Must be set to ``PluginRegistry``.

``id``
   *Required.* A short identifier for the plugin registry, for example ``mypluginregistry``.

``name``
   *Required.* A display name for the plugin registry, for example ``My Plugin Registry``.

``layout``
   *Required.* An object defining the plugin registry's layout together with its options.

   ``type``
      *Required.* A plugin registry layout type. See `Plugin Registry Layouts`_ below.

   Other
      Additional properties depending on the plugin registry layout type. See `Plugin Registry Layouts`_ below.

``layers``
   *Required.* A list of objects describing the layers of the plugin registry. See `Plugin Registry Layers`_ below.

``plugin-identifiers``
   *Required.* Non-empty list of the plugin identifiers in this plugin registry.

``suppressed-plugin-identifiers``
   *Optional.* Non-empty list of plugin identifiers that are excluded from this plugin registry.

   Turtles does not currently do anything with this information, but it can be used to record plugins that have been abandoned or retracted over the lifetime of the plugin registry.

Plugin Registry Layouts
=======================

Turtles supports two kinds of plugin registry layouts:

*  `Directory Plugin Registry Layout`_

*  `RCS Plugin Registry Layout`_

Directory Plugin Registry Layout
--------------------------------

In this type of plugin registry layout, each layer consists of a directory on the local file system where signed plugin JARs are stored, which is then typically served by a Web server. The directory for each layer is designated by the layer's ``path`` property.

Directory Plugin Registry Layout Prerequisites
++++++++++++++++++++++++++++++++++++++++++++++

None.

Directory Plugin Registry Layout Declaration
++++++++++++++++++++++++++++++++++++++++++++

For this plugin registry layout type, the ``layout`` object in the plugin registry definition has the following structure::

    ---
    kind: PluginRegistry
    id: ...
    name: ...
    layout:
      type: directory
      file-naming-convention: ...
    layers:
      - ...
    plugin-identifiers:
      - ...
    suppressed-plugin-identifiers:
      - ...

``type``
   *Required.* Must be set to ``directory``.

``file-naming-convention``
   *Optional.* A rule for what to name each deployed JAR file. If unspecified, the behavior is that of ``identifier``. Can be one of:

   *  ``identifier``: Use the plugin identifier and add ``.jar``. For example ``edu.myuniversity.plugin.publisherx.PublisherXPlugin`` results in ``edu.myuniversity.plugin.publisherx.PublisherXPlugin.jar``.

   *  ``underscore``: Replace ``.`` in the plugin identifier with ``_``, and add ``.jar``. For example ``edu.myuniversity.plugin.publisherx.PublisherXPlugin`` results in ``edu_myuniversity_plugin_publisherx_PublisherXPlugin.jar``.

   *  ``abbreviated``: Use the last dotted component of the plugin identifier and add ``.jar``. For example ``edu.myuniversity.plugin.publisherx.PublisherXPlugin`` results in ``PublisherXPlugin.jar``.

RCS Plugin Registry Layout
--------------------------

In this specialization of the `Directory Plugin Registry Layout`_, each successive version of a given JAR is kept locally in RCS.

RCS Plugin Registry Layout Prerequisites
++++++++++++++++++++++++++++++++++++++++

*  `GNU RCS <https://www.gnu.org/software/rcs/>`_.

RCS Plugin Registry Layout Declaration
++++++++++++++++++++++++++++++++++++++

For this plugin registry layout type, the ``layout`` object in the plugin registry definition has the following structure::

    ---
    kind: PluginRegistry
    id: ...
    name: ...
    layout:
      type: rcs
      file-naming-convention: ...
    layers:
      - ...
    plugin-identifiers:
      - ...
    suppressed-plugin-identifiers:
      - ...

``type``
   *Required.* Must be set to ``rcs``.

``file-naming-convention``
   *Optional.* A rule for what to name each deployed JAR file. If unspecified, the behavior is that of ``identifier``. Can be one of:

   *  ``identifier``: Use the plugin identifier and add ``.jar``. For example ``edu.myuniversity.plugin.publisherx.PublisherXPlugin`` results in ``edu.myuniversity.plugin.publisherx.PublisherXPlugin.jar``.

   *  ``underscore``: Replace ``.`` in the plugin identifier with ``_``, and add ``.jar``. For example ``edu.myuniversity.plugin.publisherx.PublisherXPlugin`` results in ``edu_myuniversity_plugin_publisherx_PublisherXPlugin.jar``.

   *  ``abbreviated``: Use the last dotted component of the plugin identifier and add ``.jar``. For example ``edu.myuniversity.plugin.publisherx.PublisherXPlugin`` results in ``PublisherXPlugin.jar``.

Plugin Registry Layers
======================

A plugin registry consists of one or more layers.

Some plugin registries only one layer, in which case the LOCKSS boxes in a network using the plugin registry will get what is released to it. Some plugin registries may have two or more layers, with the additional layers used for plugin development or content processing quality assurance.

Layers are sequential in nature; a new version of a plugin is released to the lowest layer first, then to the next layer (after some process), and so on until the highest layer. This sequencing is reflected in the ordering of the ``layers`` list in the plugin registry definition.

Although the identifiers (see ``id`` below) and display names (see ``name`` below) of plugin registry layers are arbitrary, the highest layer is commonly referred to as the *production* layer, and when there are exactly two layers, the lower layer is commonly referred to as the *testing* layer. Turtles reflects this common idiom with built-in |PRODUCTION| and |TESTING| options that are shorthand for ``--layer=production`` and ``--layer=testing`` respectively.

It is possible for multiple plugin registries to have a layer ``path`` in common. An example would be a team working on several plugin registries for different purposes, having distinct (public) production layer paths, but sharing a single (internal) testing layer path, if they are the only audience for it.

A plugin registry layer is defined as one of the objects in the plugin registry definition's ``layers`` list. Each layer object has the following structure::

    ---
    kind: PluginRegistry
    id: ...
    name: ...
    layout:
      type: ...
      ...
    layers:
      - id: testing
        name: My Plugin Registry (Testing)
        path: /path/to/testing
      - id: production
        name: My Plugin Registry (Production)
        path: /path/to/production
      - ...
    plugin-identifiers:
      - ...
    suppressed-plugin-identifiers:
      - ...

``id``
   *Required.* A short identifier for the plugin registry layer, for example ``testing``.

``name``
   *Required.* A display name for the plugin registry layer, for example ``My Plugin Registry (Testing)``.

``path``
   *Required.* The local path to the root of the plugin registry layer, for example ``/path/to/testing``.

Plugin Signing Credentials
==========================

Turtles commands that are `Building Plugins`_ (`build-plugin`_, `release-plugin`_) need a reference to plugin signing credentials. They can be specified via the |PLUGIN_SIGNING_CREDENTIALS| option, otherwise Turtles looks through `Configuration Files`_ for a file named ``plugin-signing-credentials.yaml``.

Plugin signing credentials are defined by a YAML document::

    ---
    kind: PluginSigningCredentials
    plugin-signing-keystore: /path/to/myalias.keystore
    plugin-signing-alias: myalias

The contents are described below:

``kind``
   *Required.* Must be set to ``PluginSigningCredentials``.

``plugin-signing-keystore``
   *Required.* Path to the plugin signing key (keystore).

``plugin-signing-alias``
   *Required.* The alias to use, which must be that of the plugin signing key (keystore) and also found in the LOCKSS network's shared keystore.

-----------------
Command Line Tool
-----------------

Turtles is invoked at the command line as::

   turtles

or as a Python module::

   python3 -m lockss.turtles

Help messages and this document use ``turtles`` throughout, but the two invocation styles are interchangeable.

Synopsis
========

Turtles uses `Commands`_, in the style of programs like ``git``, ``dnf``/``yum``, ``apt``/``apt-get``, and the like. You can see the list of available `Commands`_ by invoking ``turtles --help``, and you can find a usage summary of all the `Commands`_ by invoking ``turtles usage``::

    usage: turtles [-h] [--debug-cli] [--non-interactive] COMMAND ...

           turtles build-plugin [-h] [--output-format FMT] [--password PASS]
                                [--plugin-set-catalog FILE]
                                [--plugin-signing-credentials FILE]
                                [--identifier PLUGID] [--identifiers FILE]
                                [PLUGID ...]

           turtles copyright [-h]

           turtles deploy-plugin [-h] [--output-format FMT]
                                 [--plugin-registry-catalog FILE] [--production]
                                 [--testing] [--jar PLUGJAR] [--jars FILE]
                                 [--layer LAYER] [--layers FILE]
                                 [PLUGJAR ...]

           turtles license [-h]

           turtles release-plugin [-h] [--output-format FMT] [--password PASS]
                                  [--plugin-registry-catalog FILE]
                                  [--plugin-set-catalog FILE]
                                  [--plugin-signing-credentials FILE]
                                  [--production] [--testing] [--identifier PLUGID]
                                  [--identifiers FILE] [--layer LAYER]
                                  [--layers FILE]
                                  [PLUGID ...]

           turtles usage [-h]

           turtles version [-h]

Commands
========

The available commands are:

================= ============ =======
Command           Abbreviation Purpose
================= ============ =======
`build-plugin`_   bp           build (package and sign) plugins
`copyright`_                   show copyright and exit
`deploy-plugin`_  dp           deploy plugins
`license`_                     show license and exit
`release-plugin`_ rp           release (build and deploy) plugins
`usage`_                       show detailed usage and exit
`version`_                     show version and exit
================= ============ =======

Top-Level Program
-----------------

The top-level executable alone does not perform any action or default to a given command. It does define a few options, which you can see by invoking Turtles with the |HELP| option::

    usage: turtles [-h] [--debug-cli] [--non-interactive] COMMAND ...

    options:
      -h, --help            show this help message and exit
      --debug-cli           print the result of parsing command line arguments
      --non-interactive, -n
                            disallow interactive prompts (default: allow)

    commands:
      Add --help to see the command's own help message.

      COMMAND               DESCRIPTION
        build-plugin (bp)   build (package and sign) plugins
        copyright           show copyright and exit
        deploy-plugin (dp)  deploy plugins
        license             show license and exit
        release-plugin (rp)
                            release (build and deploy) plugins
        usage               show detailed usage and exit
        version             show version and exit

.. _build-plugin:

``build-plugin`` (``bp``)
-------------------------

The ``build-plugin`` command is used for `Building Plugins`_. It has its own |HELP| option::

    usage: turtles build-plugin [-h] [--output-format FMT] [--password PASS]
                                [--plugin-set-catalog FILE]
                                [--plugin-signing-credentials FILE]
                                [--identifier PLUGID] [--identifiers FILE]
                                [PLUGID ...]

    Build (package and sign) plugins.

    options:
      -h, --help            show this help message and exit
      --output-format FMT   set tabular output format to FMT (default: simple;
                            choices: asciidoc, double_grid, double_outline,
                            fancy_grid, fancy_outline, github, grid, heavy_grid,
                            heavy_outline, html, jira, latex, latex_booktabs,
                            latex_longtable, latex_raw, mediawiki, mixed_grid,
                            mixed_outline, moinmoin, orgtbl, outline, pipe, plain,
                            presto, pretty, psql, rounded_grid, rounded_outline,
                            rst, simple, simple_grid, simple_outline, textile,
                            tsv, unsafehtml, youtrack)
      --password PASS       set the plugin signing password
      --plugin-set-catalog FILE, -s FILE
                            load plugin set catalog from FILE (default:
                            $HOME/.config/lockss.turtles/plugin-set-
                            catalog.yaml or
                            /usr/local/share/lockss.turtles/plugin-set-
                            catalog.yaml or /etc/lockss.turtles/plugin-set-
                            catalog.yaml)
      --plugin-signing-credentials FILE, -c FILE
                            load plugin signing credentials from FILE (default:
                            $HOME/.config/lockss.turtles/plugin-signing-
                            credentials.yaml or
                            /usr/local/share/lockss.turtles/plugin-signing-
                            credentials.yaml or /etc/lockss.turtles/plugin-
                            signing-credentials.yaml)

    plugin identifier arguments and options:
      --identifier PLUGID, -i PLUGID
                            add PLUGID to the list of plugin identifiers to build
      --identifiers FILE, -I FILE
                            add the plugin identifiers in FILE to the list of
                            plugin identifiers to build
      PLUGID                plugin identifier to build

The command needs:

*  `Plugin Signing Credentials`_, either from the |PLUGIN_SIGNING_CREDENTIALS| option or from ``plugin-signing-credentials.yaml`` in the `Configuration Files`_.

*  A `Plugin Set Catalog`_, either from the |PLUGIN_SET_CATALOG| option or from ``plugin-set-catalog.yaml`` in the `Configuration Files`_.

*  One or more plugin identifiers, from the `Plugin Identifier Arguments and Options`_ (bare arguments, |IDENTIFIER| options, |IDENTIFIERS| options).

It also accepts `Options`_ for `Output Format Control`_

Examples::

    # Help message
    turtles build-plugin --help
    # Abbreviation
    turtles bp -h

    # List of plugin identifiers
    turtles build-plugin edu.myuniversity.plugin.publisherx.PublisherXPlugin edu.myuniversity.plugin.publishery.PublisherYPlugin ...
    # Abbreviation
    turtles bp edu.myuniversity.plugin.publisherx.PublisherXPlugin edu.myuniversity.plugin.publishery.PublisherYPlugin ...

    # Alternative invocation
    turtles build-plugin --identifier=edu.myuniversity.plugin.publisherx.PublisherXPlugin --identifier=edu.myuniversity.plugin.publishery.PublisherYPlugin ...
    # Abbreviation
    turtles bp -i edu.myuniversity.plugin.publisherx.PublisherXPlugin -i edu.myuniversity.plugin.publishery.PublisherYPlugin ...

    # Alternative invocation
    # /tmp/pluginids.txt has one plugin identifier per line
    turtles build-plugin --identifiers=/tmp/pluginids.txt
    # Abbreviation
    turtles bp -I /tmp/pluginids.txt

.. _copyright:

``copyright``
-------------

The ``copyright`` command displays the copyright notice for Turtles and exits.

.. _deploy-plugin:

``deploy-plugin`` (``dp``)
--------------------------

The ``deploy-plugin`` command is used for `Deploying Plugins`_. It has its own |HELP| option::

    usage: turtles deploy-plugin [-h] [--output-format FMT]
                                 [--plugin-registry-catalog FILE] [--production]
                                 [--testing] [--jar PLUGJAR] [--jars FILE]
                                 [--layer LAYER] [--layers FILE]
                                 [PLUGJAR ...]

    Deploy plugins.

    options:
      -h, --help            show this help message and exit
      --output-format FMT   set tabular output format to FMT (default: simple;
                            choices: asciidoc, double_grid, double_outline,
                            fancy_grid, fancy_outline, github, grid, heavy_grid,
                            heavy_outline, html, jira, latex, latex_booktabs,
                            latex_longtable, latex_raw, mediawiki, mixed_grid,
                            mixed_outline, moinmoin, orgtbl, outline, pipe, plain,
                            presto, pretty, psql, rounded_grid, rounded_outline,
                            rst, simple, simple_grid, simple_outline, textile,
                            tsv, unsafehtml, youtrack)
      --plugin-registry-catalog FILE, -r FILE
                            load plugin registry catalog from FILE (default:
                            $HOME/.config/lockss.turtles/plugin-registry-
                            catalog.yaml or
                            /usr/local/share/lockss.turtles/plugin-registry-
                            catalog.yaml or /etc/lockss.turtles/plugin-registry-
                            catalog.yaml)
      --production, -p      synonym for --layer=production (i.e. add 'production'
                            to the list of plugin registry layers to process)
      --testing, -t         synonym for --layer=testing (i.e. add 'testing' to the
                            list of plugin registry layers to process)

    plugin JAR arguments and options:
      --jar PLUGJAR, -j PLUGJAR
                            add PLUGJAR to the list of plugin JARs to deploy
      --jars FILE, -J FILE  add the plugin JARs in FILE to the list of plugin JARs
                            to deploy
      PLUGJAR               plugin JAR to deploy

    plugin registry layer options:
      --layer LAYER, -l LAYER
                            add LAYER to the list of plugin registry layers to
                            process
      --layers FILE, -L FILE
                            add the layers in FILE to the list of plugin registry
                            layers to process

The command needs:

*  A `Plugin Registry Catalog`_, either from the |PLUGIN_REGISTRY_CATALOG| option or from ``plugin-signing-credentials.yaml`` in the `Configuration Files`_.

*  One or more plugin registry layer IDs, from the `Plugin Registry Layer Options`_ (|LAYER| options, |LAYERS| options, and alternatively, |TESTING| options, |PRODUCTION| option).

*  One or more JAR paths. The list of JAR paths to process is derived from:

   *  The JAR paths listed as bare arguments to the command.

   *  The JAR paths listed as |JAR| options.

   *  The JAR paths found in the files listed as |JARS| options.

It also accepts `Options`_ for `Output Format Control`_.

Examples::

    # Help message
    turtles deploy-plugin --help
    # Abbreviation
    turtles dp -h

    # List of JARs
    # Deploy to 'testing' layer only
    turtles deploy-plugin --testing /path/to/edu.myuniversity.plugin.publisherx.PublisherXPlugin.jar /path/to/edu.myuniversity.plugin.publishery.PublisherYPlugin.jar ...
    # Abbreviation
    turtles dp -t /path/to/edu.myuniversity.plugin.publisherx.PublisherXPlugin.jar /path/to/edu.myuniversity.plugin.publishery.PublisherYPlugin.jar ...

    # Alternative invocation
    # Deploy to 'production' layer only
    turtles deploy-plugin --production --jar=/path/to/edu.myuniversity.plugin.publisherx.PublisherXPlugin.jar --jar=/path/to/edu.myuniversity.plugin.publishery.PublisherYPlugin.jar ...
    # Abbreviation
    turtles dp -p -j /path/to/edu.myuniversity.plugin.publisherx.PublisherXPlugin.jar -j /path/to/edu.myuniversity.plugin.publishery.PublisherYPlugin.jar ...

    # Alternative invocation
    # /tmp/pluginjars.txt has one JAR path per line
    # Deploy to both 'testing' and 'production' layers
    turtles deploy-plugin --testing --production --jars=/tmp/pluginjars.txt
    # Abbreviation
    turtles bp -tp -J /tmp/pluginids.txt

.. _license:

``license``
-----------

The ``license`` command displays the license terms for Turtles and exits.

.. _release-plugin:

``release-plugin`` (``rp``)
---------------------------

The ``release-plugin`` command is used for `Building Plugins`_ and `Deploying Plugins`_, being essentially `build-plugin`_ followed by `deploy-plugin`_. It has its own |HELP| option::

    usage: turtles release-plugin [-h] [--output-format FMT] [--password PASS]
                                  [--plugin-registry-catalog FILE]
                                  [--plugin-set-catalog FILE]
                                  [--plugin-signing-credentials FILE]
                                  [--production] [--testing] [--identifier PLUGID]
                                  [--identifiers FILE] [--layer LAYER]
                                  [--layers FILE]
                                  [PLUGID ...]

    Release (build and deploy) plugins.

    options:
      -h, --help            show this help message and exit
      --output-format FMT   set tabular output format to FMT (default: simple;
                            choices: asciidoc, double_grid, double_outline,
                            fancy_grid, fancy_outline, github, grid, heavy_grid,
                            heavy_outline, html, jira, latex, latex_booktabs,
                            latex_longtable, latex_raw, mediawiki, mixed_grid,
                            mixed_outline, moinmoin, orgtbl, outline, pipe, plain,
                            presto, pretty, psql, rounded_grid, rounded_outline,
                            rst, simple, simple_grid, simple_outline, textile,
                            tsv, unsafehtml, youtrack)
      --password PASS       set the plugin signing password
      --plugin-registry-catalog FILE, -r FILE
                            load plugin registry catalog from FILE (default:
                            $HOME/.config/lockss.turtles/plugin-registry-
                            catalog.yaml or
                            /usr/local/share/lockss.turtles/plugin-registry-
                            catalog.yaml or /etc/lockss.turtles/plugin-registry-
                            catalog.yaml)
      --plugin-set-catalog FILE, -s FILE
                            load plugin set catalog from FILE (default:
                            $HOME/.config/lockss.turtles/plugin-set-
                            catalog.yaml or
                            /usr/local/share/lockss.turtles/plugin-set-
                            catalog.yaml or /etc/lockss.turtles/plugin-set-
                            catalog.yaml)
      --plugin-signing-credentials FILE, -c FILE
                            load plugin signing credentials from FILE (default:
                            $HOME/.config/lockss.turtles/plugin-signing-
                            credentials.yaml or
                            /usr/local/share/lockss.turtles/plugin-signing-
                            credentials.yaml or /etc/lockss.turtles/plugin-
                            signing-credentials.yaml)
      --production, -p      synonym for --layer=production (i.e. add 'production'
                            to the list of plugin registry layers to process)
      --testing, -t         synonym for --layer=testing (i.e. add 'testing' to the
                            list of plugin registry layers to process)

    plugin identifier arguments and options:
      --identifier PLUGID, -i PLUGID
                            add PLUGID to the list of plugin identifiers to build
      --identifiers FILE, -I FILE
                            add the plugin identifiers in FILE to the list of
                            plugin identifiers to build
      PLUGID                plugin identifier to build

    plugin registry layer options:
      --layer LAYER, -l LAYER
                            add LAYER to the list of plugin registry layers to
                            process
      --layers FILE, -L FILE
                            add the layers in FILE to the list of plugin registry
                            layers to process

The command needs:

*  `Plugin Signing Credentials`_, either from the |PLUGIN_SIGNING_CREDENTIALS| option or from ``plugin-signing-credentials.yaml`` in the `Configuration Files`_.

*  A `Plugin Set Catalog`_, either from the |PLUGIN_SET_CATALOG| option or from ``plugin-set-catalog.yaml`` in the `Configuration Files`_.

*  A `Plugin Registry Catalog`_, either from the |PLUGIN_REGISTRY_CATALOG| option or from ``plugin-signing-credentials.yaml`` in the `Configuration Files`_.

*  One or more plugin registry layer IDs, from the `Plugin Registry Layer Options`_ (|IDENTIFIER| options, |IDENTIFIERS| options, and alternatively, |TESTING| options, |PRODUCTION| option).

*  One or more plugin identifiers, from the `Plugin Identifier Arguments and Options`_ (bare arguments, |IDENTIFIER| options, |IDENTIFIERS| options).

It also accepts `Options`_ for `Output Format Control`_.

Examples::

    # Help message
    turtles release-plugin --help
    # Abbreviation
    turtles rp -h

    # List of plugin identifiers
    # Deploy to 'testing' layer only
    turtles release-plugin --testing edu.myuniversity.plugin.publisherx.PublisherXPlugin edu.myuniversity.plugin.publishery.PublisherYPlugin ...
    # Abbreviation
    turtles rp -t edu.myuniversity.plugin.publisherx.PublisherXPlugin edu.myuniversity.plugin.publishery.PublisherYPlugin ...

    # Alternative invocation
    # Deploy to 'production' layer only
    turtles release-plugin --production --identifier=edu.myuniversity.plugin.publisherx.PublisherXPlugin --identifier=edu.myuniversity.plugin.publishery.PublisherYPlugin ...
    # Abbreviation
    turtles rp -p -i edu.myuniversity.plugin.publisherx.PublisherXPlugin -i edu.myuniversity.plugin.publishery.PublisherYPlugin ...

    # Alternative invocation
    # /tmp/pluginids.txt has one plugin identifier per line
    # Deploy to both 'testing' and 'production' layers
    turtles release-plugin --testing --production --identifiers=/tmp/pluginids.txt
    # Abbreviation
    turtles rp -tp -I /tmp/pluginids.txt

.. _usage:

``usage``
---------

The ``usage`` command displays the usage message of all the Turtles `Commands`_.

.. _version:

``version``
-----------

The ``version`` command displays the version number of Turtles and exits.

Options
=======

Plugin Identifier Arguments and Options
---------------------------------------

Commands that are `Building Plugins`_ expect one or more plugin identifiers. The list of plugin identifiers to process is derived from:

*  The plugin identifiers listed as bare arguments to the command.

*  The plugin identifiers listed as |IDENTIFIER| options.

*  The plugin identifiers found in the files listed as |IDENTIFIERS| options.

Plugin Registry Layer Options
-----------------------------

Commands that are `Deploying Plugins`_ expect one or more plugin registry layer IDs. The list of plugin registry layer IDs to target is derived from:

*  The plugin registry layer IDs listed as |LAYER| options.

*  The plugin registry layer IDs found in the files listed as |LAYERS| options.

As a convenience, the following synonyms also exist:

*  |TESTING| is a synonym for ``--layer=testing``

*  |PRODUCTION| is a synonym for ``--layer=production``

Output Format Control
---------------------

Turtles' tabular output is performed by the `tabulate <https://pypi.org/project/tabulate>`_ library through the ``--output-format`` option. See its PyPI page for a visual reference of the various output formats available. The **default** is ``simple``.
