from user import User
from shows import Show
import os
import click
from spider import init


@click.command()
@click.argument("user_name")
@click.argument("url")
@click.argument("episode_number")
def start(user_name, url, episode_number):
    try:
        print("here")
        user   = User(user_name,Show(url,episode_number))
        init(user) 
    except Exception:
        print("Validation failed")

if __name__ == "__main__":
    start()


