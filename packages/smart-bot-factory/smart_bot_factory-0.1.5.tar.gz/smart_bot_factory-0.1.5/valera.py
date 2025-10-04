#!/usr/bin/env python3
"""
Бот valera - создан с помощью Smart Bot Factory
"""

import asyncio

from smart_bot_factory.core import Router
from smart_bot_factory.core import send_message_by_human
from smart_bot_factory.clients import supabase_client
from smart_bot_factory.creation import BotBuilder

# Создаем роутер для всех обработчиков
router = Router("valera_handlers")

# =============================================================================
# ОБРАБОТЧИКИ СОБЫТИЙ
# =============================================================================

@router.event_handler("example_event")
async def handle_example_event(user_id: int, event_data: str):
    """Пример обработчика события"""
    # Отправляем подтверждение пользователю
    await send_message_by_human(
        user_id=user_id,
        message_text=f"✅ Событие обработано! Данные: {event_data}"
    )
    
    return {
        "status": "success",
        "message": "Событие обработано"
    }

# =============================================================================
# ВРЕМЕННЫЕ ЗАДАЧИ ДЛЯ ОДНОГО ПОЛЬЗОВАТЕЛЯ
# =============================================================================

@router.schedule_task("send_reminder")
async def send_user_reminder(user_id: int, reminder_text: str):
    """Отправляет напоминание пользователю"""
    await send_message_by_human(
        user_id=user_id,
        message_text=f"🔔 Напоминание: {reminder_text}"
    )
    
    return {
        "status": "reminder_sent",
        "message": f"Напоминание отправлено пользователю {user_id}"
    }

# =============================================================================
# ГЛОБАЛЬНЫЕ ОБРАБОТЧИКИ (для всех пользователей)
# =============================================================================

@router.global_handler("mass_notification", notify=True)
async def send_global_announcement(announcement_text: str):
    """Отправляет анонс всем пользователям бота"""
    import logging
    logger = logging.getLogger(__name__)
    
    logger.info(f"🚀 Начинаем глобальную рассылку: '{announcement_text[:50]}...'")
    
    # Проверяем доступность клиента
    if not supabase_client:
        logger.error("❌ Supabase клиент не найден для глобальной рассылки")
        return {"status": "error", "message": "Supabase клиент не найден"}
    
    try:
        # Получаем всех пользователей из БД с учетом bot_id (изоляция данных)
        users_response = supabase_client.client.table('sales_users').select(
            'telegram_id'
        ).eq('bot_id', supabase_client.bot_id).execute()
        
        if not users_response.data:
            logger.warning("⚠️ Пользователи не найдены для глобальной рассылки")
            return {"status": "no_users", "message": "Пользователи не найдены"}
        
        total_users = len(users_response.data)
        logger.info(f"👥 Найдено {total_users} пользователей для рассылки")
        
        # Отправляем сообщение каждому пользователю
        sent_count = 0
        failed_count = 0
        
        for user in users_response.data:
            try:
                await send_message_by_human(
                    user_id=user['telegram_id'],
                    message_text=f"📢 {announcement_text}"
                )
                sent_count += 1
                # Небольшая задержка между отправками
                await asyncio.sleep(0.1)
                
            except Exception as e:
                logger.error(f"❌ Ошибка отправки пользователю {user['telegram_id']}: {e}")
                failed_count += 1
        
        return {
            "status": "completed",
            "sent_count": sent_count,
            "failed_count": failed_count,
            "total_users": total_users,
            "message": f"Рассылка завершена: {sent_count} отправлено, {failed_count} ошибок"
        }
        
    except Exception as e:
        logger.error(f"❌ Критическая ошибка глобальной рассылки: {e}")
        return {"status": "error", "message": str(e)}

# =============================================================================
# ОСНОВНАЯ ФУНКЦИЯ
# =============================================================================

async def main():
    """Основная функция запуска бота"""
    try:
        # Создаем и собираем бота
        bot_builder = BotBuilder("valera")
        
        # Регистрируем роутер ПЕРЕД сборкой, чтобы обработчики были доступны
        bot_builder.register_router(router)
        
        await bot_builder.build()
        
        # Запускаем бота
        await bot_builder.start()
        
    except Exception as e:
        print(f"❌ Ошибка запуска бота: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
