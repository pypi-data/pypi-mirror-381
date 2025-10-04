"""
Core модули smart_bot_factory
"""

# Импортируем основные компоненты для удобства
from .globals import (
    get_supabase_client,
    get_openai_client,
    get_config,
    get_admin_manager,
    get_analytics_manager,
    get_conversation_manager,
    get_prompt_loader,
    get_bot,
    get_dp
)

from .decorators import event_handler, schedule_task, global_handler
from .message_sender import send_message_by_human
from .router import Router
from .router_manager import RouterManager

__all__ = [
    # Функции получения (для внутреннего использования)
    'get_supabase_client',
    'get_openai_client',
    'get_config',
    'get_admin_manager',
    'get_analytics_manager',
    'get_conversation_manager',
    'get_prompt_loader',
    'get_bot',
    'get_dp',
    # Декораторы
    'event_handler',
    'schedule_task',
    'global_handler',
    # Роутеры
    'Router',
    'RouterManager',
    # Утилиты
    'send_message_by_human'
]