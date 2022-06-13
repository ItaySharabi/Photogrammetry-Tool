from time import sleep


def pretty_print(content: str) -> None:
    """ Prints the content with a nice delay
        where the char `=` is printed out faster so
        headlines consisting `=` look nice """
    for c in content:
        if "=" in c:
            sleep(0.007)
        else:
            sleep(0.035)
        print(c, end="", flush=True)
    print("")

