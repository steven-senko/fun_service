# fun_service

virtualenv test_service_venv && cd test_service_venv
source bin/activate
pip install chalice
chalice new-project test_service && cd test_service
git clone https://github.com/steven-senko/fun_service.git
mv fun_service/* .
rm -rf fun_service
pip install -r requirements.txt
chalice deploy