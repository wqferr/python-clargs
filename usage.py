from sys import argv
from clargs import cli, Option


@cli
class Args:
    x = 2
    y = "3"
    z = Option(str, "DEFAULT")


if __name__ == "__main__":
    args = Args(argv)
