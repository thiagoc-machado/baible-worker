from celery import shared_task
import httpx
import os

@shared_task
def ping_huggingface_space():
    try:
        url = 'https://thiagocmach-bible-embeddings-api.hf.space/embed'
        payload = {'texto': 'Jesus é o caminho, a verdade e a vida.'}
        headers = {
            'Authorization': f'Bearer {os.getenv("EMBEDDING_API_TOKEN")}',
            'Content-Type': 'application/json'
        }
        response = httpx.post(url, json=payload, headers=headers, timeout=10)
        print(f'✅ Ping enviado ao HuggingFace: {response.status_code}')
    except Exception as e:
        print(f'❌ Erro ao pingar o HuggingFace: {e}')
