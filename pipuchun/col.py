

import logging

from aiogram import  Bot, Dispatcher, executor, types

TOKENn = '1979983147:AAFsdXnaSTYgdSXDGdgubBcxyMynFkCYEwQ'
logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKENn)
dp = Dispatcher(bot)
CHANNEL_ID = '@uzb143'
import markups as nav

def check_sub_channel(chat_member):
    
    if chat_member['status'] != 'left':
        return True
    else:
        return False

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
           if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
               await bot.send_message(message.from_user.id, 'salom ishladi' , reply_markup=nav.checksubmenu)
           else:
               await bot.send_message(message.from_user.id, 'ishlamadi', reply_markup=nav.checksubmenu)



@dp.callback_query_handler(text="subchanneldone")
async def subchanell(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id,'azo buldi', reply_markup=nav.profilekey)
    else:
        await bot.send_message(message.from_user.id, 'aldama', reply_markup=nav.checksubmenu)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True)