# Как аннотировать декоратор в Python

## example_01_intro.py
Пример аннотирования декоратора-трейсера, который отслеживает, что пришло в функцию и печатает логи.

Для передачи параметров (агсов и кваргсов) нужно использовать ParamSpec. Он указывает, что это те же самые входные параметры для функции, которые далее передаются в декоратор