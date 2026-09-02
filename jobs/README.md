## Datasphere Jobs

В этой директории содержатся пример для запуска обучения нейросетевой модели предсказания оценки отзыва, описанной подробнее в `NLP_Demo.ipynb`. Что нужно сделать для запуска:

- Установить интерфейс командной строки [Yandex Cloud CLI](https://yandex.cloud/ru/docs/cli/)
- Установить библиотеку `datasphere` и соответствующую утилиту командной строки:

```bash
pip install datasphere
```
После этого становится доступна команда `datasphere`, через которую осуществляется постановка задач и контроль над ними.

- Установить все необходимые библиотеки в локальное окружение:
```bash
pip install -r requirements.txt
```
- Убедиться, что скрипт `train.py` запускается в локальном окружении:
```bash
python train.py data\rail_reviews.zip
```
- Отправить задание на выполнение в Datasphere:
```bash
datasphere project job execute -p <project_id> -c train-model.yml
``` 
Здесь вместо `<project_id>` необходимо подставить идентификатор проекта Datasphere, который можно скопировать в веб-интерфейсе Datasphere на главной странице проекта.

Смотреть за ходом выполнения задания можно как в консоли, так и на портале Datasphere в разделе **Datasphere Jobs -> История запусков**.

Также много других примеров использования Jobs есть [в официальном репозитории с примерами](https://github.com/yandex-cloud-examples/yc-datasphere-jobs-examples/).