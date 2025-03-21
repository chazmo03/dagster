from collections.abc import Sequence

from dagster_components import (
    AssetSpecSchema,
    Component,
    ComponentSchema,
    registered_component_type,
)


class ShellCommandParams(ComponentSchema):
    path: str
    asset_specs: Sequence[AssetSpecSchema]


@registered_component_type(name="shell_command")
class ShellCommand(Component): ...
