import inspect
from typing import (
    get_type_hints,
    Optional,
    Union,
    List,
    Tuple,
    get_origin,
    get_args,
    Type,
)
import graphene

from general_manager.api.graphql import GraphQL
from general_manager.manager.generalManager import GeneralManager

from general_manager.utils.formatString import snake_to_camel
from typing import TypeAliasType
from general_manager.permission.mutationPermission import MutationPermission


def graphQlMutation(_func=None, permission: Optional[Type[MutationPermission]] = None):
    """
    Decorator that converts a function into a GraphQL mutation class for use with Graphene, automatically generating argument and output fields from the function's signature and type annotations.

    The decorated function must provide type hints for all parameters (except `info`) and a return annotation. The decorator dynamically constructs a mutation class with appropriate Graphene fields, enforces permission checks if a `permission` class is provided, and registers the mutation for use in the GraphQL API.

    Parameters:
        permission (Optional[Type[MutationPermission]]): An optional permission class to enforce access control on the mutation.

    Returns:
        Callable: A decorator that registers the mutation and returns the original function.
    """
    if (
        _func is not None
        and inspect.isclass(_func)
        and issubclass(_func, MutationPermission)
    ):
        permission = _func
        _func = None

    def decorator(fn):
        """
        Decorator that transforms a function into a GraphQL mutation class compatible with Graphene.

        Analyzes the decorated function's signature and type hints to dynamically generate a mutation class with appropriate argument and output fields. Handles permission checks if a permission class is provided, manages mutation execution, and registers the mutation for use in the GraphQL API. On success, returns output fields and a `success` flag; on error, returns only `success=False`.
        """
        sig = inspect.signature(fn)
        hints = get_type_hints(fn)

        # Mutation name in PascalCase
        mutation_name = snake_to_camel(fn.__name__)

        # Build Arguments inner class dynamically
        arg_fields = {}
        for name, param in sig.parameters.items():
            if name == "info":
                continue
            ann = hints.get(name)
            if ann is None:
                raise TypeError(
                    f"Missing type hint for parameter {name} in {fn.__name__}"
                )
            required = True
            default = param.default
            has_default = default is not inspect._empty

            # Prepare kwargs
            kwargs = {}
            if required:
                kwargs["required"] = True
            if has_default:
                kwargs["default_value"] = default

            # Handle Optional[...] → not required
            origin = get_origin(ann)
            if origin is Union and type(None) in get_args(ann):
                required = False
                # extract inner type
                ann = [a for a in get_args(ann) if a is not type(None)][0]
                kwargs["required"] = False

            # Resolve list types to List scalar
            if get_origin(ann) is list or get_origin(ann) is List:
                inner = get_args(ann)[0]
                field = graphene.List(
                    GraphQL._mapFieldToGrapheneBaseType(inner),
                    **kwargs,
                )
            else:
                if inspect.isclass(ann) and issubclass(ann, GeneralManager):
                    field = graphene.ID(**kwargs)
                else:
                    field = GraphQL._mapFieldToGrapheneBaseType(ann)(**kwargs)

            arg_fields[name] = field

        Arguments = type("Arguments", (), arg_fields)

        # Build output fields: success + fn return types
        outputs = {
            "success": graphene.Boolean(required=True),
        }
        return_ann: type | tuple[type] | None = hints.get("return")
        if return_ann is None:
            raise TypeError(f"Mutation {fn.__name__} missing return annotation")

        # Unpack tuple return or single
        out_types = (
            list(get_args(return_ann))
            if get_origin(return_ann) in (tuple, Tuple)
            else [return_ann]
        )
        for out in out_types:
            is_named_type = isinstance(out, TypeAliasType)
            is_type = isinstance(out, type)
            if not is_type and not is_named_type:
                raise TypeError(
                    f"Mutation {fn.__name__} return type {out} is not a type"
                )
            name = out.__name__
            field_name = name[0].lower() + name[1:]

            basis_type = out.__value__ if is_named_type else out

            outputs[field_name] = GraphQL._mapFieldToGrapheneRead(
                basis_type, field_name
            )

        # Define mutate method
        def _mutate(root, info, **kwargs):
            """
            Handles the execution of a GraphQL mutation, including permission checks, result unpacking, and error handling.

            Returns:
                An instance of the mutation class with output fields populated from the mutation result and a success status.
            """
            if permission:
                permission.check(kwargs, info.context.user)
            try:
                result = fn(info, **kwargs)
                data = {}
                if isinstance(result, tuple):
                    # unpack according to outputs ordering after success
                    for (field, _), val in zip(
                        outputs.items(),
                        [None, *list(result)],  # None for success field to be set later
                    ):
                        # skip success
                        if field == "success":
                            continue
                        data[field] = val
                else:
                    only = next(k for k in outputs if k != "success")
                    data[only] = result
                data["success"] = True
                return mutation_class(**data)
            except Exception as e:
                GraphQL._handleGraphQLError(e)
                return mutation_class(**{"success": False})

        # Assemble class dict
        class_dict = {
            "Arguments": Arguments,
            "__doc__": fn.__doc__,
            "mutate": staticmethod(_mutate),
        }
        class_dict.update(outputs)

        # Create Mutation class
        mutation_class = type(mutation_name, (graphene.Mutation,), class_dict)

        if mutation_class.__name__ not in GraphQL._mutations:
            GraphQL._mutations[mutation_class.__name__] = mutation_class

        return fn

    if _func is not None and inspect.isfunction(_func):
        return decorator(_func)
    return decorator
