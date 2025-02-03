from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Формат логов
    filename='bot.log',  # Имя файла для записи логов
    filemode='a'  # Режим записи ('a' — добавление, 'w' — перезапись)
)
logger = logging.getLogger(__name__)

# Токен вашего бота
TOKEN = ''

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я бот, который может показать текущее время. Напиши "день".')

# Функция для обработки сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    if text == 'день':
        now = datetime.now()
        date_time = now.strftime("%H:%M:%S, %d.%m.%Y, %A")
        await update.message.reply_text(f'Текущее время и дата: {date_time}')
    else:
        await update.message.reply_text('Я не понимаю эту команду. Напиши "день".')

# Основная функция
def main() -> None:
    # Создаем Application и передаем ему токен вашего бота
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
