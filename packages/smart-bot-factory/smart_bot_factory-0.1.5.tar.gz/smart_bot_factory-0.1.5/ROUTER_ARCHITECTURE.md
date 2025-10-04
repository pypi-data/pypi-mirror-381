# 🚀 Архитектура с роутерами Smart Bot Factory

Новая архитектура с роутерами позволяет организовать код по модулям, как в aiogram.

## 📁 Структура

```
routers/
├── notifications.py      # Глобальные уведомления
├── scheduled_tasks.py    # Запланированные задачи
├── events.py            # Обработчики событий
└── custom_router.py     # Ваши кастомные роутеры

valera_with_routers.py   # Главный файл бота
```

## 🔧 Создание роутера

```python
from smart_bot_factory.core import Router

# Создаем роутер
my_router = Router("my_router")

@my_router.event_handler("custom_event")
async def handle_custom_event(user_id: int, event_data: str):
    """Обработчик кастомного события"""
    return {"status": "success"}

@my_router.schedule_task("custom_task", notify=True)
async def custom_scheduled_task(user_id: int, task_data: str):
    """Запланированная задача"""
    return {"status": "completed"}

@my_router.global_handler("custom_global")
async def custom_global_handler(data: str):
    """Глобальный обработчик"""
    return {"status": "sent"}
```

## 🎯 Использование в боте

```python
#!/usr/bin/env python3
from smart_bot_factory.creation import BotBuilder

# Импортируем роутеры
from routers.notifications import notifications_router
from routers.scheduled_tasks import scheduled_tasks_router
from routers.events import events_router

async def main():
    # Создаем и собираем бота
    bot_builder = BotBuilder("my_bot")
    await bot_builder.build()
    
    # Регистрируем роутеры
    bot_builder.register_router(notifications_router)
    bot_builder.register_router(scheduled_tasks_router)
    bot_builder.register_router(events_router)
    
    # Запускаем бота
    await bot_builder.start()

if __name__ == "__main__":
    asyncio.run(main())
```

## 📊 Преимущества

### ✅ **Модульность**
- Код разделен по функциональности
- Легко добавлять новые роутеры
- Простое тестирование отдельных модулей

### ✅ **Организация**
- Уведомления в `notifications.py`
- Задачи в `scheduled_tasks.py`
- События в `events.py`

### ✅ **Переиспользование**
- Роутеры можно использовать в разных ботах
- Легко копировать и модифицировать

### ✅ **Конфликты**
- Автоматическое обнаружение конфликтов имен
- Предупреждения о дублировании обработчиков

## 🔄 Обратная совместимость

Старый код продолжает работать! Можно использовать:

```python
# Старый способ (все еще работает)
from smart_bot_factory.core import event_handler, schedule_task, global_handler

@event_handler("old_event")
async def old_handler(user_id: int, data: str):
    return {"status": "success"}

# Новый способ (рекомендуется)
from smart_bot_factory.core import Router
my_router = Router("my_router")

@my_router.event_handler("new_event")
async def new_handler(user_id: int, data: str):
    return {"status": "success"}
```

## 📈 Статистика

```python
# Получить статистику роутеров
router_manager = bot_builder.get_router_manager()
stats = router_manager.get_router_stats()

print(f"Всего роутеров: {stats['total_routers']}")
for router_stat in stats['routers']:
    print(f"Роутер {router_stat['name']}:")
    print(f"  - События: {router_stat['event_handlers']}")
    print(f"  - Задачи: {router_stat['scheduled_tasks']}")
    print(f"  - Глобальные: {router_stat['global_handlers']}")
```

## 🎉 Готовые роутеры

### **notifications.py**
- `mass_notification` - массовая рассылка
- `targeted_notification` - целевая рассылка
- `emergency_notification` - экстренные уведомления

### **scheduled_tasks.py**
- `send_reminder` - напоминания
- `follow_up` - последующие сообщения
- `appointment_reminder` - напоминания о встречах
- `offer_reminder` - напоминания о предложениях

### **events.py**
- `имя` - пример обработчика
- `appointment_booking` - запись на прием
- `phone_collection` - сбор телефона
- `payment_confirmation` - подтверждение платежа

## 🚀 Быстрый старт

1. **Скопируйте роутеры** в папку `routers/`
2. **Используйте** `valera_with_routers.py` как пример
3. **Добавьте свои роутеры** по необходимости
4. **Зарегистрируйте** роутеры в `BotBuilder`

Теперь ваш код организован, модулен и легко расширяем! 🎉
