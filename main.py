def main():
    """
       Runs the start screen 
    """
    from Match.game import Game # placing the import in a func makes python import that module only when needed
    start = Game()
    start.start_scene()

if __name__ == "__main__":
    main()