import click
import subprocess
import json
from bris_fiab.checkpoint.metadata import adapt_metdata

import anemoi.utils.checkpoints

description = '''
A command-line tool to update the metadata of a bris-generated checkpoint, so that it is runnable by anemoi-inference with mars input.

Note that this tool will _modify_ (not copy) the checkpoint file.
'''
default_replace_path = 'dataset.variables_metadata'


@click.command(help=description)
@click.option('--checkpoint', type=click.Path(exists=True),  required=True,
              help='Path to checkpoint to update metadata.')
@click.option('--replace-path',  type=str, default=f'{default_replace_path}',
              help=f'Dot-separated path to the key in the metadata to be replaced. Default: {default_replace_path}')
def cli(checkpoint: str, replace_path: str):

    print(f'Updating metadata in checkpoint: {checkpoint}')
    print(f'Keys updated: {replace_path}')

    metadata = anemoi.utils.checkpoints.load_metadata(checkpoint)

    adapt_metdata(metadata, replace_path)

    print(f'Loading updated metadata into {checkpoint}')

    anemoi.utils.checkpoints.replace_metadata(checkpoint, metadata)

    print(f'Updated metadata saved to checkpoint {checkpoint}')


if __name__ == "__main__":
    cli()
