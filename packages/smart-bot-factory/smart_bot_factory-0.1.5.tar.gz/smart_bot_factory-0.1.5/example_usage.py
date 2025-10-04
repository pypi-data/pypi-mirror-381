#!/usr/bin/env python3
"""
Пример использования простого импорта компонентов бота
"""

from smart_bot_factory.core import global_handler
from smart_bot_factory.clients import supabase_client, openai_client

# Теперь можно просто использовать импортированные переменные
async def example_function():
    """Пример функции с использованием импортированных компонентов"""
    
    # Проверяем доступность
    if not supabase_client:
        print("Supabase клиент не доступен")
        return
    
    if not openai_client:
        print("OpenAI клиент не доступен")
        return
    
    # Используем напрямую - теперь автозаполнение работает!
    try:
        # Получаем пользователей из БД с учетом bot_id
        # IDE теперь знает тип supabase_client и предлагает методы
        users = supabase_client.client.table('sales_users').select('*').eq('bot_id', supabase_client.bot_id).execute()
        print(f"Найдено пользователей: {len(users.data)}")
        
        # Пример использования OpenAI клиента
        # IDE знает тип openai_client и предлагает методы
        print("OpenAI клиент доступен для использования")
        
    except Exception as e:
        print(f"Ошибка: {e}")

# Пример глобального обработчика с простым импортом
@global_handler("example_notification")
async def send_example_notification(message_text: str):
    """Пример глобального обработчика с простым импортом"""
    
    # Просто используем импортированный supabase_client
    if not supabase_client:
        return {"status": "error", "message": "Supabase клиент не найден"}
    
    try:
        # Получаем всех пользователей с учетом bot_id
        users_response = supabase_client.client.table('sales_users').select('telegram_id').eq('bot_id', supabase_client.bot_id).execute()
        
        if not users_response.data:
            return {"status": "no_users", "message": "Пользователи не найдены"}
        
        # Отправляем сообщения (пример)
        sent_count = 0
        for user in users_response.data:
            # Здесь была бы отправка сообщения
            sent_count += 1
        
        return {
            "status": "completed",
            "sent_count": sent_count,
            "message": f"Отправлено {sent_count} сообщений"
        }
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import asyncio
    asyncio.run(example_function())
