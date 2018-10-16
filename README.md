To run tests :

pip install -r requirements.txt

py.test -vv -n 4 --reruns 2 test_ui.py --alluredir=./allure-results

Generate report:

get https://bintray.com/qameta/generic/download_file?file_path=io%2Fqameta%2Fallure%2Fallure%2F2.7.0%2Fallure-2.7.0.zip

allure-2.7.0/bin/allure generate -c
