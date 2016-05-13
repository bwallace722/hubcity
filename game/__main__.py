import time
import state
import default

# main creates a default game state and runs it until the game is over.
def main():
    default_state = default.get_default_state()

    while default_state.game_going():
        default_state.transition([])
        print default_state
        time.sleep(.5)

    print('game over!')

if __name__ == '__main__':
    main()
