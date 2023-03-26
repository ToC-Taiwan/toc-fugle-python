from hashlib import md5

from jinja2 import Environment, FileSystemLoader
from keyring import set_keyring, set_password
from keyrings.cryptfile.cryptfile import CryptFileKeyring

from env import RequiredEnv

if __name__ == "__main__":
    env = RequiredEnv()

    environment = Environment(loader=FileSystemLoader("data/"))
    template = environment.get_template("config.template.ini")

    FILENAME = "data/config.ini"
    content = template.render(
        api_key=env.api_key,
        api_secret=env.api_secret,
        api_user=env.api_user,
    )

    with open(FILENAME, mode="w", encoding="utf-8") as message:
        message.write(content)

    kr = CryptFileKeyring()
    kr.keyring_key = md5(env.api_user.encode("utf-8")).hexdigest()

    set_keyring(kr)
    set_password("fugle_trade_sdk:account", env.api_user, env.login_password)
    set_password("fugle_trade_sdk:cert", env.api_user, env.ca_password)
