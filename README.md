# fun_service

virtualenv fun_service_venv && cd fun_service_venv<br/>
source bin/activate
pip install chalice
chalice new-project fun_service && cd fun_service
git clone https://github.com/steven-senko/fun_service.git
mv fun_service/* .
rm -rf fun_service
pip install -r requirements.txt
chalice deploy

