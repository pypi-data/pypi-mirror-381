.. raw:: html

    <p align="center">
        <img
            src="https://raw.githubusercontent.com/janLuke/cloup/master/docs/_static/logo-on-white.svg"
            width="50%" />
    </p>

    <p align="center">
        <i>
            <a href="https://github.com/pallets/click">Click</a>
            + option groups + constraints + aliases + help themes + ...
        </i>
    </p>

    <p align="center">
        <a href="https://cloup.readthedocs.io/">https://cloup.readthedocs.io/</a>
    </a>

----------

.. docs-index-start

.. |pypi-release| image:: https://img.shields.io/pypi/v/asynccloup.svg
    :alt: Latest release on PyPI
    :target: https://pypi.org/project/asynccloup/

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/asynccloup.svg
    :alt: Supported versions
    :target: https://pypi.org/project/asynccloup

========
Overview
========
|pypi-release|

**AsyncCloup** is a **Cloup** fork that works with `AsyncClick
<https://github.com/python-trio/asyncclick>` instead of
Click. This should be a drop-in change.

**Cloup** — originally from "**Cl**\ick + option gr\ **oup**\s" — enriches
`Click <https://github.com/pallets/click>`_ with several features that make it
more expressive and configurable:

- **option groups** and an (optional) help section for positional arguments

- **constraints**, like ``mutually_exclusive``, that can be applied to option groups
  or to any group of parameters, even *conditionally*

- **subcommand aliases**

- **subcommands sections**, i.e. the possibility of organizing the subcommands of a
  ``Group`` in multiple help sections

- a **themeable HelpFormatter**  that:

  - has more parameters for adjusting widths and spacing, which can be provided
    at the context and command level
  - use a different layout when the terminal width is below a certain threshold
    in order to improve readability

- suggestions like "did you mean <subcommand>?" when you mistype a subcommand.

Moreover, Cloup improves on **IDE support** providing decorators with *detailed*
type hints and adding the static methods ``Context.settings()`` and
``HelpFormatter.settings()`` for creating dictionaries of settings.

Cloup is **statically type-checked** with MyPy in strict mode and extensively **tested**
against multiple versions of Python with nearly 100% coverage.


A simple example
================

.. code-block:: python

    from cloup import (
        HelpFormatter, HelpTheme, Style,
        command, option, option_group
    )
    from cloup.constraints import RequireAtLeast, mutually_exclusive

    # Check the docs for all available arguments of HelpFormatter and HelpTheme.
    formatter_settings = HelpFormatter.settings(
        theme=HelpTheme(
            invoked_command=Style(fg='bright_yellow'),
            heading=Style(fg='bright_white', bold=True),
            constraint=Style(fg='magenta'),
            col1=Style(fg='bright_yellow'),
        )
    )

    # In a multi-command app, you can pass formatter_settings as part
    # of your context_settings so that they are propagated to subcommands.
    @command(formatter_settings=formatter_settings)
    @option_group(
        "Cool options",
        option('--foo', help='This text should describe the option --foo.'),
        option('--bar', help='This text should describe the option --bar.'),
        constraint=mutually_exclusive,
    )
    @option_group(
        "Other cool options",
        "This is the optional description of this option group.",
        option('--pippo', help='This text should describe the option --pippo.'),
        option('--pluto', help='This text should describe the option --pluto.'),
        constraint=RequireAtLeast(1),
    )
    async def cmd(**kwargs):
        """This is the command description."""
        await anyio.sleep(1)

    if __name__ == '__main__':
        cmd(prog_name='invoked-command')


.. image:: https://raw.githubusercontent.com/janLuke/cloup/master/docs/_static/basic-example.png
    :alt: Basic example --help screenshot

If you don't provide ``--pippo`` or ``--pluto``:

.. code-block:: text

    Usage: invoked-command [OPTIONS]
    Try 'invoked-command --help' for help.

    Error: at least 1 of the following parameters must be set:
      --pippo
      --pluto

This simple example just scratches the surface. Read more in the documentation
(links below).

.. docs-index-end


Links
=====

* `GitHub repository <https://github.com/M-o-a-T/asynccloup>`_
* `Async-specific issues <https://github.com/M-o-a-T/asynccloup/issues>`_
* `Cloup <https://github.com/janLuke/cloup>`_
* `AsyncClick <https://github.com/M-o-a-T/asyncclick>`_

99% of Cloup's documentation applies to AsyncCloup.
Thus replicating it doesn't seem to be necessary.
Thus, please refer to their examples; feel fre to liberally
sprinkle ``async`` and ``await`` onto your code, and don't
hesitate to file an issue if something doesn't work.
