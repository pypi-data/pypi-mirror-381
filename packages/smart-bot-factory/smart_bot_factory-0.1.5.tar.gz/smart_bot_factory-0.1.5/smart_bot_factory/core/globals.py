"""
Глобальные переменные для удобного доступа к компонентам бота
"""

from typing import Optional
from ..integrations.supabase_client import SupabaseClient
from ..integrations.openai_client import OpenAIClient
from ..config import Config
from ..admin.admin_manager import AdminManager
from ..analytics.analytics_manager import AnalyticsManager
from ..core.conversation_manager import ConversationManager
from ..utils.prompt_loader import PromptLoader

# Глобальные переменные (будут установлены при инициализации бота)
supabase_client: Optional[SupabaseClient] = None
openai_client: Optional[OpenAIClient] = None
config: Optional[Config] = None
admin_manager: Optional[AdminManager] = None
analytics_manager: Optional[AnalyticsManager] = None
conversation_manager: Optional[ConversationManager] = None
prompt_loader: Optional[PromptLoader] = None
bot: Optional[object] = None  # aiogram Bot
dp: Optional[object] = None   # aiogram Dispatcher

def set_globals(**kwargs):
    """Устанавливает глобальные переменные"""
    global supabase_client, openai_client, config, admin_manager
    global analytics_manager, conversation_manager, prompt_loader, bot, dp
    
    for key, value in kwargs.items():
        if key in globals():
            globals()[key] = value

def get_supabase_client() -> Optional[SupabaseClient]:
    """Получает клиент Supabase"""
    return supabase_client

def get_openai_client() -> Optional[OpenAIClient]:
    """Получает клиент OpenAI"""
    return openai_client

def get_config() -> Optional[Config]:
    """Получает конфигурацию"""
    return config

def get_admin_manager() -> Optional[AdminManager]:
    """Получает менеджер админов"""
    return admin_manager

def get_analytics_manager() -> Optional[AnalyticsManager]:
    """Получает менеджер аналитики"""
    return analytics_manager

def get_conversation_manager() -> Optional[ConversationManager]:
    """Получает менеджер разговоров"""
    return conversation_manager

def get_prompt_loader() -> Optional[PromptLoader]:
    """Получает загрузчик промптов"""
    return prompt_loader

def get_bot() -> Optional[object]:
    """Получает экземпляр бота"""
    return bot

def get_dp() -> Optional[object]:
    """Получает диспетчер"""
    return dp
