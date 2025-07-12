# Демонстрация Yandex Cloud и Yandex Datasphere

[English Version](en/README.md)

В этом репозитории доступны следующие демонстрации:

* [ReviewAnalysis.ipynb](ReviewAnalysis.ipynb) - анализ отзывов на жд-вокзалы Москвы с Yandex-карт с помощью модели Sentiment Analysis с HuggingFace и YandexGPT
* [LLM_Theatre_Assistants.ipynb](LLM_Theatre_Assistants.ipynb) - диалог двух агентов YandexGPT на основе Assistants API и многоагентное рисование с помощью YandexART
* [LLM_Theatre_LocalMemory.ipynb](LLM_Theatre_LocalMemory.ipynb) - диалог двух агентов YandexGPT с использованием локальной памяти
* [RAG_Assistant.ipynb](RAG_assistant.ipynb) - пример реализации RAG-ассистента с использованием AI Assistant API и Cloud ML SDK
* [YandexOCR.ipynb](YandexOCR.ipynb) - распознавание печатного и рукописного текста с Yandex Vision OCR и корректировка мелких ошибок с помощью YandexGPT

Для корректной работы ноутбуков необходимо определить следующие секреты в Datasphere: `folder_id` и `api_key`. Соответствующий этим секретам сервисный аккаунт должен иметь права на работу с YandexGPT, YandexART, ассистентами и Yandex Vision OCR.