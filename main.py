from os import curdir
from jinja2 import Environment, PackageLoader, select_autoescape
import json
import pkgutil
import click
import gettext

env = Environment(
    loader=PackageLoader("resume"),
    autoescape=select_autoescape(),
    extensions=["jinja2.ext.i18n"],
)

def main(lang:str):
    template = env.get_template("index.html.jinja")

    localedir = curdir + '/lang'
    env.install_gettext_translations(translations=gettext.translation(
        domain='resume', localedir=localedir, languages=[lang]))

    content = pkgutil.get_data("resume", "resume.json")
    if content is None:
        print("can not find resume.json in app dir")
        exit(-1)

    resume = json.loads(content.decode("utf-8"))
    # print(resume['basics'])

    with open("index.html", "w+") as f:
        f.write(template.render(resume=resume, basics=resume["basics"]))


@click.group()
def cli():
    """A simple command line tool."""
    pass


@cli.command()
def testtrans():
    """test translate text"""
    localedir = curdir + '/lang'
    gettext.bindtextdomain('resume', localedir)
    gettext.textdomain('resume')
    print(gettext.gettext("Links"))


@cli.command()
@click.option('-l', '--lang', help="language, en_US(defualt) or zh_CN", type=str, default='en_US')
def collectmsg(lang:str):
    """generate po file"""
    template = env.get_template("index.html.jinja")
    po_file = curdir + f'/lang/{lang}/LC_MESSAGES/resume.po'
    with open(po_file, 'w+') as po:
        po.write(
            'msgid ""\n'
            'msgstr ""\n'
            '"Content-Type: text/plain; charset=UTF-8\\n"\n'
            '"Project-Id-Version: MetaSearch 0.1-dev\\n"\n'
            '"MIME-Version: 1.0\\n"\n'
        )

        msg_strings: list[str] = []
        if template.filename is None:
            print("template file is not find")
            return

        with open(template.filename) as f:
            for (lineno, function, message) in env.extract_translations(f.read()):
                if message not in msg_strings:
                    msg_strings.append(message)
                    po.write(f"#{function}:{lineno}\n")
                    po.write(f"msgid \"{message}\"\n")
                    po.write('msgstr ""\n\n')


@cli.command()
@click.option('-l', '--lang', help="language, en_US(defualt) or zh_CN", type=str, default='en_US')
def gen(lang:str):
    """generate html"""
    main(lang)


cli.add_command(testtrans)
cli.add_command(collectmsg)
cli.add_command(gen)

if __name__ == "__main__":
    cli()
