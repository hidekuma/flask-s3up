import os
import shutil
import argparse
import textwrap
import click
from config import (
    SUPPORT_TEMPLATES,
    FIXED_TEMPLATE_FOLDER,
    NAMESPACE
)

class FlaskS3UpCli:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog=NAMESPACE,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent("""\n
         ____  __     __   ____  __ _    ____  ____  _  _  ____
        (  __)(  )   / _\ / ___)(  / )  / ___)( __ \/ )( \(  _ \\
         ) _) / (_/\/    \\\___ \ )  (   \___ \ (__ () \/ ( ) __/
        (__)  \____/\_/\_/(____/(__\_)  (____/(____/\____/(__)\n
        ============= Flask S3Up Command Line Tool ==============
        """)
        )
        self.parser.add_argument(
            "-p",
            "--path",
            type=str,
            required=True,
            help="Enter the directory path where the template will be located",
        )
        self.parser.add_argument(
            "-t",
            "--template",
            type=str,
            default='base',
            help="Enter the name of the template to import.\
            (mdl means material-design-lite and base means not designed template).",
            choices=SUPPORT_TEMPLATES
        )

    def handle(self):
        args = self.parser.parse_args()

        if args.template:
            file_path = os.path.dirname(os.path.abspath(__file__))
            template_path = args.path
            base_template_path = os.path.join(
                file_path,
                'blueprints',
                FIXED_TEMPLATE_FOLDER
            )

            if os.path.exists(template_path):
                click.echo(
                    '\n {} : Already exists template directory ({}).'.format(
                        click.style(
                            "Failed",
                            fg="red",
                            bold=True
                        ),
                        os.path.abspath(template_path)
                    )
                )
            else:
                origin_template_path = os.path.join(
                    base_template_path,
                    f'{args.template}'
                )
                shutil.copytree(origin_template_path, template_path)
                click.echo(
                    '\n {} : Template successfully created. ({})'.format(
                        click.style(
                            "Success",
                            fg="green",
                            bold=True
                        ),
                        os.path.abspath(template_path)
                    )
                )
        else:
            pass

def handle():
    cli = FlaskS3UpCli()
    cli.handle()

if __name__ == "__main__":
    handle()
