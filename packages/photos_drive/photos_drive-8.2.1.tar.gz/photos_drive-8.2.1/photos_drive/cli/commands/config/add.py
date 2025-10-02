import logging

import typer
from typing_extensions import Annotated

from photos_drive.cli.shared.config import build_config_from_options
from photos_drive.cli.shared.inputs import (
    READ_ONLY_SCOPES,
    prompt_user_for_gphotos_credentials,
    prompt_user_for_mongodb_connection_string,
    prompt_user_for_non_empty_input_string,
    prompt_user_for_options,
)
from photos_drive.cli.shared.logging import setup_logging
from photos_drive.cli.shared.typer import (
    createMutuallyExclusiveGroup,
)
from photos_drive.shared.config.config import (
    AddGPhotosConfigRequest,
    AddMongoDbConfigRequest,
    AddMongoDbVectorStoreConfigRequest,
)

logger = logging.getLogger(__name__)

app = typer.Typer()
config_exclusivity_callback = createMutuallyExclusiveGroup(2)


@app.command()
def gphotos(
    config_file: Annotated[
        str | None,
        typer.Option(
            "--config-file",
            help="Path to config file",
            callback=config_exclusivity_callback,
        ),
    ] = None,
    config_mongodb: Annotated[
        str | None,
        typer.Option(
            "--config-mongodb",
            help="Connection string to a MongoDB account that has the configs",
            is_eager=False,
            callback=config_exclusivity_callback,
        ),
    ] = None,
    verbose: Annotated[
        bool,
        typer.Option(
            "--verbose",
            help="Whether to show all logging debug statements or not",
        ),
    ] = False,
):
    setup_logging(verbose)
    logger.debug(
        "Called config add gphotos handler with args:\n"
        + f" config_file: {config_file}\n"
        + f" config_mongodb={config_mongodb}\n"
        + f" verbose={verbose}"
    )

    # Set up the repos
    config = build_config_from_options(config_file, config_mongodb)
    gphotos_account_name = prompt_user_for_non_empty_input_string(
        "Enter name of your Google Photos account: "
    )

    print("Now, time to log into your Google account for read+write access\n")
    read_write_credentials = prompt_user_for_gphotos_credentials()

    print("Now, time to log into your Google account for read only access\n")
    read_only_credentials = prompt_user_for_gphotos_credentials(READ_ONLY_SCOPES)

    config.add_gphotos_config(
        AddGPhotosConfigRequest(
            name=gphotos_account_name,
            read_write_credentials=read_write_credentials,
            read_only_credentials=read_only_credentials,
        )
    )

    print("Successfully added your Google Photos account!")


@app.command()
def mongodb(
    config_file: Annotated[
        str | None,
        typer.Option(
            "--config-file",
            help="Path to config file",
            callback=config_exclusivity_callback,
        ),
    ] = None,
    config_mongodb: Annotated[
        str | None,
        typer.Option(
            "--config-mongodb",
            help="Connection string to a MongoDB account that has the configs",
            is_eager=False,
            callback=config_exclusivity_callback,
        ),
    ] = None,
    verbose: Annotated[
        bool,
        typer.Option(
            "--verbose",
            help="Whether to show all logging debug statements or not",
        ),
    ] = False,
):
    setup_logging(verbose)
    logger.debug(
        "Called config add mongodb handler with args:\n"
        + f" config_file: {config_file}\n"
        + f" config_mongodb={config_mongodb}\n"
        + f" verbose={verbose}"
    )

    # Set up the repos
    config = build_config_from_options(config_file, config_mongodb)
    name = prompt_user_for_non_empty_input_string(
        "Enter name of your Mongo DB account: "
    )

    read_write_connection_string = prompt_user_for_mongodb_connection_string(
        "Enter your admin connection string: "
    )

    read_only_connection_string = prompt_user_for_mongodb_connection_string(
        "Enter your read only connection string: "
    )

    config.add_mongodb_config(
        AddMongoDbConfigRequest(
            name=name,
            read_write_connection_string=read_write_connection_string,
            read_only_connection_string=read_only_connection_string,
        )
    )

    print("Successfully added your Mongo DB account!")


@app.command()
def vector_store(
    config_file: Annotated[
        str | None,
        typer.Option(
            "--config-file",
            help="Path to config file",
            callback=config_exclusivity_callback,
        ),
    ] = None,
    config_mongodb: Annotated[
        str | None,
        typer.Option(
            "--config-mongodb",
            help="Connection string to a MongoDB account that has the configs",
            is_eager=False,
            callback=config_exclusivity_callback,
        ),
    ] = None,
    verbose: Annotated[
        bool,
        typer.Option(
            "--verbose",
            help="Whether to show all logging debug statements or not",
        ),
    ] = False,
):
    setup_logging(verbose)
    logger.debug(
        "Called config add vector-store handler with args:\n"
        + f" config_file: {config_file}\n"
        + f" config_mongodb={config_mongodb}\n"
        + f" verbose={verbose}"
    )

    # Set up the repos
    config = build_config_from_options(config_file, config_mongodb)
    name = prompt_user_for_non_empty_input_string("Enter name of your vector store: ")
    option = prompt_user_for_options(
        'Select one of the options as your vector store', ['MongoDB']
    )

    if option == 'MongoDB':
        read_write_connection_string = prompt_user_for_mongodb_connection_string(
            "Enter your admin connection string: "
        )

        read_only_connection_string = prompt_user_for_mongodb_connection_string(
            "Enter your read only connection string: "
        )

        config.add_vector_store_config(
            AddMongoDbVectorStoreConfigRequest(
                name=name,
                read_write_connection_string=read_write_connection_string,
                read_only_connection_string=read_only_connection_string,
            )
        )

        print("Successfully added your Mongo DB Vector Store account!")
    else:
        raise NotImplementedError(f'Vector store type {option} not supported')
