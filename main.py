import click
import TextSum


@click.group()
def cli():
    pass


@cli.command()
def initialize():
    """Download required nltk libraries."""
    TextSum.setup_environment()


@cli.command()
@click.argument('filename')
def extract_summary(filename):
    """Print summary text to stdout."""
    with open(filename) as f:
        summary = TextSum.extract_sentences(f.read())
        print(summary)


@cli.command()
@click.argument('filename')
def extract_phrases(filename):
    """Print key-phrases to stdout."""
    with open(filename) as f:
        phrases = TextSum.extract_key_phrases(f.read())
        print(phrases)
