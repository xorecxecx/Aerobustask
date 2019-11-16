import subprocess, json
with open("tests/tests.json") as f:
    tests_object = json.load(f)
for test, answer in tests_object.items():
    print(f"Проверка программы с исходными данными: {test} Должно получиться {answer}")
    output = subprocess.getoutput("code.py %s" % test)
    if output == answer:
        print("Тест пройден!")
    else:
        print(f"Тест завален. Программа вернула {output}, вместо {answer}")