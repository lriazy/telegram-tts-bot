PROJECT_ID = "[your-project-id]"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}


import vertexai
from vertexai.generative_models import GenerativeModel

from google.cloud import aiplatform
from google.cloud import secretmanager

client = secretmanager.SecretManagerServiceClient()
telegram_token = {
    client.access_secret_version("name" = "TELEGRAM_TOKEN")
    ["payload"]["data"]
    .decode("UTF-8") }


vertexai.init(project=PROJECT_ID, location=LOCATION)
aiplatform.init(location=LOCATION)
context = ""
question = """Bitte erstelle einen flüssigen und vorlesbaren Text aus den folgenden Notizen. 
Alle Abkürzungen sollen ausgeschrieben werden, damit sie korrekt vorgelesen werden können. 
Es soll ein fließender Text sein. Entferne alle Symbole, wie # oder -. Nutze insgesamt eher kurze Sätze, um den Text gut verständlich zu machen.

"""

# Ask the foundational model.
model = GenerativeModel(
    model_name="gemini-1.0-pro-002",
    system_instruction=context,
)
answer = model.generate_content(question).text

print("QUESTION:")
print(question)
print()
print("ANSWER:")
print(answer)

from distutils.command.config import config
from logging import disable
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config

bot = Bot(token=config.TOKEN) #Ваш токен 
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_answer(message: types.Message):
    await message.answer("👋 <b>-hallooo</b> @" + message.from_user.username + "<b>.</b>\n✏️ <b>Ich bin ein Bot.</b> \n🦜", parse_mode="HTML")
    


@dp.message_handler(commands=['help'])
async def cmd_answer(message: types.Message):
    await message.answer("⁉️", disable_web_page_preview=True, parse_mode="HTML")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(chat_id=msg.from_user.id, text=f"<b>{msg.text}</b>", parse_mode="HTML")


if __name__ == '__main__':
    executor.start_polling(dp)
