from typing import Callable, Concatenate


def method_paramspec_from_function[O, T, U, **P](
    _: Callable[P, T],
) -> Callable[[Callable[Concatenate[O, P], U]], Callable[Concatenate[O, P], U]]:
    """Makes the decorated method ParamSpec without self match the given function."""

    def decorator(
        func: Callable[Concatenate[O, P], U],
    ) -> Callable[Concatenate[O, P], U]:
        return func

    return decorator
