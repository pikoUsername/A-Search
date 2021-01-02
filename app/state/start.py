from aiogram.dispatcher.filters.state import StatesGroup, State

class MainMenuState(StatesGroup):
    main_menu =   State()
    config_menu = State()
    meta_menu =   State()