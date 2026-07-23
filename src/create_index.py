from src.infrastructure.index_manager import IndexManager


def main():
    manager = IndexManager()
    manager.create_index()


if __name__ == "__main__":
    main()