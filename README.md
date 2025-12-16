# Abstract Factory Pattern

## Опис
Абстрактна фабрика дозволяє створювати сімейства взаємопов’язаних об’єктів
без вказівки їх конкретних класів.

## Приклад
- Button, Checkbox — інтерфейси продуктів
- WindowsButton, MacButton, WindowsCheckbox, MacCheckbox — конкретні продукти
- WindowsFactory, MacFactory — конкретні фабрики
- main.py показує використання фабрики для об’єктів різних платформ
