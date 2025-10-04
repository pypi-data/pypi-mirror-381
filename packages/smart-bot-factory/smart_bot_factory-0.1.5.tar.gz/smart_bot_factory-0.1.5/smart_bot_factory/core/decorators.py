"""
Декораторы для обработчиков событий и временных задач
"""

import asyncio
import logging
from typing import Callable, Any, Dict
from datetime import datetime, timedelta, timezone
from functools import wraps

logger = logging.getLogger(__name__)

# Глобальный реестр обработчиков событий
_event_handlers: Dict[str, Callable] = {}
_scheduled_tasks: Dict[str, Dict[str, Any]] = {}
_global_handlers: Dict[str, Dict[str, Any]] = {}

# Глобальный менеджер роутеров
_router_manager = None

def event_handler(event_type: str, notify: bool = False, once_only: bool = True):
    """
    Декоратор для регистрации обработчика события
    
    Args:
        event_type: Тип события (например, 'appointment_booking', 'phone_collection')
        notify: Уведомлять ли админов о выполнении события (по умолчанию False)
        once_only: Обрабатывать ли событие только один раз (по умолчанию True)
    
    Example:
        # Обработчик только один раз (по умолчанию)
        @event_handler("appointment_booking", notify=True)
        async def book_appointment(user_id: int, appointment_data: dict):
            # Логика записи на прием
            return {"status": "success", "appointment_id": "123"}
        
        # Обработчик может выполняться многократно
        @event_handler("phone_collection", once_only=False)
        async def collect_phone(user_id: int, phone_data: dict):
            # Логика сбора телефона
            return {"status": "phone_collected"}
    """
    def decorator(func: Callable) -> Callable:
        _event_handlers[event_type] = {
            'handler': func,
            'name': func.__name__,
            'notify': notify,
            'once_only': once_only
        }
        
        logger.info(f"📝 Зарегистрирован обработчик события '{event_type}': {func.__name__}")
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                logger.info(f"🔧 Выполняем обработчик события '{event_type}'")
                result = await func(*args, **kwargs)
                logger.info(f"✅ Обработчик '{event_type}' выполнен успешно")
                
                # Автоматически добавляем флаг notify к результату
                if isinstance(result, dict):
                    result['notify'] = notify
                else:
                    # Если результат не словарь, создаем словарь
                    result = {
                        'status': 'success',
                        'result': result,
                        'notify': notify
                    }
                
                return result
            except Exception as e:
                logger.error(f"❌ Ошибка в обработчике '{event_type}': {e}")
                raise
        
        return wrapper
    return decorator

def schedule_task(task_name: str, notify: bool = False, smart_check: bool = True, once_only: bool = True):
    """
    Декоратор для регистрации задачи, которую можно запланировать на время
    
    Args:
        task_name: Название задачи (например, 'send_reminder', 'follow_up')
        notify: Уведомлять ли админов о выполнении задачи (по умолчанию False)
        smart_check: Использовать ли умную проверку активности пользователя (по умолчанию True)
        once_only: Выполнять ли задачу только один раз (по умолчанию True)
    
    Example:
        # С умной проверкой (по умолчанию)
        @schedule_task("send_reminder", notify=False)
        async def send_reminder(user_id: int, user_data: str):
            # user_data содержит текст напоминания от ИИ
            # Логика отправки напоминания (выполняется на фоне)
            return {"status": "sent", "message": user_data}
        
        # Без умной проверки (всегда выполняется по времени)
        @schedule_task("system_notification", smart_check=False)
        async def system_notification(user_id: int, user_data: str):
            # Выполняется точно по времени, без проверки активности
            return {"status": "sent", "message": user_data}
        
        # Задача может выполняться многократно
        @schedule_task("recurring_reminder", once_only=False)
        async def recurring_reminder(user_id: int, user_data: str):
            # Может запускаться несколько раз
            return {"status": "sent", "message": user_data}
        
        # ИИ может отправлять события в форматах:
        # {"тип": "send_reminder", "инфо": "3600"} - просто время
        # {"тип": "send_reminder", "инфо": "3600|Не забудьте про встречу!"} - время + текст
    """
    def decorator(func: Callable) -> Callable:
        _scheduled_tasks[task_name] = {
            'handler': func,
            'name': func.__name__,
            'notify': notify,
            'smart_check': smart_check,
            'once_only': once_only
        }
        
        logger.info(f"⏰ Зарегистрирована задача '{task_name}': {func.__name__}")
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                logger.info(f"⏰ Выполняем запланированную задачу '{task_name}'")
                result = await func(*args, **kwargs)
                logger.info(f"✅ Задача '{task_name}' выполнена успешно")
                
                # Автоматически добавляем флаг notify к результату
                if isinstance(result, dict):
                    result['notify'] = notify
                else:
                    # Если результат не словарь, создаем словарь
                    result = {
                        'status': 'success',
                        'result': result,
                        'notify': notify
                    }
                
                return result
            except Exception as e:
                logger.error(f"❌ Ошибка в задаче '{task_name}': {e}")
                raise
        
        return wrapper
    return decorator

def global_handler(handler_type: str, notify: bool = False, once_only: bool = True):
    """
    Декоратор для регистрации глобального обработчика (для всех пользователей)
    
    Args:
        handler_type: Тип глобального обработчика (например, 'global_announcement', 'mass_notification')
        notify: Уведомлять ли админов о выполнении (по умолчанию False)
        once_only: Выполнять ли обработчик только один раз (по умолчанию True)
    
    Example:
        # Глобальный обработчик только один раз (по умолчанию)
        @global_handler("global_announcement", notify=True)
        async def send_global_announcement(announcement_text: str):
            # Логика отправки анонса всем пользователям
            return {"status": "sent", "recipients_count": 150}
        
        # Глобальный обработчик может выполняться многократно
        @global_handler("daily_report", once_only=False)
        async def send_daily_report(report_data: str):
            # Может запускаться каждый день
            return {"status": "sent", "report_type": "daily"}
    """
    def decorator(func: Callable) -> Callable:
        _global_handlers[handler_type] = {
            'handler': func,
            'name': func.__name__,
            'notify': notify,
            'once_only': once_only
        }
        
        logger.info(f"🌍 Зарегистрирован глобальный обработчик '{handler_type}': {func.__name__}")
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                logger.info(f"🌍 Выполняем глобальный обработчик '{handler_type}'")
                result = await func(*args, **kwargs)
                logger.info(f"✅ Глобальный обработчик '{handler_type}' выполнен успешно")
                
                # Автоматически добавляем флаг notify к результату
                if isinstance(result, dict):
                    result['notify'] = notify
                else:
                    # Если результат не словарь, создаем словарь
                    result = {
                        'status': 'success',
                        'result': result,
                        'notify': notify
                    }
                
                return result
            except Exception as e:
                logger.error(f"❌ Ошибка в глобальном обработчике '{handler_type}': {e}")
                raise
        
        return wrapper
    return decorator

def get_event_handlers() -> Dict[str, Dict[str, Any]]:
    """Возвращает все зарегистрированные обработчики событий"""
    return _event_handlers.copy()

def get_scheduled_tasks() -> Dict[str, Dict[str, Any]]:
    """Возвращает все зарегистрированные задачи"""
    return _scheduled_tasks.copy()

def get_global_handlers() -> Dict[str, Dict[str, Any]]:
    """Возвращает все зарегистрированные глобальные обработчики"""
    return _global_handlers.copy()

def set_router_manager(router_manager):
    """Устанавливает глобальный менеджер роутеров"""
    global _router_manager
    _router_manager = router_manager
    logger.info("🔄 RouterManager установлен в decorators")

def get_router_manager():
    """Получает глобальный менеджер роутеров"""
    return _router_manager

def get_handlers_for_prompt() -> str:
    """
    Возвращает описание всех обработчиков для добавления в промпт
    """
    # Сначала пробуем получить из роутеров
    if _router_manager:
        return _router_manager.get_handlers_for_prompt()
    
    # Fallback к старым декораторам
    if not _event_handlers and not _scheduled_tasks and not _global_handlers:
        return ""
    
    prompt_parts = []
    
    if _event_handlers:
        prompt_parts.append("ДОСТУПНЫЕ ОБРАБОТЧИКИ СОБЫТИЙ:")
        for event_type, handler_info in _event_handlers.items():
            prompt_parts.append(f"- {event_type}: {handler_info['name']}")
    
    if _scheduled_tasks:
        prompt_parts.append("\nДОСТУПНЫЕ ЗАДАЧИ ДЛЯ ПЛАНИРОВАНИЯ:")
        for task_name, task_info in _scheduled_tasks.items():
            prompt_parts.append(f"- {task_name}: {task_info['name']}")
    
    if _global_handlers:
        prompt_parts.append("\nДОСТУПНЫЕ ГЛОБАЛЬНЫЕ ОБРАБОТЧИКИ:")
        for handler_type, handler_info in _global_handlers.items():
            prompt_parts.append(f"- {handler_type}: {handler_info['name']}")
    
    return "\n".join(prompt_parts)

async def execute_event_handler(event_type: str, *args, **kwargs) -> Any:
    """Выполняет обработчик события по типу"""
    # Сначала пробуем получить из роутеров
    if _router_manager:
        event_handlers = _router_manager.get_event_handlers()
        if event_type in event_handlers:
            handler_info = event_handlers[event_type]
            return await handler_info['handler'](*args, **kwargs)
    
    # Fallback к старым декораторам
    if event_type not in _event_handlers:
        raise ValueError(f"Обработчик события '{event_type}' не найден")
    
    handler_info = _event_handlers[event_type]
    return await handler_info['handler'](*args, **kwargs)

async def execute_scheduled_task(task_name: str, user_id: int, user_data: str) -> Any:
    """Выполняет запланированную задачу по имени"""
    # Сначала пробуем получить из роутеров
    if _router_manager:
        scheduled_tasks = _router_manager.get_scheduled_tasks()
        if task_name in scheduled_tasks:
            task_info = scheduled_tasks[task_name]
            return await task_info['handler'](user_id, user_data)
    
    # Fallback к старым декораторам
    if task_name not in _scheduled_tasks:
        raise ValueError(f"Задача '{task_name}' не найдена")
    
    task_info = _scheduled_tasks[task_name]
    return await task_info['handler'](user_id, user_data)

async def execute_global_handler(handler_type: str, *args, **kwargs) -> Any:
    """Выполняет глобальный обработчик по типу"""
    # Сначала пробуем получить из роутеров
    if _router_manager:
        global_handlers = _router_manager.get_global_handlers()
        if handler_type in global_handlers:
            handler_info = global_handlers[handler_type]
            return await handler_info['handler'](*args, **kwargs)
    
    # Fallback к старым декораторам
    if handler_type not in _global_handlers:
        raise ValueError(f"Глобальный обработчик '{handler_type}' не найден")
    
    handler_info = _global_handlers[handler_type]
    return await handler_info['handler'](*args, **kwargs)

async def schedule_task_for_later(task_name: str, delay_seconds: int, user_id: int, user_data: str):
    """
    Планирует выполнение задачи через указанное время
    
    Args:
        task_name: Название задачи
        delay_seconds: Задержка в секундах
        user_id: ID пользователя
        user_data: Простой текст для задачи
    """
    if task_name not in _scheduled_tasks:
        raise ValueError(f"Задача '{task_name}' не найдена")
    
    logger.info(f"⏰ Планируем задачу '{task_name}' через {delay_seconds} секунд")
    
    async def delayed_task():
        await asyncio.sleep(delay_seconds)
        await execute_scheduled_task(task_name, user_id, user_data)
    
    # Запускаем задачу в фоне
    asyncio.create_task(delayed_task())
    
    return {
        "status": "scheduled",
        "task_name": task_name,
        "delay_seconds": delay_seconds,
        "scheduled_at": datetime.now().isoformat()
    }

async def execute_scheduled_task_from_event(user_id: int, task_name: str, event_info: str):
    """
    Выполняет запланированную задачу на основе события от ИИ
    
    Args:
        user_id: ID пользователя
        task_name: Название задачи
        event_info: Информация от ИИ (простой текст)
    """
    if task_name not in _scheduled_tasks:
        raise ValueError(f"Задача '{task_name}' не найдена")
    
    try:
        # ИИ может присылать время в двух форматах:
        # 1. Просто время: "3600" 
        # 2. Время с данными: "3600|Текст напоминания"
        
        if '|' in event_info:
            # Формат с дополнительными данными
            delay_seconds_str, user_data = event_info.split('|', 1)
            delay_seconds = int(delay_seconds_str.strip())
            user_data = user_data.strip()
        else:
            # Просто время
            delay_seconds = int(event_info)
            user_data = f"Напоминание через {delay_seconds} секунд"
        
        # Планируем задачу на фоне с сохранением в БД
        result = await schedule_task_for_later_with_db(task_name, user_id, user_data, delay_seconds)
        
        return result
        
    except ValueError as e:
        logger.error(f"Ошибка парсинга времени из event_info '{event_info}': {e}")
        # Fallback - планируем через 1 час с сохранением в БД
        return await schedule_task_for_later_with_db(task_name, user_id, "Напоминание через 1 час (fallback)", 3600)

async def schedule_global_handler_for_later(handler_type: str, delay_seconds: int, handler_data: str):
    """
    Планирует выполнение глобального обработчика через указанное время
    
    Args:
        handler_type: Тип глобального обработчика
        delay_seconds: Задержка в секундах
        handler_data: Данные для обработчика (время в секундах как строка)
    """
    if handler_type not in _global_handlers:
        raise ValueError(f"Глобальный обработчик '{handler_type}' не найден")
    
    logger.info(f"🌍 Планируем глобальный обработчик '{handler_type}' через {delay_seconds} секунд")
    
    async def delayed_global_handler():
        await asyncio.sleep(delay_seconds)
        # Передаем данные обработчику (может быть текст анонса или другие данные)
        await execute_global_handler(handler_type, handler_data)
    
    # Запускаем задачу в фоне
    asyncio.create_task(delayed_global_handler())
    
    return {
        "status": "scheduled",
        "handler_type": handler_type,
        "delay_seconds": delay_seconds,
        "scheduled_at": datetime.now().isoformat()
    }

async def execute_global_handler_from_event(handler_type: str, event_info: str):
    """
    Выполняет глобальный обработчик на основе события от ИИ
    
    Args:
        handler_type: Тип глобального обработчика
        event_info: Информация от ИИ (содержит данные для обработчика и время)
    """
    if handler_type not in _global_handlers:
        raise ValueError(f"Глобальный обработчик '{handler_type}' не найден")
    
    try:
        # ИИ присылает время в секундах, парсим его
        delay_seconds = int(event_info)
        
        # Планируем на будущее с сохранением в БД
        result = await schedule_global_handler_for_later_with_db(handler_type, delay_seconds, event_info)
        return result
        
    except ValueError as e:
        logger.error(f"Ошибка парсинга времени для глобального обработчика '{handler_type}': {e}")
        # Fallback - планируем через 1 час с сохранением в БД
        return await schedule_global_handler_for_later_with_db(handler_type, 3600, event_info)


# =============================================================================
# ФУНКЦИИ ДЛЯ РАБОТЫ С БД СОБЫТИЙ
# =============================================================================

def get_supabase_client():
    """Получает клиент Supabase из глобальных переменных"""
    import sys
    current_module = sys.modules[__name__]
    supabase_client = getattr(current_module, 'supabase_client', None)
    
    # Если не найден в decorators, пробуем получить из bot_utils
    if not supabase_client:
        try:
            bot_utils_module = sys.modules.get('smart_bot_factory.core.bot_utils')
            if bot_utils_module:
                supabase_client = getattr(bot_utils_module, 'supabase_client', None)
        except:
            pass
    
    return supabase_client

async def save_immediate_event(
    event_type: str,
    user_id: int,
    event_data: str,
    session_id: str = None
) -> str:
    """Сохраняет событие для немедленного выполнения"""
    
    supabase_client = get_supabase_client()
    if not supabase_client:
        logger.error("❌ Supabase клиент не найден")
        raise RuntimeError("Supabase клиент не инициализирован")
    
    # Проверяем, нужно ли предотвращать дублирование
    # Получаем информацию об обработчике через роутер-менеджер или fallback
    if _router_manager:
        event_handlers = _router_manager.get_event_handlers()
        event_handler_info = event_handlers.get(event_type, {})
    else:
        event_handler_info = _event_handlers.get(event_type, {})
    once_only = event_handler_info.get('once_only', True)
    
    if once_only:
        # Проверяем, было ли уже обработано аналогичное событие
        already_processed = await check_event_already_processed(event_type, user_id, session_id)
        if already_processed:
            logger.info(f"🔄 Событие '{event_type}' уже обрабатывалось для пользователя {user_id}, пропускаем")
            raise ValueError(f"Событие '{event_type}' уже обрабатывалось (once_only=True)")
    
    event_record = {
        'event_type': event_type,
        'event_category': 'user_event',
        'user_id': user_id,
        'event_data': event_data,
        'scheduled_at': None,  # Немедленное выполнение
        'status': 'immediate',
        'session_id': session_id
    }
    
    try:
        response = supabase_client.client.table('scheduled_events').insert(event_record).execute()
        event_id = response.data[0]['id']
        logger.info(f"💾 Событие сохранено в БД: {event_id}")
        return event_id
    except Exception as e:
        logger.error(f"❌ Ошибка сохранения события в БД: {e}")
        raise

async def save_scheduled_task(
    task_name: str,
    user_id: int,
    user_data: str,
    delay_seconds: int,
    session_id: str = None
) -> str:
    """Сохраняет запланированную задачу"""
    
    supabase_client = get_supabase_client()
    if not supabase_client:
        logger.error("❌ Supabase клиент не найден")
        raise RuntimeError("Supabase клиент не инициализирован")
    
    # Проверяем, нужно ли предотвращать дублирование
    # Получаем информацию о задаче через роутер-менеджер или fallback
    if _router_manager:
        scheduled_tasks = _router_manager.get_scheduled_tasks()
        task_info = scheduled_tasks.get(task_name, {})
    else:
        task_info = _scheduled_tasks.get(task_name, {})
    once_only = task_info.get('once_only', True)
    
    if once_only:
        # Проверяем, была ли уже запланирована аналогичная задача
        already_processed = await check_event_already_processed(task_name, user_id, session_id)
        if already_processed:
            logger.info(f"🔄 Задача '{task_name}' уже запланирована для пользователя {user_id}, пропускаем")
            raise ValueError(f"Задача '{task_name}' уже запланирована (once_only=True)")
    
    scheduled_at = datetime.now(timezone.utc) + timedelta(seconds=delay_seconds)
    
    event_record = {
        'event_type': task_name,
        'event_category': 'scheduled_task',
        'user_id': user_id,
        'event_data': user_data,
        'scheduled_at': scheduled_at.isoformat(),
        'status': 'pending',
        'session_id': session_id
    }
    
    try:
        response = supabase_client.client.table('scheduled_events').insert(event_record).execute()
        event_id = response.data[0]['id']
        logger.info(f"⏰ Запланированная задача сохранена в БД: {event_id} (через {delay_seconds}с)")
        return event_id
    except Exception as e:
        logger.error(f"❌ Ошибка сохранения запланированной задачи в БД: {e}")
        raise

async def save_global_event(
    handler_type: str,
    handler_data: str,
    delay_seconds: int = 0
) -> str:
    """Сохраняет глобальное событие"""
    
    supabase_client = get_supabase_client()
    if not supabase_client:
        logger.error("❌ Supabase клиент не найден")
        raise RuntimeError("Supabase клиент не инициализирован")
    
    # Проверяем, нужно ли предотвращать дублирование
    # Получаем информацию о глобальном обработчике через роутер-менеджер или fallback
    if _router_manager:
        global_handlers = _router_manager.get_global_handlers()
        handler_info = global_handlers.get(handler_type, {})
    else:
        handler_info = _global_handlers.get(handler_type, {})
    once_only = handler_info.get('once_only', True)
    
    if once_only:
        # Проверяем, было ли уже запланировано аналогичное глобальное событие
        already_processed = await check_event_already_processed(handler_type, user_id=None)
        if already_processed:
            logger.info(f"🔄 Глобальное событие '{handler_type}' уже запланировано, пропускаем")
            raise ValueError(f"Глобальное событие '{handler_type}' уже запланировано (once_only=True)")
    
    scheduled_at = None
    status = 'immediate'
    
    if delay_seconds > 0:
        scheduled_at = datetime.now(timezone.utc) + timedelta(seconds=delay_seconds)
        status = 'pending'
    
    event_record = {
        'event_type': handler_type,
        'event_category': 'global_handler',
        'user_id': None,  # Глобальное событие
        'event_data': handler_data,
        'scheduled_at': scheduled_at.isoformat() if scheduled_at else None,
        'status': status
    }
    
    try:
        response = supabase_client.client.table('scheduled_events').insert(event_record).execute()
        event_id = response.data[0]['id']
        logger.info(f"🌍 Глобальное событие сохранено в БД: {event_id}")
        return event_id
    except Exception as e:
        logger.error(f"❌ Ошибка сохранения глобального события в БД: {e}")
        raise

async def update_event_result(
    event_id: str,
    status: str,
    result_data: Any = None,
    error_message: str = None
):
    """Обновляет результат выполнения события"""
    
    supabase_client = get_supabase_client()
    if not supabase_client:
        logger.error("❌ Supabase клиент не найден")
        return
    
    update_data = {
        'status': status,
        'executed_at': datetime.now(timezone.utc).isoformat()
    }
    
    if result_data:
        import json
        update_data['result_data'] = json.dumps(result_data, ensure_ascii=False)
    
    if error_message:
        update_data['last_error'] = error_message
        # Получаем текущее количество попыток
        try:
            current_retry = supabase_client.client.table('scheduled_events').select('retry_count').eq('id', event_id).execute().data[0]['retry_count']
            update_data['retry_count'] = current_retry + 1
        except:
            update_data['retry_count'] = 1
    
    try:
        supabase_client.client.table('scheduled_events').update(update_data).eq('id', event_id).execute()
        logger.info(f"📝 Результат события {event_id} обновлен: {status}")
    except Exception as e:
        logger.error(f"❌ Ошибка обновления результата события {event_id}: {e}")

async def get_pending_events(limit: int = 50) -> list:
    """Получает события готовые к выполнению"""
    
    supabase_client = get_supabase_client()
    if not supabase_client:
        logger.error("❌ Supabase клиент не найден")
        return []
    
    try:
        now = datetime.now(timezone.utc).isoformat()
        
        response = supabase_client.client.table('scheduled_events')\
            .select('*')\
            .in_('status', ['pending', 'immediate'])\
            .or_(f'scheduled_at.is.null,scheduled_at.lte.{now}')\
            .order('created_at')\
            .limit(limit)\
            .execute()
        
        return response.data
    except Exception as e:
        logger.error(f"❌ Ошибка получения событий из БД: {e}")
        return []

async def background_event_processor():
    """Фоновый процессор для всех типов событий"""
    
    logger.info("🔄 Запуск фонового процессора событий")
    
    while True:
        try:
            # Получаем события готовые к выполнению
            pending_events = await get_pending_events(limit=50)
            
            if pending_events:
                logger.info(f"📋 Найдено {len(pending_events)} событий для обработки")
                
                for event in pending_events:
                    try:
                        await process_scheduled_event(event)
                        await update_event_result(event['id'], 'completed', {"processed": True})
                        
                    except Exception as e:
                        logger.error(f"❌ Ошибка обработки события {event['id']}: {e}")
                        await update_event_result(event['id'], 'failed', None, str(e))
            
            await asyncio.sleep(30)
            
        except Exception as e:
            logger.error(f"❌ Ошибка в фоновом процессоре: {e}")
            await asyncio.sleep(60)

async def process_scheduled_event(event: Dict):
    """Обрабатывает одно событие из БД"""
    
    event_type = event['event_type']
    event_category = event['event_category']
    event_data = event['event_data']
    user_id = event.get('user_id')
    
    logger.info(f"🔄 Обработка события {event['id']}: {event_category}/{event_type}")
    
    if event_category == 'scheduled_task':
        await execute_scheduled_task(event_type, user_id, event_data)
    elif event_category == 'global_handler':
        await execute_global_handler(event_type, event_data)
    elif event_category == 'user_event':
        await execute_event_handler(event_type, user_id, event_data)
    else:
        logger.warning(f"⚠️ Неизвестная категория события: {event_category}")

# =============================================================================
# ОБНОВЛЕННЫЕ ФУНКЦИИ С СОХРАНЕНИЕМ В БД
# =============================================================================

async def schedule_task_for_later_with_db(task_name: str, user_id: int, user_data: str, delay_seconds: int, session_id: str = None):
    """Планирует выполнение задачи через указанное время с сохранением в БД"""
    
    # Проверяем через роутер-менеджер или fallback к старым декораторам
    if _router_manager:
        scheduled_tasks = _router_manager.get_scheduled_tasks()
        if task_name not in scheduled_tasks:
            raise ValueError(f"Задача '{task_name}' не найдена")
    else:
        if task_name not in _scheduled_tasks:
            raise ValueError(f"Задача '{task_name}' не найдена")
    
    logger.info(f"⏰ Планируем задачу '{task_name}' через {delay_seconds} секунд")
    
    # Сохраняем в БД
    event_id = await save_scheduled_task(task_name, user_id, user_data, delay_seconds, session_id)
    
    async def delayed_task():
        await asyncio.sleep(delay_seconds)
        
        # Проверяем, нужна ли умная проверка
        task_info = _scheduled_tasks.get(task_name, {})
        use_smart_check = task_info.get('smart_check', True)
        
        if use_smart_check:
            # Умная проверка перед выполнением
            try:
                result = await smart_execute_check(event_id, user_id, session_id, task_name, user_data)
                if result['action'] == 'execute':
                    await execute_scheduled_task(task_name, user_id, user_data)
                    await update_event_result(event_id, 'completed', {"executed": True, "reason": "scheduled_execution"})
                elif result['action'] == 'cancel':
                    await update_event_result(event_id, 'cancelled', {"reason": result['reason']})
                elif result['action'] == 'reschedule':
                    # Перепланируем задачу на новое время
                    new_delay = result['new_delay']
                    await update_event_result(event_id, 'rescheduled', {
                        "new_delay": new_delay,
                        "reason": result['reason']
                    })
                    # Запускаем новую задачу
                    await asyncio.sleep(new_delay)
                    await execute_scheduled_task(task_name, user_id, user_data)
                    await update_event_result(event_id, 'completed', {"executed": True, "reason": "rescheduled_execution"})
                    
            except Exception as e:
                await update_event_result(event_id, 'failed', None, str(e))
                raise
        else:
            # Простое выполнение без умной проверки
            try:
                await execute_scheduled_task(task_name, user_id, user_data)
                await update_event_result(event_id, 'completed', {"executed": True, "reason": "simple_execution"})
            except Exception as e:
                await update_event_result(event_id, 'failed', None, str(e))
                raise
    
    # Запускаем задачу в фоне
    asyncio.create_task(delayed_task())
    
    return {
        "status": "scheduled",
        "task_name": task_name,
        "delay_seconds": delay_seconds,
        "event_id": event_id,
        "scheduled_at": datetime.now(timezone.utc).isoformat()
    }

async def schedule_global_handler_for_later_with_db(handler_type: str, delay_seconds: int, handler_data: str):
    """Планирует выполнение глобального обработчика через указанное время с сохранением в БД"""
    
    # Проверяем через роутер-менеджер или fallback к старым декораторам
    if _router_manager:
        global_handlers = _router_manager.get_global_handlers()
        if handler_type not in global_handlers:
            raise ValueError(f"Глобальный обработчик '{handler_type}' не найден")
    else:
        if handler_type not in _global_handlers:
            raise ValueError(f"Глобальный обработчик '{handler_type}' не найден")
    
    logger.info(f"🌍 Планируем глобальный обработчик '{handler_type}' через {delay_seconds} секунд")
    
    # Сохраняем в БД
    event_id = await save_global_event(handler_type, handler_data, delay_seconds)
    
    async def delayed_global_handler():
        await asyncio.sleep(delay_seconds)
        try:
            await execute_global_handler(handler_type, handler_data)
            await update_event_result(event_id, 'completed', {"executed": True})
        except Exception as e:
            await update_event_result(event_id, 'failed', None, str(e))
            raise
    
    # Запускаем задачу в фоне
    asyncio.create_task(delayed_global_handler())
    
    return {
        "status": "scheduled",
        "handler_type": handler_type,
        "delay_seconds": delay_seconds,
        "event_id": event_id,
        "scheduled_at": datetime.now(timezone.utc).isoformat()
    }

async def smart_execute_check(event_id: str, user_id: int, session_id: str, task_name: str, user_data: str) -> Dict[str, Any]:
    """
    Умная проверка перед выполнением запланированной задачи
    
    Логика:
    1. Если пользователь перешел на новый этап - отменяем событие
    2. Если прошло меньше времени чем планировалось - переносим на разницу
    3. Если прошло достаточно времени - выполняем
    
    Returns:
        Dict с action: 'execute', 'cancel', 'reschedule'
    """
    supabase_client = get_supabase_client()
    if not supabase_client:
        logger.error("❌ Supabase клиент не найден для умной проверки")
        return {"action": "execute", "reason": "no_supabase_client"}
    
    try:
        # Получаем информацию о последнем сообщении пользователя
        user_info = await supabase_client.get_user_last_message_info(user_id)
        
        if not user_info:
            logger.info(f"🔄 Пользователь {user_id} не найден, выполняем задачу")
            return {"action": "execute", "reason": "user_not_found"}
        
        # Проверяем, изменился ли этап
        stage_changed = await supabase_client.check_user_stage_changed(user_id, session_id)
        if stage_changed:
            logger.info(f"🔄 Пользователь {user_id} перешел на новый этап, отменяем задачу {task_name}")
            return {"action": "cancel", "reason": "user_stage_changed"}
        
        # Получаем информацию о событии из БД
        event_response = supabase_client.client.table('scheduled_events').select(
            'created_at', 'scheduled_at'
        ).eq('id', event_id).execute()
        
        if not event_response.data:
            logger.error(f"❌ Событие {event_id} не найдено в БД")
            return {"action": "execute", "reason": "event_not_found"}
        
        event = event_response.data[0]
        created_at = datetime.fromisoformat(event['created_at'].replace('Z', '+00:00'))
        scheduled_at = datetime.fromisoformat(event['scheduled_at'].replace('Z', '+00:00'))
        last_message_at = datetime.fromisoformat(user_info['last_message_at'].replace('Z', '+00:00'))
        
        # Вычисляем разницу во времени
        now = datetime.now(timezone.utc)
        time_since_creation = (now - created_at).total_seconds()
        time_since_last_message = (now - last_message_at).total_seconds()
        planned_delay = (scheduled_at - created_at).total_seconds()
        
        logger.info(f"🔄 Анализ для пользователя {user_id}:")
        logger.info(f"   Время с создания события: {time_since_creation:.0f}с")
        logger.info(f"   Время с последнего сообщения: {time_since_last_message:.0f}с")
        logger.info(f"   Запланированная задержка: {planned_delay:.0f}с")
        
        # Если прошло меньше времени чем планировалось, но пользователь недавно писал
        if time_since_creation < planned_delay and time_since_last_message < planned_delay:
            # Пересчитываем время - отправляем через planned_delay после последнего сообщения
            new_delay = max(0, planned_delay - time_since_last_message)
            logger.info(f"🔄 Переносим задачу на {new_delay:.0f}с (через {planned_delay:.0f}с после последнего сообщения)")
            return {
                "action": "reschedule", 
                "new_delay": new_delay,
                "reason": f"user_active_recently_{new_delay:.0f}s_delay"
            }
        
        # Если прошло достаточно времени - выполняем
        if time_since_creation >= planned_delay:
            logger.info(f"🔄 Выполняем задачу {task_name} для пользователя {user_id}")
            return {"action": "execute", "reason": "time_expired"}
        
        # Если что-то пошло не так - выполняем
        logger.info(f"🔄 Неожиданная ситуация, выполняем задачу {task_name}")
        return {"action": "execute", "reason": "unexpected_situation"}
        
    except Exception as e:
        logger.error(f"❌ Ошибка в умной проверке для пользователя {user_id}: {e}")
        return {"action": "execute", "reason": f"error_in_check: {str(e)}"}

async def check_event_already_processed(event_type: str, user_id: int = None, session_id: str = None) -> bool:
    """
    Проверяет, был ли уже обработан аналогичный event_type для пользователя/сессии
    
    Args:
        event_type: Тип события
        user_id: ID пользователя (для user_event и scheduled_task)
        session_id: ID сессии (для дополнительной проверки)
    
    Returns:
        True если событие уже обрабатывалось или в процессе
    """
    supabase_client = get_supabase_client()
    if not supabase_client:
        logger.error("❌ Supabase клиент не найден для проверки дублирования")
        return False
    
    try:
        # Строим запрос для поиска аналогичных событий
        query = supabase_client.client.table('scheduled_events').select('id').eq('event_type', event_type)
        
        # Для глобальных событий (user_id = None)
        if user_id is None:
            query = query.is_('user_id', 'null')
        else:
            query = query.eq('user_id', user_id)
        
        # Добавляем фильтр по статусам (pending, immediate, completed)
        query = query.in_('status', ['pending', 'immediate', 'completed'])
        
        # Если есть session_id, добавляем его в фильтр
        if session_id:
            query = query.eq('session_id', session_id)
        
        response = query.execute()
        
        if response.data:
            logger.info(f"🔄 Найдено {len(response.data)} аналогичных событий для '{event_type}'")
            return True
        
        return False
        
    except Exception as e:
        logger.error(f"❌ Ошибка проверки дублирования для '{event_type}': {e}")
        return False