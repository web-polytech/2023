# Наша Школа

_[Ссылка на макет в Figma](https://www.figma.com/file/vW04wXBzQObdKVIM6tKoEP/SchoolSite?node-id=0:1&t=8vkCHMbURQWPKwev-1)_

Участники:
- Киверин Андрей
- Бондарь Илья
- Крапивин Иван
- Савенков Виктор
- Киселев Максим

## Get Started

### Про git flow

Продакшн в main ветке. Все, что оказывается здесь, попадает на сервер

Фича ветки именуются следующим образом:

```text
andrew/<branch-name>
ilya/<branch-name>
ivan/<branch-name>
max/<branch-name>
victor/<branch-name>
```

Каждый может создавать и работать только co своей веткой

Фича ветки нужно переодически сливать в main, чтобы не было конфликтов

### Про окружение
Чтобы настроить VScode нужно установить следующие расширения:

- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
- [StyleLint](https://marketplace.visualstudio.com/items?itemName=stylelint.vscode-stylelint)
- [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
- [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar)

В Intellij Idea по идее всё, кроме ESLint плагина должно работать из коробки

### Как контрибьютить

1. Настроить SSH в github ([ссылка](https://docs.github.com/ru/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account))
1. Скопировать репу по SSH
`git clone git@github.com:web-polytech/2023.git`
1. Создать и переключиться в фича ветку
`git checkout -b <your-name>/<feature-name>`
1. Сделать изменения, закоммитить их
`git add . git commit -m 'commit-message'`
1. Запушить изменения в репозиторий
`git push --set-upstream origin branch-name`
1. Зайти на гитхаб, создать пулл реквест, проверить тесты
1. Если тесты не прошли, закоммитить правки в ту же ветку и закрыть пул реквест (новый PR создавать не нужно)
1. При наличии изменений в main ветке нужно сделать ребейз
`git rebase main`

‎

***Московский Политех 2023, группа 211-321***
