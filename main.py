from pathlib import Path
import logging

# import pkgutil
# search_path = ['.']
# all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
# print(all_modules)

from controller.TodoController import Todo

# set the paths
BASEDIR = Path(__file__).parent
LOG_DIR = BASEDIR.joinpath('log')
DATA_DIR = BASEDIR.joinpath('data')
LOG_FILE = BASEDIR.joinpath(LOG_DIR, 'day_log.txt')
DATA_FILE = BASEDIR.joinpath(DATA_DIR, 'tasks.csv')

# configure the logging module
logging.basicConfig(level=logging.DEBUG,
                    filename=LOG_FILE,
                    filemode='a',
                    format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s')

def main():
    """
    Main entry point into TodoApp
    1. Configurations are initialized
    2. TodoController is initialized
    """
    # STEP 1: define my logger.
    logger = logging.getLogger('todo_app')

    tc = Todo()
    tc.running = True
    tc.todo_logger = logger
    tc.page_width = 130
    tc.app_title = ' TO-DO App '.center(tc.page_width, ' ')
    tc.ld_tsk_to_mem()
    while tc.running:
        tc.init_interface()
        tc.get_input()

if __name__ == '__main__':
    main()
