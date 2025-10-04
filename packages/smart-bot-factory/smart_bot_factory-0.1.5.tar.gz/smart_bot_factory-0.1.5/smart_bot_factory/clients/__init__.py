"""
Клиенты для удобного доступа к внешним сервисам
"""

from typing import Optional
from ..integrations.supabase_client import SupabaseClient
from ..integrations.openai_client import OpenAIClient

# Клиенты (будут установлены при инициализации бота)
supabase_client: Optional[SupabaseClient] = None
openai_client: Optional[OpenAIClient] = None

def set_clients(supabase: Optional[SupabaseClient] = None, openai: Optional[OpenAIClient] = None):
    """Устанавливает клиенты"""
    global supabase_client, openai_client
    supabase_client = supabase
    openai_client = openai

def get_supabase_client() -> Optional[SupabaseClient]:
    """Получает клиент Supabase"""
    return supabase_client

def get_openai_client() -> Optional[OpenAIClient]:
    """Получает клиент OpenAI"""
    return openai_client

__all__ = [
    'supabase_client',
    'openai_client',
    'set_clients',
    'get_supabase_client',
    'get_openai_client'
]
