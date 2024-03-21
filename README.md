# telegram2logseq

Ретранслятор сообщений из [Telegram](https://telegram.org) в журнал [Logseq](https://logseq.com/).

## Использование

1. Установите следующие environment variables:
* `T2LOGSEQ_JOURNALS_PATH` — путь к директории с журналами;
* `T2LOGSEQ_FILE_FORMAT` — формат названий журнальных файлов;
* `T2LOGSEQ_ADMIN_USERNAME` — админский username, сообщения с иных username будут игнорироваться;
2. Запустите ретранслятор: `poetry run python3 -m telegram2logseq`
