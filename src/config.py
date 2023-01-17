from jinja2 import Environment, FileSystemLoader

from env import RequiredEnv

env = RequiredEnv()

environment = Environment(loader=FileSystemLoader("data/"))
template = environment.get_template("config.template.ini")

filename = "data/config.ini"
content = template.render(
    api_key=env.api_key,
    api_secret=env.api_secret,
    api_user=env.api_user,
)

with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
