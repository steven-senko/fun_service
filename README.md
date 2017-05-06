# fun_service

Before you start:<br/>

<ol>
<li>Sign up for AWS</li>
<li>Create S3 storage</li>
<li>Install aws on your local machine<br/>
http://docs.aws.amazon.com/cli/latest/userguide/installing.html</li>
<li>Install virtualenv on your local machine<br/>
https://www.digitalocean.com/community/tutorials/common-python-tools-using-virtualenv-installing-with-pip-and-managing-packages</li>
</ol>

virtualenv fun_service_venv && cd fun_service_venv<br/>
source bin/activate<br/>
pip install chalice<br/>
chalice new-project fun_service && cd fun_service<br/>
git clone https://github.com/steven-senko/fun_service.git<br/>
mv fun_service/* .<br/>
rm -rf fun_service<br/>
pip install -r requirements.txt<br/>
chalice deploy<br/>

