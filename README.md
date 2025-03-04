# Демонстрация Yandex Cloud и Yandex Datasphere

В этом репозитории доступны следующие демонстрации:

* [ReviewAnalysis.ipynb](ReviewAnalysis.ipynb) - анализ отзывов на жд-вокзалы Москвы с Yandex-карт с помощью модели Sentiment Analysis с HuggingFace и YandexGPT
* [LLM_Theatre_Assistants.ipynb](LLM_Theatre_Assistants.ipynb) - диалог двух агентов YandexGPT на основе Assistants API и многоагентное рисование с помощью YandexART
* [YandexOCR.ipynb](YandexOCR.ipynb) - распознавание печатного и рукописного текста с Yandex Vision OCR и корректировка мелких ошибок с помощью YandexGPT

Для корректной работы ноутбуков необходимо определить следующие секреты в Datasphere: `folder_id` и `api_key`. Соответствующий этим секретам сервисный аккаунт должен иметь права на работу с YandexGPT, YandexART, ассистентами и Yandex Vision OCR.