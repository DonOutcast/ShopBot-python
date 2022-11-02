from aiogram.dispathcer.filters import Command
from aiogram improt types
from loader import dp

@dp.message_handler(Command("meny"))
async def show_menu(message: types.Message):
    await list_categories(message)

async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = awaitcategories_keydoard()
    
