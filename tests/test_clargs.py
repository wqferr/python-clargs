from clargs import __version__, cli, Option


def test_version():
    assert __version__ == "0.1.0"


def test_thing_2():
    @cli
    class Args:
        x = 2
        y = "my_string"
        z = Option(str, "DEFAULT")

    args = Args(["a", "-i", "b"])
    print(args)
