from asyncio import run 
from set_settings import main


if __name__ == '__main__':
    try:
        run(main())
    
    except KeyboardInterrupt:
        print("exit...")