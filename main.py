import warnings

warnings.filterwarnings("ignore", category=UserWarning,
                        message="In the future version we will turn default option ignore_ncx to True.")
from gui import run_app


def main():
    run_app()


if __name__ == "__main__":
    main()
