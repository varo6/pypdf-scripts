import argparse
import argcomplete
from src import methods, pyextract, pyscanner

options = {
    "extract_pdf": pyextract.extract_pdf,
    "scan_pdf": pyscanner.scan_to_text,
}

# sysarguments parsers

def create_parser():
    parser = argparse.ArgumentParser(description="PyPDF Scripts")
    parser.add_argument(
        "operation", choices=options.keys(), help="Operation to perform"
    )
    parser.add_argument(
        "filename",
        nargs="*",
        default="example.pdf",
        help="Route of the file to process.",
    )  # Optional
    parser.add_argument("-p","--pages", nargs="?", type=methods.pages_args, default="1-3", help="Number of pages")
    parser.add_argument(
        "-o", "--output", nargs="?", default="output", help="Output file"
    )
    argcomplete.autocomplete(parser)
    return parser


def main():

    parser = create_parser()
    args = parser.parse_args()

    options[args.operation](
        args.filename[0], args.pages, args.output
    )


if __name__ == "__main__":
    main()
