import argparse
import sys
from . import remove_frameshifts as rf
from . import build_priors as bp
from . import run_mixed_assembly as rma


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="mixedassembly",
        description="MixedAssembly: tools for consensus sequence assembly and frameshift correction"
    )
    subparsers = parser.add_subparsers(
        title="subcommands",
        description="Available commands",
        dest="command",
        required=True
    )

    # ---- Subcomandos ----
    subparsers.add_parser("remove-frameshifts", help="Remove frameshifts from an alignment")
    subparsers.add_parser("build-priors", help="Build priors parquet file")
    subparsers.add_parser("run-mixed-assembly", help="Run mixed assembly pipeline")

    # Parse args hasta el primer subcomando
    args, extra = parser.parse_known_args(argv)

    # Despacho a la función main() de cada script
    if args.command == "remove-frameshifts":
        sys.exit(rf.main(extra))
    elif args.command == "build-priors":
        sys.exit(bp.main(extra))
    elif args.command == "run-mixed-assembly":
        sys.exit(rma.main(extra))
