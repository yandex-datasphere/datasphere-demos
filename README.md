# Демонстрация Yandex Cloud и Yandex Datasphere

[English Version](en/README.md)

В этом репозитории доступны следующие демонстрации:

* [ReviewAnalysis.ipynb](ReviewAnalysis.ipynb) - анализ отзывов на жд-вокзалы Москвы с Yandex-карт с помощью модели Sentiment Analysis с HuggingFace и LLM
* [LLM_Theatre_Assistants.ipynb](LLM_Theatre_Assistants.ipynb) - диалог двух агентов на основе Responses API и многоагентное рисование с помощью YandexART
* [LLM_Theatre_LocalMemory.ipynb](LLM_Theatre_LocalMemory.ipynb) - диалог двух агентов с использованием локальной памяти
* [YandexOCR.ipynb](YandexOCR.ipynb) - распознавание печатного и рукописного текста с Yandex Vision OCR и корректировка мелких ошибок с помощью LLM
* [NLP_Demo.ipynb](NLP_Demo.ipynb) - работа с локальными эмбеддингами и языковой моделью с HuggingFace в Datasphere.
* [train-trans.ipynb](train-trans.ipynb) - обучение простейшей GPT-2 модели с нуля, и до-обучение модели ruGPT-2 на вычислительных мощностях Datasphere
* [jobs](jobs) - обучение модели прогнозирования рейтинга отзыва с помощью Datasphere Jobs

Для корректной работы ноутбуков необходимо определить следующие секреты в Datasphere: `folder_id` и `api_key`. Соответствующий этим секретам сервисный аккаунт должен иметь права на работу с языковыми моделями, YandexART и Yandex Vision OCR. Рекомендуемая роль: `ai.editor`.