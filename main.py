from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("resume"),
    autoescape=select_autoescape()
)

template = env.get_template("index.html.jinja")

import json
import pkgutil

content = pkgutil.get_data('resume', 'resum.json')
if content is None:
  print('can not find resume.json in app dir')
  exit(-1)

resume = json.loads(content.decode('utf-8'))
# print(resume['basics'])

with open('index.html', 'w+') as f:
  f.write(template.render(resume=resume, basics=resume['basics']))