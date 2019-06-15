from clargs import __version__, cli


def test_version():
    assert __version__ == "0.1.0"


def test_thing_2():
    @cli
    class Sub:
        x = 2
        y = "my_string"

        def do_thing(self):
            pass

        @classmethod
        def class_do_thing(cls):
            pass
