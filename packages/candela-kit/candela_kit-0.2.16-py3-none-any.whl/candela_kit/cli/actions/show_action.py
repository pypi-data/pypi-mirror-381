import click


list_types = ["app", "directive", "session", "tool_module", "profile"]
config_args = click.Choice(list_types, case_sensitive=False)


def _print_repr(obj, title):
    from candela_kit.common.common import print_subtitle, indent_str

    print_subtitle(title)
    print(indent_str(repr(obj), 4))


def _make_title(entity, identifier, scope, version):
    if entity in ("app", "circuit", "directive", "model", "tool_module"):
        version_str = ":" + version if version else " (latest version)"
        title = f"{entity} {scope}/{identifier}{version_str}"
    elif entity == "session":
        title = f"session {scope}/{identifier}"
    elif entity == "profile":
        title = f"profile {identifier}"
    else:
        raise ValueError(f"Unknown entity {entity}")

    return title[0].upper() + title[1:]


@click.command(no_args_is_help=True)
@click.argument("entity_type", metavar="ENTITY_TYPE", type=config_args)
@click.argument("identifier", metavar="IDENTIFIER")
@click.option(
    "--scope",
    help='Specify which scope the object is in, otherwise will use "default".',
    default="default",
)
@click.option(
    "--version",
    help="Specify which version to delete, otherwise will show the latest.",
    default=None,
)
def show_main(entity_type: str, identifier: str, scope: str, version: str | None):
    """Show information for a given entity type in Candela.

    ENTITY_TYPE is the type of entity you want to show information about. Valid types are app, circuit, directive,
    model, session, tool_module, trace, profile.

    IDENTIFIER is the identifier or name of the specific entity you want to show.

    """

    from candela_kit import get_profiles
    from candela_kit import client
    from candela_kit.common.common import print_model

    c = client()

    def app_to_dict(*args):
        app = c.get_app(*args)
        return {
            "type": app.type,
            "circuit_id": app.circuit_id.model_dump(),
            "directive_id": app.directive_id.model_dump(),
        }

    handlers = {
        "app": (app_to_dict, print_model),
        "directive": (c.get_directive, _print_repr),
        "session": (lambda x, y, z: c.get_session(x, y), print_model),
        "tool_module": (c.get_tool_module, _print_repr),
        "profile": (lambda x, y, z: get_profiles().get(x), print_model),
    }

    get_obj, print_fn = handlers[entity_type]

    obj = get_obj(identifier, scope, version)
    title = _make_title(entity_type, identifier, scope, version)
    print_fn(obj, title)
