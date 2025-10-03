from typing import Callable
from keyweave.interception import HotkeyInterceptionEvent

from abc import ABC
from functools import partial

from keyweave.bindings import Binding
from keyweave.commanding import CommandMeta
from keyweave.layout._layout import Layout
from keyweave.scheduling import Scheduler
from keyweave._util.logging import keyweaveLogger
from keyweave.util.reflect import get_attrs_down_to


layoutClassLogger = keyweaveLogger.getChild("LayoutClass")


class LayoutClass(ABC):
    """
    Use this to create a hotkey layout using a class. Using this mode, you declare commands and bind hotkeys.

    Commands are declared using the `command` decorator, while hotkeys are bound by using Hotkey objects as decorators.

    >>> from pykeys.layout import LayoutClass
    >>> from pykeys import key
    >>> from pykeys.commanding import command
    >>> class MyLayout(LayoutClass):
    ...     @(key.a & key.ctrl + key.shift)
    ...     @command(label="my_command")
    ...     def my_command(self, e: HotkeyEvent):
    ...         pass

    When you create an instance of `MyLayout`, you will get a `Layout` object rather than the class you defined.

    >>> layout = MyLayout()
    >>> isinstance(layout, Layout)
    True

    However, an instance of your class is still created and will be passed to the `self` parameter of command methods.

    Note that you must apply both `command` and hotkey decorators. Using just one of them is an error.

    However, you can still have helper methods that are not hotkey commands. Just don't use either decorator. These methods
    can only be accessed internally within the LayoutClass, such as by hotkey commands.

    >>> class MyLayout(LayoutClass):
    ...     def my_helper_method(self):
    ...         pass
    ...     @(key.a & key.ctrl + key.shift)
    ...     @command(label="my_command")
    ...     def my_command(self, e: HotkeyEvent):
    ...         self.my_helper_method()

    You can define an `__intercept__` method in your layout class. This lets you capture hotkey events and modify their behavior. This can be used for logging and similar:

    >>> class MyLayout(LayoutClass):
    ...     def __intercept__(self, intercepted: HotkeyInterceptionEvent):
    ...         print(intercepted)

    """

    def __post_init__(self):
        pass

    def __intercept__(self, intercepted: HotkeyInterceptionEvent):
        pass

    def __new__(
        cls,
        name: str | None = None,
        scheduler: Scheduler | None = None,
        on_error: Callable[[BaseException], None] | None = None,
    ):

        obj = super().__new__(cls)
        obj.__post_init__()
        my_logger = layoutClassLogger.getChild(cls.__name__)
        my_logger.info(f"Creating instance")
        layout = Layout(
            name=name or cls.__name__, scheduler=scheduler, on_error=on_error
        )
        attrs = get_attrs_down_to(obj, LayoutClass)

        for k, value in attrs.items():
            if k == "__intercept__":
                my_logger.info(f"Registering __intercept__ method")
                layout = layout.intercept(partial(getattr(obj, k), obj))
            match value:
                case Binding() as b:
                    layout.add_binding(b)
                case CommandMeta() as c:
                    my_logger.warning(
                        f"Command {c} is missing a hotkey binding decorator. It will be ignored."
                    )
                case _:
                    pass
        return layout
