# fun_service

virtualenv fun_service_venv && cd fun_service_venv<br/>
source bin/activate<br/>
pip install chalice<br/>
chalice new-project fun_service && cd fun_service<br/>
git clone https://github.com/steven-senko/fun_service.git<br/>
mv fun_service/* .<br/>
rm -rf fun_service<br/>
pip install -r requirements.txt<br/>
chalice deploy<br/>

