import os
import asyncio
from src.configs.configuration import Configuration

if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    print(Configuration.settings["application"])
    print(Configuration.settings["databases"])
    print(Configuration.settings)


if __name__ == '__main__':
    asyncio.run(main())