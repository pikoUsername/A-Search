from aiogram import Dispatcher


def setup(dp: Dispatcher):
    from .admin_filter import IsAdminFilter

    dp.filters_factory.bind(IsAdminFilter)
