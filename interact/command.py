import argparse


def main():
    """
    Interact-cli

    :param output: Output file.
    """

    parser = argparse.ArgumentParser(description="Interact cli")
    parser.add_argument("-o", "--output", type=str, help="Output file.")
    args = parser.parse_args()

    print("[+]:", args)

    print("[+]:", args.output)


if __name__ == "__main__":
    main()
