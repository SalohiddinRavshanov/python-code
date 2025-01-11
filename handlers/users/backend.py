from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.default.keyboard import bosh_sahifa
from loader import dp
from states.holatlar import ALLSTATE
from keyboards.default.backend_keyboard import backend, PHP, MySQL, sariq_keyboard, sariq_dev, botir_keyboard, django, \
    sariq_django, telegram_bot


@dp.message_handler(Text('📂 BackEnd'))
async def front(message:Message):
    await message.answer('👨‍💻Quydagi darslarni birini tanlang',reply_markup=backend)

@dp.message_handler(Text('⬆️Ortga'))
async def ortgaaaa(message:Message):
    await message.answer(f"{message.text}",reply_markup=bosh_sahifa)



@dp.message_handler(Text('PHP'))
async def front(message:Message):

    await message.answer(f"{message.text}",reply_markup=PHP)
    await ALLSTATE.php.set()
@dp.message_handler(state=ALLSTATE.php)
async def php_def(message:Message,state:FSMContext):

    if message.text=='1-dars':
        file_id = 'BAACAgIAAxkBAAIEX2dnvorIIeEnKUujwFUve7igURP_AAITIwACWJ9ASOOKdVWdxe7kNgQ'
        await message.answer_video(file_id,caption='📹 PHP #1 - Dars. OpenServer yuklab olish ')

    elif message.text=='2-dars':
        file_id = 'BAACAgIAAxkBAAIEYWdnvpJAtjXBGbEeLKfSoZxCWfvCAAIZIwACWJ9ASBwEXZQjTC50NgQ'
        await message.answer_video(file_id,caption='📹 PHP #2 - Dars. PHP Sintaksisi va echo, print buyruqlari bilan ishlash')
    elif message.text=='3-dars':
        file_id = 'BAACAgIAAxkBAAIEY2dnvphQmIWmlL5QgE0mQLxvA29PAAK8GwACWJ9ISKne7bWWa8MgNgQ'
        await message.answer_video(file_id,caption='📹 PHP #3 - Dars. PHPda O\'zgaruvchilar ')
    elif message.text=='4-dars':
        file_id = 'BAACAgIAAxkBAAIEZWdnvqMAAQaZy65_FCE4SBg4hs9fnAACXB0AAu6mYUjDxS5exkXEzzYE'
        await message.answer_video(file_id,caption='📹 PHP #4 - Dars. PHPda Arifmetik amallar')

    elif message.text=='5-dars':
        file_id = 'BAACAgIAAxkBAAIEZ2dnvqzbJRc3r-uKzcBm_6cFqmT_AAJsIAACdDFoSDuUazePhWaUNgQ'
        await message.answer_video(file_id,caption='📹 PHP #5 - Dars. PHPda solishtirish operatorlari ')

    elif message.text=='6-dars':
        file_id = 'BAACAgIAAxkBAAIDZWdi4U1lYCuqhQcauY8BHPjexLl-AAKOTgACTdtQS_cl6jeRs_4yNgQ'
        await message.answer_video(file_id,caption='📹 PHP #6 - Dars. PHP da Shart operatorlari ')

    elif message.text=='7-dars':
        file_id = 'BAACAgIAAxkBAAIDZ2di4VKchRC39GDI5-oUhipVGiTlAALCXAACEWxZSRRJmbTVChn0NgQ'
        await message.answer_video(file_id,caption='📹 PHP #7 - Dars. PHP da Shart operatorlari 2-qism')

    elif message.text=='8-dars':
        file_id = 'BAACAgIAAxkBAAIDZWdi4U1lYCuqhQcauY8BHPjexLl-AAKOTgACTdtQS_cl6jeRs_4yNgQ'
        await message.answer_video(file_id,caption='📹 PHP #8 - Dars. PHP da Switch Operatori')

    elif message.text=='9-dars':
        file_id = 'BAACAgIAAxkBAAIDZ2di4VKchRC39GDI5-oUhipVGiTlAALCXAACEWxZSRRJmbTVChn0NgQ'
        await message.answer_video(file_id,caption='📹 PHP #9 - Dars. PHP da switch operatorida mashq ')
    elif message.text=='10-dars':
        file_id = 'BAACAgIAAxkBAAIDZWdi4U1lYCuqhQcauY8BHPjexLl-AAKOTgACTdtQS_cl6jeRs_4yNgQ'
        await message.answer_video(file_id,caption='📹 PHP #10 - Dars. PHP da takrorlanish operatori (For)')
    elif message.text=='11-dars':
        file_id = 'BAACAgIAAxkBAAIDZ2di4VKchRC39GDI5-oUhipVGiTlAALCXAACEWxZSRRJmbTVChn0NgQ'
        await message.answer_video(file_id,caption='11-dars, PHP uchun')

    elif message.text=='12-dars':
        file_id = 'BAACAgIAAxkBAAIDZWdi4U1lYCuqhQcauY8BHPjexLl-AAKOTgACTdtQS_cl6jeRs_4yNgQ'
        await message.answer_video(file_id,caption='📹 PHP #12 - Dars. PHP da massiv(array) ')

    elif message.text=='13-dars':
        file_id = 'BAACAgIAAxkBAAIDZ2di4VKchRC39GDI5-oUhipVGiTlAALCXAACEWxZSRRJmbTVChn0NgQ'
        await message.answer_video(file_id,caption='📹 PHP #13 Assotsative && Ko\'p o\'lchamli arrays ')

    elif message.text=='14-dars':
        file_id = 'BAACAgIAAxkBAAIDZWdi4U1lYCuqhQcauY8BHPjexLl-AAKOTgACTdtQS_cl6jeRs_4yNgQ'
        await message.answer_video(file_id,caption='📹 PHP  #14-dars. Foreach')

    elif message.text=='15-dars':
        file_id = 'BAACAgIAAxkBAAIDZ2di4VKchRC39GDI5-oUhipVGiTlAALCXAACEWxZSRRJmbTVChn0NgQ'
        await message.answer_video(file_id,caption='📹 PHP #15 - Dars. Massiv va Foreach ga doir mashq. ')

    elif message.text=='16-dars':
        file_id = 'BAACAgIAAxkBAAIDZWdi4U1lYCuqhQcauY8BHPjexLl-AAKOTgACTdtQS_cl6jeRs_4yNgQ'
        await message.answer_video(file_id,caption='📹 PHP #16-dars. PHPda funktsiya(function)')

    elif message.text=='17-dars':
        file_id = 'BAACAgIAAxkBAAIDZ2di4VKchRC39GDI5-oUhipVGiTlAALCXAACEWxZSRRJmbTVChn0NgQ'
        await message.answer_video(file_id,caption='📹 PHP #17-Dars. PHP da include')

    elif message.text=='18-dars':
        file_id = 'BAACAgIAAxkBAAIDZWdi4U1lYCuqhQcauY8BHPjexLl-AAKOTgACTdtQS_cl6jeRs_4yNgQ'
        await message.answer_video(file_id,caption='📹 PHP #18 - Dars. PHPda Super Globalniy o\'zgaruvchilar')

    elif message.text=='19-dars':
        file_id = 'BAACAgIAAxkBAAIDZ2di4VKchRC39GDI5-oUhipVGiTlAALCXAACEWxZSRRJmbTVChn0NgQ'
        await message.answer_video(file_id,caption='📹 PHP #19 - Dars. PHP POST va GET')
    elif message.text=='20-dars':
        file_id = 'BAACAgIAAxkBAAIDZWdi4U1lYCuqhQcauY8BHPjexLl-AAKOTgACTdtQS_cl6jeRs_4yNgQ'
        await message.answer_video(file_id,caption='📹 PHP #20 - Dars. PHPda SESSION va COOKIE')
    elif message.text=='21-dars':
        file_id = 'BAACAgIAAxkBAAIDZ2di4VKchRC39GDI5-oUhipVGiTlAALCXAACEWxZSRRJmbTVChn0NgQ'
        await message.answer_video(file_id,caption='📹 PHP #21 - Dars. PHPda const, define')

    elif message.text=='22-dars':
        file_id = 'BAACAgIAAxkBAAIDZWdi4U1lYCuqhQcauY8BHPjexLl-AAKOTgACTdtQS_cl6jeRs_4yNgQ'
        await message.answer_video(file_id,caption='📹 PHP #22 - Dars. PHPda mashq(fibanachi sonlar ketma-ketligi)')

    elif message.text=='23-dars':
        file_id = 'BAACAgIAAxkBAAIDZ2di4VKchRC39GDI5-oUhipVGiTlAALCXAACEWxZSRRJmbTVChn0NgQ'
        await message.answer_video(file_id,caption='📹 PHP #23 - Dars. PHPda mashq tub sonlarni aniqlash')

    elif message.text=='24-dars':
        file_id = 'BAACAgIAAxkBAAIDZWdi4U1lYCuqhQcauY8BHPjexLl-AAKOTgACTdtQS_cl6jeRs_4yNgQ'
        await message.answer_video(file_id,caption='📹 PHP #24-Dars. PHP va SQL ni bog’lanishi ')

    elif message.text=='25-dars':
        file_id = 'BAACAgIAAxkBAAIDZ2di4VKchRC39GDI5-oUhipVGiTlAALCXAACEWxZSRRJmbTVChn0NgQ'
        await message.answer_video(file_id,caption='📹 PHP #25-Dars.PHPda SQlga insert, update, delete amallari ')


    elif message.text=='⬆️Ortga':

        await message.answer(f"{message.text}",reply_markup=backend)
        await state.finish()
    elif message.text=='Davomi...':
        await message.answer(f"<b>👁 Qolgan videolarni You Tubedan tomosha qiling!\n\n"
                             f"<a href='https://www.youtube.com/watch?v=a6xtQQqx1tg'>LINK</a></b>")

#######MySQL

@dp.message_handler(Text('MySQL'))
async def mysql_def(message:Message,state:FSMContext):
    await message.answer(f"{message.text}",reply_markup=MySQL)
    file_id='BQACAgIAAxkBAAIfWmJkywHmJDV1bJyZ6G5Z_0oPGWmuAAKXEAACoUThS4FAiQXxZE6-JAQ'
    await message.answer_document(file_id,caption='\n'
                                                  'SQL – maxsus tillar sirasiga kiradi. SQL domenga xos til '
                                                  'hisoblanib, dasturlashda keng foydalaniladi. Yana ham aniq '
                                                  'aytadigan boʻlsak, ushbu til orqali foydalanuvchilar maʼlumotlar '
                                                  'omborini boshqarish tizimida saqlanadigan maʼlumotlarni boshqarishlarida '
                                                  'kerak boʻladi.')
    await ALLSTATE.mysql.set()



@dp.message_handler(state=ALLSTATE.mysql)
async def mysql_def_state(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgIAAxkBAAIFGmdtZvkeuZ0JcCsw9Bf1a930KWPhAALDXwACLrhBSUDllNTYmcLINgQ'
        await message.answer_video(file_id,caption='📹#1 SQL dasturlash tili — Farkhod Dadajanov ')

    elif message.text=='2-dars':
        file_id = 'BAACAgIAAxkBAAIFHGdtZxQdOp3nkC5r0RnrLcpPKq8HAAJLWQACTOTJSMC5G-BMllAxNgQ'
        await message.answer_video(file_id,caption='📹#2 SQL dasturlash tili — Farkhod Dadajanov')
    elif message.text=='3-dars':
        file_id = 'BAACAgIAAxkBAAIFImdtZxTGhPdAVDqUTt4BHzzzOnCQAALMXwACLrhBSTdf2FEVpk1aNgQ'
        await message.answer_video(file_id,caption='📹#3 SQL dasturlash tili — Farkhod Dadajanov')
    elif message.text=='4-dars':
        file_id = 'BAACAgIAAxkBAAIFI2dtZxTwOybdelPJppG41oAsVXRsAALNXwACLrhBSeBnpMSbBGg9NgQ'
        await message.answer_video(file_id,caption='📹 #4 SQL dasturlash tili — Farkhod Dadajanov')

    elif message.text=='5-dars':
        file_id = 'BAACAgIAAxkBAAIFJGdtZxQBmloJJXQk3hJUGfoISh2mAALPXwACLrhBSQT9C17x6yfnNgQ'
        await message.answer_video(file_id,caption='📹 #5 SQL dasturlash tili — Farkhod Dadajanov ')

    elif message.text=='6-dars':
        file_id = 'BAACAgIAAxkBAAIFIGdtZxQ2KcLgd52caDFmfTFQifIQAALIXwACLrhBScOUuI84dgFTNgQ'
        await message.answer_video(file_id,caption='📹#6 SQL dasturlash tili — Farkhod Dadajanov ')

    elif message.text=='7-dars':
        file_id = 'BAACAgIAAxkBAAIFHWdtZxR3qHgyxex_t-YVkjvfbX9uAALEXwACLrhBScT5RLG_QEubNgQ'
        await message.answer_video(file_id,caption='📹 #7 SQL dasturlash tili — Farkhod Dadajanov')

    elif message.text=='8-dars':
        file_id = 'BAACAgIAAxkBAAIFIWdtZxTpwup-6QXpIcvLyi3DPXtBAALKXwACLrhBSXAQ73GTGRVUNgQ'
        await message.answer_video(file_id,caption='📹 #8 SQL dasturlash tili — Farkhod Dadajanov')

    elif message.text=='9-dars':
        file_id = 'BAACAgIAAxkBAAIFH2dtZxRkfBLEnfakba0uSzGx4AeOAALHXwACLrhBScdTtIQlgBfhNgQ'
        await message.answer_video(file_id,caption='📹#9 SQL dasturlash tili — Farkhod Dadajanov')
    elif message.text=='10-dars':
        file_id = 'BAACAgIAAxkBAAIFHmdtZxSgwWKxv_u6D-RNIsOwRQzwAALFXwACLrhBSXmQ3wJuI3tkNgQ'
        await message.answer_video(file_id,caption='📹 #10 SQL dasturlash tili — Farkhod Dadajanov')

    elif message.text=='⬆️Ortga':

        await message.answer(f"{message.text}",reply_markup=backend)
        await state.finish()
##########



####Python
@dp.message_handler(Text('Python'))
async def python_def(message:Message,state:FSMContext):
    await message.answer(f"{message.text}",reply_markup=sariq_dev)
    await ALLSTATE.python.set()

@dp.message_handler(state=ALLSTATE.python)
async def python_def_state(message:Message,state:FSMContext):
    if message.text=='Sariqdev':
        await message.answer(f'{message.text}',reply_markup=sariq_keyboard)
        await ALLSTATE.sariqdev.set()

    elif message.text=='Botir Ziyatov':
        await message.answer(f"{message.text}",reply_markup=botir_keyboard)
        await ALLSTATE.botir.set()

    elif message.text=='⬆️Ortga':

        await message.answer(f"{message.text}",reply_markup=backend)
        await state.finish()

@dp.message_handler(state=ALLSTATE.sariqdev)
async def sariq_dev_def(message:Message,state:FSMContext):

    if message.text=='1-dars':
        file_id = 'BAACAgIAAxkBAAO4Z179IXtG84kodQOvh5_C5PBmefQAArdaAAL6cOFKdEmPRfhbWrQ2BA'
        await message.answer_video(file_id,caption='📹 #01 Python Darslari | Anaconda o\'rnatamiz \nSariq dev ')

    elif message.text=='2-dars':
        file_id = 'BAACAgIAAxkBAAO6Z179a81ATaVlYFUVNZ7PNZJ0h9UAArxaAAL6cOFKdFatk5kXgD82BA'
        await message.answer_video(file_id,caption='📹 #02 Python Darslari | Birinchi Dasturimiz ')
    elif message.text=='3-dars':
        file_id = 'BAACAgIAAxkBAAO8Z17-HXUn9iAD9FRX1rzbtp3O4qQAAr1aAAL6cOFKuUAUbXcZ6J42BA'
        await message.answer_video(file_id,caption='📹 #03 Python Darslari | print(), Arifmetik amallar va Sinteks ')
    elif message.text=='4-dars':
        file_id = 'BAACAgIAAxkBAAO-Z17-JYGlxScaHa0QLCJiw0EcCEoAAr5aAAL6cOFKVrY5XdzdJ9I2BA'
        await message.answer_video(file_id,caption='📹 #04 Python Darslari | O\'zgaruvchilar (Variables) ')

    elif message.text=='5-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #05 Python Darslari | Matn bilan ishlash (Strings)  ')

    elif message.text=='6-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #06 Python Darslari | Sonlar bilan ishlash ')

    elif message.text=='7-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #07 Python Darslari | Lists (Ro\'yxatlar) ')

    elif message.text=='8-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #08 Python Darslari | Ro\'yxat bilan ishlash. O\'zgarmas ro\'yxatlar (Tuples) ')

    elif message.text=='9-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #09 Python Darslari | for tsikli bilan tanishamiz ')
    elif message.text=='10-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #10 Python Darslari | if-else shartlari va tarmoqlanish ')
    elif message.text=='11-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #11 Python Darslari | if-elif-else ')

    elif message.text=='12-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #12 Python Darslari | Eng ko\'p uchraydigan xatolar  ')

    elif message.text=='13-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #13 Python Darslari | GitHub bilan tanishuv  ')

    elif message.text=='14-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹#14 Python Darslari | Lug\'at (Dictionary) ')

    elif message.text=='15-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #15 Python Darslari | Lug\'at bilan ishlaymiz  ')

    elif message.text=='16-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #16 Python Darslari | Nesting ')

    elif message.text=='17-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #17 Python Darslari | While tsikli ')

    elif message.text=='18-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #18 Python Darslari | While, Ro\'yxatlar va Lug\'atlar ')

    elif message.text=='19-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #19 Python Darslari | Funksiya ')
    elif message.text=='20-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #20 Python Darslari | Funksiyadan qiymat qaytarish ')
    elif message.text=='21-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #21 Python Darslari | Funksiyaga ro\'yxat uzatish ')

    elif message.text=='22-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #22 Python Darslari | Moslashuvchan funksiyalar ')

    elif message.text=='23-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #23 Python Darslari | Modullar ')

    elif message.text=='24-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #24 Python Darslari | Funksiya. So\'ngso\'z.  ')

    elif message.text=='25-dars':
        file_id = 'BAACAgIAAxkBAAPAZ17-KoXbeJ1AeGPVg4YQ02R8wBYAAshaAAL6cOFK67OMqjA8nL02BA'
        await message.answer_video(file_id,caption='📹 #25 Python Darslari | "Son topish" o\'yini. 3-qism. Kod  ')


    elif message.text=='⬆️Ortga':

        await message.answer(f"{message.text}",reply_markup=sariq_dev)
        await ALLSTATE.python.set()

    elif message.text=='Davomi...':
        await message.answer(f"<b>👁 Qolgan videolarni Sariq dev sahifasidan tomosha qiling!\n\n"
                             f"<a href='https://python.sariq.dev/'>LINK</a></b>")


@dp.message_handler(state=ALLSTATE.botir)
async def botir_def_state(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgIAAxkBAAIB-2dg_C728ZxMwHmCq1G5fTYpDSu7AAL_VQACSg4wSx0O8mTR2zApNgQ'
        await message.answer_video(file_id,caption='📹 1- dastur | Python dasturlash tili  ')

    elif message.text=='2-dars':
        file_id = 'BAACAgIAAxkBAAIB_mdg_fQV7oNcyB9-0L2KhV7wK2BAAAJrUwACQyGAS39SOCPabUKGNgQ'
        await message.answer_video(file_id,caption='📹 2- dastur | O‘zgaruvchilar, Python dasturlash tili ')
    elif message.text=='3-dars':
        file_id = 'BAACAgIAAxkBAAIB_2dg_fRnes_0pRoKcSUkMwFBulJCAALCVwACCnnhSnHlozAVls6eNgQ'
        await message.answer_video(file_id,caption='📹 #03 Python Darslari | print(), Arifmetik amallar va Sinteks ')
    elif message.text=='4-dars':
        file_id = 'BAACAgIAAxkBAAICAAFnYP30SvKnPaRSm5HmEthmCLvT8QACblMAAkMhgEvf79wK68_kBTYE'
        await message.answer_video(file_id,caption='📹 4- dastur | Operatorlar, Python dasturlash tili ')

    elif message.text=='5-dars':
        file_id = 'BAACAgIAAxkBAAICAWdg_fRwyoiWP_ZPFAisqiPbUN-hAAJvUwACQyGAS_7z3lJ4ZV8aNgQ'
        await message.answer_video(file_id,caption='📹 5- dastur | string, Python dasturlash tili ')

    elif message.text=='6-dars':
        file_id = 'BAACAgIAAxkBAAICAmdg_fShs1gWgbPn0iOqr5iHIzgKAAJwUwACQyGASw7m2oSN0H36NgQ'
        await message.answer_video(file_id,caption='📹 6- dastur | chiziqli dastur, Python dasturlash tili  ')

    elif message.text=='7-dars':
        file_id = 'BAACAgIAAxkBAAICA2dg_fTj14vxZbW1gU3ufPMVJBu5AAIGXwAC_FSRSO_Vby3SmKLRNgQ'
        await message.answer_video(file_id,caption='📹 7- dastur | shartlar,if,else Python dasturlash tili ')

    elif message.text=='8-dars':
        file_id = 'BAACAgIAAxkBAAICBGdg_fSz92Na6TDveVll-vd5FrbcAAIDYAACLrhBSXJUpDCotA3ENgQ'
        await message.answer_video(file_id,caption='📹 8- dastur | IF, murakkab shartlar. Python dasturlash tili  ')

    elif message.text=='9-dars':
        file_id = 'BAACAgIAAxkBAAICBWdg_fTnwmzsfUAFqNeldapioxmRAAKFXAACpSK4S1sRMm4er1RhNgQ'
        await message.answer_video(file_id,caption='📹 9- dastur | for, aylanma. Python dasturlash tili ')
    elif message.text=='10-dars':
        file_id = 'BAACAgIAAxkBAAICBmdg_fSQTHyN_SphZow18LCfbuwqAAIFYAACLrhBSeH0VHBDT7I5NgQ'
        await message.answer_video(file_id,caption='📹 10- dastur | while, aylanma. Python dasturlash tili ')
    elif message.text=='11-dars':
        file_id = 'BAACAgIAAxkBAAICB2dg_fQPv9B5puAHsazJ4ifWUlxbAAIGYAACLrhBSRrSNmAjjoZrNgQ'
        await message.answer_video(file_id,caption='📹 11- dastur | aylanma, turtle Python dasturlash tili  ')

    elif message.text=='12-dars':
        file_id = 'BAACAgIAAxkBAAICCGdg_fQaBNb3PaCSpIXmCaBid0T9AAIHYAACLrhBSSvBK9H9SmguNgQ'
        await message.answer_video(file_id,caption='📹 12- dastur | List, Pygal charts. Python dasturlash tili ')

    elif message.text=='13-dars':
        file_id = 'BAACAgIAAxkBAAICCWdg_fQ2qAwnx5aYClnkVSDjIS3fAAIIYAACLrhBSbLovbCAToQ5NgQ'
        await message.answer_video(file_id,caption='📹 13- dastur | Dict, JSON . Python dasturlash tili   ')

    elif message.text=='14-dars':
        file_id = 'BAACAgIAAxkBAAICCmdg_fRBtYmEczRPEXOd8bRzymYCAAIJYAACLrhBSdsKxkwd9imMNgQ'
        await message.answer_video(file_id,caption='📹 14- dastur | FUNKSIYA. Python dasturlash tili ')



    elif message.text=='⬆️Ortga':
        await message.answer(f"{message.text}",reply_markup=sariq_dev)
        await ALLSTATE.python.set()

#########


#####DJAngo

@dp.message_handler(Text('Django'))
async def python_def(message:Message,state:FSMContext):
    await message.answer(f"{message.text}",reply_markup=django)
    await ALLSTATE.django.set()

@dp.message_handler(state=ALLSTATE.django)
async def django_def(message:Message,state:FSMContext):
    if message.text=='Sariqdev':
        await message.answer(f"{message.text}",reply_markup=sariq_django)
        await ALLSTATE.django_sariq.set()

    if message.text=='⬆️Ortga':
        await message.answer(f"{message.text}",reply_markup=backend)
        await state.finish()


@dp.message_handler(state=ALLSTATE.django_sariq)
async def sariq_django_def(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgEAAxkBAAIdK2Jj18ulJmQWJ4AmSxvs-YPFbLBIAAJjAQACXYjYRQa0n0u5w8YmJAQ'
        await message.answer_video(file_id,caption='#01 Python Django _ Command Prompt.mp4 ')

    elif message.text=='2-dars':
        file_id = 'BAACAgEAAxkBAAIdLWJj1_-bocJpEP7z0NQZzaA2S8xEAAJkAQACXYjYRZX88Pq2OV1XJAQ'
        await message.answer_video(file_id,caption='#02 Python Django _ Python va PyCharm o\'rnatamiz.mp4')

    elif message.text=='3-dars':
        file_id = 'BAACAgEAAxkBAAIdL2Jj2EDsfyfyMrOY4nvfShO1_AasAAJlAQACXYjYRcACOBdTdOgYJAQ'
        await message.answer_video(file_id,caption='#03 Python Django _ pipenv va Django.mp4')

    elif message.text=='4-dars':
        file_id = 'BAACAgEAAxkBAAIdMWJj2GoHCcfW5rN8L51FJFWiHiQgAAJmAQACXYjYReG04WbWYz9OJAQ'
        await message.answer_video(file_id,caption='#04 Python Django _ Project va App.mp4')

    elif message.text=='5-dars':
        file_id = 'BAACAgEAAxkBAAIdM2Jj2K5OkIrqrPOwlLAymeWutozuAAJnAQACXYjYReVD3zXeSJu1JAQ'
        await message.answer_video(file_id,caption='#05 Python Django _ MVT Model-View-Template.mp4')

    elif message.text=='6-dars':
        file_id = 'BAACAgEAAxkBAAIdNWJj2NPcDQABhpTIyqhiStMj9ASbYgACaAEAAl2I2EVH5xnODWRItSQE'
        await message.answer_video(file_id,caption='#06 Python Django _ \'Hello, World!\'.mp4')

    elif message.text=='7-dars':
        file_id = 'BAACAgEAAxkBAAIdN2Jj2P0Csz8AAWyItSJXlzr5bFyVvQACaQEAAl2I2EXTia1P5HKRFyQE'
        await message.answer_video(file_id,caption='#07 Python Django _ Template yaratish.mp4')

    elif message.text=='8-dars':
        file_id = 'BAACAgEAAxkBAAIdOWJj2SBSwaGEulXW-qFJCn5PzSX-AAJqAQACXYjYRf5BpF19odqZJAQ'
        await message.answer_video(file_id,caption='#08 Python Django _ Tayanch Template.mp4')

    elif message.text=='9-dars':
        file_id = 'BAACAgEAAxkBAAIdO2Jj2UuwJEwYOTCXTpq6ticpRPFoAAJrAQACXYjYRXrYw9mcsHyUJAQ'
        await message.answer_video(file_id,caption='#09 Python Django _ Loyihani Heroku Serverga Yuklash.mp4')

    elif message.text=='10-dars':
        file_id = 'BAACAgEAAxkBAAIdPWJj2W8HMtt0anakUlxR_1IjBkQTAAJsAQACXYjYRWRCdH88X3wBJAQ'
        await message.answer_video(file_id,caption='#10 Python Django _ Birinchi Modelimiz.mp4')

    elif message.text=='11-dars':
        file_id = 'BAACAgEAAxkBAAIdP2Jj2b5i4EjDa76qRPZCemuwPsvSAAJtAQACXYjYRQRk9BoovWXCJAQ'
        await message.answer_video(file_id,caption='#11 Python Django _ Model-View-Template.mp4')

    elif message.text=='12-dars':
        file_id = 'BAACAgEAAxkBAAIdQWJj2dy_OVhNoaOI-Ttw3RRTVHBaAAJvAQACXYjYRU40O9KPZZlOJAQ'
        await message.answer_video(file_id,caption='#12 Python Django _ Blog yaratamiz. 1-qism.mp4')

    elif message.text=='13-dars':
        file_id = 'BAACAgEAAxkBAAIdQ2Jj2fhTw-iV6w93NbXyZlHEMw4HAAJwAQACXYjYRWfJdGJTcZmpJAQ'
        await message.answer_video(file_id,caption='#13 Python Django _ Blog yaratamiz. 2-qism.mp4')

    elif message.text=='14-dars':
        file_id = 'BAACAgEAAxkBAAIdRWJj2hRm4GYpfIcNDPMllnXVEnhzAAJxAQACXYjYRdzj953lezhuJAQ'
        await message.answer_video(file_id,caption='#14 Python Django _ Blog yaratamiz. 3-qism.mp4')

    elif message.text=='15-dars':
        file_id = 'BAACAgEAAxkBAAIdR2Jj2jfbJiA6hnPZHHXuiZ1w0AMsAAJyAQACXYjYRXCQPdhrpQvJJAQ'
        await message.answer_video(file_id,caption='#15 Python Django _ Blog yaratamiz. 4-qism.mp4')

    elif message.text=='16-dars':
        file_id = 'BAACAgEAAxkBAAIdSWJj2mTCySgBDgzVlxb6Nir4ZF4CAAJzAQACXYjYRXAMwrzPHnSoJAQ'
        await message.answer_video(file_id,caption='#16 Python Django _ Blog2.0. 1-qism - Kirish.mp4')

    elif message.text=='17-dars':
        file_id = 'BAACAgEAAxkBAAIdS2Jj2ojXBT3hJWoj_I0t1Z6on5xmAAJ0AQACXYjYRc7SzSpJCaA2JAQ'
        await message.answer_video(file_id,caption='#17 Python Django _ Blog2.0. 2-qism. Custom User Model..mp4')

    elif message.text=='18-dars':
        file_id = 'BAACAgEAAxkBAAIdTWJj2qY2Jdfpz6jLLy6_atrSLiDZAAJ1AQACXYjYRQWAK7xFar9VJAQ'
        await message.answer_video(file_id,caption='#18 Python Django _ Blog2.0. 3-qism. Foydalanuvchilar bilan ishlash.mp4')

    elif message.text=='19-dars':
        file_id = 'BAACAgEAAxkBAAIdT2Jj2sTVFYGARGzuVVQmP3ad91tMAAJ2AQACXYjYRWTmBBYDXWWSJAQ'
        await message.answer_video(file_id,caption='#19 Python Django _ Blog2.0. 4-qism. Bootstrap.mp4')

    elif message.text=='20-dars':
        file_id = 'BAACAgEAAxkBAAIdUWJj2uZML20YHfy2eWICyyNvIbjQAAJ4AQACXYjYRSmjR9RPzRHQJAQ'
        await message.answer_video(file_id,caption='#20 Python Django _ Blog2.0. 5-qism. Password reset.mp4')

    elif message.text=='21-dars':
        file_id = 'BAACAgEAAxkBAAIdU2Jj2y9HYbdW7giEWZfKZQtl0jykAAJ5AQACXYjYRaaumzJMqMo5JAQ'
        await message.answer_video(file_id,caption='#21 Python Django _ Blog2.0. 6-qism. Postlar qo\'shish.mp4')

    elif message.text=='22-dars':
        file_id = 'BAACAgEAAxkBAAIdVWJj224v4PwKFWjxhAJh_OiRhBZ3AAJ6AQACXYjYRbA5Ti5gV0wOJAQ'
        await message.answer_video(file_id,caption='#22 Python Django _ Blog2.0. 7-qism. Avtorizasiya.mp4')

    elif message.text=='23-dars':
        file_id = 'BAACAgEAAxkBAAIdV2Jj243wFmc7aN6dCTT1HJJJ9vrKAAJ7AQACXYjYRfbNEw8obUSiJAQ'
        await message.answer_video(file_id,caption='#23 Python Django _ Blog2.0. 8-qism. Matn Muharriri.mp4')

    elif message.text=='24-dars':
        file_id = 'BAACAgEAAxkBAAIdWWJj26jCyOmp4d7x6HjC9NVMKIpUAAJ8AQACXYjYRfGOz_TX5XEqJAQ'
        await message.answer_video(file_id,caption='#24 Python Django _ Blog2.0. 9-qism. Izohlar.mp4')

    elif message.text=='25-dars':
        file_id = 'BAACAgEAAxkBAAIdW2Jj28TD4v2eAVI3JkkKq7Q8q69pAAJ9AQACXYjYRebSA1_jODCCJAQ'
        await message.answer_video(file_id,caption='#25 Python Django _ Blog2.0. 10-qism. Deploy.mp4')

    elif message.text=='⬆️Ortga':
        await message.answer(f"{message.text}",reply_markup=django)
        await ALLSTATE.python.set()


@dp.message_handler(Text('Telegram Bot'))
async def python_def(message:Message,state:FSMContext):
    await message.answer(f"{message.text}",reply_markup=telegram_bot)
    await ALLSTATE.bot_telegram.set()

@dp.message_handler(state=ALLSTATE.bot_telegram)
async def def_bot(message:Message,state:FSMContext):

    if message.text=='1-dars':
        file_id = 'BAACAgEAAxkBAAIdjWJj3hBJCaPK9saYr3K_R-_DzCjbAAJdAgACwGYxRjL8CywcpEBRJAQ'
        await message.answer_video(file_id,caption='#01 MUKAMMAL TELEGRAM BOT _ KERAKLI DASTURLAR.mp4')

    elif message.text=='2-dars':
        file_id = 'BAACAgEAAxkBAAIdkGJj3qBNBNOkskcaVeQORTqfzEM0AAJeAgACwGYxRgEXodZFZ5z5JAQ'
        await message.answer_video(file_id,caption='#02 MUKAMMAL TELEGRAM BOT _ METODOLOGIYA.mp4')

    elif message.text=='3-dars':
        file_id = 'BAACAgEAAxkBAAIdkmJj3rxvG3RAyj2zo1Z78mPOjp1GAAJfAgACwGYxRi7QigWlHxtmJAQ'
        await message.answer_video(file_id,caption='#03 MUKAMMAL TELEGRAM BOT _ botFather.mp4')

    elif message.text=='4-dars':
        file_id = 'BAACAgEAAxkBAAIdlGJj3tbbUmIC5fO2cewMrwkyuTwqAAJtAgACwGYxRjUsFT-FVpusJAQ'
        await message.answer_video(file_id,caption='#04 MUKAMMAL TELEGRAM BOT _ aiogram.mp4')

    elif message.text=='5-dars':
        file_id = 'BAACAgEAAxkBAAIdmWJj3wsakn02qaJLNI3OhJG4ynr4AAJgAgACwGYxRnP4Oo1Wx3w8JAQ'
        await message.answer_video(file_id,caption='#05 MUKAMMAL TELEGRAM BOT _ wikibot.mp4')

    elif message.text=='6-dars':
        file_id = 'BAACAgEAAxkBAAIdm2Jj3zo2l4yu6wPYKk6b55ecDAaeAAJhAgACwGYxRrRxRazztChGJAQ'
        await message.answer_video(file_id,caption='#06 MUKAMMAL TELEGRAM BOT _ API nima.mp4')

    elif message.text=='7-dars':
        file_id = 'BAACAgEAAxkBAAIdnWJj32YfY32TQw0kYRD6UAv3Wu_UAAJiAgACwGYxRjopGEncZHH2JAQ'
        await message.answer_video(file_id,caption='#07 MUKAMMAL TELEGRAM BOT _ Bot uchun qiziqarli API topamiz.mp4')

    elif message.text=='8-dars':
        file_id = 'BAACAgEAAxkBAAIdn2Jj34LmJm1M3Wt1j8EcWTfVgD-pAAJjAgACwGYxRmmRe6hI9I2KJAQ'
        await message.answer_video(file_id,caption='#08 MUKAMMAL TELEGRAM BOT _ Pythonda API bilan ishlash.mp4')

    elif message.text=='9-dars':
        file_id = 'BAACAgEAAxkBAAIdoWJj35mAK0o43ql8CwM9uS6NksGGAAJkAgACwGYxRlrjUbDOgH5eJAQ'
        await message.answer_video(file_id,caption='#09 MUKAMMAL TELEGRAM BOT _ speakEnglish bot.mp4')

    elif message.text=='10-dars':
        file_id = 'BAACAgEAAxkBAAIdo2Jj37Wv6Zz_LNEv2ZzB7sWDzLxMAAJlAgACwGYxRhUVfl6US3t9JAQ'
        await message.answer_video(file_id,caption='#10 MUKAMMAL TELEGRAM BOT _ imloBot. 1-qism - So\'zlarni tekshirish.mp4')

    elif message.text=='11-dars':
        file_id = 'BAACAgEAAxkBAAIdpWJj39UcwzDEpBMXYlTuJabimXGKAAJmAgACwGYxRlfJ0sjd0F8CJAQ'
        await message.answer_video(file_id,caption='#11 MUKAMMAL TELEGRAM BOT _ imloBot. 2-qism - Bot dasturi.mp4')

    elif message.text=='12-dars':
        file_id = 'BAACAgEAAxkBAAIdp2Jj4AtPCh6YrxCRS4_8vyg2YsULAAJnAgACwGYxRjdeDlYGDExJJAQ'
        await message.answer_video(file_id,caption='#12 MUKAMMAL TELEGRAM BOT _ Botni serverga yuklash.mp4')

    elif message.text=='13-dars':
        file_id = 'BAACAgEAAxkBAAIdqWJj4DcdwUnDM3JthumsTvo0YUpOAAJoAgACwGYxRiyqscXXff51JAQ'
        await message.answer_video(file_id,caption='#13 MUKAMMAL TELEGRAM BOT _ DIQQAT, AKSIYA!.mp4')

    elif message.text=='Kurs bilan tanishuv':
        file = 'BAACAgEAAxkBAAIlYmJlEnbLO6vqhyp-e6AEvyQixfyIAAJcAgACwGYxRslhGyuo7lVRJAQ'
        await message.answer_video(file,caption='#00 MUKAMMAL TELEGRAM BOT _ KURS BILAN TANISHUV.mp4')

    elif message.text=='⬆️Ortga':
        await message.answer(f"{message.text}",reply_markup=backend)
        await state.finish()


############